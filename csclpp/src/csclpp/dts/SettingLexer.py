# Generated from Setting.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
import Setting as S
import copy


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\22\u009d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\7\5\60")
        buf.write(u"\n\5\f\5\16\5\63\13\5\3\5\3\5\3\6\3\6\7\69\n\6\f\6\16")
        buf.write(u"\6<\13\6\3\6\3\6\3\6\7\6A\n\6\f\6\16\6D\13\6\3\6\5\6")
        buf.write(u"G\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write(u"\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\r\3\r\3\r\3\r\7\rr\n\r\f\r\16\ru\13\r\3\16\3\16")
        buf.write(u"\3\17\3\17\3\20\6\20|\n\20\r\20\16\20}\3\20\3\20\6\20")
        buf.write(u"\u0082\n\20\r\20\16\20\u0083\3\20\6\20\u0087\n\20\r\20")
        buf.write(u"\16\20\u0088\5\20\u008b\n\20\3\21\6\21\u008e\n\21\r\21")
        buf.write(u"\16\21\u008f\3\22\5\22\u0093\n\22\3\22\3\22\3\23\6\23")
        buf.write(u"\u0098\n\23\r\23\16\23\u0099\3\23\3\23\4:B\2\24\3\3\5")
        buf.write(u"\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write(u"\2\35\2\37\17!\20#\21%\22\3\2\7\4\2\f\f\17\17\4\2$$^")
        buf.write(u"^\4\2))^^\4\2C\\c|\4\2\13\13\"\"\u00a8\2\3\3\2\2\2\2")
        buf.write(u"\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write(u"\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write(u"\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write(u"\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5)\3\2\2\2\7+")
        buf.write(u"\3\2\2\2\t-\3\2\2\2\13F\3\2\2\2\rH\3\2\2\2\17L\3\2\2")
        buf.write(u"\2\21R\3\2\2\2\23W\3\2\2\2\25^\3\2\2\2\27g\3\2\2\2\31")
        buf.write(u"m\3\2\2\2\33v\3\2\2\2\35x\3\2\2\2\37{\3\2\2\2!\u008d")
        buf.write(u"\3\2\2\2#\u0092\3\2\2\2%\u0097\3\2\2\2\'(\7?\2\2(\4\3")
        buf.write(u"\2\2\2)*\7.\2\2*\6\3\2\2\2+,\7\60\2\2,\b\3\2\2\2-\61")
        buf.write(u"\7%\2\2.\60\n\2\2\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2")
        buf.write(u"\2\61\62\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\b")
        buf.write(u"\5\2\2\65\n\3\2\2\2\66:\7$\2\2\679\n\3\2\28\67\3\2\2")
        buf.write(u"\29<\3\2\2\2:;\3\2\2\2:8\3\2\2\2;=\3\2\2\2<:\3\2\2\2")
        buf.write(u"=G\7$\2\2>B\7)\2\2?A\n\4\2\2@?\3\2\2\2AD\3\2\2\2BC\3")
        buf.write(u"\2\2\2B@\3\2\2\2CE\3\2\2\2DB\3\2\2\2EG\7)\2\2F\66\3\2")
        buf.write(u"\2\2F>\3\2\2\2G\f\3\2\2\2HI\7g\2\2IJ\7p\2\2JK\7f\2\2")
        buf.write(u"K\16\3\2\2\2LM\7u\2\2MN\7v\2\2NO\7w\2\2OP\7f\2\2PQ\7")
        buf.write(u"{\2\2Q\20\3\2\2\2RS\7f\2\2ST\7c\2\2TU\7v\2\2UV\7c\2\2")
        buf.write(u"V\22\3\2\2\2WX\7x\2\2XY\7c\2\2YZ\7t\2\2Z[\7f\2\2[\\\7")
        buf.write(u"g\2\2\\]\7h\2\2]\24\3\2\2\2^_\7o\2\2_`\7g\2\2`a\7v\2")
        buf.write(u"\2ab\7c\2\2bc\7f\2\2cd\7c\2\2de\7v\2\2ef\7c\2\2f\26\3")
        buf.write(u"\2\2\2gh\7y\2\2hi\7t\2\2ij\7g\2\2jk\7u\2\2kl\7n\2\2l")
        buf.write(u"\30\3\2\2\2ms\5\33\16\2nr\5\33\16\2or\5\35\17\2pr\7a")
        buf.write(u"\2\2qn\3\2\2\2qo\3\2\2\2qp\3\2\2\2ru\3\2\2\2sq\3\2\2")
        buf.write(u"\2st\3\2\2\2t\32\3\2\2\2us\3\2\2\2vw\t\5\2\2w\34\3\2")
        buf.write(u"\2\2xy\4\62;\2y\36\3\2\2\2z|\5\35\17\2{z\3\2\2\2|}\3")
        buf.write(u"\2\2\2}{\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u008a\7\60")
        buf.write(u"\2\2\u0080\u0082\5\35\17\2\u0081\u0080\3\2\2\2\u0082")
        buf.write(u"\u0083\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2")
        buf.write(u"\2\u0084\u008b\3\2\2\2\u0085\u0087\7\"\2\2\u0086\u0085")
        buf.write(u"\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088")
        buf.write(u"\u0089\3\2\2\2\u0089\u008b\3\2\2\2\u008a\u0081\3\2\2")
        buf.write(u"\2\u008a\u0086\3\2\2\2\u008b \3\2\2\2\u008c\u008e\5\35")
        buf.write(u"\17\2\u008d\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u008d")
        buf.write(u"\3\2\2\2\u008f\u0090\3\2\2\2\u0090\"\3\2\2\2\u0091\u0093")
        buf.write(u"\7\17\2\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write(u"\u0094\3\2\2\2\u0094\u0095\7\f\2\2\u0095$\3\2\2\2\u0096")
        buf.write(u"\u0098\t\6\2\2\u0097\u0096\3\2\2\2\u0098\u0099\3\2\2")
        buf.write(u"\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b")
        buf.write(u"\3\2\2\2\u009b\u009c\b\23\2\2\u009c&\3\2\2\2\20\2\61")
        buf.write(u":BFqs}\u0083\u0088\u008a\u008f\u0092\u0099\3\b\2\2")
        return buf.getvalue()


class SettingLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    LINE_COMMENT = 4
    STRING = 5
    END = 6
    STUDY = 7
    DATA = 8
    VARDEF = 9
    METADATA = 10
    WRESL = 11
    ID = 12
    FLOAT = 13
    INT = 14
    NL = 15
    WS = 16

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'='", u"','", u"'.'", u"'end'", u"'study'", u"'data'", u"'vardef'", 
            u"'metadata'", u"'wresl'" ]

    symbolicNames = [ u"<INVALID>",
            u"LINE_COMMENT", u"STRING", u"END", u"STUDY", u"DATA", u"VARDEF", 
            u"METADATA", u"WRESL", u"ID", u"FLOAT", u"INT", u"NL", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"LINE_COMMENT", u"STRING", 
                  u"END", u"STUDY", u"DATA", u"VARDEF", u"METADATA", u"WRESL", 
                  u"ID", u"LETTER", u"DIGIT", u"FLOAT", u"INT", u"NL", u"WS" ]

    grammarFileName = u"Setting.g4"

    def __init__(self, input=None):
        super(SettingLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


