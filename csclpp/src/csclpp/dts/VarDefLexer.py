# Generated from VarDef.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
from collections import defaultdict
import collections
from antlr4.error import Err


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u",\u0145\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write(u"\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f")
        buf.write(u"\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\7\17|\n\17\f\17")
        buf.write(u"\16\17\177\13\17\3\17\3\17\3\20\3\20\3\21\3\21\5\21\u0087")
        buf.write(u"\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u0090\n")
        buf.write(u"\21\f\21\16\21\u0093\13\21\5\21\u0095\n\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\5\21\u009d\n\21\3\21\3\21\5\21\u00a1")
        buf.write(u"\n\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3")
        buf.write(u"\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write(u"\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3")
        buf.write(u"\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write(u"\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write(u"!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#")
        buf.write(u"\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\6&\u010b\n&\r&\16&")
        buf.write(u"\u010c\3&\3&\7&\u0111\n&\f&\16&\u0114\13&\3\'\3\'\3\'")
        buf.write(u"\3\'\7\'\u011a\n\'\f\'\16\'\u011d\13\'\3(\3(\3)\3)\3")
        buf.write(u"*\6*\u0124\n*\r*\16*\u0125\3+\3+\7+\u012a\n+\f+\16+\u012d")
        buf.write(u"\13+\3+\3+\3+\7+\u0132\n+\f+\16+\u0135\13+\3+\5+\u0138")
        buf.write(u"\n+\3,\5,\u013b\n,\3,\3,\3-\6-\u0140\n-\r-\16-\u0141")
        buf.write(u"\3-\3-\4\u012b\u0133\2.\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write(u"\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write(u"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(u";\37= ?!A\"C#E$G%I&K\'M(O\2Q\2S)U*W+Y,\3\2\b\4\2\f\f")
        buf.write(u"\17\17\4\2//aa\4\2C\\c|\4\2$$^^\4\2))^^\4\2\13\13\"\"")
        buf.write(u"\u0155\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write(u"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write(u"\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write(u"\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write(u"#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write(u"\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write(u"\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write(u"\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write(u"\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2S\3\2\2\2\2")
        buf.write(u"U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\3[\3\2\2\2\5]\3\2\2\2")
        buf.write(u"\7_\3\2\2\2\ta\3\2\2\2\13c\3\2\2\2\re\3\2\2\2\17g\3\2")
        buf.write(u"\2\2\21i\3\2\2\2\23k\3\2\2\2\25n\3\2\2\2\27p\3\2\2\2")
        buf.write(u"\31s\3\2\2\2\33v\3\2\2\2\35y\3\2\2\2\37\u0082\3\2\2\2")
        buf.write(u"!\u0084\3\2\2\2#\u00a4\3\2\2\2%\u00a6\3\2\2\2\'\u00a8")
        buf.write(u"\3\2\2\2)\u00aa\3\2\2\2+\u00ac\3\2\2\2-\u00b2\3\2\2\2")
        buf.write(u"/\u00b7\3\2\2\2\61\u00bb\3\2\2\2\63\u00c3\3\2\2\2\65")
        buf.write(u"\u00ca\3\2\2\2\67\u00ce\3\2\2\29\u00d4\3\2\2\2;\u00d7")
        buf.write(u"\3\2\2\2=\u00de\3\2\2\2?\u00e3\3\2\2\2A\u00e9\3\2\2\2")
        buf.write(u"C\u00f2\3\2\2\2E\u00f8\3\2\2\2G\u00ff\3\2\2\2I\u0103")
        buf.write(u"\3\2\2\2K\u010a\3\2\2\2M\u0115\3\2\2\2O\u011e\3\2\2\2")
        buf.write(u"Q\u0120\3\2\2\2S\u0123\3\2\2\2U\u0137\3\2\2\2W\u013a")
        buf.write(u"\3\2\2\2Y\u013f\3\2\2\2[\\\7.\2\2\\\4\3\2\2\2]^\7}\2")
        buf.write(u"\2^\6\3\2\2\2_`\7\177\2\2`\b\3\2\2\2ab\7?\2\2b\n\3\2")
        buf.write(u"\2\2cd\7\60\2\2d\f\3\2\2\2ef\7*\2\2f\16\3\2\2\2gh\7+")
        buf.write(u"\2\2h\20\3\2\2\2ij\7@\2\2j\22\3\2\2\2kl\7@\2\2lm\7?\2")
        buf.write(u"\2m\24\3\2\2\2no\7>\2\2o\26\3\2\2\2pq\7>\2\2qr\7?\2\2")
        buf.write(u"r\30\3\2\2\2st\7?\2\2tu\7?\2\2u\32\3\2\2\2vw\7#\2\2w")
        buf.write(u"x\7?\2\2x\34\3\2\2\2y}\7%\2\2z|\n\2\2\2{z\3\2\2\2|\177")
        buf.write(u"\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080\3\2\2\2\177}\3\2")
        buf.write(u"\2\2\u0080\u0081\b\17\2\2\u0081\36\3\2\2\2\u0082\u0083")
        buf.write(u"\7B\2\2\u0083 \3\2\2\2\u0084\u0086\7\61\2\2\u0085\u0087")
        buf.write(u"\5M\'\2\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write(u"\u0088\3\2\2\2\u0088\u0089\7\61\2\2\u0089\u008a\5M\'")
        buf.write(u"\2\u008a\u0094\7\61\2\2\u008b\u0091\5M\'\2\u008c\u0090")
        buf.write(u"\5O(\2\u008d\u0090\5Q)\2\u008e\u0090\t\3\2\2\u008f\u008c")
        buf.write(u"\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090")
        buf.write(u"\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2")
        buf.write(u"\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u008b")
        buf.write(u"\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write(u"\u0097\7\61\2\2\u0097\u0098\7\61\2\2\u0098\u009c\3\2")
        buf.write(u"\2\2\u0099\u009a\5S*\2\u009a\u009b\5M\'\2\u009b\u009d")
        buf.write(u"\3\2\2\2\u009c\u0099\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write(u"\u009e\3\2\2\2\u009e\u00a0\7\61\2\2\u009f\u00a1\5M\'")
        buf.write(u"\2\u00a0\u009f\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2")
        buf.write(u"\3\2\2\2\u00a2\u00a3\7\61\2\2\u00a3\"\3\2\2\2\u00a4\u00a5")
        buf.write(u"\7,\2\2\u00a5$\3\2\2\2\u00a6\u00a7\7\61\2\2\u00a7&\3")
        buf.write(u"\2\2\2\u00a8\u00a9\7-\2\2\u00a9(\3\2\2\2\u00aa\u00ab")
        buf.write(u"\7/\2\2\u00ab*\3\2\2\2\u00ac\u00ad\7\"\2\2\u00ad\u00ae")
        buf.write(u"\7c\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7f\2\2\u00b0\u00b1")
        buf.write(u"\7\"\2\2\u00b1,\3\2\2\2\u00b2\u00b3\7\"\2\2\u00b3\u00b4")
        buf.write(u"\7q\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6\7\"\2\2\u00b6")
        buf.write(u".\3\2\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9\7u\2\2\u00b9")
        buf.write(u"\u00ba\7g\2\2\u00ba\60\3\2\2\2\u00bb\u00bc\7k\2\2\u00bc")
        buf.write(u"\u00bd\7p\2\2\u00bd\u00be\7e\2\2\u00be\u00bf\7n\2\2\u00bf")
        buf.write(u"\u00c0\7w\2\2\u00c0\u00c1\7f\2\2\u00c1\u00c2\7g\2\2\u00c2")
        buf.write(u"\62\3\2\2\2\u00c3\u00c4\7x\2\2\u00c4\u00c5\7c\2\2\u00c5")
        buf.write(u"\u00c6\7t\2\2\u00c6\u00c7\7f\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write(u"\u00c9\7h\2\2\u00c9\64\3\2\2\2\u00ca\u00cb\7g\2\2\u00cb")
        buf.write(u"\u00cc\7p\2\2\u00cc\u00cd\7f\2\2\u00cd\66\3\2\2\2\u00ce")
        buf.write(u"\u00cf\7c\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1\7t\2\2\u00d1")
        buf.write(u"\u00d2\7c\2\2\u00d2\u00d3\7{\2\2\u00d38\3\2\2\2\u00d4")
        buf.write(u"\u00d5\7k\2\2\u00d5\u00d6\7h\2\2\u00d6:\3\2\2\2\u00d7")
        buf.write(u"\u00d8\7g\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da\7u\2\2\u00da")
        buf.write(u"\u00db\7g\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7h\2\2\u00dd")
        buf.write(u"<\3\2\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7n\2\2\u00e0")
        buf.write(u"\u00e1\7u\2\2\u00e1\u00e2\7g\2\2\u00e2>\3\2\2\2\u00e3")
        buf.write(u"\u00e4\7w\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7k\2\2\u00e6")
        buf.write(u"\u00e7\7v\2\2\u00e7\u00e8\7u\2\2\u00e8@\3\2\2\2\u00e9")
        buf.write(u"\u00ea\7e\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7r\2\2\u00ec")
        buf.write(u"\u00ed\7c\2\2\u00ed\u00ee\7e\2\2\u00ee\u00ef\7k\2\2\u00ef")
        buf.write(u"\u00f0\7v\2\2\u00f0\u00f1\7{\2\2\u00f1B\3\2\2\2\u00f2")
        buf.write(u"\u00f3\7i\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7q\2\2\u00f5")
        buf.write(u"\u00f6\7w\2\2\u00f6\u00f7\7r\2\2\u00f7D\3\2\2\2\u00f8")
        buf.write(u"\u00f9\7u\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7t\2\2\u00fb")
        buf.write(u"\u00fc\7k\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7i\2\2\u00fe")
        buf.write(u"F\3\2\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7p\2\2\u0101")
        buf.write(u"\u0102\7v\2\2\u0102H\3\2\2\2\u0103\u0104\7h\2\2\u0104")
        buf.write(u"\u0105\7n\2\2\u0105\u0106\7q\2\2\u0106\u0107\7c\2\2\u0107")
        buf.write(u"\u0108\7v\2\2\u0108J\3\2\2\2\u0109\u010b\4\62;\2\u010a")
        buf.write(u"\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010a\3\2\2")
        buf.write(u"\2\u010c\u010d\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0112")
        buf.write(u"\7\60\2\2\u010f\u0111\4\62;\2\u0110\u010f\3\2\2\2\u0111")
        buf.write(u"\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2")
        buf.write(u"\2\u0113L\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u011b\5O")
        buf.write(u"(\2\u0116\u011a\5O(\2\u0117\u011a\5Q)\2\u0118\u011a\7")
        buf.write(u"a\2\2\u0119\u0116\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u0118")
        buf.write(u"\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b")
        buf.write(u"\u011c\3\2\2\2\u011cN\3\2\2\2\u011d\u011b\3\2\2\2\u011e")
        buf.write(u"\u011f\t\4\2\2\u011fP\3\2\2\2\u0120\u0121\4\62;\2\u0121")
        buf.write(u"R\3\2\2\2\u0122\u0124\5Q)\2\u0123\u0122\3\2\2\2\u0124")
        buf.write(u"\u0125\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2")
        buf.write(u"\2\u0126T\3\2\2\2\u0127\u012b\7$\2\2\u0128\u012a\n\5")
        buf.write(u"\2\2\u0129\u0128\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u012c")
        buf.write(u"\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u012e\3\2\2\2\u012d")
        buf.write(u"\u012b\3\2\2\2\u012e\u0138\7$\2\2\u012f\u0133\7)\2\2")
        buf.write(u"\u0130\u0132\n\6\2\2\u0131\u0130\3\2\2\2\u0132\u0135")
        buf.write(u"\3\2\2\2\u0133\u0134\3\2\2\2\u0133\u0131\3\2\2\2\u0134")
        buf.write(u"\u0136\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0138\7)\2\2")
        buf.write(u"\u0137\u0127\3\2\2\2\u0137\u012f\3\2\2\2\u0138V\3\2\2")
        buf.write(u"\2\u0139\u013b\7\17\2\2\u013a\u0139\3\2\2\2\u013a\u013b")
        buf.write(u"\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\7\f\2\2\u013d")
        buf.write(u"X\3\2\2\2\u013e\u0140\t\7\2\2\u013f\u013e\3\2\2\2\u0140")
        buf.write(u"\u0141\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2")
        buf.write(u"\2\u0142\u0143\3\2\2\2\u0143\u0144\b-\2\2\u0144Z\3\2")
        buf.write(u"\2\2\24\2}\u0086\u008f\u0091\u0094\u009c\u00a0\u010c")
        buf.write(u"\u0112\u0119\u011b\u0125\u012b\u0133\u0137\u013a\u0141")
        buf.write(u"\3\b\2\2")
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
    USE = 23
    INCLUDE = 24
    VARDEF = 25
    END = 26
    ARRAY = 27
    IF = 28
    ELSEIF = 29
    ELSE = 30
    UNITS = 31
    CAPACITY = 32
    GROUP = 33
    STRING_L = 34
    INT_L = 35
    FLOAT_L = 36
    FLOAT = 37
    ID = 38
    INT = 39
    STRING = 40
    NL = 41
    WS = 42

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"','", u"'{'", u"'}'", u"'='", u"'.'", u"'('", u"')'", u"'>'", 
            u"'>='", u"'<'", u"'<='", u"'=='", u"'!='", u"'@'", u"'*'", 
            u"'/'", u"'+'", u"'-'", u"' and '", u"' or '", u"'use'", u"'include'", 
            u"'vardef'", u"'end'", u"'array'", u"'if'", u"'elseif'", u"'else'", 
            u"'units'", u"'capacity'", u"'group'", u"'string'", u"'int'", 
            u"'float'" ]

    symbolicNames = [ u"<INVALID>",
            u"LINE_COMMENT", u"T", u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", 
            u"AND", u"OR", u"USE", u"INCLUDE", u"VARDEF", u"END", u"ARRAY", 
            u"IF", u"ELSEIF", u"ELSE", u"UNITS", u"CAPACITY", u"GROUP", 
            u"STRING_L", u"INT_L", u"FLOAT_L", u"FLOAT", u"ID", u"INT", 
            u"STRING", u"NL", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"LINE_COMMENT", u"T", u"PATH", u"MUL", u"DIV", 
                  u"ADD", u"SUB", u"AND", u"OR", u"USE", u"INCLUDE", u"VARDEF", 
                  u"END", u"ARRAY", u"IF", u"ELSEIF", u"ELSE", u"UNITS", 
                  u"CAPACITY", u"GROUP", u"STRING_L", u"INT_L", u"FLOAT_L", 
                  u"FLOAT", u"ID", u"LETTER", u"DIGIT", u"INT", u"STRING", 
                  u"NL", u"WS" ]

    grammarFileName = u"VarDef.g4"

    def __init__(self, input=None):
        super(VarDefLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


