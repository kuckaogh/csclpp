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
        buf.write(u"\16]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write(u"\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\7\t\62\n\t")
        buf.write(u"\f\t\16\t\65\13\t\3\n\3\n\3\13\3\13\3\f\6\f<\n\f\r\f")
        buf.write(u"\16\f=\3\f\3\f\6\fB\n\f\r\f\16\fC\3\f\6\fG\n\f\r\f\16")
        buf.write(u"\fH\5\fK\n\f\3\r\6\rN\n\r\r\r\16\rO\3\16\5\16S\n\16\3")
        buf.write(u"\16\3\16\3\17\6\17X\n\17\r\17\16\17Y\3\17\3\17\2\2\20")
        buf.write(u"\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\2\25\2\27\13\31")
        buf.write(u"\f\33\r\35\16\3\2\4\4\2C\\c|\4\2\13\13\"\"d\2\3\3\2\2")
        buf.write(u"\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write(u"\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write(u"\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3")
        buf.write(u"\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r)\3\2\2\2")
        buf.write(u"\17+\3\2\2\2\21-\3\2\2\2\23\66\3\2\2\2\258\3\2\2\2\27")
        buf.write(u";\3\2\2\2\31M\3\2\2\2\33R\3\2\2\2\35W\3\2\2\2\37 \7?")
        buf.write(u"\2\2 \4\3\2\2\2!\"\7*\2\2\"\6\3\2\2\2#$\7+\2\2$\b\3\2")
        buf.write(u"\2\2%&\7,\2\2&\n\3\2\2\2\'(\7\61\2\2(\f\3\2\2\2)*\7-")
        buf.write(u"\2\2*\16\3\2\2\2+,\7/\2\2,\20\3\2\2\2-\63\5\23\n\2.\62")
        buf.write(u"\5\23\n\2/\62\5\25\13\2\60\62\7a\2\2\61.\3\2\2\2\61/")
        buf.write(u"\3\2\2\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63")
        buf.write(u"\64\3\2\2\2\64\22\3\2\2\2\65\63\3\2\2\2\66\67\t\2\2\2")
        buf.write(u"\67\24\3\2\2\289\4\62;\29\26\3\2\2\2:<\5\25\13\2;:\3")
        buf.write(u"\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>?\3\2\2\2?J\7\60")
        buf.write(u"\2\2@B\5\25\13\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2")
        buf.write(u"\2\2DK\3\2\2\2EG\7\"\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2")
        buf.write(u"\2HI\3\2\2\2IK\3\2\2\2JA\3\2\2\2JF\3\2\2\2K\30\3\2\2")
        buf.write(u"\2LN\5\25\13\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2")
        buf.write(u"\2P\32\3\2\2\2QS\7\17\2\2RQ\3\2\2\2RS\3\2\2\2ST\3\2\2")
        buf.write(u"\2TU\7\f\2\2U\34\3\2\2\2VX\t\3\2\2WV\3\2\2\2XY\3\2\2")
        buf.write(u"\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\b\17\2\2\\\36\3\2")
        buf.write(u"\2\2\f\2\61\63=CHJORY\3\b\2\2")
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
    ID = 8
    FLOAT = 9
    INT = 10
    NEWLINE = 11
    WS = 12

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'='", u"'('", u"')'", u"'*'", u"'/'", u"'+'", u"'-'" ]

    symbolicNames = [ u"<INVALID>",
            u"MUL", u"DIV", u"ADD", u"SUB", u"ID", u"FLOAT", u"INT", u"NEWLINE", 
            u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"MUL", u"DIV", u"ADD", u"SUB", 
                  u"ID", u"LETTER", u"DIGIT", u"FLOAT", u"INT", u"NEWLINE", 
                  u"WS" ]

    grammarFileName = u"Expr.g4"

    def __init__(self, input=None):
        super(ExprLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


