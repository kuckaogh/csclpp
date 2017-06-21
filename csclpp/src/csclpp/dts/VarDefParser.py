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
        buf.write(u".\u01f0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\3\2\7\2\62\n\2\f\2\16\2\65\13\2\3\2\3\2\7\29\n")
        buf.write(u"\2\f\2\16\2<\13\2\3\2\6\2?\n\2\r\2\16\2@\3\3\3\3\3\3")
        buf.write(u"\3\3\3\4\3\4\3\4\3\4\6\4K\n\4\r\4\16\4L\3\4\6\4P\n\4")
        buf.write(u"\r\4\16\4Q\3\4\3\4\6\4V\n\4\r\4\16\4W\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5e\n\5\3\5\6\5h\n\5\r")
        buf.write(u"\5\16\5i\3\6\3\6\5\6n\n\6\3\7\3\7\3\7\3\7\7\7t\n\7\f")
        buf.write(u"\7\16\7w\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0081")
        buf.write(u"\n\b\3\b\3\b\3\t\5\t\u0086\n\t\3\t\3\t\3\t\3\t\7\t\u008c")
        buf.write(u"\n\t\f\t\16\t\u008f\13\t\3\n\3\n\5\n\u0093\n\n\3\n\3")
        buf.write(u"\n\3\n\3\13\5\13\u0099\n\13\3\13\3\13\3\13\5\13\u009e")
        buf.write(u"\n\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a6\n\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\5\13\u00ae\n\13\3\13\3\13")
        buf.write(u"\7\13\u00b2\n\13\f\13\16\13\u00b5\13\13\3\13\3\13\3\f")
        buf.write(u"\3\f\3\f\3\r\3\r\5\r\u00be\n\r\3\r\3\r\3\r\3\r\3\r\5")
        buf.write(u"\r\u00c5\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write(u"\16\3\16\3\16\3\16\5\16\u00d3\n\16\3\16\3\16\3\16\5\16")
        buf.write(u"\u00d8\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\7\17\u00e3\n\17\f\17\16\17\u00e6\13\17\3\17\3\17")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00f1\n\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00fb\n\20")
        buf.write(u"\3\20\3\20\3\21\3\21\3\22\3\22\5\22\u0103\n\22\3\22\3")
        buf.write(u"\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u010d\n\23\3\23")
        buf.write(u"\3\23\3\23\3\23\3\23\5\23\u0114\n\23\3\23\3\23\3\23\3")
        buf.write(u"\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0121\n\23")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7")
        buf.write(u"\23\u012d\n\23\f\23\16\23\u0130\13\23\3\24\3\24\3\24")
        buf.write(u"\3\24\5\24\u0136\n\24\3\24\3\24\3\24\3\24\3\24\5\24\u013d")
        buf.write(u"\n\24\3\24\3\24\3\24\3\24\3\24\5\24\u0144\n\24\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u014e\n\24\3\24")
        buf.write(u"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u015a")
        buf.write(u"\n\24\f\24\16\24\u015d\13\24\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u016a\n\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\7\25\u0171\n\25\f\25\16\25\u0174\13")
        buf.write(u"\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\5\27\u017e")
        buf.write(u"\n\27\3\30\3\30\3\30\7\30\u0183\n\30\f\30\16\30\u0186")
        buf.write(u"\13\30\3\30\3\30\7\30\u018a\n\30\f\30\16\30\u018d\13")
        buf.write(u"\30\3\30\3\30\3\30\7\30\u0192\n\30\f\30\16\30\u0195\13")
        buf.write(u"\30\6\30\u0197\n\30\r\30\16\30\u0198\3\30\3\30\7\30\u019d")
        buf.write(u"\n\30\f\30\16\30\u01a0\13\30\3\30\3\30\3\30\3\30\7\30")
        buf.write(u"\u01a6\n\30\f\30\16\30\u01a9\13\30\3\30\3\30\7\30\u01ad")
        buf.write(u"\n\30\f\30\16\30\u01b0\13\30\3\30\3\30\3\30\7\30\u01b5")
        buf.write(u"\n\30\f\30\16\30\u01b8\13\30\6\30\u01ba\n\30\r\30\16")
        buf.write(u"\30\u01bb\3\30\3\30\7\30\u01c0\n\30\f\30\16\30\u01c3")
        buf.write(u"\13\30\3\30\3\30\7\30\u01c7\n\30\f\30\16\30\u01ca\13")
        buf.write(u"\30\3\30\3\30\7\30\u01ce\n\30\f\30\16\30\u01d1\13\30")
        buf.write(u"\3\30\3\30\7\30\u01d5\n\30\f\30\16\30\u01d8\13\30\3\30")
        buf.write(u"\3\30\3\30\7\30\u01dd\n\30\f\30\16\30\u01e0\13\30\6\30")
        buf.write(u"\u01e2\n\30\r\30\16\30\u01e3\3\30\3\30\6\30\u01e8\n\30")
        buf.write(u"\r\30\16\30\u01e9\3\30\3\30\5\30\u01ee\n\30\3\30\2\5")
        buf.write(u"$&(\31\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(u",.\2\7\4\2))++\3\2\24\25\3\2\26\27\3\2\13\20\3\2\30\31")
        buf.write(u"\u0221\2\63\3\2\2\2\4B\3\2\2\2\6F\3\2\2\2\bd\3\2\2\2")
        buf.write(u"\nm\3\2\2\2\fo\3\2\2\2\16x\3\2\2\2\20\u0085\3\2\2\2\22")
        buf.write(u"\u0092\3\2\2\2\24\u0098\3\2\2\2\26\u00b8\3\2\2\2\30\u00bd")
        buf.write(u"\3\2\2\2\32\u00c8\3\2\2\2\34\u00db\3\2\2\2\36\u00f0\3")
        buf.write(u"\2\2\2 \u00fe\3\2\2\2\"\u0102\3\2\2\2$\u0120\3\2\2\2")
        buf.write(u"&\u014d\3\2\2\2(\u0169\3\2\2\2*\u0175\3\2\2\2,\u017a")
        buf.write(u"\3\2\2\2.\u017f\3\2\2\2\60\62\7-\2\2\61\60\3\2\2\2\62")
        buf.write(u"\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2")
        buf.write(u"\65\63\3\2\2\2\66:\5\4\3\2\679\7-\2\28\67\3\2\2\29<\3")
        buf.write(u"\2\2\2:8\3\2\2\2:;\3\2\2\2;>\3\2\2\2<:\3\2\2\2=?\5\6")
        buf.write(u"\4\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\3\3\2\2")
        buf.write(u"\2BC\7\32\2\2CD\7*\2\2DE\b\3\1\2E\5\3\2\2\2FG\7\34\2")
        buf.write(u"\2GH\7*\2\2HJ\b\4\1\2IK\7-\2\2JI\3\2\2\2KL\3\2\2\2LJ")
        buf.write(u"\3\2\2\2LM\3\2\2\2MO\3\2\2\2NP\5\b\5\2ON\3\2\2\2PQ\3")
        buf.write(u"\2\2\2QO\3\2\2\2QR\3\2\2\2RS\3\2\2\2SU\7\35\2\2TV\7-")
        buf.write(u"\2\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\7\3\2\2")
        buf.write(u"\2Ye\5\30\r\2Ze\5\32\16\2[\\\5\"\22\2\\]\b\5\1\2]e\3")
        buf.write(u"\2\2\2^_\5.\30\2_`\b\5\1\2`e\3\2\2\2ae\5\n\6\2be\5\26")
        buf.write(u"\f\2ce\5\f\7\2dY\3\2\2\2dZ\3\2\2\2d[\3\2\2\2d^\3\2\2")
        buf.write(u"\2da\3\2\2\2db\3\2\2\2dc\3\2\2\2eg\3\2\2\2fh\7-\2\2g")
        buf.write(u"f\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\t\3\2\2\2kn")
        buf.write(u"\5\20\t\2ln\5\24\13\2mk\3\2\2\2ml\3\2\2\2n\13\3\2\2\2")
        buf.write(u"op\7&\2\2pu\5\16\b\2qr\7\3\2\2rt\5\16\b\2sq\3\2\2\2t")
        buf.write(u"w\3\2\2\2us\3\2\2\2uv\3\2\2\2v\r\3\2\2\2wu\3\2\2\2xy")
        buf.write(u"\7*\2\2y\u0080\7\4\2\2z{\7)\2\2{\u0081\b\b\1\2|}\7+\2")
        buf.write(u"\2}\u0081\b\b\1\2~\177\7,\2\2\177\u0081\b\b\1\2\u0080")
        buf.write(u"z\3\2\2\2\u0080|\3\2\2\2\u0080~\3\2\2\2\u0081\u0082\3")
        buf.write(u"\2\2\2\u0082\u0083\b\b\1\2\u0083\17\3\2\2\2\u0084\u0086")
        buf.write(u"\7#\2\2\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write(u"\u0087\3\2\2\2\u0087\u0088\7\36\2\2\u0088\u008d\5\22")
        buf.write(u"\n\2\u0089\u008a\7\3\2\2\u008a\u008c\5\22\n\2\u008b\u0089")
        buf.write(u"\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write(u"\u008e\3\2\2\2\u008e\21\3\2\2\2\u008f\u008d\3\2\2\2\u0090")
        buf.write(u"\u0091\7\22\2\2\u0091\u0093\b\n\1\2\u0092\u0090\3\2\2")
        buf.write(u"\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095")
        buf.write(u"\7*\2\2\u0095\u0096\b\n\1\2\u0096\23\3\2\2\2\u0097\u0099")
        buf.write(u"\7#\2\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write(u"\u009a\3\2\2\2\u009a\u009d\7\36\2\2\u009b\u009c\7\22")
        buf.write(u"\2\2\u009c\u009e\b\13\1\2\u009d\u009b\3\2\2\2\u009d\u009e")
        buf.write(u"\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\7*\2\2\u00a0")
        buf.write(u"\u00a1\b\13\1\2\u00a1\u00a2\7\5\2\2\u00a2\u00a5\b\13")
        buf.write(u"\1\2\u00a3\u00a4\7\22\2\2\u00a4\u00a6\b\13\1\2\u00a5")
        buf.write(u"\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2")
        buf.write(u"\2\u00a7\u00a8\7*\2\2\u00a8\u00b3\b\13\1\2\u00a9\u00aa")
        buf.write(u"\7\3\2\2\u00aa\u00ad\b\13\1\2\u00ab\u00ac\7\22\2\2\u00ac")
        buf.write(u"\u00ae\b\13\1\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2")
        buf.write(u"\2\u00ae\u00af\3\2\2\2\u00af\u00b0\7*\2\2\u00b0\u00b2")
        buf.write(u"\b\13\1\2\u00b1\u00a9\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3")
        buf.write(u"\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\3\2\2")
        buf.write(u"\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\7\6\2\2\u00b7\25\3")
        buf.write(u"\2\2\2\u00b8\u00b9\7\33\2\2\u00b9\u00ba\7*\2\2\u00ba")
        buf.write(u"\27\3\2\2\2\u00bb\u00bc\7\22\2\2\u00bc\u00be\b\r\1\2")
        buf.write(u"\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf")
        buf.write(u"\3\2\2\2\u00bf\u00c0\7*\2\2\u00c0\u00c1\7\4\2\2\u00c1")
        buf.write(u"\u00c4\7\23\2\2\u00c2\u00c3\7\3\2\2\u00c3\u00c5\7,\2")
        buf.write(u"\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6")
        buf.write(u"\3\2\2\2\u00c6\u00c7\b\r\1\2\u00c7\31\3\2\2\2\u00c8\u00c9")
        buf.write(u"\5,\27\2\u00c9\u00ca\7\7\2\2\u00ca\u00cb\7*\2\2\u00cb")
        buf.write(u"\u00d7\7\4\2\2\u00cc\u00cd\7)\2\2\u00cd\u00d3\b\16\1")
        buf.write(u"\2\u00ce\u00cf\7+\2\2\u00cf\u00d3\b\16\1\2\u00d0\u00d1")
        buf.write(u"\7,\2\2\u00d1\u00d3\b\16\1\2\u00d2\u00cc\3\2\2\2\u00d2")
        buf.write(u"\u00ce\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d8\3\2\2")
        buf.write(u"\2\u00d4\u00d5\5\34\17\2\u00d5\u00d6\b\16\1\2\u00d6\u00d8")
        buf.write(u"\3\2\2\2\u00d7\u00d2\3\2\2\2\u00d7\u00d4\3\2\2\2\u00d8")
        buf.write(u"\u00d9\3\2\2\2\u00d9\u00da\b\16\1\2\u00da\33\3\2\2\2")
        buf.write(u"\u00db\u00dc\7\5\2\2\u00dc\u00dd\5\36\20\2\u00dd\u00e4")
        buf.write(u"\b\17\1\2\u00de\u00df\7\3\2\2\u00df\u00e0\5\36\20\2\u00e0")
        buf.write(u"\u00e1\b\17\1\2\u00e1\u00e3\3\2\2\2\u00e2\u00de\3\2\2")
        buf.write(u"\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write(u"\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7")
        buf.write(u"\u00e8\7\6\2\2\u00e8\35\3\2\2\2\u00e9\u00ea\7*\2\2\u00ea")
        buf.write(u"\u00f1\b\20\1\2\u00eb\u00ec\7,\2\2\u00ec\u00f1\b\20\1")
        buf.write(u"\2\u00ed\u00ee\5 \21\2\u00ee\u00ef\b\20\1\2\u00ef\u00f1")
        buf.write(u"\3\2\2\2\u00f0\u00e9\3\2\2\2\u00f0\u00eb\3\2\2\2\u00f0")
        buf.write(u"\u00ed\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00fa\7\b\2")
        buf.write(u"\2\u00f3\u00f4\7*\2\2\u00f4\u00fb\b\20\1\2\u00f5\u00f6")
        buf.write(u"\7,\2\2\u00f6\u00fb\b\20\1\2\u00f7\u00f8\5 \21\2\u00f8")
        buf.write(u"\u00f9\b\20\1\2\u00f9\u00fb\3\2\2\2\u00fa\u00f3\3\2\2")
        buf.write(u"\2\u00fa\u00f5\3\2\2\2\u00fa\u00f7\3\2\2\2\u00fb\u00fc")
        buf.write(u"\3\2\2\2\u00fc\u00fd\b\20\1\2\u00fd\37\3\2\2\2\u00fe")
        buf.write(u"\u00ff\t\2\2\2\u00ff!\3\2\2\2\u0100\u0101\7\22\2\2\u0101")
        buf.write(u"\u0103\b\22\1\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2")
        buf.write(u"\2\u0103\u0104\3\2\2\2\u0104\u0105\7*\2\2\u0105\u0106")
        buf.write(u"\7\4\2\2\u0106\u0107\5$\23\2\u0107#\3\2\2\2\u0108\u0109")
        buf.write(u"\b\23\1\2\u0109\u010c\b\23\1\2\u010a\u010b\7\27\2\2\u010b")
        buf.write(u"\u010d\b\23\1\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2")
        buf.write(u"\2\u010d\u010e\3\2\2\2\u010e\u010f\7+\2\2\u010f\u0121")
        buf.write(u"\b\23\1\2\u0110\u0113\b\23\1\2\u0111\u0112\7\27\2\2\u0112")
        buf.write(u"\u0114\b\23\1\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2")
        buf.write(u"\2\u0114\u0115\3\2\2\2\u0115\u0116\7)\2\2\u0116\u0121")
        buf.write(u"\b\23\1\2\u0117\u0118\7*\2\2\u0118\u0121\b\23\1\2\u0119")
        buf.write(u"\u011a\7\t\2\2\u011a\u011b\5$\23\2\u011b\u011c\7\n\2")
        buf.write(u"\2\u011c\u011d\b\23\1\2\u011d\u0121\3\2\2\2\u011e\u011f")
        buf.write(u"\7,\2\2\u011f\u0121\b\23\1\2\u0120\u0108\3\2\2\2\u0120")
        buf.write(u"\u0110\3\2\2\2\u0120\u0117\3\2\2\2\u0120\u0119\3\2\2")
        buf.write(u"\2\u0120\u011e\3\2\2\2\u0121\u012e\3\2\2\2\u0122\u0123")
        buf.write(u"\f\t\2\2\u0123\u0124\t\3\2\2\u0124\u0125\5$\23\n\u0125")
        buf.write(u"\u0126\b\23\1\2\u0126\u012d\3\2\2\2\u0127\u0128\f\b\2")
        buf.write(u"\2\u0128\u0129\t\4\2\2\u0129\u012a\5$\23\t\u012a\u012b")
        buf.write(u"\b\23\1\2\u012b\u012d\3\2\2\2\u012c\u0122\3\2\2\2\u012c")
        buf.write(u"\u0127\3\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2")
        buf.write(u"\2\u012e\u012f\3\2\2\2\u012f%\3\2\2\2\u0130\u012e\3\2")
        buf.write(u"\2\2\u0131\u0132\b\24\1\2\u0132\u0135\b\24\1\2\u0133")
        buf.write(u"\u0134\7\27\2\2\u0134\u0136\b\24\1\2\u0135\u0133\3\2")
        buf.write(u"\2\2\u0135\u0136\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138")
        buf.write(u"\7+\2\2\u0138\u014e\b\24\1\2\u0139\u013c\b\24\1\2\u013a")
        buf.write(u"\u013b\7\27\2\2\u013b\u013d\b\24\1\2\u013c\u013a\3\2")
        buf.write(u"\2\2\u013c\u013d\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f")
        buf.write(u"\7)\2\2\u013f\u014e\b\24\1\2\u0140\u0143\7*\2\2\u0141")
        buf.write(u"\u0142\7\7\2\2\u0142\u0144\7*\2\2\u0143\u0141\3\2\2\2")
        buf.write(u"\u0143\u0144\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u014e")
        buf.write(u"\b\24\1\2\u0146\u0147\7\t\2\2\u0147\u0148\5&\24\2\u0148")
        buf.write(u"\u0149\7\n\2\2\u0149\u014a\b\24\1\2\u014a\u014e\3\2\2")
        buf.write(u"\2\u014b\u014c\7,\2\2\u014c\u014e\b\24\1\2\u014d\u0131")
        buf.write(u"\3\2\2\2\u014d\u0139\3\2\2\2\u014d\u0140\3\2\2\2\u014d")
        buf.write(u"\u0146\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u015b\3\2\2")
        buf.write(u"\2\u014f\u0150\f\t\2\2\u0150\u0151\t\3\2\2\u0151\u0152")
        buf.write(u"\5&\24\n\u0152\u0153\b\24\1\2\u0153\u015a\3\2\2\2\u0154")
        buf.write(u"\u0155\f\b\2\2\u0155\u0156\t\4\2\2\u0156\u0157\5&\24")
        buf.write(u"\t\u0157\u0158\b\24\1\2\u0158\u015a\3\2\2\2\u0159\u014f")
        buf.write(u"\3\2\2\2\u0159\u0154\3\2\2\2\u015a\u015d\3\2\2\2\u015b")
        buf.write(u"\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\'\3\2\2\2\u015d")
        buf.write(u"\u015b\3\2\2\2\u015e\u015f\b\25\1\2\u015f\u0160\5&\24")
        buf.write(u"\2\u0160\u0161\t\5\2\2\u0161\u0162\5&\24\2\u0162\u0163")
        buf.write(u"\b\25\1\2\u0163\u016a\3\2\2\2\u0164\u0165\7\t\2\2\u0165")
        buf.write(u"\u0166\5(\25\2\u0166\u0167\7\n\2\2\u0167\u0168\b\25\1")
        buf.write(u"\2\u0168\u016a\3\2\2\2\u0169\u015e\3\2\2\2\u0169\u0164")
        buf.write(u"\3\2\2\2\u016a\u0172\3\2\2\2\u016b\u016c\f\3\2\2\u016c")
        buf.write(u"\u016d\t\6\2\2\u016d\u016e\5(\25\4\u016e\u016f\b\25\1")
        buf.write(u"\2\u016f\u0171\3\2\2\2\u0170\u016b\3\2\2\2\u0171\u0174")
        buf.write(u"\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write(u")\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176\5,\27\2\u0176")
        buf.write(u"\u0177\7\4\2\2\u0177\u0178\5&\24\2\u0178\u0179\b\26\1")
        buf.write(u"\2\u0179+\3\2\2\2\u017a\u017d\7*\2\2\u017b\u017c\7\7")
        buf.write(u"\2\2\u017c\u017e\7*\2\2\u017d\u017b\3\2\2\2\u017d\u017e")
        buf.write(u"\3\2\2\2\u017e-\3\2\2\2\u017f\u0180\7\37\2\2\u0180\u0184")
        buf.write(u"\5(\25\2\u0181\u0183\7-\2\2\u0182\u0181\3\2\2\2\u0183")
        buf.write(u"\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2")
        buf.write(u"\2\u0185\u0187\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u018b")
        buf.write(u"\7\5\2\2\u0188\u018a\7-\2\2\u0189\u0188\3\2\2\2\u018a")
        buf.write(u"\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2")
        buf.write(u"\2\u018c\u0196\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u018f")
        buf.write(u"\5*\26\2\u018f\u0193\b\30\1\2\u0190\u0192\7-\2\2\u0191")
        buf.write(u"\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2")
        buf.write(u"\2\u0193\u0194\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193")
        buf.write(u"\3\2\2\2\u0196\u018e\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write(u"\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\3\2\2")
        buf.write(u"\2\u019a\u019e\7\6\2\2\u019b\u019d\7-\2\2\u019c\u019b")
        buf.write(u"\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write(u"\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2")
        buf.write(u"\2\u01a1\u01c8\b\30\1\2\u01a2\u01a3\7 \2\2\u01a3\u01a7")
        buf.write(u"\5(\25\2\u01a4\u01a6\7-\2\2\u01a5\u01a4\3\2\2\2\u01a6")
        buf.write(u"\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2")
        buf.write(u"\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ae")
        buf.write(u"\7\5\2\2\u01ab\u01ad\7-\2\2\u01ac\u01ab\3\2\2\2\u01ad")
        buf.write(u"\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2")
        buf.write(u"\2\u01af\u01b9\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2")
        buf.write(u"\5*\26\2\u01b2\u01b6\b\30\1\2\u01b3\u01b5\7-\2\2\u01b4")
        buf.write(u"\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2")
        buf.write(u"\2\u01b6\u01b7\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6")
        buf.write(u"\3\2\2\2\u01b9\u01b1\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write(u"\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\3\2\2")
        buf.write(u"\2\u01bd\u01c1\7\6\2\2\u01be\u01c0\7-\2\2\u01bf\u01be")
        buf.write(u"\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1")
        buf.write(u"\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01c1\3\2\2")
        buf.write(u"\2\u01c4\u01c5\b\30\1\2\u01c5\u01c7\3\2\2\2\u01c6\u01a2")
        buf.write(u"\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write(u"\u01c9\3\2\2\2\u01c9\u01ed\3\2\2\2\u01ca\u01c8\3\2\2")
        buf.write(u"\2\u01cb\u01cf\7!\2\2\u01cc\u01ce\7-\2\2\u01cd\u01cc")
        buf.write(u"\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf")
        buf.write(u"\u01d0\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01cf\3\2\2")
        buf.write(u"\2\u01d2\u01d6\7\5\2\2\u01d3\u01d5\7-\2\2\u01d4\u01d3")
        buf.write(u"\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write(u"\u01d7\3\2\2\2\u01d7\u01e1\3\2\2\2\u01d8\u01d6\3\2\2")
        buf.write(u"\2\u01d9\u01da\5*\26\2\u01da\u01de\b\30\1\2\u01db\u01dd")
        buf.write(u"\7-\2\2\u01dc\u01db\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de")
        buf.write(u"\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e2\3\2\2")
        buf.write(u"\2\u01e0\u01de\3\2\2\2\u01e1\u01d9\3\2\2\2\u01e2\u01e3")
        buf.write(u"\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write(u"\u01e5\3\2\2\2\u01e5\u01e7\7\6\2\2\u01e6\u01e8\7-\2\2")
        buf.write(u"\u01e7\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01e7")
        buf.write(u"\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb")
        buf.write(u"\u01ec\b\30\1\2\u01ec\u01ee\3\2\2\2\u01ed\u01cb\3\2\2")
        buf.write(u"\2\u01ed\u01ee\3\2\2\2\u01ee/\3\2\2\2<\63:@LQWdimu\u0080")
        buf.write(u"\u0085\u008d\u0092\u0098\u009d\u00a5\u00ad\u00b3\u00bd")
        buf.write(u"\u00c4\u00d2\u00d7\u00e4\u00f0\u00fa\u0102\u010c\u0113")
        buf.write(u"\u0120\u012c\u012e\u0135\u013c\u0143\u014d\u0159\u015b")
        buf.write(u"\u0169\u0172\u017d\u0184\u018b\u0193\u0198\u019e\u01a7")
        buf.write(u"\u01ae\u01b6\u01bb\u01c1\u01c8\u01cf\u01d6\u01de\u01e3")
        buf.write(u"\u01e9\u01ed")
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
    RULE_metaDict = 13
    RULE_dict_pair = 14
    RULE_number = 15
    RULE_stat = 16
    RULE_ee_dts = 17
    RULE_ee = 18
    RULE_compare = 19
    RULE_assign = 20
    RULE_id2 = 21
    RULE_if_stat = 22

    ruleNames =  [ u"prog", u"use", u"vardef", u"field", u"new_var", u"constant", 
                   u"const_var", u"array", u"array_var", u"array_cluster", 
                   u"include", u"var_path", u"var_meta", u"metaDict", u"dict_pair", 
                   u"number", u"stat", u"ee_dts", u"ee", u"compare", u"assign", 
                   u"id2", u"if_stat" ]

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
        self.ifid=0;

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 46
                self.match(VarDefParser.NL)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.use()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 53
                self.match(VarDefParser.NL)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.vardef()
                self.state = 62 
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
            self.state = 64
            self.match(VarDefParser.USE)
            self.state = 65
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

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(VarDefParser.VARDEF)
            self.state = 69
            localctx.name = self.match(VarDefParser.ID)
            groupName=str((None if localctx.name is None else localctx.name.text)).lower();self.vardefName=groupName;
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.match(VarDefParser.NL)
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.field()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ARRAY) | (1 << VarDefParser.IF) | (1 << VarDefParser.STRING_L) | (1 << VarDefParser.CONST) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 81
            self.match(VarDefParser.END)
            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self.match(VarDefParser.NL)
                self.state = 85 
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
                self.state = 87
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 88
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 89
                self.stat()
                self.ifid=self.ifid+1;
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
            self.l = None # Token

        def ARRAY(self):
            return self.getToken(VarDefParser.ARRAY, 0)

        def array_var(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.Array_varContext)
            else:
                return self.getTypedRuleContext(VarDefParser.Array_varContext,i)


        def STRING_L(self):
            return self.getToken(VarDefParser.STRING_L, 0)

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
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.STRING_L:
                self.state = 130
                localctx.l = self.match(VarDefParser.STRING_L)


            self.state = 133
            self.match(VarDefParser.ARRAY)
            self.state = 134
            self.array_var(localctx.l!=None)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 135
                self.match(VarDefParser.T__0)
                self.state = 136
                self.array_var(localctx.l!=None)
                self.state = 141
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

        def __init__(self, parser, parent=None, invokingState=-1, isStr=None):
            super(VarDefParser.Array_varContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.isStr = None
            self.i = None # Token
            self.isStr = isStr

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




    def array_var(self, isStr):

        localctx = VarDefParser.Array_varContext(self, self._ctx, self.state, isStr)
        self.enterRule(localctx, 16, self.RULE_array_var)
        isTemp=False;
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 142
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 146
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();
            if isStr:
            	v.type='str'
            	#print (name+' is string')
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
            self.l = None # Token
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

        def STRING_L(self):
            return self.getToken(VarDefParser.STRING_L, 0)

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
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.STRING_L:
                self.state = 149
                localctx.l = self.match(VarDefParser.STRING_L)


            self.state = 152
            self.match(VarDefParser.ARRAY)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 153
                self.match(VarDefParser.T)
                isGroupTemp=True


            self.state = 157
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 159
            self.match(VarDefParser.T__2)
            isTemp=False;
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 161
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 165
            localctx.i = self.match(VarDefParser.ID)
            subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 167
                self.match(VarDefParser.T__0)
                isTemp=False;
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 169
                    self.match(VarDefParser.T)
                    isTemp=True


                self.state = 173
                localctx.i = self.match(VarDefParser.ID)
                subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(VarDefParser.T__3)
            self._ctx.stop = self._input.LT(-1)

            for k in subvar.keys():
            	o = Var('')
            	name=header.lower()+'.'+k.lower()
            	if localctx.l!=None: 
            		o.type='str';
            		#print (name+' is string')
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
            self.state = 182
            self.match(VarDefParser.INCLUDE)
            self.state = 183
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

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def PATH(self):
            return self.getToken(VarDefParser.PATH, 0)

        def T(self):
            return self.getToken(VarDefParser.T, 0)

        def STRING(self):
            return self.getToken(VarDefParser.STRING, 0)

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
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 185
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 189
            localctx.i = self.match(VarDefParser.ID)
            self.state = 190
            self.match(VarDefParser.T__1)
            self.state = 191
            localctx.p = self.match(VarDefParser.PATH)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__0:
                self.state = 192
                self.match(VarDefParser.T__0)
                self.state = 193
                localctx.u = self.match(VarDefParser.STRING)


            p =str((None if localctx.p is None else localctx.p.text)); t = Var(p); 
            name=str((None if localctx.i is None else localctx.i.text)).lower(); self.varPathMap[name]=t;
            if localctx.u: self.varPathMap[name].metaData['units']=str((None if localctx.u is None else localctx.u.text))[1:-1].lower();
            if isTemp: self.tempVarList.append(name); 
            self.varPathMap[name].metaData['_partc']=str((None if localctx.p is None else localctx.p.text)).split("/")[3];	
            self.varPathMap[name].metaData['_partb']=str((None if localctx.p is None else localctx.p.text)).split("/")[2];	

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
            self.m = None # Token
            self.k = None # Token
            self.dv = None # MetaDictContext

        def id2(self):
            return self.getTypedRuleContext(VarDefParser.Id2Context,0)


        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def FLOAT(self):
            return self.getToken(VarDefParser.FLOAT, 0)

        def INT(self):
            return self.getToken(VarDefParser.INT, 0)

        def STRING(self):
            return self.getToken(VarDefParser.STRING, 0)

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
        ha=False
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            localctx.i = self.id2()
            self.state = 199
            self.match(VarDefParser.T__4)
            self.state = 200
            localctx.m = self.match(VarDefParser.ID)
            self.state = 201
            self.match(VarDefParser.T__1)
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT, VarDefParser.INT, VarDefParser.STRING]:
                self.state = 208
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VarDefParser.FLOAT]:
                    self.state = 202
                    localctx.k = self.match(VarDefParser.FLOAT)
                    c=float((None if localctx.k is None else localctx.k.text))
                    pass
                elif token in [VarDefParser.INT]:
                    self.state = 204
                    localctx.k = self.match(VarDefParser.INT)
                    c=int((None if localctx.k is None else localctx.k.text))
                    pass
                elif token in [VarDefParser.STRING]:
                    self.state = 206
                    localctx.k = self.match(VarDefParser.STRING)
                    c=str((None if localctx.k is None else localctx.k.text))[1:-1].lower()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [VarDefParser.T__2]:
                self.state = 210
                localctx.dv = self.metaDict()
                c=str(localctx.dv.x).lower();
                if localctx.dv.hasV: ha=True;
                	
                pass
            else:
                raise NoViableAltException(self)

            name=str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop)))).lower();mk=str((None if localctx.m is None else localctx.m.text)).lower();

            if self.varPathMap.has_key(name):
            	self.varPathMap[name].metaData[mk]=c;
            	if ha: self.varPathMap[name].metaDataPost.append(mk);
            elif self.varExprMap.has_key(name):
            	self.varExprMap[name].metaData[mk]=c;
            	if ha: self.varExprMap[name].metaDataPost.append(mk); 
            elif self.newArrayMap.has_key(name):
            	self.newArrayMap[name].metaData[mk]=c; 
            	if ha: self.newArrayMap[name].metaDataPost.append(mk);
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

    class MetaDictContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.MetaDictContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.hasV = None
            self.x = None
            self.d = None # Dict_pairContext

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
        self.enterRule(localctx, 26, self.RULE_metaDict)
        hasV=False
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(VarDefParser.T__2)
            self.state = 218
            localctx.d = self.dict_pair()
            if localctx.d.hasV: localctx.hasV = True
            localctx.x = localctx.d.x	

            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 220
                self.match(VarDefParser.T__0)
                self.state = 221
                localctx.d = self.dict_pair()
                if localctx.d.hasV: localctx.hasV = True
                localctx.x = localctx.x+','+localctx.d.x	

                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
            self.match(VarDefParser.T__3)
            self._ctx.stop = self._input.LT(-1)
            localctx.x='{'+localctx.x+'}'
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
            self.hasV = None
            self.x = None
            self.i1 = None # Token
            self.s1 = None # Token
            self.s11 = None # NumberContext
            self.i2 = None # Token
            self.s2 = None # Token
            self.s22 = None # NumberContext

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
        self.enterRule(localctx, 28, self.RULE_dict_pair)
        r1='';r2=''
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.ID]:
                self.state = 231
                localctx.i1 = self.match(VarDefParser.ID)
                localctx.hasV = True 
                r1='_cm[\''+str((None if localctx.i1 is None else localctx.i1.text))+'\'].const'

                pass
            elif token in [VarDefParser.STRING]:
                self.state = 233
                localctx.s1 = self.match(VarDefParser.STRING)
                r1=str((None if localctx.s1 is None else localctx.s1.text))
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 235
                localctx.s11 = self.number()
                r1=str((None if localctx.s11 is None else self._input.getText((localctx.s11.start,localctx.s11.stop))))
                pass
            else:
                raise NoViableAltException(self)

            self.state = 240
            self.match(VarDefParser.T__5)
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.ID]:
                self.state = 241
                localctx.i2 = self.match(VarDefParser.ID)
                localctx.hasV = True 
                r2='_cm[\''+str((None if localctx.i2 is None else localctx.i2.text))+'\'].const'

                pass
            elif token in [VarDefParser.STRING]:
                self.state = 243
                localctx.s2 = self.match(VarDefParser.STRING)
                r2=str((None if localctx.s2 is None else localctx.s2.text))
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 245
                localctx.s22 = self.number()
                r2=str((None if localctx.s22 is None else self._input.getText((localctx.s22.start,localctx.s22.stop))))
                pass
            else:
                raise NoViableAltException(self)

            localctx.x = r1+':'+r2
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
        self.enterRule(localctx, 30, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
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
            self.e = None # Ee_dtsContext

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def ee_dts(self):
            return self.getTypedRuleContext(VarDefParser.Ee_dtsContext,0)


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
        self.enterRule(localctx, 32, self.RULE_stat)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 254
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 258
            localctx.i = self.match(VarDefParser.ID)
            self.state = 259
            self.match(VarDefParser.T__1)
            self.state = 260
            localctx.e = self.ee_dts(0)
            self._ctx.stop = self._input.LT(-1)

            v = Var('');
            e=str((None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))).lower();v.expr=e;
            name=str((None if localctx.i is None else localctx.i.text)).lower(); self.varExprMap[name]=v; 
            e2=str(localctx.e.x).lower()
            name2=self.ifsAppend+"['"+str((None if localctx.i is None else localctx.i.text)).lower()+"']"
            k='!'+name2+'='+e2;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;
            if isTemp: 
            	self.tempVarList.append(name);	
            #print('i am here', self.ifid, name)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ee_dtsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.Ee_dtsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.x = None
            self.a = None # Ee_dtsContext
            self.i = None # Token
            self.o = None # Token
            self.b = None # Ee_dtsContext

        def INT(self):
            return self.getToken(VarDefParser.INT, 0)

        def FLOAT(self):
            return self.getToken(VarDefParser.FLOAT, 0)

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def ee_dts(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.Ee_dtsContext)
            else:
                return self.getTypedRuleContext(VarDefParser.Ee_dtsContext,i)


        def STRING(self):
            return self.getToken(VarDefParser.STRING, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_ee_dts

        def accept(self, visitor):
            if hasattr(visitor, "visitEe_dts"):
                return visitor.visitEe_dts(self)
            else:
                return visitor.visitChildren(self)



    def ee_dts(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VarDefParser.Ee_dtsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_ee_dts, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                s=''
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 264
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 268
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 271
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 275
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 277
                localctx.i = self.match(VarDefParser.ID)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();
                if vName in self.newArrayMap.keys() or vName in self.varPathMap.keys() or vName in self.varExprMap.keys():
                	localctx.x = self.ifsAppend+"['"+vName+"']"
                	#print (vName) 
                else:
                	Err.addError(vName+' not defined.', self.vardefFile, self.vardefName)

                pass

            elif la_ == 4:
                self.state = 279
                self.match(VarDefParser.T__6)
                self.state = 280
                localctx.a = self.ee_dts(0)
                self.state = 281
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.a.x)+")"
                pass

            elif la_ == 5:
                self.state = 284
                localctx.i = self.match(VarDefParser.STRING)
                localctx.x=  str((None if localctx.i is None else localctx.i.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 298
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.Ee_dtsContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee_dts)
                        self.state = 288
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 289
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 290
                        localctx.b = self.ee_dts(8)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.Ee_dtsContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee_dts)
                        self.state = 293
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 294
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 295
                        localctx.b = self.ee_dts(7)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class EeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.EeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.x = None
            self.a = None # EeContext
            self.i = None # Token
            self.j = None # Token
            self.o = None # Token
            self.b = None # EeContext

        def INT(self):
            return self.getToken(VarDefParser.INT, 0)

        def FLOAT(self):
            return self.getToken(VarDefParser.FLOAT, 0)

        def ID(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.ID)
            else:
                return self.getToken(VarDefParser.ID, i)

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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                s=''
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 305
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 309
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 312
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 316
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 318
                localctx.i = self.match(VarDefParser.ID)
                self.state = 321
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 319
                    self.match(VarDefParser.T__4)
                    self.state = 320
                    localctx.j = self.match(VarDefParser.ID)


                vName=str((None if localctx.i is None else localctx.i.text)).lower();
                if localctx.j!=None: vName=str((None if localctx.i is None else localctx.i.text)).lower()+'.'+str((None if localctx.j is None else localctx.j.text)).lower();
                if vName in self.newArrayMap.keys() or vName in self.varPathMap.keys() or vName in self.varExprMap.keys():
                	localctx.x = self.ifsAppend+"['"+vName+"']"+"[i]"
                	#print (vName) 
                else:
                	Err.addError(vName+' not defined.', self.vardefFile, self.vardefName)

                pass

            elif la_ == 4:
                self.state = 324
                self.match(VarDefParser.T__6)
                self.state = 325
                localctx.a = self.ee(0)
                self.state = 326
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.a.x)+")"
                pass

            elif la_ == 5:
                self.state = 329
                localctx.i = self.match(VarDefParser.STRING)
                localctx.x=  str((None if localctx.i is None else localctx.i.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 343
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 333
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 334
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 335
                        localctx.b = self.ee(8)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 338
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 339
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 340
                        localctx.b = self.ee(7)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_compare, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 349
                localctx.a = self.ee(0)
                self.state = 350
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10) | (1 << VarDefParser.T__11) | (1 << VarDefParser.T__12) | (1 << VarDefParser.T__13))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 351
                localctx.b = self.ee(0)
                localctx.x=str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 354
                self.match(VarDefParser.T__6)
                self.state = 355
                localctx.c = self.compare(0)
                self.state = 356
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VarDefParser.CompareContext(self, _parentctx, _parentState)
                    localctx.c1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare)
                    self.state = 361
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 362
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 363
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        self.enterRule(localctx, 40, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            localctx.i = self.id2()
            self.state = 372
            self.match(VarDefParser.T__1)
            self.state = 373
            localctx.a = self.ee(0)
            vName=str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop)))).lower();
            if vName in self.newArrayMap.keys() or vName in self.varExprMap.keys() or vName in self.varPathMap.keys():
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
        self.enterRule(localctx, 42, self.RULE_id2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(VarDefParser.ID)
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 377
                self.match(VarDefParser.T__4)
                self.state = 378
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
        self.enterRule(localctx, 44, self.RULE_if_stat)
        ifs=collections.OrderedDict();al=[];
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(VarDefParser.IF)
            self.state = 382
            localctx.c = self.compare(0)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 383
                self.match(VarDefParser.NL)
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 389
            self.match(VarDefParser.T__2)
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 390
                self.match(VarDefParser.NL)
                self.state = 395
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 404 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 396
                localctx.a = self.assign()
                t=str(localctx.a.x).lower();al.append(t)
                self.state = 401
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 398
                    self.match(VarDefParser.NL)
                    self.state = 403
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 406 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 408
            self.match(VarDefParser.T__3)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 409
                    self.match(VarDefParser.NL) 
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 416
                self.match(VarDefParser.ELSEIF)
                self.state = 417
                localctx.c = self.compare(0)
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 418
                    self.match(VarDefParser.NL)
                    self.state = 423
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 424
                self.match(VarDefParser.T__2)
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 425
                    self.match(VarDefParser.NL)
                    self.state = 430
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 439 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 431
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 436
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 433
                        self.match(VarDefParser.NL)
                        self.state = 438
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 441 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 443
                self.match(VarDefParser.T__3)
                self.state = 447
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 444
                        self.match(VarDefParser.NL) 
                    self.state = 449
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

                k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 457
                self.match(VarDefParser.ELSE)
                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 458
                    self.match(VarDefParser.NL)
                    self.state = 463
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 464
                self.match(VarDefParser.T__2)
                self.state = 468
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 465
                    self.match(VarDefParser.NL)
                    self.state = 470
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 479 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 471
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 476
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 473
                        self.match(VarDefParser.NL)
                        self.state = 478
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 481 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 483
                self.match(VarDefParser.T__3)
                self.state = 485 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 484
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 487 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
        self._predicates[17] = self.ee_dts_sempred
        self._predicates[18] = self.ee_sempred
        self._predicates[19] = self.compare_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def ee_dts_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

    def ee_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

    def compare_sempred(self, localctx, predIndex):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




