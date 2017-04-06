grammar Setting;
options {language=Python2;}
@header {
from Study import Study
from Var import Var
import Setting as S
import Temp as T
import copy
}
//@parser::members{
//global studyMap; studyMap={}	
//}

prog
@init {S.studyMap={}	}
:   NL* sty+ ;

sty
@init {T.sty=Study()} 
@after{stycopy=copy.deepcopy(T.sty);styName=$name.text; S.studyMap[styName]=stycopy;}
 :   STUDY name=ID  NL+ 
       field+
       END NL+
    ;

field: (data | vardef | meta | wresl) NL+ ;

data:  DATA '=' STRING (',' STRING)* ;

vardef
: VARDEF '=' f=ID '.' d=ID {f=$f.text;d=$d.text;T.sty.varFile=f;T.sty.varDef=d;}; 
meta : META '=' STRING ;
wresl: WRESL '=' STRING ; 



LINE_COMMENT
    : '#' ~[\r\n]* -> skip ;

END : 'end' ;
STUDY : 'study' ;
DATA  : 'data' ;
VARDEF : 'vardef' ;
META : 'metadata' ;
WRESL : 'wresl' ;

ID  :   LETTER (LETTER|DIGIT|'_')* ;
fragment LETTER  : [a-zA-Z] ;
fragment DIGIT:  '0'..'9' ; 

STRING
    :   '"' ( ~[\\"] )*? '"'
    |   '\'' ( ~[\\'] )*? '\''
    ;


INT :   DIGIT+ ;

//ID  :   LETTER (LETTER|DIGIT|'_')* ;




    

//ID  :   [a-zA-Z][a-zA-Z0-9_]+ ;      // match identifiers

NL:('\r'? '\n') ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
