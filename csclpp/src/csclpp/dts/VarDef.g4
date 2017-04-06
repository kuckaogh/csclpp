grammar VarDef; // rename to distinguish from Expr.g4
options {language=Python2;}

@header {
from Study import Study
from Var import Var
import Temp as T
}

//@members {
//varMap = {}
//}

prog
@init {T.varGroupMap={};T.dtsGroupMap={}}
:    NL* vardef+ ;

vardef
@init {T.varMap={};T.dtsMap={}}
@after
{vm=T.varPathMap.copy(); groupName=$name.text; T.varPathGroupMap[groupName]=vm;
dm=T.varExprMap.copy(); groupName=$name.text; T.varExprGroupMap[groupName]=dm;	
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
name=$i.text; T.varPathMap[name]=t; 	
}   ;

       
var_meta : v=ID '.' p=ID '=' inf=info 
{vn=$v.text;pn=$p.text;
if vn in T.varPathMap:
	T.varPathMap[vn].metaData[pn]=$inf.text; 
else: 
	T.varExprMap[vn].metaData[pn]=$inf.text; 
}; 

info: number | STRING ;


stat
@init{isTemp=False }
@after{v = Var('');v.isTemp=isTemp;e=$e.text;v.expr=e; 
name=$i.text; T.varExprMap[name]=v; 	
}
:   (T {isTemp=True} )? i=ID '=' e=expr          # assign
    ;

expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   number                       # int
    |   T?ID                          # id
    |   '(' expr ')'                # parens
    ;


//expr:   expr '*' expr      # MulDiv
//    |   expr '/' expr      # MulDiv
//    |   expr '+' expr      # MulDiv
//    |   expr '-' expr      # MulDiv                  
//    |   ID                          # id
//    |   '(' expr ')'                # parens
//    ;




number : FLOAT | INT ;


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

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   LETTER (LETTER|DIGIT|'_')* ;
fragment LETTER  : [a-zA-Z] ;
fragment DIGIT:  '0'..'9' ; 

STRING
    :   '"' ( ~[\\"] )*? '"'
    |   '\'' ( ~[\\'] )*? '\''
    ;
FLOAT : INT '.' (INT|' '+) ;
INT :   [0-9]+ ;         // match integers
NL:('\r'? '\n') ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
