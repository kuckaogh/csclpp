# Generated from VarDef.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
from collections import defaultdict
import collections


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"%\u0113\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6")
        buf.write(u"\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write(u"\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\7\17n\n")
        buf.write(u"\17\f\17\16\17q\13\17\3\17\3\17\3\20\3\20\3\21\3\21\5")
        buf.write(u"\21y\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u0082")
        buf.write(u"\n\21\f\21\16\21\u0085\13\21\5\21\u0087\n\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\5\21\u008f\n\21\3\21\3\21\5\21\u0093")
        buf.write(u"\n\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3")
        buf.write(u"\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write(u"\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3")
        buf.write(u"\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write(u"\3\37\3\37\3\37\7\37\u00d6\n\37\f\37\16\37\u00d9\13\37")
        buf.write(u"\3 \3 \3!\3!\3\"\6\"\u00e0\n\"\r\"\16\"\u00e1\3\"\3\"")
        buf.write(u"\6\"\u00e6\n\"\r\"\16\"\u00e7\3\"\6\"\u00eb\n\"\r\"\16")
        buf.write(u"\"\u00ec\5\"\u00ef\n\"\3#\6#\u00f2\n#\r#\16#\u00f3\3")
        buf.write(u"$\3$\7$\u00f8\n$\f$\16$\u00fb\13$\3$\3$\3$\7$\u0100\n")
        buf.write(u"$\f$\16$\u0103\13$\3$\5$\u0106\n$\3%\5%\u0109\n%\3%\3")
        buf.write(u"%\3&\6&\u010e\n&\r&\16&\u010f\3&\3&\4\u00f9\u0101\2\'")
        buf.write(u"\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write(u"\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write(u"\61\32\63\33\65\34\67\359\36;\37= ?\2A\2C!E\"G#I$K%\3")
        buf.write(u"\2\b\4\2\f\f\17\17\4\2//aa\4\2C\\c|\4\2$$^^\4\2))^^\4")
        buf.write(u"\2\13\13\"\"\u0125\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write(u"\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write(u"\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write(u"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write(u"\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write(u"\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write(u"\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write(u"\2\2\2\2=\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2")
        buf.write(u"I\3\2\2\2\2K\3\2\2\2\3M\3\2\2\2\5O\3\2\2\2\7Q\3\2\2\2")
        buf.write(u"\tS\3\2\2\2\13U\3\2\2\2\rW\3\2\2\2\17Y\3\2\2\2\21\\\3")
        buf.write(u"\2\2\2\23^\3\2\2\2\25a\3\2\2\2\27d\3\2\2\2\31g\3\2\2")
        buf.write(u"\2\33i\3\2\2\2\35k\3\2\2\2\37t\3\2\2\2!v\3\2\2\2#\u0096")
        buf.write(u"\3\2\2\2%\u0098\3\2\2\2\'\u009a\3\2\2\2)\u009c\3\2\2")
        buf.write(u"\2+\u009e\3\2\2\2-\u00a4\3\2\2\2/\u00a9\3\2\2\2\61\u00b1")
        buf.write(u"\3\2\2\2\63\u00b8\3\2\2\2\65\u00bc\3\2\2\2\67\u00c2\3")
        buf.write(u"\2\2\29\u00c5\3\2\2\2;\u00cc\3\2\2\2=\u00d1\3\2\2\2?")
        buf.write(u"\u00da\3\2\2\2A\u00dc\3\2\2\2C\u00df\3\2\2\2E\u00f1\3")
        buf.write(u"\2\2\2G\u0105\3\2\2\2I\u0108\3\2\2\2K\u010d\3\2\2\2M")
        buf.write(u"N\7.\2\2N\4\3\2\2\2OP\7?\2\2P\6\3\2\2\2QR\7\60\2\2R\b")
        buf.write(u"\3\2\2\2ST\7*\2\2T\n\3\2\2\2UV\7+\2\2V\f\3\2\2\2WX\7")
        buf.write(u"@\2\2X\16\3\2\2\2YZ\7@\2\2Z[\7?\2\2[\20\3\2\2\2\\]\7")
        buf.write(u">\2\2]\22\3\2\2\2^_\7>\2\2_`\7?\2\2`\24\3\2\2\2ab\7?")
        buf.write(u"\2\2bc\7?\2\2c\26\3\2\2\2de\7#\2\2ef\7?\2\2f\30\3\2\2")
        buf.write(u"\2gh\7}\2\2h\32\3\2\2\2ij\7\177\2\2j\34\3\2\2\2ko\7%")
        buf.write(u"\2\2ln\n\2\2\2ml\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2")
        buf.write(u"\2pr\3\2\2\2qo\3\2\2\2rs\b\17\2\2s\36\3\2\2\2tu\7B\2")
        buf.write(u"\2u \3\2\2\2vx\7\61\2\2wy\5=\37\2xw\3\2\2\2xy\3\2\2\2")
        buf.write(u"yz\3\2\2\2z{\7\61\2\2{|\5=\37\2|\u0086\7\61\2\2}\u0083")
        buf.write(u"\5=\37\2~\u0082\5? \2\177\u0082\5A!\2\u0080\u0082\t\3")
        buf.write(u"\2\2\u0081~\3\2\2\2\u0081\177\3\2\2\2\u0081\u0080\3\2")
        buf.write(u"\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084")
        buf.write(u"\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0086")
        buf.write(u"}\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write(u"\u0089\7\61\2\2\u0089\u008a\7\61\2\2\u008a\u008e\3\2")
        buf.write(u"\2\2\u008b\u008c\5E#\2\u008c\u008d\5=\37\2\u008d\u008f")
        buf.write(u"\3\2\2\2\u008e\u008b\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write(u"\u0090\3\2\2\2\u0090\u0092\7\61\2\2\u0091\u0093\5=\37")
        buf.write(u"\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094")
        buf.write(u"\3\2\2\2\u0094\u0095\7\61\2\2\u0095\"\3\2\2\2\u0096\u0097")
        buf.write(u"\7,\2\2\u0097$\3\2\2\2\u0098\u0099\7\61\2\2\u0099&\3")
        buf.write(u"\2\2\2\u009a\u009b\7-\2\2\u009b(\3\2\2\2\u009c\u009d")
        buf.write(u"\7/\2\2\u009d*\3\2\2\2\u009e\u009f\7\"\2\2\u009f\u00a0")
        buf.write(u"\7c\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2\7f\2\2\u00a2\u00a3")
        buf.write(u"\7\"\2\2\u00a3,\3\2\2\2\u00a4\u00a5\7\"\2\2\u00a5\u00a6")
        buf.write(u"\7q\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7\"\2\2\u00a8")
        buf.write(u".\3\2\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7p\2\2\u00ab")
        buf.write(u"\u00ac\7e\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae\7w\2\2\u00ae")
        buf.write(u"\u00af\7f\2\2\u00af\u00b0\7g\2\2\u00b0\60\3\2\2\2\u00b1")
        buf.write(u"\u00b2\7x\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4\7t\2\2\u00b4")
        buf.write(u"\u00b5\7f\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7h\2\2\u00b7")
        buf.write(u"\62\3\2\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7p\2\2\u00ba")
        buf.write(u"\u00bb\7f\2\2\u00bb\64\3\2\2\2\u00bc\u00bd\7c\2\2\u00bd")
        buf.write(u"\u00be\7t\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7c\2\2\u00c0")
        buf.write(u"\u00c1\7{\2\2\u00c1\66\3\2\2\2\u00c2\u00c3\7k\2\2\u00c3")
        buf.write(u"\u00c4\7h\2\2\u00c48\3\2\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write(u"\u00c7\7n\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9\7g\2\2\u00c9")
        buf.write(u"\u00ca\7k\2\2\u00ca\u00cb\7h\2\2\u00cb:\3\2\2\2\u00cc")
        buf.write(u"\u00cd\7g\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf\7u\2\2\u00cf")
        buf.write(u"\u00d0\7g\2\2\u00d0<\3\2\2\2\u00d1\u00d7\5? \2\u00d2")
        buf.write(u"\u00d6\5? \2\u00d3\u00d6\5A!\2\u00d4\u00d6\7a\2\2\u00d5")
        buf.write(u"\u00d2\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4\3\2\2")
        buf.write(u"\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8")
        buf.write(u"\3\2\2\2\u00d8>\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db")
        buf.write(u"\t\4\2\2\u00db@\3\2\2\2\u00dc\u00dd\4\62;\2\u00ddB\3")
        buf.write(u"\2\2\2\u00de\u00e0\5A!\2\u00df\u00de\3\2\2\2\u00e0\u00e1")
        buf.write(u"\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write(u"\u00e3\3\2\2\2\u00e3\u00ee\7\60\2\2\u00e4\u00e6\5A!\2")
        buf.write(u"\u00e5\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e5")
        buf.write(u"\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ef\3\2\2\2\u00e9")
        buf.write(u"\u00eb\7\"\2\2\u00ea\u00e9\3\2\2\2\u00eb\u00ec\3\2\2")
        buf.write(u"\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ef")
        buf.write(u"\3\2\2\2\u00ee\u00e5\3\2\2\2\u00ee\u00ea\3\2\2\2\u00ef")
        buf.write(u"D\3\2\2\2\u00f0\u00f2\5A!\2\u00f1\u00f0\3\2\2\2\u00f2")
        buf.write(u"\u00f3\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2")
        buf.write(u"\2\u00f4F\3\2\2\2\u00f5\u00f9\7$\2\2\u00f6\u00f8\n\5")
        buf.write(u"\2\2\u00f7\u00f6\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00fa")
        buf.write(u"\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb")
        buf.write(u"\u00f9\3\2\2\2\u00fc\u0106\7$\2\2\u00fd\u0101\7)\2\2")
        buf.write(u"\u00fe\u0100\n\6\2\2\u00ff\u00fe\3\2\2\2\u0100\u0103")
        buf.write(u"\3\2\2\2\u0101\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0102")
        buf.write(u"\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0106\7)\2\2")
        buf.write(u"\u0105\u00f5\3\2\2\2\u0105\u00fd\3\2\2\2\u0106H\3\2\2")
        buf.write(u"\2\u0107\u0109\7\17\2\2\u0108\u0107\3\2\2\2\u0108\u0109")
        buf.write(u"\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\7\f\2\2\u010b")
        buf.write(u"J\3\2\2\2\u010c\u010e\t\7\2\2\u010d\u010c\3\2\2\2\u010e")
        buf.write(u"\u010f\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2")
        buf.write(u"\2\u0110\u0111\3\2\2\2\u0111\u0112\b&\2\2\u0112L\3\2")
        buf.write(u"\2\2\26\2ox\u0081\u0083\u0086\u008e\u0092\u00d5\u00d7")
        buf.write(u"\u00e1\u00e7\u00ec\u00ee\u00f3\u00f9\u0101\u0105\u0108")
        buf.write(u"\u010f\3\b\2\2")
        return buf.getvalue()


class VarDefLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    LINE_COMMENT = 14
    T = 15
    PATH = 16
    MUL = 17
    DIV = 18
    ADD = 19
    SUB = 20
    AND = 21
    OR = 22
    INCLUDE = 23
    VARDEF = 24
    END = 25
    ARRAY = 26
    IF = 27
    ELSEIF = 28
    ELSE = 29
    ID = 30
    FLOAT = 31
    INT = 32
    STRING = 33
    NL = 34
    WS = 35

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"','", u"'='", u"'.'", u"'('", u"')'", u"'>'", u"'>='", u"'<'", 
            u"'<='", u"'=='", u"'!='", u"'{'", u"'}'", u"'@'", u"'*'", u"'/'", 
            u"'+'", u"'-'", u"' and '", u"' or '", u"'include'", u"'vardef'", 
            u"'end'", u"'array'", u"'if'", u"'elseif'", u"'else'" ]

    symbolicNames = [ u"<INVALID>",
            u"LINE_COMMENT", u"T", u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", 
            u"AND", u"OR", u"INCLUDE", u"VARDEF", u"END", u"ARRAY", u"IF", 
            u"ELSEIF", u"ELSE", u"ID", u"FLOAT", u"INT", u"STRING", u"NL", 
            u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"LINE_COMMENT", u"T", u"PATH", u"MUL", u"DIV", 
                  u"ADD", u"SUB", u"AND", u"OR", u"INCLUDE", u"VARDEF", 
                  u"END", u"ARRAY", u"IF", u"ELSEIF", u"ELSE", u"ID", u"LETTER", 
                  u"DIGIT", u"FLOAT", u"INT", u"STRING", u"NL", u"WS" ]

    grammarFileName = u"VarDef.g4"

    def __init__(self, input=None):
        super(VarDefLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


