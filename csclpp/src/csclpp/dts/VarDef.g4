grammar VarDef; // rename to distinguish from Expr.g4
options {language=Python2;}

@header {
from Study import Study
from Var import Var
from collections import defaultdict
import collections
from antlr4.error import Err
import numpy as np
}

@parser::members {
varMetaKeys=[];
ifsAppend='';
ifsNewAppend='';
varPathGroupMap={};

tempVarGroupList={};
ifsMapGroupMap={};
strArrayGroupMap={};
intArrayGroupMap={};
floatArrayGroupMap={};
constGroupMap={};
varPathMap=collections.OrderedDict();
allVarsGroupList={}

tempVarList=[];
strArrayMap=collections.OrderedDict();
intArrayMap=collections.OrderedDict();
floatArrayMap=collections.OrderedDict();
constMap=collections.OrderedDict();
ifsMap=collections.OrderedDict(); # (if statement ID, (condition, assignments)) 
vardefName='';
vardefFile='';
vardefDefault='';
systemVars=['year','month','oct','nov','dec','jan','feb','mar','apr','may','jun','jul','aug','sep'];
systemConstMap=collections.OrderedDict();
allVars=[];

def isConst(self, name):
	if name in self.constMap.keys():
		return True
	else:
		return False

def checkDup(self, name):
	if name in self.allVars:
		msg=name+' is already defined.'
		Err.addError(msg, self.vardefFile, self.vardefName)
	else:
		self.allVars.append(name)
		
def checkExist(self, name):
	if name not in self.allVars:
		msg=name+' is not defined.'
		Err.addError(msg, self.vardefFile, self.vardefName)
		
}

prog 
@init 
{self.varPathGroupMap={};

self.tempVarGroupList={};
self.ifsMapGroupMap={};
self.strArrayGroupMap={};
self.intArrayGroupMap={};
self.floatArrayGroupMap={};
self.constGroupMap={};
self.allVarsGroupList={};
self.ifid=0;
}
:    NL* use NL* vardef+ ;

use
:USE i=ID{self.vardefDefault=str($i.text).lower()};

vardef
@init {
self.varPathMap=collections.OrderedDict();

self.tempVarList=[];
self.ifsMap=collections.OrderedDict();
self.strArrayMap=collections.OrderedDict();
self.intArrayMap=collections.OrderedDict();
self.floatArrayMap=collections.OrderedDict();
self.constMap=self.systemConstMap;
self.allVars=self.systemVars[:];
}
@after
{
self.varPathGroupMap[groupName]=self.varPathMap;

self.tempVarGroupList[groupName]=self.tempVarList;	
self.ifsMapGroupMap[groupName]=self.ifsMap;
self.strArrayGroupMap[groupName]=self.strArrayMap;
self.intArrayGroupMap[groupName]=self.intArrayMap;
self.floatArrayGroupMap[groupName]=self.floatArrayMap;
self.constGroupMap[groupName]=self.constMap;
self.allVarsGroupList[groupName]=self.allVars;
#print(groupName, self.allVars)
}
:   VARDEF name=ID {groupName=str($name.text).lower();self.vardefName=groupName;} NL+ 
       field+
       END NL+
    ;

field
: ( var_path | var_meta  | stat | if_stat {self.ifid=self.ifid+1;}| new_var | include | constant) NL+ ;

new_var : strArray| intArray| floatArray ; 

constant: floatConst|intConst;

intConst: INT_L CONST intConstVar (',' intConstVar)*  ;
floatConst: CONST floatConstVar (',' floatConstVar)*  ;

floatConstVar
@init{v = Var('');}
: i=ID '=' e=ee 
{name=str($i.text).lower();
self.checkDup(name);
v.const='('+str($e.x)+')';v.metaData['_dataType']=np.float;
self.constMap[name]=v;
};


intConstVar
@init{v = Var('');}
: i=ID '=' e=ee 
{name=str($i.text).lower();
self.checkDup(name);
v.const='int('+str($e.x)+')';v.metaData['_dataType']=np.int;
self.constMap[name]=v;
};

stat
@init{isTemp=False;ifs=collections.OrderedDict();k='';}
:  (T {isTemp=True} )? i=ID 
{v = Var('');name=str($i.text).lower();self.checkExist(name);}

'=' e=ee
{e2=str($e.x).lower()
name2=self.ifsAppend+"['"+str($i.text).lower()+"'][i]"
k='!'+name2+'='+e2;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;}
;


strArray: strArrayCluster| strArrayLone;

strArrayCluster
@init
{header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;
expr='';ifs=collections.OrderedDict();k='';}
@after{
for k in subvar.keys():
	o = Var('')
	name=header.lower()+'.'+k.lower()
	self.checkDup(name)	
	print (name+' is string')
	self.strArrayMap[name]=o;
	if isGroupTemp or subvar[k]:
		self.tempVarList.append(name);
	if expr:
		name2=self.ifsAppend+"['"+name+"'][i]"
		k='!'+name2+'='+expr;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;
}
: STR_L ARRAY 
 (T {isGroupTemp=True} )? i=ID {header=str($i.text);} '{' 
{isTemp=False;} (T {isTemp=True} )? i=ID  
{subvar[str($i.text)]=isTemp;} 
(',' {isTemp=False;} (T {isTemp=True} )? i=ID 
{subvar[str($i.text)]=isTemp;} 
)* '}'
('=' e=ee {expr=str($e.x).lower()})? 
;

strArrayLone
: STR_L ARRAY strArrayVar (',' strArrayVar)*   ;

strArrayVar
@init{isTemp=False;ifs=collections.OrderedDict();k='';}
:  (T {isTemp=True} )? i=ID 
{v = Var('');name=str($i.text).lower();
self.checkDup(name);self.strArrayMap[name]=v;
if isTemp: self.tempVarList.append(name); 
print (name+' is string')
}
('=' e=ee
{e2=str($e.x).lower()
name2=self.ifsAppend+"['"+str($i.text).lower()+"'][i]"
k='!'+name2+'='+e2;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;}
)?;

intArray: intArrayCluster| intArrayLone;

intArrayCluster
@init
{header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;
expr='';ifs=collections.OrderedDict();k='';}
@after{
for k in subvar.keys():
	o = Var('')
	name=header.lower()+'.'+k.lower()
	self.checkDup(name)	
	print (name+' is integer')
	self.intArrayMap[name]=o;
	if isGroupTemp or subvar[k]:
		self.tempVarList.append(name);
	if expr:
		name2=self.ifsAppend+"['"+name+"'][i]"
		k='!'+name2+'='+expr;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;
}
: INT_L ARRAY 
 (T {isGroupTemp=True} )? i=ID {header=str($i.text);} '{' 
{isTemp=False;} (T {isTemp=True} )? i=ID  
{subvar[str($i.text)]=isTemp;} 
(',' {isTemp=False;} (T {isTemp=True} )? i=ID 
{subvar[str($i.text)]=isTemp;} 
)* '}'
('=' e=ee {expr=str($e.x).lower()})? 
;

intArrayLone
: INT_L ARRAY intArrayVar (',' intArrayVar)*   ;

intArrayVar
@init{isTemp=False;ifs=collections.OrderedDict();k='';}
:  (T {isTemp=True} )? i=ID 
{v = Var('');name=str($i.text).lower();
self.checkDup(name);self.intArrayMap[name]=v;
if isTemp: self.tempVarList.append(name); 
print (name+' is integer')}
('=' e=ee
{e2=str($e.x).lower()
name2=self.ifsAppend+"['"+str($i.text).lower()+"'][i]"
k='!'+name2+'='+e2;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;}
)?;


floatArray: floatArrayCluster| floatArrayLone;

floatArrayCluster
@init
{header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;
expr='';ifs=collections.OrderedDict();k='';}
@after{
for k in subvar.keys():
	o = Var('')
	name=header.lower()+'.'+k.lower()
	self.checkDup(name)	
	print (name+' is float')
	self.floatArrayMap[name]=o;
	if isGroupTemp or subvar[k]:
		self.tempVarList.append(name);
	if expr:
		name2=self.ifsAppend+"['"+name+"'][i]"
		k='!'+name2+'='+expr;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;
}
: ARRAY 
 (T {isGroupTemp=True} )? i=ID {header=str($i.text);} '{' 
{isTemp=False;} (T {isTemp=True} )? i=ID  
{subvar[str($i.text)]=isTemp;} 
(',' {isTemp=False;} (T {isTemp=True} )? i=ID 
{subvar[str($i.text)]=isTemp;} 
)* '}'
('=' e=ee {expr=str($e.x).lower()})? 
;

floatArrayLone
: ARRAY floatArrayVar (',' floatArrayVar)*   ;

floatArrayVar
@init{isTemp=False;ifs=collections.OrderedDict();k='';}
:  (T {isTemp=True} )? i=ID 
{v = Var('');name=str($i.text).lower();
self.checkDup(name);self.floatArrayMap[name]=v;
if isTemp: self.tempVarList.append(name); 
print (name+' is float')}
 
('=' e=ee
{e2=str($e.x).lower()
name2=self.ifsAppend+"['"+str($i.text).lower()+"'][i]"
k='!'+name2+'='+e2;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;}
)?
;


include
@after{gn=str($g.text).lower();
if gn: 
	self.varPathMap.update(self.varPathGroupMap[gn])

	self.tempVarList.extend(self.tempVarGroupList[gn])
	self.ifsMap.update(self.ifsMapGroupMap[gn])
	self.strArrayMap.update(self.strArrayGroupMap[gn])
	self.intArrayMap.update(self.intArrayGroupMap[gn])
	self.floatArrayMap.update(self.floatArrayGroupMap[gn])
	self.constMap.update(self.constGroupMap[gn])
	self.allVars.extend(self.allVarsGroupList[gn])
}
: INCLUDE g=ID ;

 //{print $p.text}
var_path
@init{isTemp=False;}
:  (T {isTemp=True} )? i=ID  '=' p=PATH (',' u=STRING )?
{p =str($p.text); t = Var(p); 
name=str($i.text).lower(); self.varPathMap[name]=t; 
if name in self.allVars:
	Err.addError(name+' is already defined.', self.vardefFile, self.vardefName)
else:
	self.allVars.append(name)
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
elif self.strArrayMap.has_key(name):
	self.strArrayMap[name].metaData[mk]=c; 
elif self.intArrayMap.has_key(name):
	self.intArrayMap[name].metaData[mk]=c; 
elif self.floatArrayMap.has_key(name):
	self.floatArrayMap[name].metaData[mk]=c; 
else:
	msg=name+'.'+mk+'='+str(c)+' variable \"'+name+'\" not found!'
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
:  ((i1=ID|i1=SYSCONST) {$hasV=True; 
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


ee returns [String x]
    : a=ee o=('*'|'/') b=ee           {$x=str($a.x)+str($o.text)+str($b.x);}   
    | a=ee o=('+'|'-') b=ee           {$x=str($a.x)+str($o.text)+str($b.x);} 
    | {s=''} ('-'{s='-'})? i=INT      {$x=s+str($i.text)}             
    | {s=''} ('-'{s='-'})? i=FLOAT    {$x=s+str($i.text)}              
    | i=SYSARRAY        {vName=str($i.text).lower();$x=self.ifsAppend+"['"+vName+"']"+"[i]";}   
    | i=SYSCONST        {vName=str($i.text).lower();$x=self.constMap[vName].const;} 
    | i=ID
{vName=str($i.text).lower();
self.checkExist(vName);
if vName in self.allVars:
	if vName in self.constMap.keys():
		$x=self.constMap[vName].const
	else:
		$x=self.ifsAppend+"['"+vName+"']"+"[i]"	
else:
		print('not found ***',vName, $x)
		print(self.allVars)
}      
    | (i=ID '.' j=ID)                        
{
name1=str($i.text).lower();name2=str($j.text).lower();vName=name1+'.'+name2; 
if vName in self.allVars:
	$x=self.ifsAppend+"['"+vName+"']"+"[i]"
 
elif name1 in self.allVars:
	m=None
	if name1 in self.varPathMap.keys():
		m=self.varPathMap[name1].metaData[name2]
	elif name1 in self.floatArrayMap.keys():
		m=self.floatArrayMap[name1].metaData[name2]
	elif name1 in self.intArrayMap.keys():	
		m=self.intArrayMap[name1].metaData[name2]
	$x=str(m)
}  
    | '(' a=ee ')'                    {$x="("+str($a.x)+")"}   
    | i= STRING                       {$x=  str($i.text) }  
    ; 

compare returns [String x]
    : a=ee o=('>'|'>='|'<'|'<='|'=='|'!=') b=ee    {$x=str($a.x)+str($o.text)+str($b.x);}  
    | '(' c=compare ')'                            {$x="("+str($c.x)+")"}    
    |    c1=compare op=(AND|OR) c2=compare         {$x=str($c1.x)+str($op.text)+str($c2.x)}  
    ; 


assign returns [String x]
	: i=id2 '=' a=ee 
{vName=str($i.text).lower();
if vName in self.allVars:
	$x=self.ifsNewAppend+"['"+str($i.text)+"'][i]="+$a.x
	#print (vName); 
else:
	Err.addError(vName+' not defined yet.', self.vardefFile, self.vardefName)
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
STR_L : 'str'  ;
INT_L :   'int' ;
FLOAT_L : 'float' ;
CONST : 'const' ;
SYSARRAY: 'year'|'month'|'cfs_taf'|'taf_cfs'|'daysin';
SYSCONST: 'oct'|'nov'|'dec'|'jan'|'feb'|'mar'|'apr'|'may'|'jun'|'jul'|'aug'|'sep';

//MONTH : 'month' ;
//YEAR  : 'year'  ;
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

