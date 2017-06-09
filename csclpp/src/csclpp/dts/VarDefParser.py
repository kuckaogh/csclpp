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
        buf.write(u",\u015f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\3\2\7\2*\n\2\f\2\16\2-\13\2\3\2\3")
        buf.write(u"\2\7\2\61\n\2\f\2\16\2\64\13\2\3\2\6\2\67\n\2\r\2\16")
        buf.write(u"\28\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\6\4C\n\4\r\4\16\4")
        buf.write(u"D\3\4\6\4H\n\4\r\4\16\4I\3\4\3\4\6\4N\n\4\r\4\16\4O\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5Z\n\5\3\5\6\5]\n\5")
        buf.write(u"\r\5\16\5^\3\6\3\6\5\6c\n\6\3\7\3\7\3\7\3\7\7\7i\n\7")
        buf.write(u"\f\7\16\7l\13\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write(u"\t\3\t\3\t\7\tz\n\t\f\t\16\t}\13\t\3\t\3\t\3\n\3\n\3")
        buf.write(u"\n\3\13\3\13\5\13\u0086\n\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\5\13\u008d\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\r\3\r\3\16\3\16\3\16\5\16\u009d\n\16\3\17\3\17\5")
        buf.write(u"\17\u00a1\n\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write(u"\5\20\u00ab\n\20\3\20\3\20\3\20\3\20\3\20\5\20\u00b2")
        buf.write(u"\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5")
        buf.write(u"\20\u00bd\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\7\20\u00c9\n\20\f\20\16\20\u00cc\13\20\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5")
        buf.write(u"\21\u00d9\n\21\3\21\3\21\3\21\3\21\3\21\7\21\u00e0\n")
        buf.write(u"\21\f\21\16\21\u00e3\13\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write(u"\23\3\23\3\23\5\23\u00ed\n\23\3\24\3\24\3\24\7\24\u00f2")
        buf.write(u"\n\24\f\24\16\24\u00f5\13\24\3\24\3\24\7\24\u00f9\n\24")
        buf.write(u"\f\24\16\24\u00fc\13\24\3\24\3\24\3\24\7\24\u0101\n\24")
        buf.write(u"\f\24\16\24\u0104\13\24\6\24\u0106\n\24\r\24\16\24\u0107")
        buf.write(u"\3\24\3\24\7\24\u010c\n\24\f\24\16\24\u010f\13\24\3\24")
        buf.write(u"\3\24\3\24\3\24\7\24\u0115\n\24\f\24\16\24\u0118\13\24")
        buf.write(u"\3\24\3\24\7\24\u011c\n\24\f\24\16\24\u011f\13\24\3\24")
        buf.write(u"\3\24\3\24\7\24\u0124\n\24\f\24\16\24\u0127\13\24\6\24")
        buf.write(u"\u0129\n\24\r\24\16\24\u012a\3\24\3\24\7\24\u012f\n\24")
        buf.write(u"\f\24\16\24\u0132\13\24\3\24\3\24\7\24\u0136\n\24\f\24")
        buf.write(u"\16\24\u0139\13\24\3\24\3\24\7\24\u013d\n\24\f\24\16")
        buf.write(u"\24\u0140\13\24\3\24\3\24\7\24\u0144\n\24\f\24\16\24")
        buf.write(u"\u0147\13\24\3\24\3\24\3\24\7\24\u014c\n\24\f\24\16\24")
        buf.write(u"\u014f\13\24\6\24\u0151\n\24\r\24\16\24\u0152\3\24\3")
        buf.write(u"\24\6\24\u0157\n\24\r\24\16\24\u0158\3\24\3\24\5\24\u015d")
        buf.write(u"\n\24\3\24\2\4\36 \25\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write(u"\34\36 \"$&\2\7\3\2!\"\3\2\23\24\3\2\25\26\3\2\n\17\3")
        buf.write(u"\2\27\30\u017a\2+\3\2\2\2\4:\3\2\2\2\6>\3\2\2\2\bY\3")
        buf.write(u"\2\2\2\nb\3\2\2\2\fd\3\2\2\2\16m\3\2\2\2\20p\3\2\2\2")
        buf.write(u"\22\u0080\3\2\2\2\24\u0085\3\2\2\2\26\u0090\3\2\2\2\30")
        buf.write(u"\u0097\3\2\2\2\32\u009c\3\2\2\2\34\u00a0\3\2\2\2\36\u00bc")
        buf.write(u"\3\2\2\2 \u00d8\3\2\2\2\"\u00e4\3\2\2\2$\u00e9\3\2\2")
        buf.write(u"\2&\u00ee\3\2\2\2(*\7+\2\2)(\3\2\2\2*-\3\2\2\2+)\3\2")
        buf.write(u"\2\2+,\3\2\2\2,.\3\2\2\2-+\3\2\2\2.\62\5\4\3\2/\61\7")
        buf.write(u"+\2\2\60/\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3")
        buf.write(u"\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\65\67\5\6\4\2\66\65")
        buf.write(u"\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29\3\3\2\2\2")
        buf.write(u":;\7\31\2\2;<\7(\2\2<=\b\3\1\2=\5\3\2\2\2>?\7\33\2\2")
        buf.write(u"?@\7(\2\2@B\b\4\1\2AC\7+\2\2BA\3\2\2\2CD\3\2\2\2DB\3")
        buf.write(u"\2\2\2DE\3\2\2\2EG\3\2\2\2FH\5\b\5\2GF\3\2\2\2HI\3\2")
        buf.write(u"\2\2IG\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KM\7\34\2\2LN\7+\2")
        buf.write(u"\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\7\3\2\2\2")
        buf.write(u"QZ\5\24\13\2RZ\5\26\f\2SZ\5\34\17\2TU\5&\24\2UV\b\5\1")
        buf.write(u"\2VZ\3\2\2\2WZ\5\n\6\2XZ\5\22\n\2YQ\3\2\2\2YR\3\2\2\2")
        buf.write(u"YS\3\2\2\2YT\3\2\2\2YW\3\2\2\2YX\3\2\2\2Z\\\3\2\2\2[")
        buf.write(u"]\7+\2\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\t")
        buf.write(u"\3\2\2\2`c\5\f\7\2ac\5\20\t\2b`\3\2\2\2ba\3\2\2\2c\13")
        buf.write(u"\3\2\2\2de\7\35\2\2ej\5\16\b\2fg\7\3\2\2gi\5\16\b\2h")
        buf.write(u"f\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2k\r\3\2\2\2lj")
        buf.write(u"\3\2\2\2mn\7(\2\2no\b\b\1\2o\17\3\2\2\2pq\7\35\2\2qr")
        buf.write(u"\7(\2\2rs\b\t\1\2st\7\4\2\2tu\7(\2\2u{\b\t\1\2vw\7\3")
        buf.write(u"\2\2wx\7(\2\2xz\b\t\1\2yv\3\2\2\2z}\3\2\2\2{y\3\2\2\2")
        buf.write(u"{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\177\7\5\2\2\177\21\3")
        buf.write(u"\2\2\2\u0080\u0081\7\32\2\2\u0081\u0082\7(\2\2\u0082")
        buf.write(u"\23\3\2\2\2\u0083\u0084\7\21\2\2\u0084\u0086\b\13\1\2")
        buf.write(u"\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087")
        buf.write(u"\3\2\2\2\u0087\u0088\7(\2\2\u0088\u0089\7\6\2\2\u0089")
        buf.write(u"\u008c\7\22\2\2\u008a\u008b\7\3\2\2\u008b\u008d\7(\2")
        buf.write(u"\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e")
        buf.write(u"\3\2\2\2\u008e\u008f\b\13\1\2\u008f\25\3\2\2\2\u0090")
        buf.write(u"\u0091\5$\23\2\u0091\u0092\7\7\2\2\u0092\u0093\5\30\r")
        buf.write(u"\2\u0093\u0094\7\6\2\2\u0094\u0095\5\32\16\2\u0095\u0096")
        buf.write(u"\b\f\1\2\u0096\27\3\2\2\2\u0097\u0098\t\2\2\2\u0098\31")
        buf.write(u"\3\2\2\2\u0099\u009d\7\'\2\2\u009a\u009d\7)\2\2\u009b")
        buf.write(u"\u009d\7(\2\2\u009c\u0099\3\2\2\2\u009c\u009a\3\2\2\2")
        buf.write(u"\u009c\u009b\3\2\2\2\u009d\33\3\2\2\2\u009e\u009f\7\21")
        buf.write(u"\2\2\u009f\u00a1\b\17\1\2\u00a0\u009e\3\2\2\2\u00a0\u00a1")
        buf.write(u"\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\7(\2\2\u00a3")
        buf.write(u"\u00a4\7\6\2\2\u00a4\u00a5\5\36\20\2\u00a5\35\3\2\2\2")
        buf.write(u"\u00a6\u00a7\b\20\1\2\u00a7\u00aa\b\20\1\2\u00a8\u00a9")
        buf.write(u"\7\26\2\2\u00a9\u00ab\b\20\1\2\u00aa\u00a8\3\2\2\2\u00aa")
        buf.write(u"\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\7)\2\2")
        buf.write(u"\u00ad\u00bd\b\20\1\2\u00ae\u00b1\b\20\1\2\u00af\u00b0")
        buf.write(u"\7\26\2\2\u00b0\u00b2\b\20\1\2\u00b1\u00af\3\2\2\2\u00b1")
        buf.write(u"\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\7\'\2")
        buf.write(u"\2\u00b4\u00bd\b\20\1\2\u00b5\u00b6\7(\2\2\u00b6\u00bd")
        buf.write(u"\b\20\1\2\u00b7\u00b8\7\b\2\2\u00b8\u00b9\5\36\20\2\u00b9")
        buf.write(u"\u00ba\7\t\2\2\u00ba\u00bb\b\20\1\2\u00bb\u00bd\3\2\2")
        buf.write(u"\2\u00bc\u00a6\3\2\2\2\u00bc\u00ae\3\2\2\2\u00bc\u00b5")
        buf.write(u"\3\2\2\2\u00bc\u00b7\3\2\2\2\u00bd\u00ca\3\2\2\2\u00be")
        buf.write(u"\u00bf\f\b\2\2\u00bf\u00c0\t\3\2\2\u00c0\u00c1\5\36\20")
        buf.write(u"\t\u00c1\u00c2\b\20\1\2\u00c2\u00c9\3\2\2\2\u00c3\u00c4")
        buf.write(u"\f\7\2\2\u00c4\u00c5\t\4\2\2\u00c5\u00c6\5\36\20\b\u00c6")
        buf.write(u"\u00c7\b\20\1\2\u00c7\u00c9\3\2\2\2\u00c8\u00be\3\2\2")
        buf.write(u"\2\u00c8\u00c3\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8")
        buf.write(u"\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\37\3\2\2\2\u00cc\u00ca")
        buf.write(u"\3\2\2\2\u00cd\u00ce\b\21\1\2\u00ce\u00cf\5\36\20\2\u00cf")
        buf.write(u"\u00d0\t\5\2\2\u00d0\u00d1\5\36\20\2\u00d1\u00d2\b\21")
        buf.write(u"\1\2\u00d2\u00d9\3\2\2\2\u00d3\u00d4\7\b\2\2\u00d4\u00d5")
        buf.write(u"\5 \21\2\u00d5\u00d6\7\t\2\2\u00d6\u00d7\b\21\1\2\u00d7")
        buf.write(u"\u00d9\3\2\2\2\u00d8\u00cd\3\2\2\2\u00d8\u00d3\3\2\2")
        buf.write(u"\2\u00d9\u00e1\3\2\2\2\u00da\u00db\f\3\2\2\u00db\u00dc")
        buf.write(u"\t\6\2\2\u00dc\u00dd\5 \21\4\u00dd\u00de\b\21\1\2\u00de")
        buf.write(u"\u00e0\3\2\2\2\u00df\u00da\3\2\2\2\u00e0\u00e3\3\2\2")
        buf.write(u"\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2!\3\2")
        buf.write(u"\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\5$\23\2\u00e5\u00e6")
        buf.write(u"\7\6\2\2\u00e6\u00e7\5\36\20\2\u00e7\u00e8\b\22\1\2\u00e8")
        buf.write(u"#\3\2\2\2\u00e9\u00ec\7(\2\2\u00ea\u00eb\7\7\2\2\u00eb")
        buf.write(u"\u00ed\7(\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write(u"\u00ed%\3\2\2\2\u00ee\u00ef\7\36\2\2\u00ef\u00f3\5 \21")
        buf.write(u"\2\u00f0\u00f2\7+\2\2\u00f1\u00f0\3\2\2\2\u00f2\u00f5")
        buf.write(u"\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4")
        buf.write(u"\u00f6\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00fa\7\4\2")
        buf.write(u"\2\u00f7\u00f9\7+\2\2\u00f8\u00f7\3\2\2\2\u00f9\u00fc")
        buf.write(u"\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write(u"\u0105\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe\5\"\22")
        buf.write(u"\2\u00fe\u0102\b\24\1\2\u00ff\u0101\7+\2\2\u0100\u00ff")
        buf.write(u"\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2\u0102")
        buf.write(u"\u0103\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2")
        buf.write(u"\2\u0105\u00fd\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0105")
        buf.write(u"\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write(u"\u010d\7\5\2\2\u010a\u010c\7+\2\2\u010b\u010a\3\2\2\2")
        buf.write(u"\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e")
        buf.write(u"\3\2\2\2\u010e\u0110\3\2\2\2\u010f\u010d\3\2\2\2\u0110")
        buf.write(u"\u0137\b\24\1\2\u0111\u0112\7\37\2\2\u0112\u0116\5 \21")
        buf.write(u"\2\u0113\u0115\7+\2\2\u0114\u0113\3\2\2\2\u0115\u0118")
        buf.write(u"\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write(u"\u0119\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011d\7\4\2")
        buf.write(u"\2\u011a\u011c\7+\2\2\u011b\u011a\3\2\2\2\u011c\u011f")
        buf.write(u"\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e")
        buf.write(u"\u0128\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121\5\"\22")
        buf.write(u"\2\u0121\u0125\b\24\1\2\u0122\u0124\7+\2\2\u0123\u0122")
        buf.write(u"\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125")
        buf.write(u"\u0126\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2")
        buf.write(u"\2\u0128\u0120\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u0128")
        buf.write(u"\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write(u"\u0130\7\5\2\2\u012d\u012f\7+\2\2\u012e\u012d\3\2\2\2")
        buf.write(u"\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131")
        buf.write(u"\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0130\3\2\2\2\u0133")
        buf.write(u"\u0134\b\24\1\2\u0134\u0136\3\2\2\2\u0135\u0111\3\2\2")
        buf.write(u"\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write(u"\3\2\2\2\u0138\u015c\3\2\2\2\u0139\u0137\3\2\2\2\u013a")
        buf.write(u"\u013e\7 \2\2\u013b\u013d\7+\2\2\u013c\u013b\3\2\2\2")
        buf.write(u"\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f")
        buf.write(u"\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u013e\3\2\2\2\u0141")
        buf.write(u"\u0145\7\4\2\2\u0142\u0144\7+\2\2\u0143\u0142\3\2\2\2")
        buf.write(u"\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146")
        buf.write(u"\3\2\2\2\u0146\u0150\3\2\2\2\u0147\u0145\3\2\2\2\u0148")
        buf.write(u"\u0149\5\"\22\2\u0149\u014d\b\24\1\2\u014a\u014c\7+\2")
        buf.write(u"\2\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b")
        buf.write(u"\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0151\3\2\2\2\u014f")
        buf.write(u"\u014d\3\2\2\2\u0150\u0148\3\2\2\2\u0151\u0152\3\2\2")
        buf.write(u"\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154")
        buf.write(u"\3\2\2\2\u0154\u0156\7\5\2\2\u0155\u0157\7+\2\2\u0156")
        buf.write(u"\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0156\3\2\2")
        buf.write(u"\2\u0158\u0159\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b")
        buf.write(u"\b\24\1\2\u015b\u015d\3\2\2\2\u015c\u013a\3\2\2\2\u015c")
        buf.write(u"\u015d\3\2\2\2\u015d\'\3\2\2\2*+\628DIOY^bj{\u0085\u008c")
        buf.write(u"\u009c\u00a0\u00aa\u00b1\u00bc\u00c8\u00ca\u00d8\u00e1")
        buf.write(u"\u00ec\u00f3\u00fa\u0102\u0107\u010d\u0116\u011d\u0125")
        buf.write(u"\u012a\u0130\u0137\u013e\u0145\u014d\u0152\u0158\u015c")
        return buf.getvalue()


class VarDefParser ( Parser ):

    grammarFileName = "VarDef.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"','", u"'{'", u"'}'", u"'='", u"'.'", 
                     u"'('", u"')'", u"'>'", u"'>='", u"'<'", u"'<='", u"'=='", 
                     u"'!='", u"<INVALID>", u"'@'", u"<INVALID>", u"'*'", 
                     u"'/'", u"'+'", u"'-'", u"' and '", u"' or '", u"'use'", 
                     u"'include'", u"'vardef'", u"'end'", u"'array'", u"'if'", 
                     u"'elseif'", u"'else'", u"'units'", u"'capacity'", 
                     u"'group'", u"'string'", u"'int'", u"'float'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"LINE_COMMENT", u"T", 
                      u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", u"AND", u"OR", 
                      u"USE", u"INCLUDE", u"VARDEF", u"END", u"ARRAY", u"IF", 
                      u"ELSEIF", u"ELSE", u"UNITS", u"CAPACITY", u"GROUP", 
                      u"STRING_L", u"INT_L", u"FLOAT_L", u"FLOAT", u"ID", 
                      u"INT", u"STRING", u"NL", u"WS" ]

    RULE_prog = 0
    RULE_use = 1
    RULE_vardef = 2
    RULE_field = 3
    RULE_new_var = 4
    RULE_array = 5
    RULE_array_var = 6
    RULE_array_cluster = 7
    RULE_include = 8
    RULE_var_path = 9
    RULE_var_meta = 10
    RULE_metaKey = 11
    RULE_metaValue = 12
    RULE_stat = 13
    RULE_ee = 14
    RULE_compare = 15
    RULE_assign = 16
    RULE_id2 = 17
    RULE_if_stat = 18

    ruleNames =  [ u"prog", u"use", u"vardef", u"field", u"new_var", u"array", 
                   u"array_var", u"array_cluster", u"include", u"var_path", 
                   u"var_meta", u"metaKey", u"metaValue", u"stat", u"ee", 
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
    LINE_COMMENT=14
    T=15
    PATH=16
    MUL=17
    DIV=18
    ADD=19
    SUB=20
    AND=21
    OR=22
    USE=23
    INCLUDE=24
    VARDEF=25
    END=26
    ARRAY=27
    IF=28
    ELSEIF=29
    ELSE=30
    UNITS=31
    CAPACITY=32
    GROUP=33
    STRING_L=34
    INT_L=35
    FLOAT_L=36
    FLOAT=37
    ID=38
    INT=39
    STRING=40
    NL=41
    WS=42

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
    varPathMap=collections.OrderedDict();
    varExprMap=collections.OrderedDict();
    tempVarList=[];
    newArrayMap=collections.OrderedDict();
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
        self.varPathGroupMap={};self.varExprGroupMap={};self.tempVarGroupList={};
        ifsMapGroupMap={};newArrayGroupMap={};

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 38
                self.match(VarDefParser.NL)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.use()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 45
                self.match(VarDefParser.NL)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.vardef()
                self.state = 54 
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
            self.state = 56
            self.match(VarDefParser.USE)
            self.state = 57
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
        self.ifid=0;

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(VarDefParser.VARDEF)
            self.state = 61
            localctx.name = self.match(VarDefParser.ID)
            groupName=str((None if localctx.name is None else localctx.name.text)).lower();self.vardefName=groupName;
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.match(VarDefParser.NL)
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.field()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ARRAY) | (1 << VarDefParser.IF) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 73
            self.match(VarDefParser.END)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.match(VarDefParser.NL)
                self.state = 77 
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
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 79
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 80
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 81
                self.stat()
                pass

            elif la_ == 4:
                self.state = 82
                self.if_stat()
                self.ifid=self.ifid+1;
                pass

            elif la_ == 5:
                self.state = 85
                self.new_var()
                pass

            elif la_ == 6:
                self.state = 86
                self.include()
                pass


            self.state = 90 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 89
                self.match(VarDefParser.NL)
                self.state = 92 
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
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.array_cluster()
                pass


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
        self.enterRule(localctx, 10, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(VarDefParser.ARRAY)
            self.state = 99
            self.array_var()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 100
                self.match(VarDefParser.T__0)
                self.state = 101
                self.array_var()
                self.state = 106
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

        def getRuleIndex(self):
            return VarDefParser.RULE_array_var

        def accept(self, visitor):
            if hasattr(visitor, "visitArray_var"):
                return visitor.visitArray_var(self)
            else:
                return visitor.visitChildren(self)




    def array_var(self):

        localctx = VarDefParser.Array_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();
            self.newArrayMap[name]=v;

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

        def getRuleIndex(self):
            return VarDefParser.RULE_array_cluster

        def accept(self, visitor):
            if hasattr(visitor, "visitArray_cluster"):
                return visitor.visitArray_cluster(self)
            else:
                return visitor.visitChildren(self)




    def array_cluster(self):

        localctx = VarDefParser.Array_clusterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_cluster)
        header='';subvar=[];
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(VarDefParser.ARRAY)
            self.state = 111
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 113
            self.match(VarDefParser.T__1)
            self.state = 114
            localctx.i = self.match(VarDefParser.ID)
            subvar.append(str((None if localctx.i is None else localctx.i.text)));
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 116
                self.match(VarDefParser.T__0)
                self.state = 117
                localctx.i = self.match(VarDefParser.ID)
                subvar.append(str((None if localctx.i is None else localctx.i.text)));
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(VarDefParser.T__2)
            self._ctx.stop = self._input.LT(-1)

            for v in subvar:
            	o = Var('')
            	self.newArrayMap[header.lower()+'.'+v.lower()]=o;

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
        self.enterRule(localctx, 16, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(VarDefParser.INCLUDE)
            self.state = 127
            localctx.g = self.match(VarDefParser.ID)
            self._ctx.stop = self._input.LT(-1)
            gn=str((None if localctx.g is None else localctx.g.text)).lower();
            if gn: 
            	self.varPathMap.update(self.varPathGroupMap[gn])
            	self.varExprMap.update(self.varExprGroupMap[gn])
            	self.tempVarList.extend(self.tempVarGroupList[gn])
            	self.ifsMap.update(self.ifsMapGroupMap[gn])
            	self.newArrayMap.update(self.newArrayGroupMap[gn])

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
        self.enterRule(localctx, 18, self.RULE_var_path)
        isTemp=False;
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 129
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 133
            localctx.i = self.match(VarDefParser.ID)
            self.state = 134
            self.match(VarDefParser.T__3)
            self.state = 135
            localctx.p = self.match(VarDefParser.PATH)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__0:
                self.state = 136
                self.match(VarDefParser.T__0)
                self.state = 137
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

        def id2(self):
            return self.getTypedRuleContext(VarDefParser.Id2Context,0)


        def metaKey(self):
            return self.getTypedRuleContext(VarDefParser.MetaKeyContext,0)


        def metaValue(self):
            return self.getTypedRuleContext(VarDefParser.MetaValueContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_var_meta

        def accept(self, visitor):
            if hasattr(visitor, "visitVar_meta"):
                return visitor.visitVar_meta(self)
            else:
                return visitor.visitChildren(self)




    def var_meta(self):

        localctx = VarDefParser.Var_metaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_meta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            localctx.i = self.id2()
            self.state = 143
            self.match(VarDefParser.T__4)
            self.state = 144
            localctx.m = self.metaKey()
            self.state = 145
            self.match(VarDefParser.T__3)
            self.state = 146
            localctx.inf = self.metaValue()
            name=str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop)))).lower();mk=str((None if localctx.m is None else self._input.getText((localctx.m.start,localctx.m.stop)))).lower();c=str((None if localctx.inf is None else self._input.getText((localctx.inf.start,localctx.inf.stop)))).lower();
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

        def UNITS(self):
            return self.getToken(VarDefParser.UNITS, 0)

        def CAPACITY(self):
            return self.getToken(VarDefParser.CAPACITY, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_metaKey

        def accept(self, visitor):
            if hasattr(visitor, "visitMetaKey"):
                return visitor.visitMetaKey(self)
            else:
                return visitor.visitChildren(self)




    def metaKey(self):

        localctx = VarDefParser.MetaKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_metaKey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not(_la==VarDefParser.UNITS or _la==VarDefParser.CAPACITY):
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

    class MetaValueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.MetaValueContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token

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
        self.enterRule(localctx, 24, self.RULE_metaValue)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                localctx.i = self.match(VarDefParser.FLOAT)
                pass
            elif token in [VarDefParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(VarDefParser.INT)
                pass
            elif token in [VarDefParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.match(VarDefParser.ID)
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
        self.enterRule(localctx, 26, self.RULE_stat)
        isTemp=False 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 156
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 160
            localctx.i = self.match(VarDefParser.ID)
            self.state = 161
            self.match(VarDefParser.T__3)
            self.state = 162
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                s=''
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 166
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 170
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 173
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 177
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 179
                localctx.i = self.match(VarDefParser.ID)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();
                if vName in self.newArrayMap.keys() or vName in self.varPathMap.keys() or vName in self.varExprMap.keys():
                	localctx.x = self.ifsAppend+"['"+vName+"']"+"[i]"
                	#print (vName) 
                else:
                	Err.addError(vName+' not defined.', self.vardefFile, self.vardefName)

                pass

            elif la_ == 4:
                self.state = 181
                self.match(VarDefParser.T__5)
                self.state = 182
                localctx.a = self.ee(0)
                self.state = 183
                self.match(VarDefParser.T__6)
                localctx.x="("+str(localctx.a.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 198
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 188
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 189
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 190
                        localctx.b = self.ee(7)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 193
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 194
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 195
                        localctx.b = self.ee(6)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_compare, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 204
                localctx.a = self.ee(0)
                self.state = 205
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__7) | (1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10) | (1 << VarDefParser.T__11) | (1 << VarDefParser.T__12))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 206
                localctx.b = self.ee(0)
                localctx.x=str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 209
                self.match(VarDefParser.T__5)
                self.state = 210
                localctx.c = self.compare(0)
                self.state = 211
                self.match(VarDefParser.T__6)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VarDefParser.CompareContext(self, _parentctx, _parentState)
                    localctx.c1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare)
                    self.state = 216
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 217
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 218
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            localctx.i = self.id2()
            self.state = 227
            self.match(VarDefParser.T__3)
            self.state = 228
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
        self.enterRule(localctx, 34, self.RULE_id2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(VarDefParser.ID)
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 232
                self.match(VarDefParser.T__4)
                self.state = 233
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
        self.enterRule(localctx, 36, self.RULE_if_stat)
        ifs=collections.OrderedDict();al=[];
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(VarDefParser.IF)
            self.state = 237
            localctx.c = self.compare(0)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 238
                self.match(VarDefParser.NL)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244
            self.match(VarDefParser.T__1)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 245
                self.match(VarDefParser.NL)
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 259 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 251
                localctx.a = self.assign()
                t=str(localctx.a.x).lower();al.append(t)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 253
                    self.match(VarDefParser.NL)
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 261 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 263
            self.match(VarDefParser.T__2)
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 264
                    self.match(VarDefParser.NL) 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 271
                self.match(VarDefParser.ELSEIF)
                self.state = 272
                localctx.c = self.compare(0)
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 273
                    self.match(VarDefParser.NL)
                    self.state = 278
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 279
                self.match(VarDefParser.T__1)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 280
                    self.match(VarDefParser.NL)
                    self.state = 285
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 294 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 286
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 288
                        self.match(VarDefParser.NL)
                        self.state = 293
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 296 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 298
                self.match(VarDefParser.T__2)
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 299
                        self.match(VarDefParser.NL) 
                    self.state = 304
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 312
                self.match(VarDefParser.ELSE)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 313
                    self.match(VarDefParser.NL)
                    self.state = 318
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 319
                self.match(VarDefParser.T__1)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 320
                    self.match(VarDefParser.NL)
                    self.state = 325
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 334 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 326
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 331
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 328
                        self.match(VarDefParser.NL)
                        self.state = 333
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 336 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 338
                self.match(VarDefParser.T__2)
                self.state = 340 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 339
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 342 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        self._predicates[14] = self.ee_sempred
        self._predicates[15] = self.compare_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def ee_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

    def compare_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




