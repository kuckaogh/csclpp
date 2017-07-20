grammar Setting;
options {language=Python2;}
@header {
from Study import Study
from Var import Var
import Setting as S
import copy
}
@parser::members {
styobj=None
thisFile='';
}


prog
@init {S.studyMap={}}
:   NL* sty+ ;

sty
@init {self.styobj=Study()} 
@after{stycopy=copy.deepcopy(self.styobj);styName=str($name.text); S.studyMap[styName]=stycopy;}
 :   STUDY name=ID  NL+ 
       field+
       END NL+
    ;

field: (data | vardef | meta | wresl) NL+ ;

data:  DATA '='? s1=STRING {s1=$s1.text[1:-1];self.styobj.data_src.append(str(s1))} 
(',' s2=STRING {s2=$s2.text[1:-1];self.styobj.data_src.append(str(s2))} )* ;

vardef
: VARDEF '='? s1=STRING {s=$s1.text[1:-1];self.styobj.varFile=s;} 
;

vardef_old
: VARDEF '=' f=ID '.' VARDEF  {f=str($f.text);self.styobj.varFile=f;}; 

meta : METADATA '=' STRING ;
wresl: WRESL '=' STRING ; 



LINE_COMMENT
    : '#' ~[\r\n]* -> skip ;

STRING
    :   '"' ( ~[\\"] )*? '"'
    |   '\'' ( ~[\\'] )*? '\''
    ;


END : 'end' ;
STUDY : 'study' ;
DATA  : 'data' ;
VARDEF : 'dt' ;
METADATA : 'metadata' ;
WRESL : 'wresl' ;

ID  :   LETTER (LETTER|DIGIT|'_')* ;
fragment LETTER  : [a-zA-Z] ;
fragment DIGIT:  '0'..'9' ; 
FLOAT : DIGIT+ '.' (DIGIT+|' '+) ;
INT : DIGIT+ ;







    

//ID  :   [a-zA-Z][a-zA-Z0-9_]+ ;      // match identifiers

NL:('\r'? '\n') ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
