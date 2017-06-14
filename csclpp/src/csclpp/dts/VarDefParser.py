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
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u".\u01af\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\3")
        buf.write(u"\2\7\2;\n\2\f\2\16\2>\13\2\3\2\6\2A\n\2\r\2\16\2B\3\3")
        buf.write(u"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\6\4M\n\4\r\4\16\4N\3\4\6")
        buf.write(u"\4R\n\4\r\4\16\4S\3\4\3\4\6\4X\n\4\r\4\16\4Y\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5e\n\5\3\5\6\5h\n\5\r")
        buf.write(u"\5\16\5i\3\6\3\6\5\6n\n\6\3\7\3\7\3\7\3\7\7\7t\n\7\f")
        buf.write(u"\7\16\7w\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0081")
        buf.write(u"\n\b\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u0089\n\t\f\t\16\t\u008c")
        buf.write(u"\13\t\3\n\3\n\5\n\u0090\n\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write(u"\5\13\u0098\n\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a0")
        buf.write(u"\n\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a8\n\13\3")
        buf.write(u"\13\3\13\7\13\u00ac\n\13\f\13\16\13\u00af\13\13\3\13")
        buf.write(u"\3\13\3\f\3\f\3\f\3\r\3\r\5\r\u00b8\n\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\5\r\u00bf\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\5\16\u00cd\n\16\3\16\3\16\3")
        buf.write(u"\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\7\21\u00d9\n\21")
        buf.write(u"\f\21\16\21\u00dc\13\21\3\21\3\21\3\22\3\22\3\22\5\22")
        buf.write(u"\u00e3\n\22\3\22\3\22\3\22\3\22\5\22\u00e9\n\22\3\23")
        buf.write(u"\3\23\3\24\3\24\5\24\u00ef\n\24\3\24\3\24\3\24\3\24\3")
        buf.write(u"\25\3\25\3\25\3\25\5\25\u00f9\n\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\5\25\u0100\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\5\25\u010d\n\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0119\n\25\f")
        buf.write(u"\25\16\25\u011c\13\25\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\5\26\u0129\n\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\7\26\u0130\n\26\f\26\16\26\u0133\13\26\3\27")
        buf.write(u"\3\27\3\27\3\27\3\27\3\30\3\30\3\30\5\30\u013d\n\30\3")
        buf.write(u"\31\3\31\3\31\7\31\u0142\n\31\f\31\16\31\u0145\13\31")
        buf.write(u"\3\31\3\31\7\31\u0149\n\31\f\31\16\31\u014c\13\31\3\31")
        buf.write(u"\3\31\3\31\7\31\u0151\n\31\f\31\16\31\u0154\13\31\6\31")
        buf.write(u"\u0156\n\31\r\31\16\31\u0157\3\31\3\31\7\31\u015c\n\31")
        buf.write(u"\f\31\16\31\u015f\13\31\3\31\3\31\3\31\3\31\7\31\u0165")
        buf.write(u"\n\31\f\31\16\31\u0168\13\31\3\31\3\31\7\31\u016c\n\31")
        buf.write(u"\f\31\16\31\u016f\13\31\3\31\3\31\3\31\7\31\u0174\n\31")
        buf.write(u"\f\31\16\31\u0177\13\31\6\31\u0179\n\31\r\31\16\31\u017a")
        buf.write(u"\3\31\3\31\7\31\u017f\n\31\f\31\16\31\u0182\13\31\3\31")
        buf.write(u"\3\31\7\31\u0186\n\31\f\31\16\31\u0189\13\31\3\31\3\31")
        buf.write(u"\7\31\u018d\n\31\f\31\16\31\u0190\13\31\3\31\3\31\7\31")
        buf.write(u"\u0194\n\31\f\31\16\31\u0197\13\31\3\31\3\31\3\31\7\31")
        buf.write(u"\u019c\n\31\f\31\16\31\u019f\13\31\6\31\u01a1\n\31\r")
        buf.write(u"\31\16\31\u01a2\3\31\3\31\6\31\u01a7\n\31\r\31\16\31")
        buf.write(u"\u01a8\3\31\3\31\5\31\u01ad\n\31\3\31\2\4(*\32\2\4\6")
        buf.write(u"\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\b\3\2")
        buf.write(u")+\4\2))++\3\2\24\25\3\2\26\27\3\2\13\20\3\2\30\31\u01d2")
        buf.write(u"\2\65\3\2\2\2\4D\3\2\2\2\6H\3\2\2\2\bd\3\2\2\2\nm\3\2")
        buf.write(u"\2\2\fo\3\2\2\2\16x\3\2\2\2\20\u0084\3\2\2\2\22\u008f")
        buf.write(u"\3\2\2\2\24\u0094\3\2\2\2\26\u00b2\3\2\2\2\30\u00b7\3")
        buf.write(u"\2\2\2\32\u00c2\3\2\2\2\34\u00d0\3\2\2\2\36\u00d2\3\2")
        buf.write(u"\2\2 \u00d4\3\2\2\2\"\u00e2\3\2\2\2$\u00ea\3\2\2\2&\u00ee")
        buf.write(u"\3\2\2\2(\u010c\3\2\2\2*\u0128\3\2\2\2,\u0134\3\2\2\2")
        buf.write(u".\u0139\3\2\2\2\60\u013e\3\2\2\2\62\64\7-\2\2\63\62\3")
        buf.write(u"\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\668")
        buf.write(u"\3\2\2\2\67\65\3\2\2\28<\5\4\3\29;\7-\2\2:9\3\2\2\2;")
        buf.write(u">\3\2\2\2<:\3\2\2\2<=\3\2\2\2=@\3\2\2\2><\3\2\2\2?A\5")
        buf.write(u"\6\4\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\3\3\2")
        buf.write(u"\2\2DE\7\32\2\2EF\7*\2\2FG\b\3\1\2G\5\3\2\2\2HI\7\34")
        buf.write(u"\2\2IJ\7*\2\2JL\b\4\1\2KM\7-\2\2LK\3\2\2\2MN\3\2\2\2")
        buf.write(u"NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PR\5\b\5\2QP\3\2\2\2RS")
        buf.write(u"\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UW\7\35\2\2VX\7")
        buf.write(u"-\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\7\3\2")
        buf.write(u"\2\2[e\5\30\r\2\\e\5\32\16\2]e\5&\24\2^_\5\60\31\2_`")
        buf.write(u"\b\5\1\2`e\3\2\2\2ae\5\n\6\2be\5\26\f\2ce\5\f\7\2d[\3")
        buf.write(u"\2\2\2d\\\3\2\2\2d]\3\2\2\2d^\3\2\2\2da\3\2\2\2db\3\2")
        buf.write(u"\2\2dc\3\2\2\2eg\3\2\2\2fh\7-\2\2gf\3\2\2\2hi\3\2\2\2")
        buf.write(u"ig\3\2\2\2ij\3\2\2\2j\t\3\2\2\2kn\5\20\t\2ln\5\24\13")
        buf.write(u"\2mk\3\2\2\2ml\3\2\2\2n\13\3\2\2\2op\7&\2\2pu\5\16\b")
        buf.write(u"\2qr\7\3\2\2rt\5\16\b\2sq\3\2\2\2tw\3\2\2\2us\3\2\2\2")
        buf.write(u"uv\3\2\2\2v\r\3\2\2\2wu\3\2\2\2xy\7*\2\2y\u0080\7\4\2")
        buf.write(u"\2z{\7)\2\2{\u0081\b\b\1\2|}\7+\2\2}\u0081\b\b\1\2~\177")
        buf.write(u"\7,\2\2\177\u0081\b\b\1\2\u0080z\3\2\2\2\u0080|\3\2\2")
        buf.write(u"\2\u0080~\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\b\b")
        buf.write(u"\1\2\u0083\17\3\2\2\2\u0084\u0085\7\36\2\2\u0085\u008a")
        buf.write(u"\5\22\n\2\u0086\u0087\7\3\2\2\u0087\u0089\5\22\n\2\u0088")
        buf.write(u"\u0086\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2")
        buf.write(u"\2\u008a\u008b\3\2\2\2\u008b\21\3\2\2\2\u008c\u008a\3")
        buf.write(u"\2\2\2\u008d\u008e\7\22\2\2\u008e\u0090\b\n\1\2\u008f")
        buf.write(u"\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091\3\2\2")
        buf.write(u"\2\u0091\u0092\7*\2\2\u0092\u0093\b\n\1\2\u0093\23\3")
        buf.write(u"\2\2\2\u0094\u0097\7\36\2\2\u0095\u0096\7\22\2\2\u0096")
        buf.write(u"\u0098\b\13\1\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2")
        buf.write(u"\2\u0098\u0099\3\2\2\2\u0099\u009a\7*\2\2\u009a\u009b")
        buf.write(u"\b\13\1\2\u009b\u009c\7\5\2\2\u009c\u009f\b\13\1\2\u009d")
        buf.write(u"\u009e\7\22\2\2\u009e\u00a0\b\13\1\2\u009f\u009d\3\2")
        buf.write(u"\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2")
        buf.write(u"\7*\2\2\u00a2\u00ad\b\13\1\2\u00a3\u00a4\7\3\2\2\u00a4")
        buf.write(u"\u00a7\b\13\1\2\u00a5\u00a6\7\22\2\2\u00a6\u00a8\b\13")
        buf.write(u"\1\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9")
        buf.write(u"\3\2\2\2\u00a9\u00aa\7*\2\2\u00aa\u00ac\b\13\1\2\u00ab")
        buf.write(u"\u00a3\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2")
        buf.write(u"\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ad")
        buf.write(u"\3\2\2\2\u00b0\u00b1\7\6\2\2\u00b1\25\3\2\2\2\u00b2\u00b3")
        buf.write(u"\7\33\2\2\u00b3\u00b4\7*\2\2\u00b4\27\3\2\2\2\u00b5\u00b6")
        buf.write(u"\7\22\2\2\u00b6\u00b8\b\r\1\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write(u"\u00b8\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\7*\2\2")
        buf.write(u"\u00ba\u00bb\7\4\2\2\u00bb\u00be\7\23\2\2\u00bc\u00bd")
        buf.write(u"\7\3\2\2\u00bd\u00bf\7*\2\2\u00be\u00bc\3\2\2\2\u00be")
        buf.write(u"\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\b\r\1")
        buf.write(u"\2\u00c1\31\3\2\2\2\u00c2\u00c3\5.\30\2\u00c3\u00c4\7")
        buf.write(u"\7\2\2\u00c4\u00c5\5\34\17\2\u00c5\u00cc\7\4\2\2\u00c6")
        buf.write(u"\u00c7\5\36\20\2\u00c7\u00c8\b\16\1\2\u00c8\u00cd\3\2")
        buf.write(u"\2\2\u00c9\u00ca\5 \21\2\u00ca\u00cb\b\16\1\2\u00cb\u00cd")
        buf.write(u"\3\2\2\2\u00cc\u00c6\3\2\2\2\u00cc\u00c9\3\2\2\2\u00cd")
        buf.write(u"\u00ce\3\2\2\2\u00ce\u00cf\b\16\1\2\u00cf\33\3\2\2\2")
        buf.write(u"\u00d0\u00d1\7*\2\2\u00d1\35\3\2\2\2\u00d2\u00d3\t\2")
        buf.write(u"\2\2\u00d3\37\3\2\2\2\u00d4\u00d5\7\5\2\2\u00d5\u00da")
        buf.write(u"\5\"\22\2\u00d6\u00d7\7\3\2\2\u00d7\u00d9\5\"\22\2\u00d8")
        buf.write(u"\u00d6\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2")
        buf.write(u"\2\u00da\u00db\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00da")
        buf.write(u"\3\2\2\2\u00dd\u00de\7\6\2\2\u00de!\3\2\2\2\u00df\u00e3")
        buf.write(u"\7*\2\2\u00e0\u00e3\7,\2\2\u00e1\u00e3\5$\23\2\u00e2")
        buf.write(u"\u00df\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e1\3\2\2")
        buf.write(u"\2\u00e3\u00e4\3\2\2\2\u00e4\u00e8\7\b\2\2\u00e5\u00e9")
        buf.write(u"\7*\2\2\u00e6\u00e9\7,\2\2\u00e7\u00e9\5$\23\2\u00e8")
        buf.write(u"\u00e5\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2")
        buf.write(u"\2\u00e9#\3\2\2\2\u00ea\u00eb\t\3\2\2\u00eb%\3\2\2\2")
        buf.write(u"\u00ec\u00ed\7\22\2\2\u00ed\u00ef\b\24\1\2\u00ee\u00ec")
        buf.write(u"\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write(u"\u00f1\7*\2\2\u00f1\u00f2\7\4\2\2\u00f2\u00f3\5(\25\2")
        buf.write(u"\u00f3\'\3\2\2\2\u00f4\u00f5\b\25\1\2\u00f5\u00f8\b\25")
        buf.write(u"\1\2\u00f6\u00f7\7\27\2\2\u00f7\u00f9\b\25\1\2\u00f8")
        buf.write(u"\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\3\2\2")
        buf.write(u"\2\u00fa\u00fb\7+\2\2\u00fb\u010d\b\25\1\2\u00fc\u00ff")
        buf.write(u"\b\25\1\2\u00fd\u00fe\7\27\2\2\u00fe\u0100\b\25\1\2\u00ff")
        buf.write(u"\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2")
        buf.write(u"\2\u0101\u0102\7)\2\2\u0102\u010d\b\25\1\2\u0103\u0104")
        buf.write(u"\7*\2\2\u0104\u010d\b\25\1\2\u0105\u0106\7\t\2\2\u0106")
        buf.write(u"\u0107\5(\25\2\u0107\u0108\7\n\2\2\u0108\u0109\b\25\1")
        buf.write(u"\2\u0109\u010d\3\2\2\2\u010a\u010b\7,\2\2\u010b\u010d")
        buf.write(u"\b\25\1\2\u010c\u00f4\3\2\2\2\u010c\u00fc\3\2\2\2\u010c")
        buf.write(u"\u0103\3\2\2\2\u010c\u0105\3\2\2\2\u010c\u010a\3\2\2")
        buf.write(u"\2\u010d\u011a\3\2\2\2\u010e\u010f\f\t\2\2\u010f\u0110")
        buf.write(u"\t\4\2\2\u0110\u0111\5(\25\n\u0111\u0112\b\25\1\2\u0112")
        buf.write(u"\u0119\3\2\2\2\u0113\u0114\f\b\2\2\u0114\u0115\t\5\2")
        buf.write(u"\2\u0115\u0116\5(\25\t\u0116\u0117\b\25\1\2\u0117\u0119")
        buf.write(u"\3\2\2\2\u0118\u010e\3\2\2\2\u0118\u0113\3\2\2\2\u0119")
        buf.write(u"\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2")
        buf.write(u"\2\u011b)\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u011e\b\26")
        buf.write(u"\1\2\u011e\u011f\5(\25\2\u011f\u0120\t\6\2\2\u0120\u0121")
        buf.write(u"\5(\25\2\u0121\u0122\b\26\1\2\u0122\u0129\3\2\2\2\u0123")
        buf.write(u"\u0124\7\t\2\2\u0124\u0125\5*\26\2\u0125\u0126\7\n\2")
        buf.write(u"\2\u0126\u0127\b\26\1\2\u0127\u0129\3\2\2\2\u0128\u011d")
        buf.write(u"\3\2\2\2\u0128\u0123\3\2\2\2\u0129\u0131\3\2\2\2\u012a")
        buf.write(u"\u012b\f\3\2\2\u012b\u012c\t\7\2\2\u012c\u012d\5*\26")
        buf.write(u"\4\u012d\u012e\b\26\1\2\u012e\u0130\3\2\2\2\u012f\u012a")
        buf.write(u"\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2\u0131")
        buf.write(u"\u0132\3\2\2\2\u0132+\3\2\2\2\u0133\u0131\3\2\2\2\u0134")
        buf.write(u"\u0135\5.\30\2\u0135\u0136\7\4\2\2\u0136\u0137\5(\25")
        buf.write(u"\2\u0137\u0138\b\27\1\2\u0138-\3\2\2\2\u0139\u013c\7")
        buf.write(u"*\2\2\u013a\u013b\7\7\2\2\u013b\u013d\7*\2\2\u013c\u013a")
        buf.write(u"\3\2\2\2\u013c\u013d\3\2\2\2\u013d/\3\2\2\2\u013e\u013f")
        buf.write(u"\7\37\2\2\u013f\u0143\5*\26\2\u0140\u0142\7-\2\2\u0141")
        buf.write(u"\u0140\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2")
        buf.write(u"\2\u0143\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0143")
        buf.write(u"\3\2\2\2\u0146\u014a\7\5\2\2\u0147\u0149\7-\2\2\u0148")
        buf.write(u"\u0147\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2")
        buf.write(u"\2\u014a\u014b\3\2\2\2\u014b\u0155\3\2\2\2\u014c\u014a")
        buf.write(u"\3\2\2\2\u014d\u014e\5,\27\2\u014e\u0152\b\31\1\2\u014f")
        buf.write(u"\u0151\7-\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2")
        buf.write(u"\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0156")
        buf.write(u"\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u014d\3\2\2\2\u0156")
        buf.write(u"\u0157\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2")
        buf.write(u"\2\u0158\u0159\3\2\2\2\u0159\u015d\7\6\2\2\u015a\u015c")
        buf.write(u"\7-\2\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d")
        buf.write(u"\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160\3\2\2")
        buf.write(u"\2\u015f\u015d\3\2\2\2\u0160\u0187\b\31\1\2\u0161\u0162")
        buf.write(u"\7 \2\2\u0162\u0166\5*\26\2\u0163\u0165\7-\2\2\u0164")
        buf.write(u"\u0163\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2")
        buf.write(u"\2\u0166\u0167\3\2\2\2\u0167\u0169\3\2\2\2\u0168\u0166")
        buf.write(u"\3\2\2\2\u0169\u016d\7\5\2\2\u016a\u016c\7-\2\2\u016b")
        buf.write(u"\u016a\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2")
        buf.write(u"\2\u016d\u016e\3\2\2\2\u016e\u0178\3\2\2\2\u016f\u016d")
        buf.write(u"\3\2\2\2\u0170\u0171\5,\27\2\u0171\u0175\b\31\1\2\u0172")
        buf.write(u"\u0174\7-\2\2\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2\2")
        buf.write(u"\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0179")
        buf.write(u"\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0170\3\2\2\2\u0179")
        buf.write(u"\u017a\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2")
        buf.write(u"\2\u017b\u017c\3\2\2\2\u017c\u0180\7\6\2\2\u017d\u017f")
        buf.write(u"\7-\2\2\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180")
        buf.write(u"\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0183\3\2\2")
        buf.write(u"\2\u0182\u0180\3\2\2\2\u0183\u0184\b\31\1\2\u0184\u0186")
        buf.write(u"\3\2\2\2\u0185\u0161\3\2\2\2\u0186\u0189\3\2\2\2\u0187")
        buf.write(u"\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u01ac\3\2\2")
        buf.write(u"\2\u0189\u0187\3\2\2\2\u018a\u018e\7!\2\2\u018b\u018d")
        buf.write(u"\7-\2\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e")
        buf.write(u"\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0191\3\2\2")
        buf.write(u"\2\u0190\u018e\3\2\2\2\u0191\u0195\7\5\2\2\u0192\u0194")
        buf.write(u"\7-\2\2\u0193\u0192\3\2\2\2\u0194\u0197\3\2\2\2\u0195")
        buf.write(u"\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u01a0\3\2\2")
        buf.write(u"\2\u0197\u0195\3\2\2\2\u0198\u0199\5,\27\2\u0199\u019d")
        buf.write(u"\b\31\1\2\u019a\u019c\7-\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write(u"\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2")
        buf.write(u"\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u0198")
        buf.write(u"\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write(u"\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a6\7\6\2")
        buf.write(u"\2\u01a5\u01a7\7-\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write(u"\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write(u"\u01aa\3\2\2\2\u01aa\u01ab\b\31\1\2\u01ab\u01ad\3\2\2")
        buf.write(u"\2\u01ac\u018a\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\61\3")
        buf.write(u"\2\2\2\63\65<BNSYdimu\u0080\u008a\u008f\u0097\u009f\u00a7")
        buf.write(u"\u00ad\u00b7\u00be\u00cc\u00da\u00e2\u00e8\u00ee\u00f8")
        buf.write(u"\u00ff\u010c\u0118\u011a\u0128\u0131\u013c\u0143\u014a")
        buf.write(u"\u0152\u0157\u015d\u0166\u016d\u0175\u017a\u0180\u0187")
        buf.write(u"\u018e\u0195\u019d\u01a2\u01a8\u01ac")
        return buf.getvalue()


class VarDefParser ( Parser ):

    grammarFileName = "VarDef.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"','", u"'='", u"'{'", u"'}'", u"'.'", 
                     u"':'", u"'('", u"')'", u"'>'", u"'>='", u"'<'", u"'<='", 
                     u"'=='", u"'!='", u"<INVALID>", u"'@'", u"<INVALID>", 
                     u"'*'", u"'/'", u"'+'", u"'-'", u"' and '", u"' or '", 
                     u"'use'", u"'include'", u"'vardef'", u"'end'", u"'array'", 
                     u"'if'", u"'elseif'", u"'else'", u"'group'", u"'string'", 
                     u"'int'", u"'float'", u"'const'", u"'month'", u"'year'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"LINE_COMMENT", 
                      u"T", u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", u"AND", 
                      u"OR", u"USE", u"INCLUDE", u"VARDEF", u"END", u"ARRAY", 
                      u"IF", u"ELSEIF", u"ELSE", u"GROUP", u"STRING_L", 
                      u"INT_L", u"FLOAT_L", u"CONST", u"MONTH", u"YEAR", 
                      u"FLOAT", u"ID", u"INT", u"STRING", u"NL", u"WS" ]

    RULE_prog = 0
    RULE_use = 1
    RULE_vardef = 2
    RULE_field = 3
    RULE_new_var = 4
    RULE_constant = 5
    RULE_const_var = 6
    RULE_array = 7
    RULE_array_var = 8
    RULE_array_cluster = 9
    RULE_include = 10
    RULE_var_path = 11
    RULE_var_meta = 12
    RULE_metaKey = 13
    RULE_metaValue = 14
    RULE_metaDict = 15
    RULE_dict_pair = 16
    RULE_number = 17
    RULE_stat = 18
    RULE_ee = 19
    RULE_compare = 20
    RULE_assign = 21
    RULE_id2 = 22
    RULE_if_stat = 23

    ruleNames =  [ u"prog", u"use", u"vardef", u"field", u"new_var", u"constant", 
                   u"const_var", u"array", u"array_var", u"array_cluster", 
                   u"include", u"var_path", u"var_meta", u"metaKey", u"metaValue", 
                   u"metaDict", u"dict_pair", u"number", u"stat", u"ee", 
                   u"compare", u"assign", u"id2", u"if_stat" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    LINE_COMMENT=15
    T=16
    PATH=17
    MUL=18
    DIV=19
    ADD=20
    SUB=21
    AND=22
    OR=23
    USE=24
    INCLUDE=25
    VARDEF=26
    END=27
    ARRAY=28
    IF=29
    ELSEIF=30
    ELSE=31
    GROUP=32
    STRING_L=33
    INT_L=34
    FLOAT_L=35
    CONST=36
    MONTH=37
    YEAR=38
    FLOAT=39
    ID=40
    INT=41
    STRING=42
    NL=43
    WS=44

    def __init__(self, input):
        super(VarDefParser, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    varMetaKeys=[];
    ifsAppend='';
    ifsNewAppend='';
    varPathGroupMap={};
    varExprGroupMap={};
    tempVarGroupList={};
    ifsMapGroupMap={};
    newArrayGroupMap={};
    newConstGroupMap={};
    varPathMap=collections.OrderedDict();
    varExprMap=collections.OrderedDict();
    tempVarList=[];
    newArrayMap=collections.OrderedDict();
    newConstMap=collections.OrderedDict();
    #newArrayClusterMap=collections.OrderedDict();
    ifsMap=collections.OrderedDict(); # (if statement ID, (condition, assignments)) 
    vardefName='';
    vardefFile='';
    vardefDefault='';


    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

        def use(self):
            return self.getTypedRuleContext(VarDefParser.UseContext,0)


        def NL(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.NL)
            else:
                return self.getToken(VarDefParser.NL, i)

        def vardef(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.VardefContext)
            else:
                return self.getTypedRuleContext(VarDefParser.VardefContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_prog

        def accept(self, visitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = VarDefParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self.varPathGroupMap={};
        self.varExprGroupMap={};
        self.tempVarGroupList={};
        ifsMapGroupMap={};
        newArrayGroupMap={};
        newConstGroupMap={};

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 48
                self.match(VarDefParser.NL)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.use()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 55
                self.match(VarDefParser.NL)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.vardef()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.VARDEF):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.UseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token

        def USE(self):
            return self.getToken(VarDefParser.USE, 0)

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_use

        def accept(self, visitor):
            if hasattr(visitor, "visitUse"):
                return visitor.visitUse(self)
            else:
                return visitor.visitChildren(self)




    def use(self):

        localctx = VarDefParser.UseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_use)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(VarDefParser.USE)
            self.state = 67
            localctx.i = self.match(VarDefParser.ID)
            self.vardefDefault=str((None if localctx.i is None else localctx.i.text)).lower()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.VardefContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def VARDEF(self):
            return self.getToken(VarDefParser.VARDEF, 0)

        def END(self):
            return self.getToken(VarDefParser.END, 0)

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def NL(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.NL)
            else:
                return self.getToken(VarDefParser.NL, i)

        def field(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.FieldContext)
            else:
                return self.getTypedRuleContext(VarDefParser.FieldContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_vardef

        def accept(self, visitor):
            if hasattr(visitor, "visitVardef"):
                return visitor.visitVardef(self)
            else:
                return visitor.visitChildren(self)




    def vardef(self):

        localctx = VarDefParser.VardefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardef)

        self.varPathMap=collections.OrderedDict();
        self.varExprMap=collections.OrderedDict();
        self.tempVarList=[];
        self.ifsMap=collections.OrderedDict();
        self.newArrayMap=collections.OrderedDict();
        self.newConstMap=collections.OrderedDict();
        self.ifid=0;

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(VarDefParser.VARDEF)
            self.state = 71
            localctx.name = self.match(VarDefParser.ID)
            groupName=str((None if localctx.name is None else localctx.name.text)).lower();self.vardefName=groupName;
            self.state = 74 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 73
                self.match(VarDefParser.NL)
                self.state = 76 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.field()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ARRAY) | (1 << VarDefParser.IF) | (1 << VarDefParser.CONST) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 83
            self.match(VarDefParser.END)
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.match(VarDefParser.NL)
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self._ctx.stop = self._input.LT(-1)

            self.varPathGroupMap[groupName]=self.varPathMap;
            self.varExprGroupMap[groupName]=self.varExprMap;
            self.tempVarGroupList[groupName]=self.tempVarList;	
            self.ifsMapGroupMap[groupName]=self.ifsMap;
            self.newArrayGroupMap[groupName]=self.newArrayMap;
            self.newConstGroupMap[groupName]=self.newConstMap;

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.FieldContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var_path(self):
            return self.getTypedRuleContext(VarDefParser.Var_pathContext,0)


        def var_meta(self):
            return self.getTypedRuleContext(VarDefParser.Var_metaContext,0)


        def stat(self):
            return self.getTypedRuleContext(VarDefParser.StatContext,0)


        def if_stat(self):
            return self.getTypedRuleContext(VarDefParser.If_statContext,0)


        def new_var(self):
            return self.getTypedRuleContext(VarDefParser.New_varContext,0)


        def include(self):
            return self.getTypedRuleContext(VarDefParser.IncludeContext,0)


        def constant(self):
            return self.getTypedRuleContext(VarDefParser.ConstantContext,0)


        def NL(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.NL)
            else:
                return self.getToken(VarDefParser.NL, i)

        def getRuleIndex(self):
            return VarDefParser.RULE_field

        def accept(self, visitor):
            if hasattr(visitor, "visitField"):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = VarDefParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 89
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 90
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 91
                self.stat()
                pass

            elif la_ == 4:
                self.state = 92
                self.if_stat()
                self.ifid=self.ifid+1;
                pass

            elif la_ == 5:
                self.state = 95
                self.new_var()
                pass

            elif la_ == 6:
                self.state = 96
                self.include()
                pass

            elif la_ == 7:
                self.state = 97
                self.constant()
                pass


            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 100
                self.match(VarDefParser.NL)
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class New_varContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.New_varContext, self).__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(VarDefParser.ArrayContext,0)


        def array_cluster(self):
            return self.getTypedRuleContext(VarDefParser.Array_clusterContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_new_var

        def accept(self, visitor):
            if hasattr(visitor, "visitNew_var"):
                return visitor.visitNew_var(self)
            else:
                return visitor.visitChildren(self)




    def new_var(self):

        localctx = VarDefParser.New_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_new_var)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.array_cluster()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.ConstantContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(VarDefParser.CONST, 0)

        def const_var(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.Const_varContext)
            else:
                return self.getTypedRuleContext(VarDefParser.Const_varContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_constant

        def accept(self, visitor):
            if hasattr(visitor, "visitConstant"):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = VarDefParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(VarDefParser.CONST)
            self.state = 110
            self.const_var()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 111
                self.match(VarDefParser.T__0)
                self.state = 112
                self.const_var()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Const_varContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.Const_varContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.c = None # Token

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def FLOAT(self):
            return self.getToken(VarDefParser.FLOAT, 0)

        def INT(self):
            return self.getToken(VarDefParser.INT, 0)

        def STRING(self):
            return self.getToken(VarDefParser.STRING, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_const_var

        def accept(self, visitor):
            if hasattr(visitor, "visitConst_var"):
                return visitor.visitConst_var(self)
            else:
                return visitor.visitChildren(self)




    def const_var(self):

        localctx = VarDefParser.Const_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const_var)
        v = Var('');
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            localctx.i = self.match(VarDefParser.ID)
            self.state = 119
            self.match(VarDefParser.T__1)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT]:
                self.state = 120
                localctx.c = self.match(VarDefParser.FLOAT)
                v.const=float((None if localctx.c is None else localctx.c.text))
                pass
            elif token in [VarDefParser.INT]:
                self.state = 122
                localctx.c = self.match(VarDefParser.INT)
                v.const=int((None if localctx.c is None else localctx.c.text))
                pass
            elif token in [VarDefParser.STRING]:
                self.state = 124
                localctx.c = self.match(VarDefParser.STRING)
                v.const=str((None if localctx.c is None else localctx.c.text))
                pass
            else:
                raise NoViableAltException(self)

            name=str((None if localctx.i is None else localctx.i.text)).lower();self.newConstMap[name]=v;
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.ArrayContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(VarDefParser.ARRAY, 0)

        def array_var(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.Array_varContext)
            else:
                return self.getTypedRuleContext(VarDefParser.Array_varContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_array

        def accept(self, visitor):
            if hasattr(visitor, "visitArray"):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = VarDefParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(VarDefParser.ARRAY)
            self.state = 131
            self.array_var()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 132
                self.match(VarDefParser.T__0)
                self.state = 133
                self.array_var()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_varContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.Array_varContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def T(self):
            return self.getToken(VarDefParser.T, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_array_var

        def accept(self, visitor):
            if hasattr(visitor, "visitArray_var"):
                return visitor.visitArray_var(self)
            else:
                return visitor.visitChildren(self)




    def array_var(self):

        localctx = VarDefParser.Array_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_var)
        isTemp=False;
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 139
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 143
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();
            self.newArrayMap[name]=v;
            if isTemp: self.tempVarList.append(name); 

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_clusterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.Array_clusterContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token

        def ARRAY(self):
            return self.getToken(VarDefParser.ARRAY, 0)

        def ID(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.ID)
            else:
                return self.getToken(VarDefParser.ID, i)

        def T(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.T)
            else:
                return self.getToken(VarDefParser.T, i)

        def getRuleIndex(self):
            return VarDefParser.RULE_array_cluster

        def accept(self, visitor):
            if hasattr(visitor, "visitArray_cluster"):
                return visitor.visitArray_cluster(self)
            else:
                return visitor.visitChildren(self)




    def array_cluster(self):

        localctx = VarDefParser.Array_clusterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_cluster)
        header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(VarDefParser.ARRAY)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 147
                self.match(VarDefParser.T)
                isGroupTemp=True


            self.state = 151
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 153
            self.match(VarDefParser.T__2)
            isTemp=False;
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 155
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 159
            localctx.i = self.match(VarDefParser.ID)
            subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 161
                self.match(VarDefParser.T__0)
                isTemp=False;
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 163
                    self.match(VarDefParser.T)
                    isTemp=True


                self.state = 167
                localctx.i = self.match(VarDefParser.ID)
                subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 174
            self.match(VarDefParser.T__3)
            self._ctx.stop = self._input.LT(-1)

            for k in subvar.keys():
            	o = Var('')
            	name=header.lower()+'.'+k.lower()
            	self.newArrayMap[name]=o;
            	if isGroupTemp or subvar[k]:
            		self.tempVarList.append(name);

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncludeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.IncludeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.g = None # Token

        def INCLUDE(self):
            return self.getToken(VarDefParser.INCLUDE, 0)

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_include

        def accept(self, visitor):
            if hasattr(visitor, "visitInclude"):
                return visitor.visitInclude(self)
            else:
                return visitor.visitChildren(self)




    def include(self):

        localctx = VarDefParser.IncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(VarDefParser.INCLUDE)
            self.state = 177
            localctx.g = self.match(VarDefParser.ID)
            self._ctx.stop = self._input.LT(-1)
            gn=str((None if localctx.g is None else localctx.g.text)).lower();
            if gn: 
            	self.varPathMap.update(self.varPathGroupMap[gn])
            	self.varExprMap.update(self.varExprGroupMap[gn])
            	self.tempVarList.extend(self.tempVarGroupList[gn])
            	self.ifsMap.update(self.ifsMapGroupMap[gn])
            	self.newArrayMap.update(self.newArrayGroupMap[gn])
            	self.newConstMap.update(self.newConstGroupMap[gn])

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_pathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.Var_pathContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.p = None # Token
            self.u = None # Token

        def ID(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.ID)
            else:
                return self.getToken(VarDefParser.ID, i)

        def PATH(self):
            return self.getToken(VarDefParser.PATH, 0)

        def T(self):
            return self.getToken(VarDefParser.T, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_var_path

        def accept(self, visitor):
            if hasattr(visitor, "visitVar_path"):
                return visitor.visitVar_path(self)
            else:
                return visitor.visitChildren(self)




    def var_path(self):

        localctx = VarDefParser.Var_pathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var_path)
        isTemp=False;
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 179
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 183
            localctx.i = self.match(VarDefParser.ID)
            self.state = 184
            self.match(VarDefParser.T__1)
            self.state = 185
            localctx.p = self.match(VarDefParser.PATH)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__0:
                self.state = 186
                self.match(VarDefParser.T__0)
                self.state = 187
                localctx.u = self.match(VarDefParser.ID)


            p =str((None if localctx.p is None else localctx.p.text)); t = Var(p); 
            name=str((None if localctx.i is None else localctx.i.text)).lower(); self.varPathMap[name]=t;
            if localctx.u: self.varPathMap[name].metaData['units']=str((None if localctx.u is None else localctx.u.text)).lower();
            if isTemp: self.tempVarList.append(name); 	

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_metaContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.Var_metaContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Id2Context
            self.m = None # MetaKeyContext
            self.inf = None # MetaValueContext
            self.dv = None # MetaDictContext

        def id2(self):
            return self.getTypedRuleContext(VarDefParser.Id2Context,0)


        def metaKey(self):
            return self.getTypedRuleContext(VarDefParser.MetaKeyContext,0)


        def metaValue(self):
            return self.getTypedRuleContext(VarDefParser.MetaValueContext,0)


        def metaDict(self):
            return self.getTypedRuleContext(VarDefParser.MetaDictContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_var_meta

        def accept(self, visitor):
            if hasattr(visitor, "visitVar_meta"):
                return visitor.visitVar_meta(self)
            else:
                return visitor.visitChildren(self)




    def var_meta(self):

        localctx = VarDefParser.Var_metaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var_meta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            localctx.i = self.id2()
            self.state = 193
            self.match(VarDefParser.T__4)
            self.state = 194
            localctx.m = self.metaKey()
            self.state = 195
            self.match(VarDefParser.T__1)
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT, VarDefParser.ID, VarDefParser.INT]:
                self.state = 196
                localctx.inf = self.metaValue()
                c=str((None if localctx.inf is None else self._input.getText((localctx.inf.start,localctx.inf.stop)))).lower()
                pass
            elif token in [VarDefParser.T__2]:
                self.state = 199
                localctx.dv = self.metaDict()
                c=str((None if localctx.dv is None else self._input.getText((localctx.dv.start,localctx.dv.stop)))).lower()
                pass
            else:
                raise NoViableAltException(self)

            name=str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop)))).lower();mk=str((None if localctx.m is None else self._input.getText((localctx.m.start,localctx.m.stop)))).lower();

            	
            if name in self.varPathMap:
            	self.varPathMap[name].metaData[mk]=c; 
            elif name in self.varExprMap:
            	self.varExprMap[name].metaData[mk]=c; 
            elif name in self.newArrayMap:
            	self.newArrayMap[name].metaData[mk]=c; 
            else:
            	msg=name+'.'+mk+'='+c+' variable \"'+name+'\" not found!'
            	Err.addError(msg, self.vardefFile, self.vardefName)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetaKeyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.MetaKeyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_metaKey

        def accept(self, visitor):
            if hasattr(visitor, "visitMetaKey"):
                return visitor.visitMetaKey(self)
            else:
                return visitor.visitChildren(self)




    def metaKey(self):

        localctx = VarDefParser.MetaKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_metaKey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(VarDefParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetaValueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.MetaValueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(VarDefParser.FLOAT, 0)

        def INT(self):
            return self.getToken(VarDefParser.INT, 0)

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_metaValue

        def accept(self, visitor):
            if hasattr(visitor, "visitMetaValue"):
                return visitor.visitMetaValue(self)
            else:
                return visitor.visitChildren(self)




    def metaValue(self):

        localctx = VarDefParser.MetaValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_metaValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.FLOAT) | (1 << VarDefParser.ID) | (1 << VarDefParser.INT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetaDictContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.MetaDictContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dict_pair(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.Dict_pairContext)
            else:
                return self.getTypedRuleContext(VarDefParser.Dict_pairContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_metaDict

        def accept(self, visitor):
            if hasattr(visitor, "visitMetaDict"):
                return visitor.visitMetaDict(self)
            else:
                return visitor.visitChildren(self)




    def metaDict(self):

        localctx = VarDefParser.MetaDictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_metaDict)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(VarDefParser.T__2)
            self.state = 211
            self.dict_pair()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 212
                self.match(VarDefParser.T__0)
                self.state = 213
                self.dict_pair()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self.match(VarDefParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_pairContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.Dict_pairContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.ID)
            else:
                return self.getToken(VarDefParser.ID, i)

        def STRING(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.STRING)
            else:
                return self.getToken(VarDefParser.STRING, i)

        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.NumberContext)
            else:
                return self.getTypedRuleContext(VarDefParser.NumberContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_dict_pair

        def accept(self, visitor):
            if hasattr(visitor, "visitDict_pair"):
                return visitor.visitDict_pair(self)
            else:
                return visitor.visitChildren(self)




    def dict_pair(self):

        localctx = VarDefParser.Dict_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_dict_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.ID]:
                self.state = 221
                self.match(VarDefParser.ID)
                pass
            elif token in [VarDefParser.STRING]:
                self.state = 222
                self.match(VarDefParser.STRING)
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 223
                self.number()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 226
            self.match(VarDefParser.T__5)
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.ID]:
                self.state = 227
                self.match(VarDefParser.ID)
                pass
            elif token in [VarDefParser.STRING]:
                self.state = 228
                self.match(VarDefParser.STRING)
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 229
                self.number()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.NumberContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(VarDefParser.FLOAT, 0)

        def INT(self):
            return self.getToken(VarDefParser.INT, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_number

        def accept(self, visitor):
            if hasattr(visitor, "visitNumber"):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = VarDefParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not(_la==VarDefParser.FLOAT or _la==VarDefParser.INT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.StatContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.e = None # EeContext

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def T(self):
            return self.getToken(VarDefParser.T, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_stat

        def accept(self, visitor):
            if hasattr(visitor, "visitStat"):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = VarDefParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stat)
        isTemp=False 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 234
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 238
            localctx.i = self.match(VarDefParser.ID)
            self.state = 239
            self.match(VarDefParser.T__1)
            self.state = 240
            localctx.e = self.ee(0)
            self._ctx.stop = self._input.LT(-1)

            v = Var('');
            e=str((None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop))));v.expr=e.lower();
            name=str((None if localctx.i is None else localctx.i.text)).lower(); self.varExprMap[name]=v; 
            if isTemp: 
            	self.tempVarList.append(name);	

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.EeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.x = None
            self.a = None # EeContext
            self.i = None # Token
            self.o = None # Token
            self.b = None # EeContext

        def INT(self):
            return self.getToken(VarDefParser.INT, 0)

        def FLOAT(self):
            return self.getToken(VarDefParser.FLOAT, 0)

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def ee(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.EeContext)
            else:
                return self.getTypedRuleContext(VarDefParser.EeContext,i)


        def STRING(self):
            return self.getToken(VarDefParser.STRING, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_ee

        def accept(self, visitor):
            if hasattr(visitor, "visitEe"):
                return visitor.visitEe(self)
            else:
                return visitor.visitChildren(self)



    def ee(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VarDefParser.EeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                s=''
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 244
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 248
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 251
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 255
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 257
                localctx.i = self.match(VarDefParser.ID)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();
                if vName in self.newArrayMap.keys() or vName in self.varPathMap.keys() or vName in self.varExprMap.keys():
                	localctx.x = self.ifsAppend+"['"+vName+"']"+"[i]"
                	#print (vName) 
                else:
                	Err.addError(vName+' not defined.', self.vardefFile, self.vardefName)

                pass

            elif la_ == 4:
                self.state = 259
                self.match(VarDefParser.T__6)
                self.state = 260
                localctx.a = self.ee(0)
                self.state = 261
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.a.x)+")"
                pass

            elif la_ == 5:
                self.state = 264
                localctx.i = self.match(VarDefParser.STRING)
                localctx.x=  str((None if localctx.i is None else localctx.i.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 278
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 268
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 269
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 270
                        localctx.b = self.ee(8)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 273
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 274
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 275
                        localctx.b = self.ee(7)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class CompareContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.CompareContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.x = None
            self.c1 = None # CompareContext
            self.a = None # EeContext
            self.o = None # Token
            self.b = None # EeContext
            self.c = None # CompareContext
            self.op = None # Token
            self.c2 = None # CompareContext

        def ee(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.EeContext)
            else:
                return self.getTypedRuleContext(VarDefParser.EeContext,i)


        def compare(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.CompareContext)
            else:
                return self.getTypedRuleContext(VarDefParser.CompareContext,i)


        def AND(self):
            return self.getToken(VarDefParser.AND, 0)

        def OR(self):
            return self.getToken(VarDefParser.OR, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_compare

        def accept(self, visitor):
            if hasattr(visitor, "visitCompare"):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)



    def compare(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VarDefParser.CompareContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_compare, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 284
                localctx.a = self.ee(0)
                self.state = 285
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10) | (1 << VarDefParser.T__11) | (1 << VarDefParser.T__12) | (1 << VarDefParser.T__13))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 286
                localctx.b = self.ee(0)
                localctx.x=str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 289
                self.match(VarDefParser.T__6)
                self.state = 290
                localctx.c = self.compare(0)
                self.state = 291
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VarDefParser.CompareContext(self, _parentctx, _parentState)
                    localctx.c1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare)
                    self.state = 296
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 297
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 298
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.x = None
            self.i = None # Id2Context
            self.a = None # EeContext

        def id2(self):
            return self.getTypedRuleContext(VarDefParser.Id2Context,0)


        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_assign

        def accept(self, visitor):
            if hasattr(visitor, "visitAssign"):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = VarDefParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            localctx.i = self.id2()
            self.state = 307
            self.match(VarDefParser.T__1)
            self.state = 308
            localctx.a = self.ee(0)
            vName=str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop)))).lower();
            if vName in self.newArrayMap.keys() or vName in self.varExprMap.keys():
            	localctx.x = self.ifsNewAppend+"['"+str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop))))+"'][i]="+localctx.a.x
            	#print (vName) 
            else:
            	Err.addError(vName+' not valid.', self.vardefFile, self.vardefName)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Id2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.Id2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.ID)
            else:
                return self.getToken(VarDefParser.ID, i)

        def getRuleIndex(self):
            return VarDefParser.RULE_id2

        def accept(self, visitor):
            if hasattr(visitor, "visitId2"):
                return visitor.visitId2(self)
            else:
                return visitor.visitChildren(self)




    def id2(self):

        localctx = VarDefParser.Id2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_id2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(VarDefParser.ID)
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 312
                self.match(VarDefParser.T__4)
                self.state = 313
                self.match(VarDefParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_statContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.If_statContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None # CompareContext
            self.a = None # AssignContext

        def IF(self):
            return self.getToken(VarDefParser.IF, 0)

        def compare(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.CompareContext)
            else:
                return self.getTypedRuleContext(VarDefParser.CompareContext,i)


        def NL(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.NL)
            else:
                return self.getToken(VarDefParser.NL, i)

        def ELSEIF(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.ELSEIF)
            else:
                return self.getToken(VarDefParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(VarDefParser.ELSE, 0)

        def assign(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.AssignContext)
            else:
                return self.getTypedRuleContext(VarDefParser.AssignContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_if_stat

        def accept(self, visitor):
            if hasattr(visitor, "visitIf_stat"):
                return visitor.visitIf_stat(self)
            else:
                return visitor.visitChildren(self)




    def if_stat(self):

        localctx = VarDefParser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stat)
        ifs=collections.OrderedDict();al=[];
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(VarDefParser.IF)
            self.state = 317
            localctx.c = self.compare(0)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 318
                self.match(VarDefParser.NL)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 324
            self.match(VarDefParser.T__2)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 325
                self.match(VarDefParser.NL)
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 339 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 331
                localctx.a = self.assign()
                t=str(localctx.a.x).lower();al.append(t)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 333
                    self.match(VarDefParser.NL)
                    self.state = 338
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 341 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 343
            self.match(VarDefParser.T__3)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 344
                    self.match(VarDefParser.NL) 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 351
                self.match(VarDefParser.ELSEIF)
                self.state = 352
                localctx.c = self.compare(0)
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 353
                    self.match(VarDefParser.NL)
                    self.state = 358
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 359
                self.match(VarDefParser.T__2)
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 360
                    self.match(VarDefParser.NL)
                    self.state = 365
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 374 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 366
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 371
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 368
                        self.match(VarDefParser.NL)
                        self.state = 373
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 376 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 378
                self.match(VarDefParser.T__3)
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 379
                        self.match(VarDefParser.NL) 
                    self.state = 384
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

                k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 392
                self.match(VarDefParser.ELSE)
                self.state = 396
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 393
                    self.match(VarDefParser.NL)
                    self.state = 398
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 399
                self.match(VarDefParser.T__2)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 400
                    self.match(VarDefParser.NL)
                    self.state = 405
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 414 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 406
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 411
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 408
                        self.match(VarDefParser.NL)
                        self.state = 413
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 416 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 418
                self.match(VarDefParser.T__3)
                self.state = 420 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 419
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 422 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

                ifs['always']=al


            self._ctx.stop = self._input.LT(-1)
            self.ifsMap[self.ifid]=ifs;
            #for s in ifs: print(s,ifs[s]);

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.ee_sempred
        self._predicates[20] = self.compare_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def ee_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

    def compare_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




