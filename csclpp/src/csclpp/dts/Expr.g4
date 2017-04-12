grammar Expr;
options {language=Python2;}

@header {
from Study import Study
from Var import Var
import ParserTools as P
}

@parser::members {

varTs={}

def evaluate(self, left, op, right):
    if   ExprParser.MUL == op.type:
        return left * right
    elif ExprParser.DIV == op.type:
        return left / right
    elif ExprParser.ADD == op.type:
        return left + right
    elif ExprParser.SUB == op.type:
        return left - right
    else:
        return 0
}

prog: (i=ID '=' ee NEWLINE {id = str($i.text);self.varTs[id] = $ee.v}  )+           
    ;

ee returns [int v]
    : a=ee op=('*'|'/') b=ee  {$v = self.evaluate($a.v, $op, $b.v)}
    | a=ee op=('+'|'-') b=ee  {$v = self.evaluate($a.v, $op, $b.v)}
    | number=(INT|FLOAT)      {$v = float($number.text)}                        
    | i=ID {
id = str($i.text);$v = self.varTs[id];
    } 
    | '(' ee ')'             {$v = $ee.v}       
    ; 

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;

ID  :   LETTER (LETTER|DIGIT|'_')* ;
fragment LETTER  : [a-zA-Z] ;
fragment DIGIT:  '0'..'9' ; 
FLOAT : DIGIT+ '.' (DIGIT+|' '+) ;
INT : DIGIT+ ;
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
