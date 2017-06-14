grammar VarDef; // rename to distinguish from Expr.g4
options {language=Python2;}

@header {
from Study import Study
from Var import Var
from collections import defaultdict
import collections
from antlr4.error import Err
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
newConstGroupMap={};
varPathMap=collections.OrderedDict();
varExprMap=collections.OrderedDict();
tempVarList=[];
newArrayMap=collections.OrderedDict();
newConstMap=collections.OrderedDict();
#newArrayClusterMap=collections.OrderedDict();
ifsMap=collections.OrderedDict(); # (if statement ID, (condition, assignments)) 
vardefName='';
vardefFile='';
vardefDefault='';
}

prog 
@init 
{self.varPathGroupMap={};
self.varExprGroupMap={};
self.tempVarGroupList={};
ifsMapGroupMap={};
newArrayGroupMap={};
newConstGroupMap={};
}
:    NL* use NL* vardef+ ;

use
:USE i=ID{self.vardefDefault=str($i.text).lower()};

vardef
@init {
self.varPathMap=collections.OrderedDict();
self.varExprMap=collections.OrderedDict();
self.tempVarList=[];
self.ifsMap=collections.OrderedDict();
self.newArrayMap=collections.OrderedDict();
self.newConstMap=collections.OrderedDict();
self.ifid=0;
}
@after
{
self.varPathGroupMap[groupName]=self.varPathMap;
self.varExprGroupMap[groupName]=self.varExprMap;
self.tempVarGroupList[groupName]=self.tempVarList;	
self.ifsMapGroupMap[groupName]=self.ifsMap;
self.newArrayGroupMap[groupName]=self.newArrayMap;
self.newConstGroupMap[groupName]=self.newConstMap;
}
:   VARDEF name=ID {groupName=str($name.text).lower();self.vardefName=groupName;} NL+ 
       field+
       END NL+
    ;

field
: ( var_path | var_meta | stat | if_stat {self.ifid=self.ifid+1;}| new_var | include | constant) NL+ ;

new_var : array | array_cluster ; 

constant
: CONST const_var (',' const_var)*  ;

const_var
@init{v = Var('');}
: i=ID '=' (c=FLOAT {v.const=float($c.text)}|c=INT {v.const=int($c.text)}|c=STRING{v.const=str($c.text)}) 
{name=str($i.text).lower();self.newConstMap[name]=v;}
;



array
: ARRAY array_var (',' array_var)*   ;

array_var
@init{isTemp=False;}
:  (T {isTemp=True} )? i=ID 
{v = Var('');name=str($i.text).lower();
self.newArrayMap[name]=v;
if isTemp: self.tempVarList.append(name); 
}
;


array_cluster
@init{header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;}
@after{
for k in subvar.keys():
	o = Var('')
	name=header.lower()+'.'+k.lower()
	self.newArrayMap[name]=o;
	if isGroupTemp or subvar[k]:
		self.tempVarList.append(name);
}
: ARRAY 
 (T {isGroupTemp=True} )? i=ID {header=str($i.text);} '{' 
{isTemp=False;} (T {isTemp=True} )? i=ID  
{subvar[str($i.text)]=isTemp;} 
(',' {isTemp=False;} (T {isTemp=True} )? i=ID 
{subvar[str($i.text)]=isTemp;} 
)* 
'}' ;



include
@after{gn=str($g.text).lower();
if gn: 
	self.varPathMap.update(self.varPathGroupMap[gn])
	self.varExprMap.update(self.varExprGroupMap[gn])
	self.tempVarList.extend(self.tempVarGroupList[gn])
	self.ifsMap.update(self.ifsMapGroupMap[gn])
	self.newArrayMap.update(self.newArrayGroupMap[gn])
	self.newConstMap.update(self.newConstGroupMap[gn])
}
: INCLUDE g=ID ;

 //{print $p.text}
var_path
@init{isTemp=False;}
:  (T {isTemp=True} )? i=ID  '=' p=PATH  (',' u=ID )?
{p =str($p.text); t = Var(p); 
name=str($i.text).lower(); self.varPathMap[name]=t;
if $u: self.varPathMap[name].metaData['units']=str($u.text).lower();
if isTemp: self.tempVarList.append(name); 	
}   ;

       
var_meta : i=id2 '.' m=metaKey '=' (inf=metaValue{c=str($inf.text).lower()}|dv=metaDict{c=str($dv.text).lower()}) 
{name=str($i.text).lower();mk=str($m.text).lower();

	
if name in self.varPathMap:
	self.varPathMap[name].metaData[mk]=c; 
elif name in self.varExprMap:
	self.varExprMap[name].metaData[mk]=c; 
elif name in self.newArrayMap:
	self.newArrayMap[name].metaData[mk]=c; 
else:
	msg=name+'.'+mk+'='+c+' variable \"'+name+'\" not found!'
	Err.addError(msg, self.vardefFile, self.vardefName)
}; 

metaKey : ID;

metaValue
: FLOAT | INT | ID;

metaDict: '{'   dict_pair (',' dict_pair)* '}' ;

dict_pair :  (ID|STRING|number) ':' (ID|STRING|number) ;

number: FLOAT|INT;


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
	Err.addError(vName+' not defined.', self.vardefFile, self.vardefName)
}  
    | '(' a=ee ')'                    {$x="("+str($a.x)+")"}   
    | i= STRING                       {$x=  str($i.text) }  
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
	Err.addError(vName+' not valid.', self.vardefFile, self.vardefName)
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

USE:   'use' ;


INCLUDE : 'include' ;
VARDEF : 'vardef' ;
END    : 'end' ;
ARRAY    : 'array' ;
IF     : 'if' ;
ELSEIF   : 'elseif' ;
ELSE   : 'else' ;
//UNITS : 'units';
//CAPACITY : 'capacity' ;
GROUP : 'group' ;
STRING_L : 'string'  ;
INT_L :   'int' ;
FLOAT_L : 'float' ;
CONST : 'const' ;
MONTH : 'month' ;
YEAR  : 'year'  ;

FLOAT:  ('0'..'9')+'.'('0'..'9')* ;  
ID  :   LETTER (LETTER|DIGIT|'_')* ;
fragment LETTER  : [a-zA-Z] ;
fragment DIGIT:  '0'..'9' ; 
//FLOAT : DIGIT+ '.' (DIGIT+|' '+) ; //FLOAT : DIGIT+ '.' DIGIT+ ;
INT : DIGIT+ ;


STRING
    :   '"' ( ~[\\"] )*? '"'
    |   '\'' ( ~[\\'] )*? '\''
    ;
//FLOAT : INT '.' (INT|' '+) ;
//INT :   [0-9]+ ;         // match integers
NL:('\r'? '\n') ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
//UNKNOWN_CHAR : . ;

