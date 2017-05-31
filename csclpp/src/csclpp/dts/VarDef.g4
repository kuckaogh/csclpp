grammar VarDef; // rename to distinguish from Expr.g4
options {language=Python2;}

@header {
from Study import Study
from Var import Var
from collections import defaultdict
import collections
}

@parser::members {
varMetaKeys=[];
ifsAppend='';
ifsNewAppend='';
varPathGroupMap={};
varExprGroupMap={};
tempVarGroupList={};
ifsMapGroupMap={};
newArrayGroupList={};
varPathMap={};
varExprMap={};
tempVarList=[];
newArrayList=[];
ifsMap=collections.OrderedDict(); # (if statement ID, (condition, assignments)) 
}

prog 
@init 
{self.varPathGroupMap={};self.varExprGroupMap={};self.tempVarGroupList={};
ifsMapGroupMap={};newArrayGroupList={};
}
:    NL* vardef+ ;

vardef
@init {
self.varPathMap={};self.varExprMap={};self.tempVarList=[];
self.ifsMap=collections.OrderedDict();self.newArrayList=[];
self.ifid=0;
}
@after
{groupName=$name.text;
self.varPathGroupMap[groupName]=self.varPathMap;
self.varExprGroupMap[groupName]=self.varExprMap;
self.tempVarGroupList[groupName]=self.tempVarList;	
self.ifsMapGroupMap[groupName]=self.ifsMap;
self.newArrayGroupList[groupName]=self.newArrayList;
}
:   VARDEF name=ID  NL+ 
       field+
       END NL+
    ;

field
: ( var_path | var_meta | stat | if_stat {self.ifid=self.ifid+1;}| new_var | include ) NL+ ;

new_var
: ARRAY i=ID {name=str($i.text); self.newArrayList.append(name);} 
       (',' i=ID {name=str($i.text); self.newArrayList.append(name);} )*   ;

include
@after{gn=$g.text;
if gn: 
	self.varPathMap.update(self.varPathGroupMap[gn])
	self.varExprMap.update(self.varExprGroupMap[gn])
	self.tempVarList.extend(self.tempVarGroupList[gn])
	self.ifsMap.update(self.ifsMapGroupMap[gn])
	self.newArrayList.extend(self.newArrayGroupList[gn])
}
: INCLUDE g=ID ;

 //{print $p.text}
var_path
@init{isTemp=False }
:  (T {isTemp=True} )? i=ID  '=' p=PATH  
{p =str($p.text); t = Var(p); 
name=str($i.text); self.varPathMap[name]=t;
if isTemp: self.tempVarList.append(name); 	
}   ;

       
var_meta : v=ID '.' p=ID '=' inf=info 
{vn=str($v.text);pn=str($p.text);c=str($inf.x);
	
if pn in self.varMetaKeys:
	if vn in self.varPathMap:
		self.varPathMap[vn].metaData[pn]=c; 
	elif vn in self.varExprMap:
		self.varExprMap[vn].metaData[pn]=c; 
	else:
		print ('#Error: '+vn+'.'+pn+'='+c+' variable \"'+vn+'\" not found!')
else:
	print ('#Error: '+vn+'.'+pn+'='+c+' metadata keyword \"'+pn+'\" not recognized!')
}; 

info returns[String x]
: i=FLOAT {$x=$i.text}| i=INT {$x=$i.text}| i=STRING {$x=$i.text[1:-1]};


stat
@init{isTemp=False }
@after
{
v = Var('');
e=str($e.text);v.expr=e;
name=str($i.text); self.varExprMap[name]=v; 
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
    | i=ID                            {$x=self.ifsAppend+"['"+str($i.text)+"']"+"[i]"}  
    | '(' a=ee ')'                    {$x="("+str($a.x)+")"}       
    ; 

compare returns [String x]
    : a=ee o=('>'|'>='|'<'|'<='|'=='|'!=') b=ee    {$x=str($a.x)+str($o.text)+str($b.x)}  
    | '(' c=compare ')'                            {$x="("+str($c.x)+")"}    
    |    c1=compare op=(AND|OR) c2=compare         {$x=str($c1.x)+str($op.text)+str($c2.x)}  
    ; 


assign returns [String x]
	: i=ID '=' a=ee {$x=self.ifsNewAppend+"['"+str($i.text)+"'][i]="+$a.x}  
	;


if_stat
@init{ifs=collections.OrderedDict();al=[];}
@after{self.ifsMap[self.ifid]=ifs;
#for s in ifs: print(s,ifs[s]);
}
	: IF c=compare NL* '{' NL* (a=assign {t=str($a.x);al.append(t)} NL*  )+ '}' NL*
	{k=str($c.x); ifs[k]=al;al=[]}
	 
	 (ELSEIF c=compare NL* '{' NL* (a=assign {t=str($a.x);al.append(t)} NL*  )+ '}' NL*
	{k=str($c.x); ifs[k]=al;al=[]})*
     
     (ELSE NL* '{' NL* (a=assign {t=str($a.x);al.append(t)} NL*  )+ '}' NL+
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
