# Generated from Setting.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
import Setting as S
import Temp as T
import copy


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\21\u0089\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\7\5.\n\5\f\5\16\5")
        buf.write(u"\61\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write(u"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f^\n\f\f\f\16\fa\13\f")
        buf.write(u"\3\r\3\r\3\16\3\16\3\17\3\17\7\17i\n\17\f\17\16\17l\13")
        buf.write(u"\17\3\17\3\17\3\17\7\17q\n\17\f\17\16\17t\13\17\3\17")
        buf.write(u"\5\17w\n\17\3\20\6\20z\n\20\r\20\16\20{\3\21\5\21\177")
        buf.write(u"\n\21\3\21\3\21\3\22\6\22\u0084\n\22\r\22\16\22\u0085")
        buf.write(u"\3\22\3\22\4jr\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write(u"\n\23\13\25\f\27\r\31\2\33\2\35\16\37\17!\20#\21\3\2")
        buf.write(u"\7\4\2\f\f\17\17\4\2C\\c|\4\2$$^^\4\2))^^\4\2\13\13\"")
        buf.write(u"\"\u0090\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write(u"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write(u"\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35\3\2\2")
        buf.write(u"\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5\'")
        buf.write(u"\3\2\2\2\7)\3\2\2\2\t+\3\2\2\2\13\64\3\2\2\2\r8\3\2\2")
        buf.write(u"\2\17>\3\2\2\2\21C\3\2\2\2\23J\3\2\2\2\25S\3\2\2\2\27")
        buf.write(u"Y\3\2\2\2\31b\3\2\2\2\33d\3\2\2\2\35v\3\2\2\2\37y\3\2")
        buf.write(u"\2\2!~\3\2\2\2#\u0083\3\2\2\2%&\7?\2\2&\4\3\2\2\2\'(")
        buf.write(u"\7.\2\2(\6\3\2\2\2)*\7\60\2\2*\b\3\2\2\2+/\7%\2\2,.\n")
        buf.write(u"\2\2\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60")
        buf.write(u"\62\3\2\2\2\61/\3\2\2\2\62\63\b\5\2\2\63\n\3\2\2\2\64")
        buf.write(u"\65\7g\2\2\65\66\7p\2\2\66\67\7f\2\2\67\f\3\2\2\289\7")
        buf.write(u"u\2\29:\7v\2\2:;\7w\2\2;<\7f\2\2<=\7{\2\2=\16\3\2\2\2")
        buf.write(u">?\7f\2\2?@\7c\2\2@A\7v\2\2AB\7c\2\2B\20\3\2\2\2CD\7")
        buf.write(u"x\2\2DE\7c\2\2EF\7t\2\2FG\7f\2\2GH\7g\2\2HI\7h\2\2I\22")
        buf.write(u"\3\2\2\2JK\7o\2\2KL\7g\2\2LM\7v\2\2MN\7c\2\2NO\7f\2\2")
        buf.write(u"OP\7c\2\2PQ\7v\2\2QR\7c\2\2R\24\3\2\2\2ST\7y\2\2TU\7")
        buf.write(u"t\2\2UV\7g\2\2VW\7u\2\2WX\7n\2\2X\26\3\2\2\2Y_\5\31\r")
        buf.write(u"\2Z^\5\31\r\2[^\5\33\16\2\\^\7a\2\2]Z\3\2\2\2][\3\2\2")
        buf.write(u"\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\30\3\2\2")
        buf.write(u"\2a_\3\2\2\2bc\t\3\2\2c\32\3\2\2\2de\4\62;\2e\34\3\2")
        buf.write(u"\2\2fj\7$\2\2gi\n\4\2\2hg\3\2\2\2il\3\2\2\2jk\3\2\2\2")
        buf.write(u"jh\3\2\2\2km\3\2\2\2lj\3\2\2\2mw\7$\2\2nr\7)\2\2oq\n")
        buf.write(u"\5\2\2po\3\2\2\2qt\3\2\2\2rs\3\2\2\2rp\3\2\2\2su\3\2")
        buf.write(u"\2\2tr\3\2\2\2uw\7)\2\2vf\3\2\2\2vn\3\2\2\2w\36\3\2\2")
        buf.write(u"\2xz\5\33\16\2yx\3\2\2\2z{\3\2\2\2{y\3\2\2\2{|\3\2\2")
        buf.write(u"\2| \3\2\2\2}\177\7\17\2\2~}\3\2\2\2~\177\3\2\2\2\177")
        buf.write(u"\u0080\3\2\2\2\u0080\u0081\7\f\2\2\u0081\"\3\2\2\2\u0082")
        buf.write(u"\u0084\t\6\2\2\u0083\u0082\3\2\2\2\u0084\u0085\3\2\2")
        buf.write(u"\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087")
        buf.write(u"\3\2\2\2\u0087\u0088\b\22\2\2\u0088$\3\2\2\2\f\2/]_j")
        buf.write(u"rv{~\u0085\3\b\2\2")
        return buf.getvalue()


class SettingLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    LINE_COMMENT = 4
    END = 5
    STUDY = 6
    DATA = 7
    VARDEF = 8
    METADATA = 9
    WRESL = 10
    ID = 11
    STRING = 12
    INT = 13
    NL = 14
    WS = 15

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'='", u"','", u"'.'", u"'end'", u"'study'", u"'data'", u"'vardef'", 
            u"'metadata'", u"'wresl'" ]

    symbolicNames = [ u"<INVALID>",
            u"LINE_COMMENT", u"END", u"STUDY", u"DATA", u"VARDEF", u"METADATA", 
            u"WRESL", u"ID", u"STRING", u"INT", u"NL", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"LINE_COMMENT", u"END", u"STUDY", 
                  u"DATA", u"VARDEF", u"METADATA", u"WRESL", u"ID", u"LETTER", 
                  u"DIGIT", u"STRING", u"INT", u"NL", u"WS" ]

    grammarFileName = u"Setting.g4"

    def __init__(self, input=None):
        super(SettingLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


