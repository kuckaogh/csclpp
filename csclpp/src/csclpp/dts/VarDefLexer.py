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
        buf.write(u".\u0185\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
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
        buf.write(u"\22\3\22\3\22\3\22\7\22\u0095\n\22\f\22\16\22\u0098\13")
        buf.write(u"\22\3\22\3\22\3\22\3\22\5\22\u009e\n\22\3\22\5\22\u00a1")
        buf.write(u"\n\22\3\22\3\22\3\22\3\22\7\22\u00a7\n\22\f\22\16\22")
        buf.write(u"\u00aa\13\22\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write(u"\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3")
        buf.write(u"\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write(u"\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write(u"\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write(u"\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3")
        buf.write(u"!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write(u"$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&")
        buf.write(u"\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write(u"&\3&\3&\3&\5&\u0122\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\5\'\u0148\n\'\3(\6(\u014b\n(\r(\16(\u014c")
        buf.write(u"\3(\3(\7(\u0151\n(\f(\16(\u0154\13(\3)\3)\3)\3)\7)\u015a")
        buf.write(u"\n)\f)\16)\u015d\13)\3*\3*\3+\3+\3,\6,\u0164\n,\r,\16")
        buf.write(u",\u0165\3-\3-\7-\u016a\n-\f-\16-\u016d\13-\3-\3-\3-\7")
        buf.write(u"-\u0172\n-\f-\16-\u0175\13-\3-\5-\u0178\n-\3.\5.\u017b")
        buf.write(u"\n.\3.\3.\3/\6/\u0180\n/\r/\16/\u0181\3/\3/\4\u016b\u0173")
        buf.write(u"\2\60\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write(u"\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-")
        buf.write(u"\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write(u"I&K\'M(O)Q*S\2U\2W+Y,[-].\3\2\b\4\2\f\f\17\17\4\2//a")
        buf.write(u"a\4\2C\\c|\4\2$$^^\4\2))^^\4\2\13\13\"\"\u01a6\2\3\3")
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
        buf.write(u"\2!\u0088\3\2\2\2#\u008a\3\2\2\2%\u00ad\3\2\2\2\'\u00af")
        buf.write(u"\3\2\2\2)\u00b1\3\2\2\2+\u00b3\3\2\2\2-\u00b5\3\2\2\2")
        buf.write(u"/\u00bb\3\2\2\2\61\u00c0\3\2\2\2\63\u00c4\3\2\2\2\65")
        buf.write(u"\u00cc\3\2\2\2\67\u00cf\3\2\2\29\u00d3\3\2\2\2;\u00d9")
        buf.write(u"\3\2\2\2=\u00dc\3\2\2\2?\u00e3\3\2\2\2A\u00e8\3\2\2\2")
        buf.write(u"C\u00ee\3\2\2\2E\u00f2\3\2\2\2G\u00f6\3\2\2\2I\u00fc")
        buf.write(u"\3\2\2\2K\u0121\3\2\2\2M\u0147\3\2\2\2O\u014a\3\2\2\2")
        buf.write(u"Q\u0155\3\2\2\2S\u015e\3\2\2\2U\u0160\3\2\2\2W\u0163")
        buf.write(u"\3\2\2\2Y\u0177\3\2\2\2[\u017a\3\2\2\2]\u017f\3\2\2\2")
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
        buf.write(u"\u0090\u0096\7\61\2\2\u0091\u0095\5S*\2\u0092\u0095\5")
        buf.write(u"U+\2\u0093\u0095\t\3\2\2\u0094\u0091\3\2\2\2\u0094\u0092")
        buf.write(u"\3\2\2\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2\u0096")
        buf.write(u"\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2")
        buf.write(u"\2\u0098\u0096\3\2\2\2\u0099\u009a\7\61\2\2\u009a\u009b")
        buf.write(u"\7\61\2\2\u009b\u00a0\3\2\2\2\u009c\u009e\5W,\2\u009d")
        buf.write(u"\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2")
        buf.write(u"\2\u009f\u00a1\5Q)\2\u00a0\u009d\3\2\2\2\u00a0\u00a1")
        buf.write(u"\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a8\7\61\2\2\u00a3")
        buf.write(u"\u00a7\5S*\2\u00a4\u00a7\5U+\2\u00a5\u00a7\t\3\2\2\u00a6")
        buf.write(u"\u00a3\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2")
        buf.write(u"\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9")
        buf.write(u"\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab")
        buf.write(u"\u00ac\7\61\2\2\u00ac$\3\2\2\2\u00ad\u00ae\7,\2\2\u00ae")
        buf.write(u"&\3\2\2\2\u00af\u00b0\7\61\2\2\u00b0(\3\2\2\2\u00b1\u00b2")
        buf.write(u"\7-\2\2\u00b2*\3\2\2\2\u00b3\u00b4\7/\2\2\u00b4,\3\2")
        buf.write(u"\2\2\u00b5\u00b6\7\"\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8")
        buf.write(u"\7p\2\2\u00b8\u00b9\7f\2\2\u00b9\u00ba\7\"\2\2\u00ba")
        buf.write(u".\3\2\2\2\u00bb\u00bc\7\"\2\2\u00bc\u00bd\7q\2\2\u00bd")
        buf.write(u"\u00be\7t\2\2\u00be\u00bf\7\"\2\2\u00bf\60\3\2\2\2\u00c0")
        buf.write(u"\u00c1\7w\2\2\u00c1\u00c2\7u\2\2\u00c2\u00c3\7g\2\2\u00c3")
        buf.write(u"\62\3\2\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6")
        buf.write(u"\u00c7\7e\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9\7w\2\2\u00c9")
        buf.write(u"\u00ca\7f\2\2\u00ca\u00cb\7g\2\2\u00cb\64\3\2\2\2\u00cc")
        buf.write(u"\u00cd\7f\2\2\u00cd\u00ce\7v\2\2\u00ce\66\3\2\2\2\u00cf")
        buf.write(u"\u00d0\7g\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7f\2\2\u00d2")
        buf.write(u"8\3\2\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7t\2\2\u00d5")
        buf.write(u"\u00d6\7t\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7{\2\2\u00d8")
        buf.write(u":\3\2\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7h\2\2\u00db")
        buf.write(u"<\3\2\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de\7n\2\2\u00de")
        buf.write(u"\u00df\7u\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1\7k\2\2\u00e1")
        buf.write(u"\u00e2\7h\2\2\u00e2>\3\2\2\2\u00e3\u00e4\7g\2\2\u00e4")
        buf.write(u"\u00e5\7n\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7\7g\2\2\u00e7")
        buf.write(u"@\3\2\2\2\u00e8\u00e9\7i\2\2\u00e9\u00ea\7t\2\2\u00ea")
        buf.write(u"\u00eb\7q\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7r\2\2\u00ed")
        buf.write(u"B\3\2\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0\7v\2\2\u00f0")
        buf.write(u"\u00f1\7t\2\2\u00f1D\3\2\2\2\u00f2\u00f3\7k\2\2\u00f3")
        buf.write(u"\u00f4\7p\2\2\u00f4\u00f5\7v\2\2\u00f5F\3\2\2\2\u00f6")
        buf.write(u"\u00f7\7h\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7q\2\2\u00f9")
        buf.write(u"\u00fa\7c\2\2\u00fa\u00fb\7v\2\2\u00fbH\3\2\2\2\u00fc")
        buf.write(u"\u00fd\7e\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7p\2\2\u00ff")
        buf.write(u"\u0100\7u\2\2\u0100\u0101\7v\2\2\u0101J\3\2\2\2\u0102")
        buf.write(u"\u0103\7{\2\2\u0103\u0104\7g\2\2\u0104\u0105\7c\2\2\u0105")
        buf.write(u"\u0122\7t\2\2\u0106\u0107\7o\2\2\u0107\u0108\7q\2\2\u0108")
        buf.write(u"\u0109\7p\2\2\u0109\u010a\7v\2\2\u010a\u0122\7j\2\2\u010b")
        buf.write(u"\u010c\7e\2\2\u010c\u010d\7h\2\2\u010d\u010e\7u\2\2\u010e")
        buf.write(u"\u010f\7a\2\2\u010f\u0110\7v\2\2\u0110\u0111\7c\2\2\u0111")
        buf.write(u"\u0112\7h\2\2\u0112\u0122\7o\2\2\u0113\u0114\7v\2\2\u0114")
        buf.write(u"\u0115\7c\2\2\u0115\u0116\7h\2\2\u0116\u0117\7o\2\2\u0117")
        buf.write(u"\u0118\7a\2\2\u0118\u0119\7e\2\2\u0119\u011a\7h\2\2\u011a")
        buf.write(u"\u0122\7u\2\2\u011b\u011c\7f\2\2\u011c\u011d\7c\2\2\u011d")
        buf.write(u"\u011e\7{\2\2\u011e\u011f\7u\2\2\u011f\u0120\7k\2\2\u0120")
        buf.write(u"\u0122\7p\2\2\u0121\u0102\3\2\2\2\u0121\u0106\3\2\2\2")
        buf.write(u"\u0121\u010b\3\2\2\2\u0121\u0113\3\2\2\2\u0121\u011b")
        buf.write(u"\3\2\2\2\u0122L\3\2\2\2\u0123\u0124\7q\2\2\u0124\u0125")
        buf.write(u"\7e\2\2\u0125\u0148\7v\2\2\u0126\u0127\7p\2\2\u0127\u0128")
        buf.write(u"\7q\2\2\u0128\u0148\7x\2\2\u0129\u012a\7f\2\2\u012a\u012b")
        buf.write(u"\7g\2\2\u012b\u0148\7e\2\2\u012c\u012d\7l\2\2\u012d\u012e")
        buf.write(u"\7c\2\2\u012e\u0148\7p\2\2\u012f\u0130\7h\2\2\u0130\u0131")
        buf.write(u"\7g\2\2\u0131\u0148\7d\2\2\u0132\u0133\7o\2\2\u0133\u0134")
        buf.write(u"\7c\2\2\u0134\u0148\7t\2\2\u0135\u0136\7c\2\2\u0136\u0137")
        buf.write(u"\7r\2\2\u0137\u0148\7t\2\2\u0138\u0139\7o\2\2\u0139\u013a")
        buf.write(u"\7c\2\2\u013a\u0148\7{\2\2\u013b\u013c\7l\2\2\u013c\u013d")
        buf.write(u"\7w\2\2\u013d\u0148\7p\2\2\u013e\u013f\7l\2\2\u013f\u0140")
        buf.write(u"\7w\2\2\u0140\u0148\7n\2\2\u0141\u0142\7c\2\2\u0142\u0143")
        buf.write(u"\7w\2\2\u0143\u0148\7i\2\2\u0144\u0145\7u\2\2\u0145\u0146")
        buf.write(u"\7g\2\2\u0146\u0148\7r\2\2\u0147\u0123\3\2\2\2\u0147")
        buf.write(u"\u0126\3\2\2\2\u0147\u0129\3\2\2\2\u0147\u012c\3\2\2")
        buf.write(u"\2\u0147\u012f\3\2\2\2\u0147\u0132\3\2\2\2\u0147\u0135")
        buf.write(u"\3\2\2\2\u0147\u0138\3\2\2\2\u0147\u013b\3\2\2\2\u0147")
        buf.write(u"\u013e\3\2\2\2\u0147\u0141\3\2\2\2\u0147\u0144\3\2\2")
        buf.write(u"\2\u0148N\3\2\2\2\u0149\u014b\4\62;\2\u014a\u0149\3\2")
        buf.write(u"\2\2\u014b\u014c\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d")
        buf.write(u"\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0152\7\60\2\2\u014f")
        buf.write(u"\u0151\4\62;\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2")
        buf.write(u"\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153P\3\2")
        buf.write(u"\2\2\u0154\u0152\3\2\2\2\u0155\u015b\5S*\2\u0156\u015a")
        buf.write(u"\5S*\2\u0157\u015a\5U+\2\u0158\u015a\7a\2\2\u0159\u0156")
        buf.write(u"\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015a")
        buf.write(u"\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2")
        buf.write(u"\2\u015cR\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\t\4")
        buf.write(u"\2\2\u015fT\3\2\2\2\u0160\u0161\4\62;\2\u0161V\3\2\2")
        buf.write(u"\2\u0162\u0164\5U+\2\u0163\u0162\3\2\2\2\u0164\u0165")
        buf.write(u"\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166")
        buf.write(u"X\3\2\2\2\u0167\u016b\7$\2\2\u0168\u016a\n\5\2\2\u0169")
        buf.write(u"\u0168\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u016c\3\2\2")
        buf.write(u"\2\u016b\u0169\3\2\2\2\u016c\u016e\3\2\2\2\u016d\u016b")
        buf.write(u"\3\2\2\2\u016e\u0178\7$\2\2\u016f\u0173\7)\2\2\u0170")
        buf.write(u"\u0172\n\6\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2")
        buf.write(u"\2\u0173\u0174\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0176")
        buf.write(u"\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0178\7)\2\2\u0177")
        buf.write(u"\u0167\3\2\2\2\u0177\u016f\3\2\2\2\u0178Z\3\2\2\2\u0179")
        buf.write(u"\u017b\7\17\2\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2")
        buf.write(u"\2\u017b\u017c\3\2\2\2\u017c\u017d\7\f\2\2\u017d\\\3")
        buf.write(u"\2\2\2\u017e\u0180\t\7\2\2\u017f\u017e\3\2\2\2\u0180")
        buf.write(u"\u0181\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2")
        buf.write(u"\2\u0182\u0183\3\2\2\2\u0183\u0184\b/\2\2\u0184^\3\2")
        buf.write(u"\2\2\27\2\u0083\u008c\u0094\u0096\u009d\u00a0\u00a6\u00a8")
        buf.write(u"\u0121\u0147\u014c\u0152\u0159\u015b\u0165\u016b\u0173")
        buf.write(u"\u0177\u017a\u0181\3\b\2\2")
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
    STR_L = 33
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
            u"'include'", u"'dt'", u"'end'", u"'array'", u"'if'", u"'elseif'", 
            u"'else'", u"'group'", u"'str'", u"'int'", u"'float'", u"'const'" ]

    symbolicNames = [ u"<INVALID>",
            u"LINE_COMMENT", u"T", u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", 
            u"AND", u"OR", u"USE", u"INCLUDE", u"VARDEF", u"END", u"ARRAY", 
            u"IF", u"ELSEIF", u"ELSE", u"GROUP", u"STR_L", u"INT_L", u"FLOAT_L", 
            u"CONST", u"SYSARRAY", u"SYSCONST", u"FLOAT", u"ID", u"INT", 
            u"STRING", u"NL", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"T__13", u"LINE_COMMENT", u"T", u"PATH", u"MUL", 
                  u"DIV", u"ADD", u"SUB", u"AND", u"OR", u"USE", u"INCLUDE", 
                  u"VARDEF", u"END", u"ARRAY", u"IF", u"ELSEIF", u"ELSE", 
                  u"GROUP", u"STR_L", u"INT_L", u"FLOAT_L", u"CONST", u"SYSARRAY", 
                  u"SYSCONST", u"FLOAT", u"ID", u"LETTER", u"DIGIT", u"INT", 
                  u"STRING", u"NL", u"WS" ]

    grammarFileName = u"VarDef.g4"

    def __init__(self, input=None):
        super(VarDefLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


