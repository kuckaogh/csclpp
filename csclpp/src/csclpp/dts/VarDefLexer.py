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
import numpy as np


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u",\u013e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write(u"\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r")
        buf.write(u"\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\7\20")
        buf.write(u"~\n\20\f\20\16\20\u0081\13\20\3\20\3\20\3\21\3\21\3\22")
        buf.write(u"\3\22\5\22\u0089\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write(u"\22\7\22\u0092\n\22\f\22\16\22\u0095\13\22\5\22\u0097")
        buf.write(u"\n\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u009f\n\22\3")
        buf.write(u"\22\3\22\5\22\u00a3\n\22\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write(u"\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write(u"\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write(u"\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write(u"\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(u"\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"")
        buf.write(u"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%")
        buf.write(u"\3%\3%\3%\3%\3&\6&\u0104\n&\r&\16&\u0105\3&\3&\7&\u010a")
        buf.write(u"\n&\f&\16&\u010d\13&\3\'\3\'\3\'\3\'\7\'\u0113\n\'\f")
        buf.write(u"\'\16\'\u0116\13\'\3(\3(\3)\3)\3*\6*\u011d\n*\r*\16*")
        buf.write(u"\u011e\3+\3+\7+\u0123\n+\f+\16+\u0126\13+\3+\3+\3+\7")
        buf.write(u"+\u012b\n+\f+\16+\u012e\13+\3+\5+\u0131\n+\3,\5,\u0134")
        buf.write(u"\n,\3,\3,\3-\6-\u0139\n-\r-\16-\u013a\3-\3-\4\u0124\u012c")
        buf.write(u"\2.\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write(u"\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-")
        buf.write(u"\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write(u"I&K\'M(O\2Q\2S)U*W+Y,\3\2\b\4\2\f\f\17\17\4\2//aa\4\2")
        buf.write(u"C\\c|\4\2$$^^\4\2))^^\4\2\13\13\"\"\u014e\2\3\3\2\2\2")
        buf.write(u"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write(u"\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write(u"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write(u"\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2")
        buf.write(u"\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write(u"\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3")
        buf.write(u"\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write(u"A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write(u"\2K\3\2\2\2\2M\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write(u"\2\2Y\3\2\2\2\3[\3\2\2\2\5]\3\2\2\2\7_\3\2\2\2\ta\3\2")
        buf.write(u"\2\2\13c\3\2\2\2\re\3\2\2\2\17g\3\2\2\2\21i\3\2\2\2\23")
        buf.write(u"k\3\2\2\2\25m\3\2\2\2\27p\3\2\2\2\31r\3\2\2\2\33u\3\2")
        buf.write(u"\2\2\35x\3\2\2\2\37{\3\2\2\2!\u0084\3\2\2\2#\u0086\3")
        buf.write(u"\2\2\2%\u00a6\3\2\2\2\'\u00a8\3\2\2\2)\u00aa\3\2\2\2")
        buf.write(u"+\u00ac\3\2\2\2-\u00ae\3\2\2\2/\u00b4\3\2\2\2\61\u00b9")
        buf.write(u"\3\2\2\2\63\u00bd\3\2\2\2\65\u00c5\3\2\2\2\67\u00cc\3")
        buf.write(u"\2\2\29\u00d0\3\2\2\2;\u00d6\3\2\2\2=\u00d9\3\2\2\2?")
        buf.write(u"\u00e0\3\2\2\2A\u00e5\3\2\2\2C\u00eb\3\2\2\2E\u00f2\3")
        buf.write(u"\2\2\2G\u00f6\3\2\2\2I\u00fc\3\2\2\2K\u0103\3\2\2\2M")
        buf.write(u"\u010e\3\2\2\2O\u0117\3\2\2\2Q\u0119\3\2\2\2S\u011c\3")
        buf.write(u"\2\2\2U\u0130\3\2\2\2W\u0133\3\2\2\2Y\u0138\3\2\2\2[")
        buf.write(u"\\\7.\2\2\\\4\3\2\2\2]^\7?\2\2^\6\3\2\2\2_`\7}\2\2`\b")
        buf.write(u"\3\2\2\2ab\7\177\2\2b\n\3\2\2\2cd\7\60\2\2d\f\3\2\2\2")
        buf.write(u"ef\7<\2\2f\16\3\2\2\2gh\7*\2\2h\20\3\2\2\2ij\7+\2\2j")
        buf.write(u"\22\3\2\2\2kl\7@\2\2l\24\3\2\2\2mn\7@\2\2no\7?\2\2o\26")
        buf.write(u"\3\2\2\2pq\7>\2\2q\30\3\2\2\2rs\7>\2\2st\7?\2\2t\32\3")
        buf.write(u"\2\2\2uv\7?\2\2vw\7?\2\2w\34\3\2\2\2xy\7#\2\2yz\7?\2")
        buf.write(u"\2z\36\3\2\2\2{\177\7%\2\2|~\n\2\2\2}|\3\2\2\2~\u0081")
        buf.write(u"\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3")
        buf.write(u"\2\2\2\u0081\177\3\2\2\2\u0082\u0083\b\20\2\2\u0083 ")
        buf.write(u"\3\2\2\2\u0084\u0085\7B\2\2\u0085\"\3\2\2\2\u0086\u0088")
        buf.write(u"\7\61\2\2\u0087\u0089\5M\'\2\u0088\u0087\3\2\2\2\u0088")
        buf.write(u"\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\7\61\2")
        buf.write(u"\2\u008b\u008c\5M\'\2\u008c\u0096\7\61\2\2\u008d\u0093")
        buf.write(u"\5M\'\2\u008e\u0092\5O(\2\u008f\u0092\5Q)\2\u0090\u0092")
        buf.write(u"\t\3\2\2\u0091\u008e\3\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write(u"\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2")
        buf.write(u"\2\u0093\u0094\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093")
        buf.write(u"\3\2\2\2\u0096\u008d\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write(u"\u0098\3\2\2\2\u0098\u0099\7\61\2\2\u0099\u009a\7\61")
        buf.write(u"\2\2\u009a\u009e\3\2\2\2\u009b\u009c\5S*\2\u009c\u009d")
        buf.write(u"\5M\'\2\u009d\u009f\3\2\2\2\u009e\u009b\3\2\2\2\u009e")
        buf.write(u"\u009f\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\7\61\2")
        buf.write(u"\2\u00a1\u00a3\5M\'\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3")
        buf.write(u"\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\7\61\2\2\u00a5")
        buf.write(u"$\3\2\2\2\u00a6\u00a7\7,\2\2\u00a7&\3\2\2\2\u00a8\u00a9")
        buf.write(u"\7\61\2\2\u00a9(\3\2\2\2\u00aa\u00ab\7-\2\2\u00ab*\3")
        buf.write(u"\2\2\2\u00ac\u00ad\7/\2\2\u00ad,\3\2\2\2\u00ae\u00af")
        buf.write(u"\7\"\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7p\2\2\u00b1")
        buf.write(u"\u00b2\7f\2\2\u00b2\u00b3\7\"\2\2\u00b3.\3\2\2\2\u00b4")
        buf.write(u"\u00b5\7\"\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7t\2\2")
        buf.write(u"\u00b7\u00b8\7\"\2\2\u00b8\60\3\2\2\2\u00b9\u00ba\7w")
        buf.write(u"\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7g\2\2\u00bc\62\3")
        buf.write(u"\2\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0")
        buf.write(u"\7e\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3")
        buf.write(u"\7f\2\2\u00c3\u00c4\7g\2\2\u00c4\64\3\2\2\2\u00c5\u00c6")
        buf.write(u"\7x\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write(u"\7f\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb\7h\2\2\u00cb\66")
        buf.write(u"\3\2\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7p\2\2\u00ce")
        buf.write(u"\u00cf\7f\2\2\u00cf8\3\2\2\2\u00d0\u00d1\7c\2\2\u00d1")
        buf.write(u"\u00d2\7t\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7c\2\2\u00d4")
        buf.write(u"\u00d5\7{\2\2\u00d5:\3\2\2\2\u00d6\u00d7\7k\2\2\u00d7")
        buf.write(u"\u00d8\7h\2\2\u00d8<\3\2\2\2\u00d9\u00da\7g\2\2\u00da")
        buf.write(u"\u00db\7n\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7g\2\2\u00dd")
        buf.write(u"\u00de\7k\2\2\u00de\u00df\7h\2\2\u00df>\3\2\2\2\u00e0")
        buf.write(u"\u00e1\7g\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3\7u\2\2\u00e3")
        buf.write(u"\u00e4\7g\2\2\u00e4@\3\2\2\2\u00e5\u00e6\7i\2\2\u00e6")
        buf.write(u"\u00e7\7t\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7w\2\2\u00e9")
        buf.write(u"\u00ea\7r\2\2\u00eaB\3\2\2\2\u00eb\u00ec\7u\2\2\u00ec")
        buf.write(u"\u00ed\7v\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7k\2\2\u00ef")
        buf.write(u"\u00f0\7p\2\2\u00f0\u00f1\7i\2\2\u00f1D\3\2\2\2\u00f2")
        buf.write(u"\u00f3\7k\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7v\2\2\u00f5")
        buf.write(u"F\3\2\2\2\u00f6\u00f7\7h\2\2\u00f7\u00f8\7n\2\2\u00f8")
        buf.write(u"\u00f9\7q\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7v\2\2\u00fb")
        buf.write(u"H\3\2\2\2\u00fc\u00fd\7e\2\2\u00fd\u00fe\7q\2\2\u00fe")
        buf.write(u"\u00ff\7p\2\2\u00ff\u0100\7u\2\2\u0100\u0101\7v\2\2\u0101")
        buf.write(u"J\3\2\2\2\u0102\u0104\4\62;\2\u0103\u0102\3\2\2\2\u0104")
        buf.write(u"\u0105\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2")
        buf.write(u"\2\u0106\u0107\3\2\2\2\u0107\u010b\7\60\2\2\u0108\u010a")
        buf.write(u"\4\62;\2\u0109\u0108\3\2\2\2\u010a\u010d\3\2\2\2\u010b")
        buf.write(u"\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010cL\3\2\2\2\u010d")
        buf.write(u"\u010b\3\2\2\2\u010e\u0114\5O(\2\u010f\u0113\5O(\2\u0110")
        buf.write(u"\u0113\5Q)\2\u0111\u0113\7a\2\2\u0112\u010f\3\2\2\2\u0112")
        buf.write(u"\u0110\3\2\2\2\u0112\u0111\3\2\2\2\u0113\u0116\3\2\2")
        buf.write(u"\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115N\3\2")
        buf.write(u"\2\2\u0116\u0114\3\2\2\2\u0117\u0118\t\4\2\2\u0118P\3")
        buf.write(u"\2\2\2\u0119\u011a\4\62;\2\u011aR\3\2\2\2\u011b\u011d")
        buf.write(u"\5Q)\2\u011c\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e")
        buf.write(u"\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011fT\3\2\2\2\u0120")
        buf.write(u"\u0124\7$\2\2\u0121\u0123\n\5\2\2\u0122\u0121\3\2\2\2")
        buf.write(u"\u0123\u0126\3\2\2\2\u0124\u0125\3\2\2\2\u0124\u0122")
        buf.write(u"\3\2\2\2\u0125\u0127\3\2\2\2\u0126\u0124\3\2\2\2\u0127")
        buf.write(u"\u0131\7$\2\2\u0128\u012c\7)\2\2\u0129\u012b\n\6\2\2")
        buf.write(u"\u012a\u0129\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012d")
        buf.write(u"\3\2\2\2\u012c\u012a\3\2\2\2\u012d\u012f\3\2\2\2\u012e")
        buf.write(u"\u012c\3\2\2\2\u012f\u0131\7)\2\2\u0130\u0120\3\2\2\2")
        buf.write(u"\u0130\u0128\3\2\2\2\u0131V\3\2\2\2\u0132\u0134\7\17")
        buf.write(u"\2\2\u0133\u0132\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135")
        buf.write(u"\3\2\2\2\u0135\u0136\7\f\2\2\u0136X\3\2\2\2\u0137\u0139")
        buf.write(u"\t\7\2\2\u0138\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write(u"\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\3\2\2")
        buf.write(u"\2\u013c\u013d\b-\2\2\u013dZ\3\2\2\2\24\2\177\u0088\u0091")
        buf.write(u"\u0093\u0096\u009e\u00a2\u0105\u010b\u0112\u0114\u011e")
        buf.write(u"\u0124\u012c\u0130\u0133\u013a\3\b\2\2")
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
    T__13 = 14
    LINE_COMMENT = 15
    T = 16
    PATH = 17
    MUL = 18
    DIV = 19
    ADD = 20
    SUB = 21
    AND = 22
    OR = 23
    USE = 24
    INCLUDE = 25
    VARDEF = 26
    END = 27
    ARRAY = 28
    IF = 29
    ELSEIF = 30
    ELSE = 31
    GROUP = 32
    STRING_L = 33
    INT_L = 34
    FLOAT_L = 35
    CONST = 36
    FLOAT = 37
    ID = 38
    INT = 39
    STRING = 40
    NL = 41
    WS = 42

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"','", u"'='", u"'{'", u"'}'", u"'.'", u"':'", u"'('", u"')'", 
            u"'>'", u"'>='", u"'<'", u"'<='", u"'=='", u"'!='", u"'@'", 
            u"'*'", u"'/'", u"'+'", u"'-'", u"' and '", u"' or '", u"'use'", 
            u"'include'", u"'vardef'", u"'end'", u"'array'", u"'if'", u"'elseif'", 
            u"'else'", u"'group'", u"'string'", u"'int'", u"'float'", u"'const'" ]

    symbolicNames = [ u"<INVALID>",
            u"LINE_COMMENT", u"T", u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", 
            u"AND", u"OR", u"USE", u"INCLUDE", u"VARDEF", u"END", u"ARRAY", 
            u"IF", u"ELSEIF", u"ELSE", u"GROUP", u"STRING_L", u"INT_L", 
            u"FLOAT_L", u"CONST", u"FLOAT", u"ID", u"INT", u"STRING", u"NL", 
            u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"T__13", u"LINE_COMMENT", u"T", u"PATH", u"MUL", 
                  u"DIV", u"ADD", u"SUB", u"AND", u"OR", u"USE", u"INCLUDE", 
                  u"VARDEF", u"END", u"ARRAY", u"IF", u"ELSEIF", u"ELSE", 
                  u"GROUP", u"STRING_L", u"INT_L", u"FLOAT_L", u"CONST", 
                  u"FLOAT", u"ID", u"LETTER", u"DIGIT", u"INT", u"STRING", 
                  u"NL", u"WS" ]

    grammarFileName = u"VarDef.g4"

    def __init__(self, input=None):
        super(VarDefLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


