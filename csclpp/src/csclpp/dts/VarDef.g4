grammar VarDef; // rename to distinguish from Expr.g4
options {language=Python2;}

@header {
from Study import Study
from Var import Var
import Temp as T
from collections import defaultdict
}

//@members {
//varMap = {}
//}

prog
@init 
{T.varGroupMap={};T.dtsGroupMap={};T.tempVarGroupList={}
}
:    NL* vardef+ ;

vardef
@init {T.varMap={};T.dtsMap={};T.tempVarList=[]}
@after
{groupName=$name.text;
vm=T.varPathMap.copy(); T.varPathGroupMap[groupName]=vm;
dm=T.varExprMap.copy(); T.varExprGroupMap[groupName]=dm;
tm=list(T.tempVarList); T.tempVarGroupList[groupName]=tm;	
}
:   VARDEF name=ID  NL+ 
       field+
       END NL+
    ;

field: ( var_path | var_meta | stat | include ) NL+ ;

include
@after{gn=$g.text;
if gn: T.varPathMap.update(T.varPathGroupMap[gn]); T.varExprMap.update(T.varExprGroupMap[gn]);
}
: INCLUDE g=ID ;

 //{print $p.text}
var_path
@init{isTemp=False }
:  (T {isTemp=True} )? i=ID  '=' p=PATH  
{p =$p.text; t = Var(p);t.isTemp=isTemp; 
name=str($i.text); T.varPathMap[name]=t;
if isTemp: T.tempVarList.append(name); 	
}   ;

       
var_meta : v=ID '.' p=ID '=' inf=info 
{vn=$v.text;pn=$p.text;
if vn in T.varPathMap:
	T.varPathMap[vn].metaData[pn]=$inf.text; 
else: 
	T.varExprMap[vn].metaData[pn]=$inf.text; 
}; 

info: FLOAT | INT | STRING ;


stat
@init{isTemp=False }
@after{v = Var('');e=str($e.text);v.expr=e; 
name=str($i.text); T.varExprMap[name]=v; 
if isTemp: T.tempVarList.append(name);	
}
:   (T {isTemp=True} )? i=ID '=' e=ee     
//{name=str($i.text);
//
//}
    ;

//expr:   expr op=('*'|'/') expr      # MulDiv
//    |   expr op=('+'|'-') expr      # AddSub
//    |   number                       # int
//    |   ID                          # id
//    |   '(' expr ')'                # parens
//    ;

ee 
    : a=ee op=('*'|'/') b=ee  
    | a=ee op=('+'|'-') b=ee  
    | INT                   
    | FLOAT                    
    | ID 
    | '(' ee ')'             
    ; 




//number : FLOAT | INT ;


LINE_COMMENT
    : '#' ~[\r\n]* -> skip ;

T : '@' ;
INCLUDE : 'include' ;
VARDEF : 'vardef' ;
END    : 'end' ;

PATH : '/'   ID?     
       '/'   ID 
       '/'   (ID '-'? ID)?
       '//'  (INT ID)?
       '/'   ID?
       '/'  ;

MUL :   '*' ; 
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
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
