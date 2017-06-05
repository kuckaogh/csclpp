grammar VarDef; // rename to distinguish from Expr.g4
options {language=Python2;}

@header {
from Study import Study
from Var import Var
from collections import defaultdict
import collections
import Error
}

@parser::members {
varMetaKeys=[];
ifsAppend='';
ifsNewAppend='';
varPathGroupMap={};
varExprGroupMap={};
tempVarGroupList={};
ifsMapGroupMap={};
newArrayGroupMap={};
varPathMap=collections.OrderedDict();
varExprMap=collections.OrderedDict();
tempVarList=[];
newArrayMap=collections.OrderedDict();
#newArrayClusterMap=collections.OrderedDict();
ifsMap=collections.OrderedDict(); # (if statement ID, (condition, assignments)) 
}

prog 
@init 
{self.varPathGroupMap={};self.varExprGroupMap={};self.tempVarGroupList={};
ifsMapGroupMap={};newArrayGroupMap={};
}
:    NL* vardef+ ;

vardef
@init {
self.varPathMap=collections.OrderedDict();
self.varExprMap=collections.OrderedDict();
self.tempVarList=[];
self.ifsMap=collections.OrderedDict();
self.newArrayMap=collections.OrderedDict();
self.ifid=0;
}
@after
{groupName=str($name.text).lower();
self.varPathGroupMap[groupName]=self.varPathMap;
self.varExprGroupMap[groupName]=self.varExprMap;
self.tempVarGroupList[groupName]=self.tempVarList;	
self.ifsMapGroupMap[groupName]=self.ifsMap;
self.newArrayGroupMap[groupName]=self.newArrayMap;
}
:   VARDEF name=ID  NL+ 
       field+
       END NL+
    ;

field
: ( var_path | var_meta | stat | if_stat {self.ifid=self.ifid+1;}| new_var | include ) NL+ ;

new_var : array | array_cluster ; 

array
: ARRAY array_var (',' array_var)*   ;

array_var
: i=ID 
{v = Var('');name=str($i.text).lower();
self.newArrayMap[name]=v;
}
;


array_cluster
@init{header='';subvar=[];}
@after{
for v in subvar:
	o = Var('')
	self.newArrayMap[header.lower()+'.'+v.lower()]=o;
}
: ARRAY i=ID {header=str($i.text);} '{' 
i=ID  {subvar.append(str($i.text));} (',' i=ID {subvar.append(str($i.text));} )* 
'}' ;



include
@after{gn=str($g.text).lower();
if gn: 
	self.varPathMap.update(self.varPathGroupMap[gn])
	self.varExprMap.update(self.varExprGroupMap[gn])
	self.tempVarList.extend(self.tempVarGroupList[gn])
	self.ifsMap.update(self.ifsMapGroupMap[gn])
	self.newArrayMap.update(self.newArrayGroupMap[gn])
}
: INCLUDE g=ID ;

 //{print $p.text}
var_path
@init{isTemp=False }
:  (T {isTemp=True} )? i=ID  '=' p=PATH  
{p =str($p.text); t = Var(p); 
name=str($i.text).lower(); self.varPathMap[name]=t;
if isTemp: self.tempVarList.append(name); 	
}   ;

       
var_meta : i=id2 '.' m=metaKey '=' inf=metaValue 
{name=str($i.text).lower();mk=str($m.text);c=str($inf.text);
if name in self.varPathMap:
	self.varPathMap[name].metaData[mk]=c; 
elif name in self.varExprMap:
	self.varExprMap[name].metaData[mk]=c; 
elif name in self.newArrayMap:
	self.newArrayMap[name].metaData[mk]=c; 
else:
	msg=name+'.'+mk+'='+c+' variable \"'+name+'\" not found!'
	Error.addError(msg)
}; 

metaKey : UNITS | CAPACITY ;

metaValue
: i = FLOAT | INT | ID;


stat
@init{isTemp=False }
@after
{
v = Var('');
e=str($e.text);v.expr=e.lower();
name=str($i.text).lower(); self.varExprMap[name]=v; 
if isTemp: 
	self.tempVarList.append(name);	
}
:   (T {isTemp=True} )? i=ID '=' e=ee     
//{name=str($i.text);
//
//}
    ;

ee returns [String x]
    : a=ee o=('*'|'/') b=ee           {$x=str($a.x)+str($o.text)+str($b.x);}   
    | a=ee o=('+'|'-') b=ee           {$x=str($a.x)+str($o.text)+str($b.x);} 
    | {s=''} ('-'{s='-'})? i=INT      {$x=s+str($i.text)}             
    | {s=''} ('-'{s='-'})? i=FLOAT    {$x=s+str($i.text)}              
    | i=ID                            
{vName=str($i.text).lower();
if vName in self.newArrayMap.keys() or vName in self.varPathMap.keys() or vName in self.varExprMap.keys():
	$x=self.ifsAppend+"['"+vName+"']"+"[i]"
	#print (vName); 
else:
	Error.addError(vName+' not defined.')
}  
    | '(' a=ee ')'                    {$x="("+str($a.x)+")"}       
    ; 

compare returns [String x]
    : a=ee o=('>'|'>='|'<'|'<='|'=='|'!=') b=ee    {$x=str($a.x)+str($o.text)+str($b.x)}  
    | '(' c=compare ')'                            {$x="("+str($c.x)+")"}    
    |    c1=compare op=(AND|OR) c2=compare         {$x=str($c1.x)+str($op.text)+str($c2.x)}  
    ; 


assign returns [String x]
	: i=id2 '=' a=ee 
{vName=str($i.text).lower();
if vName in self.newArrayMap.keys() or vName in self.varExprMap.keys():
	$x=self.ifsNewAppend+"['"+str($i.text)+"'][i]="+$a.x
	#print (vName); 
else:
	Error.addError(vName+' not valid.')
}  
	;

id2 : ID ('.' ID)? ;

if_stat
@init{ifs=collections.OrderedDict();al=[];}
@after{self.ifsMap[self.ifid]=ifs;
#for s in ifs: print(s,ifs[s]);
}
	: IF c=compare NL* '{' NL* (a=assign {t=str($a.x).lower();al.append(t)} NL*  )+ '}' NL*
	{k=str($c.x).lower(); ifs[k]=al;al=[]}
	 
	 (ELSEIF c=compare NL* '{' NL* (a=assign {t=str($a.x).lower();al.append(t)} NL*  )+ '}' NL*
	{k=str($c.x).lower(); ifs[k]=al;al=[]})*
     
     (ELSE NL* '{' NL* (a=assign {t=str($a.x).lower();al.append(t)} NL*  )+ '}' NL+
	{ifs['always']=al})?
	; 



LINE_COMMENT
    : '#' ~[\r\n]* -> skip ;

T : '@' ;


PATH : '/'   ID?     
       '/'   ID 
       '/'   (ID (LETTER|DIGIT|'_'|'-')* )?
       '//'  (INT ID)?
       '/'   ID?
       '/'  ;

MUL :   '*' ; 
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
AND :   ' and ';
OR  :   ' or ';
INCLUDE : 'include' ;
VARDEF : 'vardef' ;
END    : 'end' ;
ARRAY    : 'array' ;
IF     : 'if' ;
ELSEIF   : 'elseif' ;
ELSE   : 'else' ;
UNITS : 'units';
CAPACITY : 'capacity' ;
ID  :   LETTER (LETTER|DIGIT|'_')* ;
fragment LETTER  : [a-zA-Z] ;
fragment DIGIT:  '0'..'9' ; 
FLOAT : DIGIT+ '.' (DIGIT+|' '+) ;
INT : DIGIT+ ;

STRING
    :   '"' ( ~[\\"] )*? '"'
    |   '\'' ( ~[\\'] )*? '\''
    ;
//FLOAT : INT '.' (INT|' '+) ;
//INT :   [0-9]+ ;         // match integers
NL:('\r'? '\n') ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
