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
        buf.write(u".\u01b9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2")
        buf.write(u"\7\2\60\n\2\f\2\16\2\63\13\2\3\2\3\2\7\2\67\n\2\f\2\16")
        buf.write(u"\2:\13\2\3\2\6\2=\n\2\r\2\16\2>\3\3\3\3\3\3\3\3\3\4\3")
        buf.write(u"\4\3\4\3\4\6\4I\n\4\r\4\16\4J\3\4\6\4N\n\4\r\4\16\4O")
        buf.write(u"\3\4\3\4\6\4T\n\4\r\4\16\4U\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\5\5a\n\5\3\5\6\5d\n\5\r\5\16\5e\3\6\3\6\5")
        buf.write(u"\6j\n\6\3\7\3\7\3\7\3\7\7\7p\n\7\f\7\16\7s\13\7\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b}\n\b\3\b\3\b\3\t\3\t\3")
        buf.write(u"\t\3\t\7\t\u0085\n\t\f\t\16\t\u0088\13\t\3\n\3\n\5\n")
        buf.write(u"\u008c\n\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13\u0094\n\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u009c\n\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\5\13\u00a4\n\13\3\13\3\13\7\13")
        buf.write(u"\u00a8\n\13\f\13\16\13\u00ab\13\13\3\13\3\13\3\f\3\f")
        buf.write(u"\3\f\3\r\3\r\5\r\u00b4\n\r\3\r\3\r\3\r\3\r\3\r\5\r\u00bb")
        buf.write(u"\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\5\16\u00c9\n\16\3\16\3\16\3\16\5\16\u00ce")
        buf.write(u"\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7")
        buf.write(u"\17\u00d9\n\17\f\17\16\17\u00dc\13\17\3\17\3\17\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00e7\n\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00f1\n\20\3\20")
        buf.write(u"\3\20\3\21\3\21\3\22\3\22\5\22\u00f9\n\22\3\22\3\22\3")
        buf.write(u"\22\3\22\3\23\3\23\3\23\3\23\5\23\u0103\n\23\3\23\3\23")
        buf.write(u"\3\23\3\23\3\23\5\23\u010a\n\23\3\23\3\23\3\23\3\23\3")
        buf.write(u"\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0117\n\23\3\23")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u0123")
        buf.write(u"\n\23\f\23\16\23\u0126\13\23\3\24\3\24\3\24\3\24\3\24")
        buf.write(u"\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0133\n\24\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\7\24\u013a\n\24\f\24\16\24\u013d\13")
        buf.write(u"\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u0147")
        buf.write(u"\n\26\3\27\3\27\3\27\7\27\u014c\n\27\f\27\16\27\u014f")
        buf.write(u"\13\27\3\27\3\27\7\27\u0153\n\27\f\27\16\27\u0156\13")
        buf.write(u"\27\3\27\3\27\3\27\7\27\u015b\n\27\f\27\16\27\u015e\13")
        buf.write(u"\27\6\27\u0160\n\27\r\27\16\27\u0161\3\27\3\27\7\27\u0166")
        buf.write(u"\n\27\f\27\16\27\u0169\13\27\3\27\3\27\3\27\3\27\7\27")
        buf.write(u"\u016f\n\27\f\27\16\27\u0172\13\27\3\27\3\27\7\27\u0176")
        buf.write(u"\n\27\f\27\16\27\u0179\13\27\3\27\3\27\3\27\7\27\u017e")
        buf.write(u"\n\27\f\27\16\27\u0181\13\27\6\27\u0183\n\27\r\27\16")
        buf.write(u"\27\u0184\3\27\3\27\7\27\u0189\n\27\f\27\16\27\u018c")
        buf.write(u"\13\27\3\27\3\27\7\27\u0190\n\27\f\27\16\27\u0193\13")
        buf.write(u"\27\3\27\3\27\7\27\u0197\n\27\f\27\16\27\u019a\13\27")
        buf.write(u"\3\27\3\27\7\27\u019e\n\27\f\27\16\27\u01a1\13\27\3\27")
        buf.write(u"\3\27\3\27\7\27\u01a6\n\27\f\27\16\27\u01a9\13\27\6\27")
        buf.write(u"\u01ab\n\27\r\27\16\27\u01ac\3\27\3\27\6\27\u01b1\n\27")
        buf.write(u"\r\27\16\27\u01b2\3\27\3\27\5\27\u01b7\n\27\3\27\2\4")
        buf.write(u"$&\30\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(u"\2\7\4\2))++\3\2\24\25\3\2\26\27\3\2\13\20\3\2\30\31")
        buf.write(u"\u01e0\2\61\3\2\2\2\4@\3\2\2\2\6D\3\2\2\2\b`\3\2\2\2")
        buf.write(u"\ni\3\2\2\2\fk\3\2\2\2\16t\3\2\2\2\20\u0080\3\2\2\2\22")
        buf.write(u"\u008b\3\2\2\2\24\u0090\3\2\2\2\26\u00ae\3\2\2\2\30\u00b3")
        buf.write(u"\3\2\2\2\32\u00be\3\2\2\2\34\u00d1\3\2\2\2\36\u00e6\3")
        buf.write(u"\2\2\2 \u00f4\3\2\2\2\"\u00f8\3\2\2\2$\u0116\3\2\2\2")
        buf.write(u"&\u0132\3\2\2\2(\u013e\3\2\2\2*\u0143\3\2\2\2,\u0148")
        buf.write(u"\3\2\2\2.\60\7-\2\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2")
        buf.write(u"\2\61\62\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\648\5\4")
        buf.write(u"\3\2\65\67\7-\2\2\66\65\3\2\2\2\67:\3\2\2\28\66\3\2\2")
        buf.write(u"\289\3\2\2\29<\3\2\2\2:8\3\2\2\2;=\5\6\4\2<;\3\2\2\2")
        buf.write(u"=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?\3\3\2\2\2@A\7\32\2\2")
        buf.write(u"AB\7*\2\2BC\b\3\1\2C\5\3\2\2\2DE\7\34\2\2EF\7*\2\2FH")
        buf.write(u"\b\4\1\2GI\7-\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2")
        buf.write(u"\2\2KM\3\2\2\2LN\5\b\5\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2")
        buf.write(u"\2OP\3\2\2\2PQ\3\2\2\2QS\7\35\2\2RT\7-\2\2SR\3\2\2\2")
        buf.write(u"TU\3\2\2\2US\3\2\2\2UV\3\2\2\2V\7\3\2\2\2Wa\5\30\r\2")
        buf.write(u"Xa\5\32\16\2Ya\5\"\22\2Z[\5,\27\2[\\\b\5\1\2\\a\3\2\2")
        buf.write(u"\2]a\5\n\6\2^a\5\26\f\2_a\5\f\7\2`W\3\2\2\2`X\3\2\2\2")
        buf.write(u"`Y\3\2\2\2`Z\3\2\2\2`]\3\2\2\2`^\3\2\2\2`_\3\2\2\2ac")
        buf.write(u"\3\2\2\2bd\7-\2\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2")
        buf.write(u"\2\2f\t\3\2\2\2gj\5\20\t\2hj\5\24\13\2ig\3\2\2\2ih\3")
        buf.write(u"\2\2\2j\13\3\2\2\2kl\7&\2\2lq\5\16\b\2mn\7\3\2\2np\5")
        buf.write(u"\16\b\2om\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2r\r\3")
        buf.write(u"\2\2\2sq\3\2\2\2tu\7*\2\2u|\7\4\2\2vw\7)\2\2w}\b\b\1")
        buf.write(u"\2xy\7+\2\2y}\b\b\1\2z{\7,\2\2{}\b\b\1\2|v\3\2\2\2|x")
        buf.write(u"\3\2\2\2|z\3\2\2\2}~\3\2\2\2~\177\b\b\1\2\177\17\3\2")
        buf.write(u"\2\2\u0080\u0081\7\36\2\2\u0081\u0086\5\22\n\2\u0082")
        buf.write(u"\u0083\7\3\2\2\u0083\u0085\5\22\n\2\u0084\u0082\3\2\2")
        buf.write(u"\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087")
        buf.write(u"\3\2\2\2\u0087\21\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008a")
        buf.write(u"\7\22\2\2\u008a\u008c\b\n\1\2\u008b\u0089\3\2\2\2\u008b")
        buf.write(u"\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\7*\2\2")
        buf.write(u"\u008e\u008f\b\n\1\2\u008f\23\3\2\2\2\u0090\u0093\7\36")
        buf.write(u"\2\2\u0091\u0092\7\22\2\2\u0092\u0094\b\13\1\2\u0093")
        buf.write(u"\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\3\2\2")
        buf.write(u"\2\u0095\u0096\7*\2\2\u0096\u0097\b\13\1\2\u0097\u0098")
        buf.write(u"\7\5\2\2\u0098\u009b\b\13\1\2\u0099\u009a\7\22\2\2\u009a")
        buf.write(u"\u009c\b\13\1\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2")
        buf.write(u"\2\u009c\u009d\3\2\2\2\u009d\u009e\7*\2\2\u009e\u00a9")
        buf.write(u"\b\13\1\2\u009f\u00a0\7\3\2\2\u00a0\u00a3\b\13\1\2\u00a1")
        buf.write(u"\u00a2\7\22\2\2\u00a2\u00a4\b\13\1\2\u00a3\u00a1\3\2")
        buf.write(u"\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6")
        buf.write(u"\7*\2\2\u00a6\u00a8\b\13\1\2\u00a7\u009f\3\2\2\2\u00a8")
        buf.write(u"\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2")
        buf.write(u"\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad")
        buf.write(u"\7\6\2\2\u00ad\25\3\2\2\2\u00ae\u00af\7\33\2\2\u00af")
        buf.write(u"\u00b0\7*\2\2\u00b0\27\3\2\2\2\u00b1\u00b2\7\22\2\2\u00b2")
        buf.write(u"\u00b4\b\r\1\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2")
        buf.write(u"\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\7*\2\2\u00b6\u00b7")
        buf.write(u"\7\4\2\2\u00b7\u00ba\7\23\2\2\u00b8\u00b9\7\3\2\2\u00b9")
        buf.write(u"\u00bb\7,\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write(u"\u00bb\u00bc\3\2\2\2\u00bc\u00bd\b\r\1\2\u00bd\31\3\2")
        buf.write(u"\2\2\u00be\u00bf\5*\26\2\u00bf\u00c0\7\7\2\2\u00c0\u00c1")
        buf.write(u"\7*\2\2\u00c1\u00cd\7\4\2\2\u00c2\u00c3\7)\2\2\u00c3")
        buf.write(u"\u00c9\b\16\1\2\u00c4\u00c5\7+\2\2\u00c5\u00c9\b\16\1")
        buf.write(u"\2\u00c6\u00c7\7,\2\2\u00c7\u00c9\b\16\1\2\u00c8\u00c2")
        buf.write(u"\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9")
        buf.write(u"\u00ce\3\2\2\2\u00ca\u00cb\5\34\17\2\u00cb\u00cc\b\16")
        buf.write(u"\1\2\u00cc\u00ce\3\2\2\2\u00cd\u00c8\3\2\2\2\u00cd\u00ca")
        buf.write(u"\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\b\16\1\2\u00d0")
        buf.write(u"\33\3\2\2\2\u00d1\u00d2\7\5\2\2\u00d2\u00d3\5\36\20\2")
        buf.write(u"\u00d3\u00da\b\17\1\2\u00d4\u00d5\7\3\2\2\u00d5\u00d6")
        buf.write(u"\5\36\20\2\u00d6\u00d7\b\17\1\2\u00d7\u00d9\3\2\2\2\u00d8")
        buf.write(u"\u00d4\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2")
        buf.write(u"\2\u00da\u00db\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00da")
        buf.write(u"\3\2\2\2\u00dd\u00de\7\6\2\2\u00de\35\3\2\2\2\u00df\u00e0")
        buf.write(u"\7*\2\2\u00e0\u00e7\b\20\1\2\u00e1\u00e2\7,\2\2\u00e2")
        buf.write(u"\u00e7\b\20\1\2\u00e3\u00e4\5 \21\2\u00e4\u00e5\b\20")
        buf.write(u"\1\2\u00e5\u00e7\3\2\2\2\u00e6\u00df\3\2\2\2\u00e6\u00e1")
        buf.write(u"\3\2\2\2\u00e6\u00e3\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write(u"\u00f0\7\b\2\2\u00e9\u00ea\7*\2\2\u00ea\u00f1\b\20\1")
        buf.write(u"\2\u00eb\u00ec\7,\2\2\u00ec\u00f1\b\20\1\2\u00ed\u00ee")
        buf.write(u"\5 \21\2\u00ee\u00ef\b\20\1\2\u00ef\u00f1\3\2\2\2\u00f0")
        buf.write(u"\u00e9\3\2\2\2\u00f0\u00eb\3\2\2\2\u00f0\u00ed\3\2\2")
        buf.write(u"\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\b\20\1\2\u00f3\37")
        buf.write(u"\3\2\2\2\u00f4\u00f5\t\2\2\2\u00f5!\3\2\2\2\u00f6\u00f7")
        buf.write(u"\7\22\2\2\u00f7\u00f9\b\22\1\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write(u"\u00f9\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\7*\2\2")
        buf.write(u"\u00fb\u00fc\7\4\2\2\u00fc\u00fd\5$\23\2\u00fd#\3\2\2")
        buf.write(u"\2\u00fe\u00ff\b\23\1\2\u00ff\u0102\b\23\1\2\u0100\u0101")
        buf.write(u"\7\27\2\2\u0101\u0103\b\23\1\2\u0102\u0100\3\2\2\2\u0102")
        buf.write(u"\u0103\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105\7+\2\2")
        buf.write(u"\u0105\u0117\b\23\1\2\u0106\u0109\b\23\1\2\u0107\u0108")
        buf.write(u"\7\27\2\2\u0108\u010a\b\23\1\2\u0109\u0107\3\2\2\2\u0109")
        buf.write(u"\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c\7)\2\2")
        buf.write(u"\u010c\u0117\b\23\1\2\u010d\u010e\7*\2\2\u010e\u0117")
        buf.write(u"\b\23\1\2\u010f\u0110\7\t\2\2\u0110\u0111\5$\23\2\u0111")
        buf.write(u"\u0112\7\n\2\2\u0112\u0113\b\23\1\2\u0113\u0117\3\2\2")
        buf.write(u"\2\u0114\u0115\7,\2\2\u0115\u0117\b\23\1\2\u0116\u00fe")
        buf.write(u"\3\2\2\2\u0116\u0106\3\2\2\2\u0116\u010d\3\2\2\2\u0116")
        buf.write(u"\u010f\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0124\3\2\2")
        buf.write(u"\2\u0118\u0119\f\t\2\2\u0119\u011a\t\3\2\2\u011a\u011b")
        buf.write(u"\5$\23\n\u011b\u011c\b\23\1\2\u011c\u0123\3\2\2\2\u011d")
        buf.write(u"\u011e\f\b\2\2\u011e\u011f\t\4\2\2\u011f\u0120\5$\23")
        buf.write(u"\t\u0120\u0121\b\23\1\2\u0121\u0123\3\2\2\2\u0122\u0118")
        buf.write(u"\3\2\2\2\u0122\u011d\3\2\2\2\u0123\u0126\3\2\2\2\u0124")
        buf.write(u"\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125%\3\2\2\2\u0126")
        buf.write(u"\u0124\3\2\2\2\u0127\u0128\b\24\1\2\u0128\u0129\5$\23")
        buf.write(u"\2\u0129\u012a\t\5\2\2\u012a\u012b\5$\23\2\u012b\u012c")
        buf.write(u"\b\24\1\2\u012c\u0133\3\2\2\2\u012d\u012e\7\t\2\2\u012e")
        buf.write(u"\u012f\5&\24\2\u012f\u0130\7\n\2\2\u0130\u0131\b\24\1")
        buf.write(u"\2\u0131\u0133\3\2\2\2\u0132\u0127\3\2\2\2\u0132\u012d")
        buf.write(u"\3\2\2\2\u0133\u013b\3\2\2\2\u0134\u0135\f\3\2\2\u0135")
        buf.write(u"\u0136\t\6\2\2\u0136\u0137\5&\24\4\u0137\u0138\b\24\1")
        buf.write(u"\2\u0138\u013a\3\2\2\2\u0139\u0134\3\2\2\2\u013a\u013d")
        buf.write(u"\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write(u"\'\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f\5*\26\2\u013f")
        buf.write(u"\u0140\7\4\2\2\u0140\u0141\5$\23\2\u0141\u0142\b\25\1")
        buf.write(u"\2\u0142)\3\2\2\2\u0143\u0146\7*\2\2\u0144\u0145\7\7")
        buf.write(u"\2\2\u0145\u0147\7*\2\2\u0146\u0144\3\2\2\2\u0146\u0147")
        buf.write(u"\3\2\2\2\u0147+\3\2\2\2\u0148\u0149\7\37\2\2\u0149\u014d")
        buf.write(u"\5&\24\2\u014a\u014c\7-\2\2\u014b\u014a\3\2\2\2\u014c")
        buf.write(u"\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2")
        buf.write(u"\2\u014e\u0150\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0154")
        buf.write(u"\7\5\2\2\u0151\u0153\7-\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write(u"\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2")
        buf.write(u"\2\u0155\u015f\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158")
        buf.write(u"\5(\25\2\u0158\u015c\b\27\1\2\u0159\u015b\7-\2\2\u015a")
        buf.write(u"\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2")
        buf.write(u"\2\u015c\u015d\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c")
        buf.write(u"\3\2\2\2\u015f\u0157\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write(u"\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\3\2\2")
        buf.write(u"\2\u0163\u0167\7\6\2\2\u0164\u0166\7-\2\2\u0165\u0164")
        buf.write(u"\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167")
        buf.write(u"\u0168\3\2\2\2\u0168\u016a\3\2\2\2\u0169\u0167\3\2\2")
        buf.write(u"\2\u016a\u0191\b\27\1\2\u016b\u016c\7 \2\2\u016c\u0170")
        buf.write(u"\5&\24\2\u016d\u016f\7-\2\2\u016e\u016d\3\2\2\2\u016f")
        buf.write(u"\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2")
        buf.write(u"\2\u0171\u0173\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0177")
        buf.write(u"\7\5\2\2\u0174\u0176\7-\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write(u"\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2")
        buf.write(u"\2\u0178\u0182\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b")
        buf.write(u"\5(\25\2\u017b\u017f\b\27\1\2\u017c\u017e\7-\2\2\u017d")
        buf.write(u"\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2")
        buf.write(u"\2\u017f\u0180\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f")
        buf.write(u"\3\2\2\2\u0182\u017a\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write(u"\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\3\2\2")
        buf.write(u"\2\u0186\u018a\7\6\2\2\u0187\u0189\7-\2\2\u0188\u0187")
        buf.write(u"\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write(u"\u018b\3\2\2\2\u018b\u018d\3\2\2\2\u018c\u018a\3\2\2")
        buf.write(u"\2\u018d\u018e\b\27\1\2\u018e\u0190\3\2\2\2\u018f\u016b")
        buf.write(u"\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write(u"\u0192\3\2\2\2\u0192\u01b6\3\2\2\2\u0193\u0191\3\2\2")
        buf.write(u"\2\u0194\u0198\7!\2\2\u0195\u0197\7-\2\2\u0196\u0195")
        buf.write(u"\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198")
        buf.write(u"\u0199\3\2\2\2\u0199\u019b\3\2\2\2\u019a\u0198\3\2\2")
        buf.write(u"\2\u019b\u019f\7\5\2\2\u019c\u019e\7-\2\2\u019d\u019c")
        buf.write(u"\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write(u"\u01a0\3\2\2\2\u01a0\u01aa\3\2\2\2\u01a1\u019f\3\2\2")
        buf.write(u"\2\u01a2\u01a3\5(\25\2\u01a3\u01a7\b\27\1\2\u01a4\u01a6")
        buf.write(u"\7-\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7")
        buf.write(u"\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01ab\3\2\2")
        buf.write(u"\2\u01a9\u01a7\3\2\2\2\u01aa\u01a2\3\2\2\2\u01ab\u01ac")
        buf.write(u"\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write(u"\u01ae\3\2\2\2\u01ae\u01b0\7\6\2\2\u01af\u01b1\7-\2\2")
        buf.write(u"\u01b0\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b0")
        buf.write(u"\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write(u"\u01b5\b\27\1\2\u01b5\u01b7\3\2\2\2\u01b6\u0194\3\2\2")
        buf.write(u"\2\u01b6\u01b7\3\2\2\2\u01b7-\3\2\2\2\64\618>JOU`eiq")
        buf.write(u"|\u0086\u008b\u0093\u009b\u00a3\u00a9\u00b3\u00ba\u00c8")
        buf.write(u"\u00cd\u00da\u00e6\u00f0\u00f8\u0102\u0109\u0116\u0122")
        buf.write(u"\u0124\u0132\u013b\u0146\u014d\u0154\u015c\u0161\u0167")
        buf.write(u"\u0170\u0177\u017f\u0184\u018a\u0191\u0198\u019f\u01a7")
        buf.write(u"\u01ac\u01b2\u01b6")
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
    RULE_ee = 17
    RULE_compare = 18
    RULE_assign = 19
    RULE_id2 = 20
    RULE_if_stat = 21

    ruleNames =  [ u"prog", u"use", u"vardef", u"field", u"new_var", u"constant", 
                   u"const_var", u"array", u"array_var", u"array_cluster", 
                   u"include", u"var_path", u"var_meta", u"metaDict", u"dict_pair", 
                   u"number", u"stat", u"ee", u"compare", u"assign", u"id2", 
                   u"if_stat" ]

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
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 44
                self.match(VarDefParser.NL)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.use()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 51
                self.match(VarDefParser.NL)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.vardef()
                self.state = 60 
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
            self.state = 62
            self.match(VarDefParser.USE)
            self.state = 63
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
            self.state = 66
            self.match(VarDefParser.VARDEF)
            self.state = 67
            localctx.name = self.match(VarDefParser.ID)
            groupName=str((None if localctx.name is None else localctx.name.text)).lower();self.vardefName=groupName;
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.match(VarDefParser.NL)
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.field()
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ARRAY) | (1 << VarDefParser.IF) | (1 << VarDefParser.CONST) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 79
            self.match(VarDefParser.END)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.match(VarDefParser.NL)
                self.state = 83 
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
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 85
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 86
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 87
                self.stat()
                pass

            elif la_ == 4:
                self.state = 88
                self.if_stat()
                self.ifid=self.ifid+1;
                pass

            elif la_ == 5:
                self.state = 91
                self.new_var()
                pass

            elif la_ == 6:
                self.state = 92
                self.include()
                pass

            elif la_ == 7:
                self.state = 93
                self.constant()
                pass


            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self.match(VarDefParser.NL)
                self.state = 99 
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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
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
            self.state = 105
            self.match(VarDefParser.CONST)
            self.state = 106
            self.const_var()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 107
                self.match(VarDefParser.T__0)
                self.state = 108
                self.const_var()
                self.state = 113
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
            self.state = 114
            localctx.i = self.match(VarDefParser.ID)
            self.state = 115
            self.match(VarDefParser.T__1)
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT]:
                self.state = 116
                localctx.c = self.match(VarDefParser.FLOAT)
                v.const=float((None if localctx.c is None else localctx.c.text))
                pass
            elif token in [VarDefParser.INT]:
                self.state = 118
                localctx.c = self.match(VarDefParser.INT)
                v.const=int((None if localctx.c is None else localctx.c.text))
                pass
            elif token in [VarDefParser.STRING]:
                self.state = 120
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
            self.state = 126
            self.match(VarDefParser.ARRAY)
            self.state = 127
            self.array_var()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 128
                self.match(VarDefParser.T__0)
                self.state = 129
                self.array_var()
                self.state = 134
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
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 135
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 139
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
            self.state = 142
            self.match(VarDefParser.ARRAY)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 143
                self.match(VarDefParser.T)
                isGroupTemp=True


            self.state = 147
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 149
            self.match(VarDefParser.T__2)
            isTemp=False;
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 151
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 155
            localctx.i = self.match(VarDefParser.ID)
            subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 157
                self.match(VarDefParser.T__0)
                isTemp=False;
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 159
                    self.match(VarDefParser.T)
                    isTemp=True


                self.state = 163
                localctx.i = self.match(VarDefParser.ID)
                subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
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
            self.state = 172
            self.match(VarDefParser.INCLUDE)
            self.state = 173
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
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 175
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 179
            localctx.i = self.match(VarDefParser.ID)
            self.state = 180
            self.match(VarDefParser.T__1)
            self.state = 181
            localctx.p = self.match(VarDefParser.PATH)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__0:
                self.state = 182
                self.match(VarDefParser.T__0)
                self.state = 183
                localctx.u = self.match(VarDefParser.STRING)


            p =str((None if localctx.p is None else localctx.p.text)); t = Var(p); 
            name=str((None if localctx.i is None else localctx.i.text)).lower(); self.varPathMap[name]=t;
            if localctx.u: self.varPathMap[name].metaData['units']=str((None if localctx.u is None else localctx.u.text))[1:-1].lower();
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
            self.state = 188
            localctx.i = self.id2()
            self.state = 189
            self.match(VarDefParser.T__4)
            self.state = 190
            localctx.m = self.match(VarDefParser.ID)
            self.state = 191
            self.match(VarDefParser.T__1)
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT, VarDefParser.INT, VarDefParser.STRING]:
                self.state = 198
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VarDefParser.FLOAT]:
                    self.state = 192
                    localctx.k = self.match(VarDefParser.FLOAT)
                    c=float((None if localctx.k is None else localctx.k.text))
                    pass
                elif token in [VarDefParser.INT]:
                    self.state = 194
                    localctx.k = self.match(VarDefParser.INT)
                    c=int((None if localctx.k is None else localctx.k.text))
                    pass
                elif token in [VarDefParser.STRING]:
                    self.state = 196
                    localctx.k = self.match(VarDefParser.STRING)
                    c=str((None if localctx.k is None else localctx.k.text))[1:-1].lower()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [VarDefParser.T__2]:
                self.state = 200
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
            self.state = 207
            self.match(VarDefParser.T__2)
            self.state = 208
            localctx.d = self.dict_pair()
            if localctx.d.hasV: localctx.hasV = True
            localctx.x = localctx.d.x	

            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 210
                self.match(VarDefParser.T__0)
                self.state = 211
                localctx.d = self.dict_pair()
                if localctx.d.hasV: localctx.hasV = True
                localctx.x = localctx.x+','+localctx.d.x	

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
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.ID]:
                self.state = 221
                localctx.i1 = self.match(VarDefParser.ID)
                localctx.hasV = True 
                r1='sty.newConstMap['+str((None if localctx.i1 is None else localctx.i1.text))+']'

                pass
            elif token in [VarDefParser.STRING]:
                self.state = 223
                localctx.s1 = self.match(VarDefParser.STRING)
                r1=str((None if localctx.s1 is None else localctx.s1.text))
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 225
                localctx.s11 = self.number()
                r1=str((None if localctx.s11 is None else self._input.getText((localctx.s11.start,localctx.s11.stop))))
                pass
            else:
                raise NoViableAltException(self)

            self.state = 230
            self.match(VarDefParser.T__5)
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.ID]:
                self.state = 231
                localctx.i2 = self.match(VarDefParser.ID)
                localctx.hasV = True 
                r2='sty.newConstMap['+str((None if localctx.i2 is None else localctx.i2.text))+']'

                pass
            elif token in [VarDefParser.STRING]:
                self.state = 233
                localctx.s2 = self.match(VarDefParser.STRING)
                r2=str((None if localctx.s2 is None else localctx.s2.text))
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 235
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
            self.state = 242
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
        self.enterRule(localctx, 32, self.RULE_stat)
        isTemp=False 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 244
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 248
            localctx.i = self.match(VarDefParser.ID)
            self.state = 249
            self.match(VarDefParser.T__1)
            self.state = 250
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                s=''
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 254
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 258
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 261
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 265
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 267
                localctx.i = self.match(VarDefParser.ID)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();
                if vName in self.newArrayMap.keys() or vName in self.varPathMap.keys() or vName in self.varExprMap.keys():
                	localctx.x = self.ifsAppend+"['"+vName+"']"+"[i]"
                	#print (vName) 
                else:
                	Err.addError(vName+' not defined.', self.vardefFile, self.vardefName)

                pass

            elif la_ == 4:
                self.state = 269
                self.match(VarDefParser.T__6)
                self.state = 270
                localctx.a = self.ee(0)
                self.state = 271
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.a.x)+")"
                pass

            elif la_ == 5:
                self.state = 274
                localctx.i = self.match(VarDefParser.STRING)
                localctx.x=  str((None if localctx.i is None else localctx.i.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 288
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 278
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 279
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 280
                        localctx.b = self.ee(8)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 283
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 284
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 285
                        localctx.b = self.ee(7)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_compare, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 294
                localctx.a = self.ee(0)
                self.state = 295
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10) | (1 << VarDefParser.T__11) | (1 << VarDefParser.T__12) | (1 << VarDefParser.T__13))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 296
                localctx.b = self.ee(0)
                localctx.x=str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 299
                self.match(VarDefParser.T__6)
                self.state = 300
                localctx.c = self.compare(0)
                self.state = 301
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VarDefParser.CompareContext(self, _parentctx, _parentState)
                    localctx.c1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare)
                    self.state = 306
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 307
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 308
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self.enterRule(localctx, 38, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            localctx.i = self.id2()
            self.state = 317
            self.match(VarDefParser.T__1)
            self.state = 318
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
        self.enterRule(localctx, 40, self.RULE_id2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(VarDefParser.ID)
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 322
                self.match(VarDefParser.T__4)
                self.state = 323
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
        self.enterRule(localctx, 42, self.RULE_if_stat)
        ifs=collections.OrderedDict();al=[];
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(VarDefParser.IF)
            self.state = 327
            localctx.c = self.compare(0)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 328
                self.match(VarDefParser.NL)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 334
            self.match(VarDefParser.T__2)
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 335
                self.match(VarDefParser.NL)
                self.state = 340
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 349 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 341
                localctx.a = self.assign()
                t=str(localctx.a.x).lower();al.append(t)
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 343
                    self.match(VarDefParser.NL)
                    self.state = 348
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 351 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 353
            self.match(VarDefParser.T__3)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 354
                    self.match(VarDefParser.NL) 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 361
                self.match(VarDefParser.ELSEIF)
                self.state = 362
                localctx.c = self.compare(0)
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 363
                    self.match(VarDefParser.NL)
                    self.state = 368
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 369
                self.match(VarDefParser.T__2)
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 370
                    self.match(VarDefParser.NL)
                    self.state = 375
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 384 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 376
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 381
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 378
                        self.match(VarDefParser.NL)
                        self.state = 383
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 386 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 388
                self.match(VarDefParser.T__3)
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 389
                        self.match(VarDefParser.NL) 
                    self.state = 394
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
                self.state = 401
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 402
                self.match(VarDefParser.ELSE)
                self.state = 406
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 403
                    self.match(VarDefParser.NL)
                    self.state = 408
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 409
                self.match(VarDefParser.T__2)
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 410
                    self.match(VarDefParser.NL)
                    self.state = 415
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 424 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 416
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 421
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 418
                        self.match(VarDefParser.NL)
                        self.state = 423
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 426 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 428
                self.match(VarDefParser.T__3)
                self.state = 430 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 429
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 432 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
        self._predicates[17] = self.ee_sempred
        self._predicates[18] = self.compare_sempred
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
         




