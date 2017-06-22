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
self.ifid=0;
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
: ( var_path | var_meta | stat {self.ifid=self.ifid+1;} | if_stat {self.ifid=self.ifid+1;}| new_var | include | constant) NL+ ;

new_var : array | array_cluster ; 

constant
: CONST const_var (',' const_var)*  ;

const_var
@init{v = Var('');}
: i=ID '=' (c=FLOAT {v.const=float($c.text)}|c=INT {v.const=int($c.text);v.type='int';}|c=STRING{v.const=str($c.text);v.type='str';}) 
{name=str($i.text).lower();self.newConstMap[name]=v;}
;



array
: (l=STRING_L|g=INT_L)? ARRAY array_var[$l!=None,$g!=None] (',' array_var[$l!=None,$g!=None])*   ;


array_var[boolean isStr, boolean isInt]
@init{isTemp=False;}
:  (T {isTemp=True} )? i=ID 
{v = Var('');name=str($i.text).lower();
if isStr:
	v.type='str'
	print (name+' is string')
if isInt:
	v.type='int'
	print (name+' is integer')
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
	if $l!=None: 
		o.type='str';
		print (name+' is string')
	if $g!=None: 
		o.type='int';
		print (name+' is int')
	self.newArrayMap[name]=o;
	if isGroupTemp or subvar[k]:
		self.tempVarList.append(name);
}
: (l=STRING_L|g=INT_L)? ARRAY 
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
:  (T {isTemp=True} )? i=ID  '=' p=PATH (',' u=STRING )?
{p =str($p.text); t = Var(p); 
name=str($i.text).lower(); self.varPathMap[name]=t;
if $u: self.varPathMap[name].metaData['units']=str($u.text)[1:-1].lower();
if isTemp: self.tempVarList.append(name); 
self.varPathMap[name].metaData['_partc']=str($p.text).split("/")[3];	
self.varPathMap[name].metaData['_partb']=str($p.text).split("/")[2];	
}   ;

       
var_meta 
@init{ha=False}
: i=id2 '.' m=ID '=' 
( 
	(k=FLOAT{c=float($k.text)}|k=INT{c=int($k.text)}|k=STRING{c=str($k.text)[1:-1].lower()}) 
	| 
	(dv=metaDict{c=str($dv.x).lower();
if $dv.hasV: ha=True;
	})
) 
{name=str($i.text).lower();mk=str($m.text).lower();

if self.varPathMap.has_key(name):
	self.varPathMap[name].metaData[mk]=c;
	if ha: self.varPathMap[name].metaDataPost.append(mk);
elif self.varExprMap.has_key(name):
	self.varExprMap[name].metaData[mk]=c;
	if ha: self.varExprMap[name].metaDataPost.append(mk); 
elif self.newArrayMap.has_key(name):
	self.newArrayMap[name].metaData[mk]=c; 
	if ha: self.newArrayMap[name].metaDataPost.append(mk);
else:
	msg=name+'.'+mk+'='+c+' variable \"'+name+'\" not found!'
	Err.addError(msg, self.vardefFile, self.vardefName)
}; 



//metaValue 
//: FLOAT | INT | STRING;

metaDict returns [boolean hasV, String x]
@init{hasV=False}
@after{$x='{'+$x+'}'}
: '{'   d=dict_pair
{if $d.hasV: $hasV=True;
$x=$d.x;	
} 
(',' d=dict_pair
{if $d.hasV: $hasV=True;
$x=$x+','+$d.x;	
}
)* '}' ;

dict_pair returns [boolean hasV, String x]
@init{r1='';r2=''}
:  (i1=ID {$hasV=True; 
r1='_cm[\''+str($i1.text)+'\'].const'
}
|s1=STRING{r1=str($s1.text)}|s11=number{r1=str($s11.text)})

':' (i2=ID {$hasV=True; 
r2='_cm[\''+str($i2.text)+'\'].const'
}
|s2=STRING{r2=str($s2.text)}|s22=number{r2=str($s22.text)})
{$x=r1+':'+r2;}
;

number: FLOAT|INT;


stat
@init{isTemp=False;ifs=collections.OrderedDict();k='';}
@after
{
v = Var('');
e=str($e.text).lower();v.expr=e;
name=str($i.text).lower(); self.varExprMap[name]=v; 
e2=str($e.x).lower()
name2=self.ifsAppend+"['"+str($i.text).lower()+"']"
k='!'+name2+'='+e2;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;
if isTemp: 
	self.tempVarList.append(name);	
#print('i am here', self.ifid, name)
}
:   (T {isTemp=True} )? i=ID '=' e=ee_dts
//{name=str($i.text);
//
//}
    ;

ee_dts returns [String x]
    : a=ee_dts o=('*'|'/') b=ee_dts           {$x=str($a.x)+str($o.text)+str($b.x);}   
    | a=ee_dts o=('+'|'-') b=ee_dts           {$x=str($a.x)+str($o.text)+str($b.x);} 
    | {s=''} ('-'{s='-'})? i=INT      {$x=s+str($i.text)}             
    | {s=''} ('-'{s='-'})? i=FLOAT    {$x=s+str($i.text)}              
    | i=ID                           
{vName=str($i.text).lower();
if vName in self.newArrayMap.keys() or vName in self.varPathMap.keys() or vName in self.varExprMap.keys():
	$x=self.ifsAppend+"['"+vName+"']"
	#print (vName); 
else:
	Err.addError(vName+' not defined.', self.vardefFile, self.vardefName)
}  
    | '(' a=ee_dts ')'                    {$x="("+str($a.x)+")"}   
    | i= STRING                       {$x=  str($i.text) }  
    ; 


ee returns [String x]
    : a=ee o=('*'|'/') b=ee           {$x=str($a.x)+str($o.text)+str($b.x);}   
    | a=ee o=('+'|'-') b=ee           {$x=str($a.x)+str($o.text)+str($b.x);} 
    | {s=''} ('-'{s='-'})? i=INT      {$x=s+str($i.text)}             
    | {s=''} ('-'{s='-'})? i=FLOAT    {$x=s+str($i.text)}              
    | (i=ID ('.' j=ID)?)                         
{vName=str($i.text).lower();
if $j!=None: vName=str($i.text).lower()+'.'+str($j.text).lower();
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
if vName in self.newArrayMap.keys() or vName in self.varExprMap.keys() or vName in self.varPathMap.keys():
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
//WY    : 'wateryear' ;
//JAN : 'jan' ;
//FEB : 'feb' ;
//MAR : 'mar' ;
//APR : 'apr' ;
//MAY : 'may' ;
//JUN : 'jun' ;
//JUL : 'jul' ;
//AUG : 'aug' ;
//SEP : 'sep' ;
//OCT : 'oct' ;
//NOV : 'nov' ;
//DEC : 'dec' ;

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

