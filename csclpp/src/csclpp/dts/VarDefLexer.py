# Generated from VarDef.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
from collections import defaultdict
import collections
import Error


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\'\u0126\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\3\2\3\2\3\3\3\3\3\4")
        buf.write(u"\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write(u"\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write(u"\3\17\3\17\7\17r\n\17\f\17\16\17u\13\17\3\17\3\17\3\20")
        buf.write(u"\3\20\3\21\3\21\5\21}\n\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\7\21\u0086\n\21\f\21\16\21\u0089\13\21\5\21")
        buf.write(u"\u008b\n\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0093")
        buf.write(u"\n\21\3\21\3\21\5\21\u0097\n\21\3\21\3\21\3\22\3\22\3")
        buf.write(u"\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3")
        buf.write(u"\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write(u"\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(u" \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\7!\u00e9\n!\f!")
        buf.write(u"\16!\u00ec\13!\3\"\3\"\3#\3#\3$\6$\u00f3\n$\r$\16$\u00f4")
        buf.write(u"\3$\3$\6$\u00f9\n$\r$\16$\u00fa\3$\6$\u00fe\n$\r$\16")
        buf.write(u"$\u00ff\5$\u0102\n$\3%\6%\u0105\n%\r%\16%\u0106\3&\3")
        buf.write(u"&\7&\u010b\n&\f&\16&\u010e\13&\3&\3&\3&\7&\u0113\n&\f")
        buf.write(u"&\16&\u0116\13&\3&\5&\u0119\n&\3\'\5\'\u011c\n\'\3\'")
        buf.write(u"\3\'\3(\6(\u0121\n(\r(\16(\u0122\3(\3(\4\u010c\u0114")
        buf.write(u"\2)\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write(u"\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-")
        buf.write(u"\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C\2E\2")
        buf.write(u"G#I$K%M&O\'\3\2\b\4\2\f\f\17\17\4\2//aa\4\2C\\c|\4\2")
        buf.write(u"$$^^\4\2))^^\4\2\13\13\"\"\u0138\2\3\3\2\2\2\2\5\3\2")
        buf.write(u"\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write(u"\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write(u"\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write(u"\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write(u"\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write(u"\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write(u"9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write(u"\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2")
        buf.write(u"\2\3Q\3\2\2\2\5S\3\2\2\2\7U\3\2\2\2\tW\3\2\2\2\13Y\3")
        buf.write(u"\2\2\2\r[\3\2\2\2\17]\3\2\2\2\21_\3\2\2\2\23a\3\2\2\2")
        buf.write(u"\25d\3\2\2\2\27f\3\2\2\2\31i\3\2\2\2\33l\3\2\2\2\35o")
        buf.write(u"\3\2\2\2\37x\3\2\2\2!z\3\2\2\2#\u009a\3\2\2\2%\u009c")
        buf.write(u"\3\2\2\2\'\u009e\3\2\2\2)\u00a0\3\2\2\2+\u00a2\3\2\2")
        buf.write(u"\2-\u00a8\3\2\2\2/\u00ad\3\2\2\2\61\u00b5\3\2\2\2\63")
        buf.write(u"\u00bc\3\2\2\2\65\u00c0\3\2\2\2\67\u00c6\3\2\2\29\u00c9")
        buf.write(u"\3\2\2\2;\u00d0\3\2\2\2=\u00d5\3\2\2\2?\u00db\3\2\2\2")
        buf.write(u"A\u00e4\3\2\2\2C\u00ed\3\2\2\2E\u00ef\3\2\2\2G\u00f2")
        buf.write(u"\3\2\2\2I\u0104\3\2\2\2K\u0118\3\2\2\2M\u011b\3\2\2\2")
        buf.write(u"O\u0120\3\2\2\2QR\7.\2\2R\4\3\2\2\2ST\7}\2\2T\6\3\2\2")
        buf.write(u"\2UV\7\177\2\2V\b\3\2\2\2WX\7?\2\2X\n\3\2\2\2YZ\7\60")
        buf.write(u"\2\2Z\f\3\2\2\2[\\\7*\2\2\\\16\3\2\2\2]^\7+\2\2^\20\3")
        buf.write(u"\2\2\2_`\7@\2\2`\22\3\2\2\2ab\7@\2\2bc\7?\2\2c\24\3\2")
        buf.write(u"\2\2de\7>\2\2e\26\3\2\2\2fg\7>\2\2gh\7?\2\2h\30\3\2\2")
        buf.write(u"\2ij\7?\2\2jk\7?\2\2k\32\3\2\2\2lm\7#\2\2mn\7?\2\2n\34")
        buf.write(u"\3\2\2\2os\7%\2\2pr\n\2\2\2qp\3\2\2\2ru\3\2\2\2sq\3\2")
        buf.write(u"\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2vw\b\17\2\2w\36\3\2")
        buf.write(u"\2\2xy\7B\2\2y \3\2\2\2z|\7\61\2\2{}\5A!\2|{\3\2\2\2")
        buf.write(u"|}\3\2\2\2}~\3\2\2\2~\177\7\61\2\2\177\u0080\5A!\2\u0080")
        buf.write(u"\u008a\7\61\2\2\u0081\u0087\5A!\2\u0082\u0086\5C\"\2")
        buf.write(u"\u0083\u0086\5E#\2\u0084\u0086\t\3\2\2\u0085\u0082\3")
        buf.write(u"\2\2\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086")
        buf.write(u"\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2")
        buf.write(u"\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u0081")
        buf.write(u"\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\3\2\2\2\u008c")
        buf.write(u"\u008d\7\61\2\2\u008d\u008e\7\61\2\2\u008e\u0092\3\2")
        buf.write(u"\2\2\u008f\u0090\5I%\2\u0090\u0091\5A!\2\u0091\u0093")
        buf.write(u"\3\2\2\2\u0092\u008f\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write(u"\u0094\3\2\2\2\u0094\u0096\7\61\2\2\u0095\u0097\5A!\2")
        buf.write(u"\u0096\u0095\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098")
        buf.write(u"\3\2\2\2\u0098\u0099\7\61\2\2\u0099\"\3\2\2\2\u009a\u009b")
        buf.write(u"\7,\2\2\u009b$\3\2\2\2\u009c\u009d\7\61\2\2\u009d&\3")
        buf.write(u"\2\2\2\u009e\u009f\7-\2\2\u009f(\3\2\2\2\u00a0\u00a1")
        buf.write(u"\7/\2\2\u00a1*\3\2\2\2\u00a2\u00a3\7\"\2\2\u00a3\u00a4")
        buf.write(u"\7c\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7f\2\2\u00a6\u00a7")
        buf.write(u"\7\"\2\2\u00a7,\3\2\2\2\u00a8\u00a9\7\"\2\2\u00a9\u00aa")
        buf.write(u"\7q\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac\7\"\2\2\u00ac")
        buf.write(u".\3\2\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7p\2\2\u00af")
        buf.write(u"\u00b0\7e\2\2\u00b0\u00b1\7n\2\2\u00b1\u00b2\7w\2\2\u00b2")
        buf.write(u"\u00b3\7f\2\2\u00b3\u00b4\7g\2\2\u00b4\60\3\2\2\2\u00b5")
        buf.write(u"\u00b6\7x\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7t\2\2\u00b8")
        buf.write(u"\u00b9\7f\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7h\2\2\u00bb")
        buf.write(u"\62\3\2\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7p\2\2\u00be")
        buf.write(u"\u00bf\7f\2\2\u00bf\64\3\2\2\2\u00c0\u00c1\7c\2\2\u00c1")
        buf.write(u"\u00c2\7t\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4\7c\2\2\u00c4")
        buf.write(u"\u00c5\7{\2\2\u00c5\66\3\2\2\2\u00c6\u00c7\7k\2\2\u00c7")
        buf.write(u"\u00c8\7h\2\2\u00c88\3\2\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write(u"\u00cb\7n\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd\7g\2\2\u00cd")
        buf.write(u"\u00ce\7k\2\2\u00ce\u00cf\7h\2\2\u00cf:\3\2\2\2\u00d0")
        buf.write(u"\u00d1\7g\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7u\2\2\u00d3")
        buf.write(u"\u00d4\7g\2\2\u00d4<\3\2\2\2\u00d5\u00d6\7w\2\2\u00d6")
        buf.write(u"\u00d7\7p\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7v\2\2\u00d9")
        buf.write(u"\u00da\7u\2\2\u00da>\3\2\2\2\u00db\u00dc\7e\2\2\u00dc")
        buf.write(u"\u00dd\7c\2\2\u00dd\u00de\7r\2\2\u00de\u00df\7c\2\2\u00df")
        buf.write(u"\u00e0\7e\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7v\2\2\u00e2")
        buf.write(u"\u00e3\7{\2\2\u00e3@\3\2\2\2\u00e4\u00ea\5C\"\2\u00e5")
        buf.write(u"\u00e9\5C\"\2\u00e6\u00e9\5E#\2\u00e7\u00e9\7a\2\2\u00e8")
        buf.write(u"\u00e5\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2")
        buf.write(u"\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb")
        buf.write(u"\3\2\2\2\u00ebB\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ee")
        buf.write(u"\t\4\2\2\u00eeD\3\2\2\2\u00ef\u00f0\4\62;\2\u00f0F\3")
        buf.write(u"\2\2\2\u00f1\u00f3\5E#\2\u00f2\u00f1\3\2\2\2\u00f3\u00f4")
        buf.write(u"\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write(u"\u00f6\3\2\2\2\u00f6\u0101\7\60\2\2\u00f7\u00f9\5E#\2")
        buf.write(u"\u00f8\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00f8")
        buf.write(u"\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u0102\3\2\2\2\u00fc")
        buf.write(u"\u00fe\7\"\2\2\u00fd\u00fc\3\2\2\2\u00fe\u00ff\3\2\2")
        buf.write(u"\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102")
        buf.write(u"\3\2\2\2\u0101\u00f8\3\2\2\2\u0101\u00fd\3\2\2\2\u0102")
        buf.write(u"H\3\2\2\2\u0103\u0105\5E#\2\u0104\u0103\3\2\2\2\u0105")
        buf.write(u"\u0106\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2")
        buf.write(u"\2\u0107J\3\2\2\2\u0108\u010c\7$\2\2\u0109\u010b\n\5")
        buf.write(u"\2\2\u010a\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010d")
        buf.write(u"\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010f\3\2\2\2\u010e")
        buf.write(u"\u010c\3\2\2\2\u010f\u0119\7$\2\2\u0110\u0114\7)\2\2")
        buf.write(u"\u0111\u0113\n\6\2\2\u0112\u0111\3\2\2\2\u0113\u0116")
        buf.write(u"\3\2\2\2\u0114\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0115")
        buf.write(u"\u0117\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0119\7)\2\2")
        buf.write(u"\u0118\u0108\3\2\2\2\u0118\u0110\3\2\2\2\u0119L\3\2\2")
        buf.write(u"\2\u011a\u011c\7\17\2\2\u011b\u011a\3\2\2\2\u011b\u011c")
        buf.write(u"\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e\7\f\2\2\u011e")
        buf.write(u"N\3\2\2\2\u011f\u0121\t\7\2\2\u0120\u011f\3\2\2\2\u0121")
        buf.write(u"\u0122\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2")
        buf.write(u"\2\u0123\u0124\3\2\2\2\u0124\u0125\b(\2\2\u0125P\3\2")
        buf.write(u"\2\2\26\2s|\u0085\u0087\u008a\u0092\u0096\u00e8\u00ea")
        buf.write(u"\u00f4\u00fa\u00ff\u0101\u0106\u010c\u0114\u0118\u011b")
        buf.write(u"\u0122\3\b\2\2")
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
    UNITS = 30
    CAPACITY = 31
    ID = 32
    FLOAT = 33
    INT = 34
    STRING = 35
    NL = 36
    WS = 37

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"','", u"'{'", u"'}'", u"'='", u"'.'", u"'('", u"')'", u"'>'", 
            u"'>='", u"'<'", u"'<='", u"'=='", u"'!='", u"'@'", u"'*'", 
            u"'/'", u"'+'", u"'-'", u"' and '", u"' or '", u"'include'", 
            u"'vardef'", u"'end'", u"'array'", u"'if'", u"'elseif'", u"'else'", 
            u"'units'", u"'capacity'" ]

    symbolicNames = [ u"<INVALID>",
            u"LINE_COMMENT", u"T", u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", 
            u"AND", u"OR", u"INCLUDE", u"VARDEF", u"END", u"ARRAY", u"IF", 
            u"ELSEIF", u"ELSE", u"UNITS", u"CAPACITY", u"ID", u"FLOAT", 
            u"INT", u"STRING", u"NL", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"LINE_COMMENT", u"T", u"PATH", u"MUL", u"DIV", 
                  u"ADD", u"SUB", u"AND", u"OR", u"INCLUDE", u"VARDEF", 
                  u"END", u"ARRAY", u"IF", u"ELSEIF", u"ELSE", u"UNITS", 
                  u"CAPACITY", u"ID", u"LETTER", u"DIGIT", u"FLOAT", u"INT", 
                  u"STRING", u"NL", u"WS" ]

    grammarFileName = u"VarDef.g4"

    def __init__(self, input=None):
        super(VarDefLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


