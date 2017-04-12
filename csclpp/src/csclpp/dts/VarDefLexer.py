# Generated from VarDef.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
from collections import defaultdict


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\26\u00bc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\7\6:\n\6\f\6")
        buf.write(u"\16\6=\13\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write(u"\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write(u"\13\3\13\5\13X\n\13\3\13\3\13\3\13\3\13\3\13\5\13_\n")
        buf.write(u"\13\3\13\3\13\5\13c\n\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\5\13k\n\13\3\13\3\13\5\13o\n\13\3\13\3\13\3\f\3\f\3")
        buf.write(u"\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\7\20\177")
        buf.write(u"\n\20\f\20\16\20\u0082\13\20\3\21\3\21\3\22\3\22\3\23")
        buf.write(u"\6\23\u0089\n\23\r\23\16\23\u008a\3\23\3\23\6\23\u008f")
        buf.write(u"\n\23\r\23\16\23\u0090\3\23\6\23\u0094\n\23\r\23\16\23")
        buf.write(u"\u0095\5\23\u0098\n\23\3\24\6\24\u009b\n\24\r\24\16\24")
        buf.write(u"\u009c\3\25\3\25\7\25\u00a1\n\25\f\25\16\25\u00a4\13")
        buf.write(u"\25\3\25\3\25\3\25\7\25\u00a9\n\25\f\25\16\25\u00ac\13")
        buf.write(u"\25\3\25\5\25\u00af\n\25\3\26\5\26\u00b2\n\26\3\26\3")
        buf.write(u"\26\3\27\6\27\u00b7\n\27\r\27\16\27\u00b8\3\27\3\27\4")
        buf.write(u"\u00a2\u00aa\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write(u"\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\2#\2%\22\'")
        buf.write(u"\23)\24+\25-\26\3\2\7\4\2\f\f\17\17\4\2C\\c|\4\2$$^^")
        buf.write(u"\4\2))^^\4\2\13\13\"\"\u00cc\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write(u"\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write(u"\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write(u"\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write(u"\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write(u"\2-\3\2\2\2\3/\3\2\2\2\5\61\3\2\2\2\7\63\3\2\2\2\t\65")
        buf.write(u"\3\2\2\2\13\67\3\2\2\2\r@\3\2\2\2\17B\3\2\2\2\21J\3\2")
        buf.write(u"\2\2\23Q\3\2\2\2\25U\3\2\2\2\27r\3\2\2\2\31t\3\2\2\2")
        buf.write(u"\33v\3\2\2\2\35x\3\2\2\2\37z\3\2\2\2!\u0083\3\2\2\2#")
        buf.write(u"\u0085\3\2\2\2%\u0088\3\2\2\2\'\u009a\3\2\2\2)\u00ae")
        buf.write(u"\3\2\2\2+\u00b1\3\2\2\2-\u00b6\3\2\2\2/\60\7?\2\2\60")
        buf.write(u"\4\3\2\2\2\61\62\7\60\2\2\62\6\3\2\2\2\63\64\7*\2\2\64")
        buf.write(u"\b\3\2\2\2\65\66\7+\2\2\66\n\3\2\2\2\67;\7%\2\28:\n\2")
        buf.write(u"\2\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2")
        buf.write(u"\2=;\3\2\2\2>?\b\6\2\2?\f\3\2\2\2@A\7B\2\2A\16\3\2\2")
        buf.write(u"\2BC\7k\2\2CD\7p\2\2DE\7e\2\2EF\7n\2\2FG\7w\2\2GH\7f")
        buf.write(u"\2\2HI\7g\2\2I\20\3\2\2\2JK\7x\2\2KL\7c\2\2LM\7t\2\2")
        buf.write(u"MN\7f\2\2NO\7g\2\2OP\7h\2\2P\22\3\2\2\2QR\7g\2\2RS\7")
        buf.write(u"p\2\2ST\7f\2\2T\24\3\2\2\2UW\7\61\2\2VX\5\37\20\2WV\3")
        buf.write(u"\2\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\61\2\2Z[\5\37\20\2[b\7")
        buf.write(u"\61\2\2\\^\5\37\20\2]_\7/\2\2^]\3\2\2\2^_\3\2\2\2_`\3")
        buf.write(u"\2\2\2`a\5\37\20\2ac\3\2\2\2b\\\3\2\2\2bc\3\2\2\2cd\3")
        buf.write(u"\2\2\2de\7\61\2\2ef\7\61\2\2fj\3\2\2\2gh\5\'\24\2hi\5")
        buf.write(u"\37\20\2ik\3\2\2\2jg\3\2\2\2jk\3\2\2\2kl\3\2\2\2ln\7")
        buf.write(u"\61\2\2mo\5\37\20\2nm\3\2\2\2no\3\2\2\2op\3\2\2\2pq\7")
        buf.write(u"\61\2\2q\26\3\2\2\2rs\7,\2\2s\30\3\2\2\2tu\7\61\2\2u")
        buf.write(u"\32\3\2\2\2vw\7-\2\2w\34\3\2\2\2xy\7/\2\2y\36\3\2\2\2")
        buf.write(u"z\u0080\5!\21\2{\177\5!\21\2|\177\5#\22\2}\177\7a\2\2")
        buf.write(u"~{\3\2\2\2~|\3\2\2\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080")
        buf.write(u"~\3\2\2\2\u0080\u0081\3\2\2\2\u0081 \3\2\2\2\u0082\u0080")
        buf.write(u"\3\2\2\2\u0083\u0084\t\3\2\2\u0084\"\3\2\2\2\u0085\u0086")
        buf.write(u"\4\62;\2\u0086$\3\2\2\2\u0087\u0089\5#\22\2\u0088\u0087")
        buf.write(u"\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0088\3\2\2\2\u008a")
        buf.write(u"\u008b\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u0097\7\60\2")
        buf.write(u"\2\u008d\u008f\5#\22\2\u008e\u008d\3\2\2\2\u008f\u0090")
        buf.write(u"\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write(u"\u0098\3\2\2\2\u0092\u0094\7\"\2\2\u0093\u0092\3\2\2")
        buf.write(u"\2\u0094\u0095\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096")
        buf.write(u"\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u008e\3\2\2\2\u0097")
        buf.write(u"\u0093\3\2\2\2\u0098&\3\2\2\2\u0099\u009b\5#\22\2\u009a")
        buf.write(u"\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009a\3\2\2")
        buf.write(u"\2\u009c\u009d\3\2\2\2\u009d(\3\2\2\2\u009e\u00a2\7$")
        buf.write(u"\2\2\u009f\u00a1\n\4\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a4")
        buf.write(u"\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3")
        buf.write(u"\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00af\7$\2\2")
        buf.write(u"\u00a6\u00aa\7)\2\2\u00a7\u00a9\n\5\2\2\u00a8\u00a7\3")
        buf.write(u"\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00ab\3\2\2\2\u00aa")
        buf.write(u"\u00a8\3\2\2\2\u00ab\u00ad\3\2\2\2\u00ac\u00aa\3\2\2")
        buf.write(u"\2\u00ad\u00af\7)\2\2\u00ae\u009e\3\2\2\2\u00ae\u00a6")
        buf.write(u"\3\2\2\2\u00af*\3\2\2\2\u00b0\u00b2\7\17\2\2\u00b1\u00b0")
        buf.write(u"\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write(u"\u00b4\7\f\2\2\u00b4,\3\2\2\2\u00b5\u00b7\t\6\2\2\u00b6")
        buf.write(u"\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b6\3\2\2")
        buf.write(u"\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write(u"\b\27\2\2\u00bb.\3\2\2\2\25\2;W^bjn~\u0080\u008a\u0090")
        buf.write(u"\u0095\u0097\u009c\u00a2\u00aa\u00ae\u00b1\u00b8\3\b")
        buf.write(u"\2\2")
        return buf.getvalue()


class VarDefLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    LINE_COMMENT = 5
    T = 6
    INCLUDE = 7
    VARDEF = 8
    END = 9
    PATH = 10
    MUL = 11
    DIV = 12
    ADD = 13
    SUB = 14
    ID = 15
    FLOAT = 16
    INT = 17
    STRING = 18
    NL = 19
    WS = 20

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'='", u"'.'", u"'('", u"')'", u"'@'", u"'include'", u"'vardef'", 
            u"'end'", u"'*'", u"'/'", u"'+'", u"'-'" ]

    symbolicNames = [ u"<INVALID>",
            u"LINE_COMMENT", u"T", u"INCLUDE", u"VARDEF", u"END", u"PATH", 
            u"MUL", u"DIV", u"ADD", u"SUB", u"ID", u"FLOAT", u"INT", u"STRING", 
            u"NL", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"LINE_COMMENT", u"T", 
                  u"INCLUDE", u"VARDEF", u"END", u"PATH", u"MUL", u"DIV", 
                  u"ADD", u"SUB", u"ID", u"LETTER", u"DIGIT", u"FLOAT", 
                  u"INT", u"STRING", u"NL", u"WS" ]

    grammarFileName = u"VarDef.g4"

    def __init__(self, input=None):
        super(VarDefLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


