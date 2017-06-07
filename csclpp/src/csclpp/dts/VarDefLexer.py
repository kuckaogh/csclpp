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
        buf.write(u"+\u013f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write(u"\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3")
        buf.write(u"\r\3\r\3\16\3\16\3\16\3\17\3\17\7\17z\n\17\f\17\16\17")
        buf.write(u"}\13\17\3\17\3\17\3\20\3\20\3\21\3\21\5\21\u0085\n\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u008e\n\21\f")
        buf.write(u"\21\16\21\u0091\13\21\5\21\u0093\n\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\5\21\u009b\n\21\3\21\3\21\5\21\u009f")
        buf.write(u"\n\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3")
        buf.write(u"\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write(u"\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3")
        buf.write(u"\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write(u"\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 ")
        buf.write(u"\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#")
        buf.write(u"\3#\3#\3$\3$\3$\3$\3$\3$\3%\6%\u0105\n%\r%\16%\u0106")
        buf.write(u"\3%\3%\7%\u010b\n%\f%\16%\u010e\13%\3&\3&\3&\3&\7&\u0114")
        buf.write(u"\n&\f&\16&\u0117\13&\3\'\3\'\3(\3(\3)\6)\u011e\n)\r)")
        buf.write(u"\16)\u011f\3*\3*\7*\u0124\n*\f*\16*\u0127\13*\3*\3*\3")
        buf.write(u"*\7*\u012c\n*\f*\16*\u012f\13*\3*\5*\u0132\n*\3+\5+\u0135")
        buf.write(u"\n+\3+\3+\3,\6,\u013a\n,\r,\16,\u013b\3,\3,\4\u0125\u012d")
        buf.write(u"\2-\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write(u"\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-")
        buf.write(u"\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write(u"I&K\'M\2O\2Q(S)U*W+\3\2\b\4\2\f\f\17\17\4\2//aa\4\2C")
        buf.write(u"\\c|\4\2$$^^\4\2))^^\4\2\13\13\"\"\u014f\2\3\3\2\2\2")
        buf.write(u"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write(u"\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write(u"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write(u"\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2")
        buf.write(u"\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write(u"\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3")
        buf.write(u"\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write(u"A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write(u"\2K\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write(u"\2\3Y\3\2\2\2\5[\3\2\2\2\7]\3\2\2\2\t_\3\2\2\2\13a\3")
        buf.write(u"\2\2\2\rc\3\2\2\2\17e\3\2\2\2\21g\3\2\2\2\23i\3\2\2\2")
        buf.write(u"\25l\3\2\2\2\27n\3\2\2\2\31q\3\2\2\2\33t\3\2\2\2\35w")
        buf.write(u"\3\2\2\2\37\u0080\3\2\2\2!\u0082\3\2\2\2#\u00a2\3\2\2")
        buf.write(u"\2%\u00a4\3\2\2\2\'\u00a6\3\2\2\2)\u00a8\3\2\2\2+\u00aa")
        buf.write(u"\3\2\2\2-\u00b0\3\2\2\2/\u00b5\3\2\2\2\61\u00bd\3\2\2")
        buf.write(u"\2\63\u00c4\3\2\2\2\65\u00c8\3\2\2\2\67\u00ce\3\2\2\2")
        buf.write(u"9\u00d1\3\2\2\2;\u00d8\3\2\2\2=\u00dd\3\2\2\2?\u00e3")
        buf.write(u"\3\2\2\2A\u00ec\3\2\2\2C\u00f2\3\2\2\2E\u00f9\3\2\2\2")
        buf.write(u"G\u00fd\3\2\2\2I\u0104\3\2\2\2K\u010f\3\2\2\2M\u0118")
        buf.write(u"\3\2\2\2O\u011a\3\2\2\2Q\u011d\3\2\2\2S\u0131\3\2\2\2")
        buf.write(u"U\u0134\3\2\2\2W\u0139\3\2\2\2YZ\7.\2\2Z\4\3\2\2\2[\\")
        buf.write(u"\7}\2\2\\\6\3\2\2\2]^\7\177\2\2^\b\3\2\2\2_`\7?\2\2`")
        buf.write(u"\n\3\2\2\2ab\7\60\2\2b\f\3\2\2\2cd\7*\2\2d\16\3\2\2\2")
        buf.write(u"ef\7+\2\2f\20\3\2\2\2gh\7@\2\2h\22\3\2\2\2ij\7@\2\2j")
        buf.write(u"k\7?\2\2k\24\3\2\2\2lm\7>\2\2m\26\3\2\2\2no\7>\2\2op")
        buf.write(u"\7?\2\2p\30\3\2\2\2qr\7?\2\2rs\7?\2\2s\32\3\2\2\2tu\7")
        buf.write(u"#\2\2uv\7?\2\2v\34\3\2\2\2w{\7%\2\2xz\n\2\2\2yx\3\2\2")
        buf.write(u"\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2")
        buf.write(u"~\177\b\17\2\2\177\36\3\2\2\2\u0080\u0081\7B\2\2\u0081")
        buf.write(u" \3\2\2\2\u0082\u0084\7\61\2\2\u0083\u0085\5K&\2\u0084")
        buf.write(u"\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\3\2\2")
        buf.write(u"\2\u0086\u0087\7\61\2\2\u0087\u0088\5K&\2\u0088\u0092")
        buf.write(u"\7\61\2\2\u0089\u008f\5K&\2\u008a\u008e\5M\'\2\u008b")
        buf.write(u"\u008e\5O(\2\u008c\u008e\t\3\2\2\u008d\u008a\3\2\2\2")
        buf.write(u"\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e\u0091")
        buf.write(u"\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write(u"\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0089\3\2\2")
        buf.write(u"\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095")
        buf.write(u"\7\61\2\2\u0095\u0096\7\61\2\2\u0096\u009a\3\2\2\2\u0097")
        buf.write(u"\u0098\5Q)\2\u0098\u0099\5K&\2\u0099\u009b\3\2\2\2\u009a")
        buf.write(u"\u0097\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\3\2\2")
        buf.write(u"\2\u009c\u009e\7\61\2\2\u009d\u009f\5K&\2\u009e\u009d")
        buf.write(u"\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write(u"\u00a1\7\61\2\2\u00a1\"\3\2\2\2\u00a2\u00a3\7,\2\2\u00a3")
        buf.write(u"$\3\2\2\2\u00a4\u00a5\7\61\2\2\u00a5&\3\2\2\2\u00a6\u00a7")
        buf.write(u"\7-\2\2\u00a7(\3\2\2\2\u00a8\u00a9\7/\2\2\u00a9*\3\2")
        buf.write(u"\2\2\u00aa\u00ab\7\"\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad")
        buf.write(u"\7p\2\2\u00ad\u00ae\7f\2\2\u00ae\u00af\7\"\2\2\u00af")
        buf.write(u",\3\2\2\2\u00b0\u00b1\7\"\2\2\u00b1\u00b2\7q\2\2\u00b2")
        buf.write(u"\u00b3\7t\2\2\u00b3\u00b4\7\"\2\2\u00b4.\3\2\2\2\u00b5")
        buf.write(u"\u00b6\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7e\2\2\u00b8")
        buf.write(u"\u00b9\7n\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb\7f\2\2\u00bb")
        buf.write(u"\u00bc\7g\2\2\u00bc\60\3\2\2\2\u00bd\u00be\7x\2\2\u00be")
        buf.write(u"\u00bf\7c\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7f\2\2\u00c1")
        buf.write(u"\u00c2\7g\2\2\u00c2\u00c3\7h\2\2\u00c3\62\3\2\2\2\u00c4")
        buf.write(u"\u00c5\7g\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7f\2\2\u00c7")
        buf.write(u"\64\3\2\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7t\2\2\u00ca")
        buf.write(u"\u00cb\7t\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7{\2\2\u00cd")
        buf.write(u"\66\3\2\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7h\2\2\u00d0")
        buf.write(u"8\3\2\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3")
        buf.write(u"\u00d4\7u\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7k\2\2\u00d6")
        buf.write(u"\u00d7\7h\2\2\u00d7:\3\2\2\2\u00d8\u00d9\7g\2\2\u00d9")
        buf.write(u"\u00da\7n\2\2\u00da\u00db\7u\2\2\u00db\u00dc\7g\2\2\u00dc")
        buf.write(u"<\3\2\2\2\u00dd\u00de\7w\2\2\u00de\u00df\7p\2\2\u00df")
        buf.write(u"\u00e0\7k\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2\7u\2\2\u00e2")
        buf.write(u">\3\2\2\2\u00e3\u00e4\7e\2\2\u00e4\u00e5\7c\2\2\u00e5")
        buf.write(u"\u00e6\7r\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8\7e\2\2\u00e8")
        buf.write(u"\u00e9\7k\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7{\2\2\u00eb")
        buf.write(u"@\3\2\2\2\u00ec\u00ed\7i\2\2\u00ed\u00ee\7t\2\2\u00ee")
        buf.write(u"\u00ef\7q\2\2\u00ef\u00f0\7w\2\2\u00f0\u00f1\7r\2\2\u00f1")
        buf.write(u"B\3\2\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4\7v\2\2\u00f4")
        buf.write(u"\u00f5\7t\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write(u"\u00f8\7i\2\2\u00f8D\3\2\2\2\u00f9\u00fa\7k\2\2\u00fa")
        buf.write(u"\u00fb\7p\2\2\u00fb\u00fc\7v\2\2\u00fcF\3\2\2\2\u00fd")
        buf.write(u"\u00fe\7h\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100\7q\2\2\u0100")
        buf.write(u"\u0101\7c\2\2\u0101\u0102\7v\2\2\u0102H\3\2\2\2\u0103")
        buf.write(u"\u0105\4\62;\2\u0104\u0103\3\2\2\2\u0105\u0106\3\2\2")
        buf.write(u"\2\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108")
        buf.write(u"\3\2\2\2\u0108\u010c\7\60\2\2\u0109\u010b\4\62;\2\u010a")
        buf.write(u"\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2")
        buf.write(u"\2\u010c\u010d\3\2\2\2\u010dJ\3\2\2\2\u010e\u010c\3\2")
        buf.write(u"\2\2\u010f\u0115\5M\'\2\u0110\u0114\5M\'\2\u0111\u0114")
        buf.write(u"\5O(\2\u0112\u0114\7a\2\2\u0113\u0110\3\2\2\2\u0113\u0111")
        buf.write(u"\3\2\2\2\u0113\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115")
        buf.write(u"\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116L\3\2\2\2\u0117")
        buf.write(u"\u0115\3\2\2\2\u0118\u0119\t\4\2\2\u0119N\3\2\2\2\u011a")
        buf.write(u"\u011b\4\62;\2\u011bP\3\2\2\2\u011c\u011e\5O(\2\u011d")
        buf.write(u"\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u011d\3\2\2")
        buf.write(u"\2\u011f\u0120\3\2\2\2\u0120R\3\2\2\2\u0121\u0125\7$")
        buf.write(u"\2\2\u0122\u0124\n\5\2\2\u0123\u0122\3\2\2\2\u0124\u0127")
        buf.write(u"\3\2\2\2\u0125\u0126\3\2\2\2\u0125\u0123\3\2\2\2\u0126")
        buf.write(u"\u0128\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0132\7$\2\2")
        buf.write(u"\u0129\u012d\7)\2\2\u012a\u012c\n\6\2\2\u012b\u012a\3")
        buf.write(u"\2\2\2\u012c\u012f\3\2\2\2\u012d\u012e\3\2\2\2\u012d")
        buf.write(u"\u012b\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u012d\3\2\2")
        buf.write(u"\2\u0130\u0132\7)\2\2\u0131\u0121\3\2\2\2\u0131\u0129")
        buf.write(u"\3\2\2\2\u0132T\3\2\2\2\u0133\u0135\7\17\2\2\u0134\u0133")
        buf.write(u"\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write(u"\u0137\7\f\2\2\u0137V\3\2\2\2\u0138\u013a\t\7\2\2\u0139")
        buf.write(u"\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0139\3\2\2")
        buf.write(u"\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e")
        buf.write(u"\b,\2\2\u013eX\3\2\2\2\24\2{\u0084\u008d\u008f\u0092")
        buf.write(u"\u009a\u009e\u0106\u010c\u0113\u0115\u011f\u0125\u012d")
        buf.write(u"\u0131\u0134\u013b\3\b\2\2")
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
    GROUP = 32
    STRING_L = 33
    INT_L = 34
    FLOAT_L = 35
    FLOAT = 36
    ID = 37
    INT = 38
    STRING = 39
    NL = 40
    WS = 41

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"','", u"'{'", u"'}'", u"'='", u"'.'", u"'('", u"')'", u"'>'", 
            u"'>='", u"'<'", u"'<='", u"'=='", u"'!='", u"'@'", u"'*'", 
            u"'/'", u"'+'", u"'-'", u"' and '", u"' or '", u"'include'", 
            u"'vardef'", u"'end'", u"'array'", u"'if'", u"'elseif'", u"'else'", 
            u"'units'", u"'capacity'", u"'group'", u"'string'", u"'int'", 
            u"'float'" ]

    symbolicNames = [ u"<INVALID>",
            u"LINE_COMMENT", u"T", u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", 
            u"AND", u"OR", u"INCLUDE", u"VARDEF", u"END", u"ARRAY", u"IF", 
            u"ELSEIF", u"ELSE", u"UNITS", u"CAPACITY", u"GROUP", u"STRING_L", 
            u"INT_L", u"FLOAT_L", u"FLOAT", u"ID", u"INT", u"STRING", u"NL", 
            u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"LINE_COMMENT", u"T", u"PATH", u"MUL", u"DIV", 
                  u"ADD", u"SUB", u"AND", u"OR", u"INCLUDE", u"VARDEF", 
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


