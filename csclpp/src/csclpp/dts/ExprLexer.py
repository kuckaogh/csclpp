# Generated from Expr.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
import ParserTools as P


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\16W\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write(u"\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6\t/\n\t\r\t\16\t\60\3")
        buf.write(u"\t\3\t\7\t\65\n\t\f\t\16\t8\13\t\3\n\3\n\3\n\3\n\7\n")
        buf.write(u">\n\n\f\n\16\nA\13\n\3\13\3\13\3\f\3\f\3\r\6\rH\n\r\r")
        buf.write(u"\r\16\rI\3\16\5\16M\n\16\3\16\3\16\3\17\6\17R\n\17\r")
        buf.write(u"\17\16\17S\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write(u"\17\t\21\n\23\13\25\2\27\2\31\f\33\r\35\16\3\2\4\4\2")
        buf.write(u"C\\c|\4\2\13\13\"\"\\\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write(u"\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write(u"\2\2\21\3\2\2\2\2\23\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write(u"\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2\2\7#\3\2\2\2\t")
        buf.write(u"%\3\2\2\2\13\'\3\2\2\2\r)\3\2\2\2\17+\3\2\2\2\21.\3\2")
        buf.write(u"\2\2\239\3\2\2\2\25B\3\2\2\2\27D\3\2\2\2\31G\3\2\2\2")
        buf.write(u"\33L\3\2\2\2\35Q\3\2\2\2\37 \7?\2\2 \4\3\2\2\2!\"\7*")
        buf.write(u"\2\2\"\6\3\2\2\2#$\7+\2\2$\b\3\2\2\2%&\7,\2\2&\n\3\2")
        buf.write(u"\2\2\'(\7\61\2\2(\f\3\2\2\2)*\7-\2\2*\16\3\2\2\2+,\7")
        buf.write(u"/\2\2,\20\3\2\2\2-/\4\62;\2.-\3\2\2\2/\60\3\2\2\2\60")
        buf.write(u".\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\66\7\60\2\2")
        buf.write(u"\63\65\4\62;\2\64\63\3\2\2\2\658\3\2\2\2\66\64\3\2\2")
        buf.write(u"\2\66\67\3\2\2\2\67\22\3\2\2\28\66\3\2\2\29?\5\25\13")
        buf.write(u"\2:>\5\25\13\2;>\5\27\f\2<>\7a\2\2=:\3\2\2\2=;\3\2\2")
        buf.write(u"\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\24\3\2\2")
        buf.write(u"\2A?\3\2\2\2BC\t\2\2\2C\26\3\2\2\2DE\4\62;\2E\30\3\2")
        buf.write(u"\2\2FH\5\27\f\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2")
        buf.write(u"\2J\32\3\2\2\2KM\7\17\2\2LK\3\2\2\2LM\3\2\2\2MN\3\2\2")
        buf.write(u"\2NO\7\f\2\2O\34\3\2\2\2PR\t\3\2\2QP\3\2\2\2RS\3\2\2")
        buf.write(u"\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\b\17\2\2V\36\3\2\2")
        buf.write(u"\2\n\2\60\66=?ILS\3\b\2\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    MUL = 4
    DIV = 5
    ADD = 6
    SUB = 7
    FLOAT = 8
    ID = 9
    INT = 10
    NEWLINE = 11
    WS = 12

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'='", u"'('", u"')'", u"'*'", u"'/'", u"'+'", u"'-'" ]

    symbolicNames = [ u"<INVALID>",
            u"MUL", u"DIV", u"ADD", u"SUB", u"FLOAT", u"ID", u"INT", u"NEWLINE", 
            u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"MUL", u"DIV", u"ADD", u"SUB", 
                  u"FLOAT", u"ID", u"LETTER", u"DIGIT", u"INT", u"NEWLINE", 
                  u"WS" ]

    grammarFileName = u"Expr.g4"

    def __init__(self, input=None):
        super(ExprLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


