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
        buf.write(u".\u0173\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write(u"\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13")
        buf.write(u"\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write(u"\20\3\20\7\20\u0082\n\20\f\20\16\20\u0085\13\20\3\20")
        buf.write(u"\3\20\3\21\3\21\3\22\3\22\5\22\u008d\n\22\3\22\3\22\3")
        buf.write(u"\22\3\22\3\22\3\22\3\22\7\22\u0096\n\22\f\22\16\22\u0099")
        buf.write(u"\13\22\5\22\u009b\n\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\5\22\u00a3\n\22\3\22\3\22\5\22\u00a7\n\22\3\22\3\22")
        buf.write(u"\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write(u"\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write(u"\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3")
        buf.write(u"\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!")
        buf.write(u"\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$")
        buf.write(u"\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3")
        buf.write(u"&\3&\3&\5&\u0110\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\5\'\u0136\n\'\3(\6(\u0139\n(\r(\16(\u013a\3(\3")
        buf.write(u"(\7(\u013f\n(\f(\16(\u0142\13(\3)\3)\3)\3)\7)\u0148\n")
        buf.write(u")\f)\16)\u014b\13)\3*\3*\3+\3+\3,\6,\u0152\n,\r,\16,")
        buf.write(u"\u0153\3-\3-\7-\u0158\n-\f-\16-\u015b\13-\3-\3-\3-\7")
        buf.write(u"-\u0160\n-\f-\16-\u0163\13-\3-\5-\u0166\n-\3.\5.\u0169")
        buf.write(u"\n.\3.\3.\3/\6/\u016e\n/\r/\16/\u016f\3/\3/\4\u0159\u0161")
        buf.write(u"\2\60\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write(u"\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-")
        buf.write(u"\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write(u"I&K\'M(O)Q*S\2U\2W+Y,[-].\3\2\b\4\2\f\f\17\17\4\2//a")
        buf.write(u"a\4\2C\\c|\4\2$$^^\4\2))^^\4\2\13\13\"\"\u018f\2\3\3")
        buf.write(u"\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write(u"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write(u"\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write(u"\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write(u"\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write(u"/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write(u"\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2")
        buf.write(u"\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2")
        buf.write(u"\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2W\3\2")
        buf.write(u"\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\3_\3\2\2\2\5a\3")
        buf.write(u"\2\2\2\7c\3\2\2\2\te\3\2\2\2\13g\3\2\2\2\ri\3\2\2\2\17")
        buf.write(u"k\3\2\2\2\21m\3\2\2\2\23o\3\2\2\2\25q\3\2\2\2\27t\3\2")
        buf.write(u"\2\2\31v\3\2\2\2\33y\3\2\2\2\35|\3\2\2\2\37\177\3\2\2")
        buf.write(u"\2!\u0088\3\2\2\2#\u008a\3\2\2\2%\u00aa\3\2\2\2\'\u00ac")
        buf.write(u"\3\2\2\2)\u00ae\3\2\2\2+\u00b0\3\2\2\2-\u00b2\3\2\2\2")
        buf.write(u"/\u00b8\3\2\2\2\61\u00bd\3\2\2\2\63\u00c1\3\2\2\2\65")
        buf.write(u"\u00c9\3\2\2\2\67\u00d0\3\2\2\29\u00d4\3\2\2\2;\u00da")
        buf.write(u"\3\2\2\2=\u00dd\3\2\2\2?\u00e4\3\2\2\2A\u00e9\3\2\2\2")
        buf.write(u"C\u00ef\3\2\2\2E\u00f6\3\2\2\2G\u00fa\3\2\2\2I\u0100")
        buf.write(u"\3\2\2\2K\u010f\3\2\2\2M\u0135\3\2\2\2O\u0138\3\2\2\2")
        buf.write(u"Q\u0143\3\2\2\2S\u014c\3\2\2\2U\u014e\3\2\2\2W\u0151")
        buf.write(u"\3\2\2\2Y\u0165\3\2\2\2[\u0168\3\2\2\2]\u016d\3\2\2\2")
        buf.write(u"_`\7.\2\2`\4\3\2\2\2ab\7?\2\2b\6\3\2\2\2cd\7}\2\2d\b")
        buf.write(u"\3\2\2\2ef\7\177\2\2f\n\3\2\2\2gh\7\60\2\2h\f\3\2\2\2")
        buf.write(u"ij\7<\2\2j\16\3\2\2\2kl\7*\2\2l\20\3\2\2\2mn\7+\2\2n")
        buf.write(u"\22\3\2\2\2op\7@\2\2p\24\3\2\2\2qr\7@\2\2rs\7?\2\2s\26")
        buf.write(u"\3\2\2\2tu\7>\2\2u\30\3\2\2\2vw\7>\2\2wx\7?\2\2x\32\3")
        buf.write(u"\2\2\2yz\7?\2\2z{\7?\2\2{\34\3\2\2\2|}\7#\2\2}~\7?\2")
        buf.write(u"\2~\36\3\2\2\2\177\u0083\7%\2\2\u0080\u0082\n\2\2\2\u0081")
        buf.write(u"\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2")
        buf.write(u"\2\u0083\u0084\3\2\2\2\u0084\u0086\3\2\2\2\u0085\u0083")
        buf.write(u"\3\2\2\2\u0086\u0087\b\20\2\2\u0087 \3\2\2\2\u0088\u0089")
        buf.write(u"\7B\2\2\u0089\"\3\2\2\2\u008a\u008c\7\61\2\2\u008b\u008d")
        buf.write(u"\5Q)\2\u008c\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write(u"\u008e\3\2\2\2\u008e\u008f\7\61\2\2\u008f\u0090\5Q)\2")
        buf.write(u"\u0090\u009a\7\61\2\2\u0091\u0097\5Q)\2\u0092\u0096\5")
        buf.write(u"S*\2\u0093\u0096\5U+\2\u0094\u0096\t\3\2\2\u0095\u0092")
        buf.write(u"\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096")
        buf.write(u"\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2")
        buf.write(u"\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u0091")
        buf.write(u"\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write(u"\u009d\7\61\2\2\u009d\u009e\7\61\2\2\u009e\u00a2\3\2")
        buf.write(u"\2\2\u009f\u00a0\5W,\2\u00a0\u00a1\5Q)\2\u00a1\u00a3")
        buf.write(u"\3\2\2\2\u00a2\u009f\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write(u"\u00a4\3\2\2\2\u00a4\u00a6\7\61\2\2\u00a5\u00a7\5Q)\2")
        buf.write(u"\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8")
        buf.write(u"\3\2\2\2\u00a8\u00a9\7\61\2\2\u00a9$\3\2\2\2\u00aa\u00ab")
        buf.write(u"\7,\2\2\u00ab&\3\2\2\2\u00ac\u00ad\7\61\2\2\u00ad(\3")
        buf.write(u"\2\2\2\u00ae\u00af\7-\2\2\u00af*\3\2\2\2\u00b0\u00b1")
        buf.write(u"\7/\2\2\u00b1,\3\2\2\2\u00b2\u00b3\7\"\2\2\u00b3\u00b4")
        buf.write(u"\7c\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7f\2\2\u00b6\u00b7")
        buf.write(u"\7\"\2\2\u00b7.\3\2\2\2\u00b8\u00b9\7\"\2\2\u00b9\u00ba")
        buf.write(u"\7q\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc\7\"\2\2\u00bc")
        buf.write(u"\60\3\2\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7u\2\2\u00bf")
        buf.write(u"\u00c0\7g\2\2\u00c0\62\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2")
        buf.write(u"\u00c3\7p\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7n\2\2\u00c5")
        buf.write(u"\u00c6\7w\2\2\u00c6\u00c7\7f\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write(u"\64\3\2\2\2\u00c9\u00ca\7x\2\2\u00ca\u00cb\7c\2\2\u00cb")
        buf.write(u"\u00cc\7t\2\2\u00cc\u00cd\7f\2\2\u00cd\u00ce\7g\2\2\u00ce")
        buf.write(u"\u00cf\7h\2\2\u00cf\66\3\2\2\2\u00d0\u00d1\7g\2\2\u00d1")
        buf.write(u"\u00d2\7p\2\2\u00d2\u00d3\7f\2\2\u00d38\3\2\2\2\u00d4")
        buf.write(u"\u00d5\7c\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7t\2\2\u00d7")
        buf.write(u"\u00d8\7c\2\2\u00d8\u00d9\7{\2\2\u00d9:\3\2\2\2\u00da")
        buf.write(u"\u00db\7k\2\2\u00db\u00dc\7h\2\2\u00dc<\3\2\2\2\u00dd")
        buf.write(u"\u00de\7g\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7u\2\2\u00e0")
        buf.write(u"\u00e1\7g\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7h\2\2\u00e3")
        buf.write(u">\3\2\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7n\2\2\u00e6")
        buf.write(u"\u00e7\7u\2\2\u00e7\u00e8\7g\2\2\u00e8@\3\2\2\2\u00e9")
        buf.write(u"\u00ea\7i\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7q\2\2\u00ec")
        buf.write(u"\u00ed\7w\2\2\u00ed\u00ee\7r\2\2\u00eeB\3\2\2\2\u00ef")
        buf.write(u"\u00f0\7u\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7t\2\2\u00f2")
        buf.write(u"\u00f3\7k\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7i\2\2\u00f5")
        buf.write(u"D\3\2\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8")
        buf.write(u"\u00f9\7v\2\2\u00f9F\3\2\2\2\u00fa\u00fb\7h\2\2\u00fb")
        buf.write(u"\u00fc\7n\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7c\2\2\u00fe")
        buf.write(u"\u00ff\7v\2\2\u00ffH\3\2\2\2\u0100\u0101\7e\2\2\u0101")
        buf.write(u"\u0102\7q\2\2\u0102\u0103\7p\2\2\u0103\u0104\7u\2\2\u0104")
        buf.write(u"\u0105\7v\2\2\u0105J\3\2\2\2\u0106\u0107\7{\2\2\u0107")
        buf.write(u"\u0108\7g\2\2\u0108\u0109\7c\2\2\u0109\u0110\7t\2\2\u010a")
        buf.write(u"\u010b\7o\2\2\u010b\u010c\7q\2\2\u010c\u010d\7p\2\2\u010d")
        buf.write(u"\u010e\7v\2\2\u010e\u0110\7j\2\2\u010f\u0106\3\2\2\2")
        buf.write(u"\u010f\u010a\3\2\2\2\u0110L\3\2\2\2\u0111\u0112\7q\2")
        buf.write(u"\2\u0112\u0113\7e\2\2\u0113\u0136\7v\2\2\u0114\u0115")
        buf.write(u"\7p\2\2\u0115\u0116\7q\2\2\u0116\u0136\7x\2\2\u0117\u0118")
        buf.write(u"\7f\2\2\u0118\u0119\7g\2\2\u0119\u0136\7e\2\2\u011a\u011b")
        buf.write(u"\7l\2\2\u011b\u011c\7c\2\2\u011c\u0136\7p\2\2\u011d\u011e")
        buf.write(u"\7h\2\2\u011e\u011f\7g\2\2\u011f\u0136\7d\2\2\u0120\u0121")
        buf.write(u"\7o\2\2\u0121\u0122\7c\2\2\u0122\u0136\7t\2\2\u0123\u0124")
        buf.write(u"\7c\2\2\u0124\u0125\7r\2\2\u0125\u0136\7t\2\2\u0126\u0127")
        buf.write(u"\7o\2\2\u0127\u0128\7c\2\2\u0128\u0136\7{\2\2\u0129\u012a")
        buf.write(u"\7l\2\2\u012a\u012b\7w\2\2\u012b\u0136\7p\2\2\u012c\u012d")
        buf.write(u"\7l\2\2\u012d\u012e\7w\2\2\u012e\u0136\7n\2\2\u012f\u0130")
        buf.write(u"\7c\2\2\u0130\u0131\7w\2\2\u0131\u0136\7i\2\2\u0132\u0133")
        buf.write(u"\7u\2\2\u0133\u0134\7g\2\2\u0134\u0136\7r\2\2\u0135\u0111")
        buf.write(u"\3\2\2\2\u0135\u0114\3\2\2\2\u0135\u0117\3\2\2\2\u0135")
        buf.write(u"\u011a\3\2\2\2\u0135\u011d\3\2\2\2\u0135\u0120\3\2\2")
        buf.write(u"\2\u0135\u0123\3\2\2\2\u0135\u0126\3\2\2\2\u0135\u0129")
        buf.write(u"\3\2\2\2\u0135\u012c\3\2\2\2\u0135\u012f\3\2\2\2\u0135")
        buf.write(u"\u0132\3\2\2\2\u0136N\3\2\2\2\u0137\u0139\4\62;\2\u0138")
        buf.write(u"\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u0138\3\2\2")
        buf.write(u"\2\u013a\u013b\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u0140")
        buf.write(u"\7\60\2\2\u013d\u013f\4\62;\2\u013e\u013d\3\2\2\2\u013f")
        buf.write(u"\u0142\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2")
        buf.write(u"\2\u0141P\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0149\5S")
        buf.write(u"*\2\u0144\u0148\5S*\2\u0145\u0148\5U+\2\u0146\u0148\7")
        buf.write(u"a\2\2\u0147\u0144\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0146")
        buf.write(u"\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149")
        buf.write(u"\u014a\3\2\2\2\u014aR\3\2\2\2\u014b\u0149\3\2\2\2\u014c")
        buf.write(u"\u014d\t\4\2\2\u014dT\3\2\2\2\u014e\u014f\4\62;\2\u014f")
        buf.write(u"V\3\2\2\2\u0150\u0152\5U+\2\u0151\u0150\3\2\2\2\u0152")
        buf.write(u"\u0153\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2")
        buf.write(u"\2\u0154X\3\2\2\2\u0155\u0159\7$\2\2\u0156\u0158\n\5")
        buf.write(u"\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u015a")
        buf.write(u"\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015c\3\2\2\2\u015b")
        buf.write(u"\u0159\3\2\2\2\u015c\u0166\7$\2\2\u015d\u0161\7)\2\2")
        buf.write(u"\u015e\u0160\n\6\2\2\u015f\u015e\3\2\2\2\u0160\u0163")
        buf.write(u"\3\2\2\2\u0161\u0162\3\2\2\2\u0161\u015f\3\2\2\2\u0162")
        buf.write(u"\u0164\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0166\7)\2\2")
        buf.write(u"\u0165\u0155\3\2\2\2\u0165\u015d\3\2\2\2\u0166Z\3\2\2")
        buf.write(u"\2\u0167\u0169\7\17\2\2\u0168\u0167\3\2\2\2\u0168\u0169")
        buf.write(u"\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\7\f\2\2\u016b")
        buf.write(u"\\\3\2\2\2\u016c\u016e\t\7\2\2\u016d\u016c\3\2\2\2\u016e")
        buf.write(u"\u016f\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2")
        buf.write(u"\2\u0170\u0171\3\2\2\2\u0171\u0172\b/\2\2\u0172^\3\2")
        buf.write(u"\2\2\26\2\u0083\u008c\u0095\u0097\u009a\u00a2\u00a6\u010f")
        buf.write(u"\u0135\u013a\u0140\u0147\u0149\u0153\u0159\u0161\u0165")
        buf.write(u"\u0168\u016f\3\b\2\2")
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
    SYSARRAY = 37
    SYSCONST = 38
    FLOAT = 39
    ID = 40
    INT = 41
    STRING = 42
    NL = 43
    WS = 44

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
            u"FLOAT_L", u"CONST", u"SYSARRAY", u"SYSCONST", u"FLOAT", u"ID", 
            u"INT", u"STRING", u"NL", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"T__13", u"LINE_COMMENT", u"T", u"PATH", u"MUL", 
                  u"DIV", u"ADD", u"SUB", u"AND", u"OR", u"USE", u"INCLUDE", 
                  u"VARDEF", u"END", u"ARRAY", u"IF", u"ELSEIF", u"ELSE", 
                  u"GROUP", u"STRING_L", u"INT_L", u"FLOAT_L", u"CONST", 
                  u"SYSARRAY", u"SYSCONST", u"FLOAT", u"ID", u"LETTER", 
                  u"DIGIT", u"INT", u"STRING", u"NL", u"WS" ]

    grammarFileName = u"VarDef.g4"

    def __init__(self, input=None):
        super(VarDefLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


