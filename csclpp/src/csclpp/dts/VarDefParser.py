# Generated from VarDef.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
from collections import defaultdict
import collections

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\'\u014d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\3\2\7\2(\n\2\f\2\16\2+\13\2\3\2\6\2.\n\2\r")
        buf.write(u"\2\16\2/\3\3\3\3\3\3\6\3\65\n\3\r\3\16\3\66\3\3\6\3:")
        buf.write(u"\n\3\r\3\16\3;\3\3\3\3\6\3@\n\3\r\3\16\3A\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\5\4L\n\4\3\4\6\4O\n\4\r\4\16\4P")
        buf.write(u"\3\5\3\5\5\5U\n\5\3\6\3\6\3\6\3\6\7\6[\n\6\f\6\16\6^")
        buf.write(u"\13\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\7\bl\n\b\f\b\16\bo\13\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n")
        buf.write(u"\5\nx\n\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\f\3\f\3\r\3\r\3\r\5\r\u008b\n\r\3\16\3\16")
        buf.write(u"\5\16\u008f\n\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write(u"\17\5\17\u0099\n\17\3\17\3\17\3\17\3\17\3\17\5\17\u00a0")
        buf.write(u"\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5")
        buf.write(u"\17\u00ab\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\7\17\u00b7\n\17\f\17\16\17\u00ba\13\17\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5")
        buf.write(u"\20\u00c7\n\20\3\20\3\20\3\20\3\20\3\20\7\20\u00ce\n")
        buf.write(u"\20\f\20\16\20\u00d1\13\20\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\22\3\22\3\22\5\22\u00db\n\22\3\23\3\23\3\23\7\23\u00e0")
        buf.write(u"\n\23\f\23\16\23\u00e3\13\23\3\23\3\23\7\23\u00e7\n\23")
        buf.write(u"\f\23\16\23\u00ea\13\23\3\23\3\23\3\23\7\23\u00ef\n\23")
        buf.write(u"\f\23\16\23\u00f2\13\23\6\23\u00f4\n\23\r\23\16\23\u00f5")
        buf.write(u"\3\23\3\23\7\23\u00fa\n\23\f\23\16\23\u00fd\13\23\3\23")
        buf.write(u"\3\23\3\23\3\23\7\23\u0103\n\23\f\23\16\23\u0106\13\23")
        buf.write(u"\3\23\3\23\7\23\u010a\n\23\f\23\16\23\u010d\13\23\3\23")
        buf.write(u"\3\23\3\23\7\23\u0112\n\23\f\23\16\23\u0115\13\23\6\23")
        buf.write(u"\u0117\n\23\r\23\16\23\u0118\3\23\3\23\7\23\u011d\n\23")
        buf.write(u"\f\23\16\23\u0120\13\23\3\23\3\23\7\23\u0124\n\23\f\23")
        buf.write(u"\16\23\u0127\13\23\3\23\3\23\7\23\u012b\n\23\f\23\16")
        buf.write(u"\23\u012e\13\23\3\23\3\23\7\23\u0132\n\23\f\23\16\23")
        buf.write(u"\u0135\13\23\3\23\3\23\3\23\7\23\u013a\n\23\f\23\16\23")
        buf.write(u"\u013d\13\23\6\23\u013f\n\23\r\23\16\23\u0140\3\23\3")
        buf.write(u"\23\6\23\u0145\n\23\r\23\16\23\u0146\3\23\3\23\5\23\u014b")
        buf.write(u"\n\23\3\23\2\4\34\36\24\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write(u"\32\34\36 \"$\2\7\3\2 !\3\2\23\24\3\2\25\26\3\2\n\17")
        buf.write(u"\3\2\27\30\u0167\2)\3\2\2\2\4\61\3\2\2\2\6K\3\2\2\2\b")
        buf.write(u"T\3\2\2\2\nV\3\2\2\2\f_\3\2\2\2\16b\3\2\2\2\20r\3\2\2")
        buf.write(u"\2\22w\3\2\2\2\24~\3\2\2\2\26\u0085\3\2\2\2\30\u008a")
        buf.write(u"\3\2\2\2\32\u008e\3\2\2\2\34\u00aa\3\2\2\2\36\u00c6\3")
        buf.write(u"\2\2\2 \u00d2\3\2\2\2\"\u00d7\3\2\2\2$\u00dc\3\2\2\2")
        buf.write(u"&(\7&\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*")
        buf.write(u"-\3\2\2\2+)\3\2\2\2,.\5\4\3\2-,\3\2\2\2./\3\2\2\2/-\3")
        buf.write(u"\2\2\2/\60\3\2\2\2\60\3\3\2\2\2\61\62\7\32\2\2\62\64")
        buf.write(u"\7\"\2\2\63\65\7&\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66")
        buf.write(u"\64\3\2\2\2\66\67\3\2\2\2\679\3\2\2\28:\5\6\4\298\3\2")
        buf.write(u"\2\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<=\3\2\2\2=?\7\33\2")
        buf.write(u"\2>@\7&\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B")
        buf.write(u"\5\3\2\2\2CL\5\22\n\2DL\5\24\13\2EL\5\32\16\2FG\5$\23")
        buf.write(u"\2GH\b\4\1\2HL\3\2\2\2IL\5\b\5\2JL\5\20\t\2KC\3\2\2\2")
        buf.write(u"KD\3\2\2\2KE\3\2\2\2KF\3\2\2\2KI\3\2\2\2KJ\3\2\2\2LN")
        buf.write(u"\3\2\2\2MO\7&\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2")
        buf.write(u"\2\2Q\7\3\2\2\2RU\5\n\6\2SU\5\16\b\2TR\3\2\2\2TS\3\2")
        buf.write(u"\2\2U\t\3\2\2\2VW\7\34\2\2W\\\5\f\7\2XY\7\3\2\2Y[\5\f")
        buf.write(u"\7\2ZX\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\13\3")
        buf.write(u"\2\2\2^\\\3\2\2\2_`\7\"\2\2`a\b\7\1\2a\r\3\2\2\2bc\7")
        buf.write(u"\34\2\2cd\7\"\2\2de\b\b\1\2ef\7\4\2\2fg\7\"\2\2gm\b\b")
        buf.write(u"\1\2hi\7\3\2\2ij\7\"\2\2jl\b\b\1\2kh\3\2\2\2lo\3\2\2")
        buf.write(u"\2mk\3\2\2\2mn\3\2\2\2np\3\2\2\2om\3\2\2\2pq\7\5\2\2")
        buf.write(u"q\17\3\2\2\2rs\7\31\2\2st\7\"\2\2t\21\3\2\2\2uv\7\21")
        buf.write(u"\2\2vx\b\n\1\2wu\3\2\2\2wx\3\2\2\2xy\3\2\2\2yz\7\"\2")
        buf.write(u"\2z{\7\6\2\2{|\7\22\2\2|}\b\n\1\2}\23\3\2\2\2~\177\5")
        buf.write(u"\"\22\2\177\u0080\7\7\2\2\u0080\u0081\5\26\f\2\u0081")
        buf.write(u"\u0082\7\6\2\2\u0082\u0083\5\30\r\2\u0083\u0084\b\13")
        buf.write(u"\1\2\u0084\25\3\2\2\2\u0085\u0086\t\2\2\2\u0086\27\3")
        buf.write(u"\2\2\2\u0087\u008b\7#\2\2\u0088\u008b\7$\2\2\u0089\u008b")
        buf.write(u"\7\"\2\2\u008a\u0087\3\2\2\2\u008a\u0088\3\2\2\2\u008a")
        buf.write(u"\u0089\3\2\2\2\u008b\31\3\2\2\2\u008c\u008d\7\21\2\2")
        buf.write(u"\u008d\u008f\b\16\1\2\u008e\u008c\3\2\2\2\u008e\u008f")
        buf.write(u"\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091\7\"\2\2\u0091")
        buf.write(u"\u0092\7\6\2\2\u0092\u0093\5\34\17\2\u0093\33\3\2\2\2")
        buf.write(u"\u0094\u0095\b\17\1\2\u0095\u0098\b\17\1\2\u0096\u0097")
        buf.write(u"\7\26\2\2\u0097\u0099\b\17\1\2\u0098\u0096\3\2\2\2\u0098")
        buf.write(u"\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\7$\2\2")
        buf.write(u"\u009b\u00ab\b\17\1\2\u009c\u009f\b\17\1\2\u009d\u009e")
        buf.write(u"\7\26\2\2\u009e\u00a0\b\17\1\2\u009f\u009d\3\2\2\2\u009f")
        buf.write(u"\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\7#\2\2")
        buf.write(u"\u00a2\u00ab\b\17\1\2\u00a3\u00a4\7\"\2\2\u00a4\u00ab")
        buf.write(u"\b\17\1\2\u00a5\u00a6\7\b\2\2\u00a6\u00a7\5\34\17\2\u00a7")
        buf.write(u"\u00a8\7\t\2\2\u00a8\u00a9\b\17\1\2\u00a9\u00ab\3\2\2")
        buf.write(u"\2\u00aa\u0094\3\2\2\2\u00aa\u009c\3\2\2\2\u00aa\u00a3")
        buf.write(u"\3\2\2\2\u00aa\u00a5\3\2\2\2\u00ab\u00b8\3\2\2\2\u00ac")
        buf.write(u"\u00ad\f\b\2\2\u00ad\u00ae\t\3\2\2\u00ae\u00af\5\34\17")
        buf.write(u"\t\u00af\u00b0\b\17\1\2\u00b0\u00b7\3\2\2\2\u00b1\u00b2")
        buf.write(u"\f\7\2\2\u00b2\u00b3\t\4\2\2\u00b3\u00b4\5\34\17\b\u00b4")
        buf.write(u"\u00b5\b\17\1\2\u00b5\u00b7\3\2\2\2\u00b6\u00ac\3\2\2")
        buf.write(u"\2\u00b6\u00b1\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6")
        buf.write(u"\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\35\3\2\2\2\u00ba\u00b8")
        buf.write(u"\3\2\2\2\u00bb\u00bc\b\20\1\2\u00bc\u00bd\5\34\17\2\u00bd")
        buf.write(u"\u00be\t\5\2\2\u00be\u00bf\5\34\17\2\u00bf\u00c0\b\20")
        buf.write(u"\1\2\u00c0\u00c7\3\2\2\2\u00c1\u00c2\7\b\2\2\u00c2\u00c3")
        buf.write(u"\5\36\20\2\u00c3\u00c4\7\t\2\2\u00c4\u00c5\b\20\1\2\u00c5")
        buf.write(u"\u00c7\3\2\2\2\u00c6\u00bb\3\2\2\2\u00c6\u00c1\3\2\2")
        buf.write(u"\2\u00c7\u00cf\3\2\2\2\u00c8\u00c9\f\3\2\2\u00c9\u00ca")
        buf.write(u"\t\6\2\2\u00ca\u00cb\5\36\20\4\u00cb\u00cc\b\20\1\2\u00cc")
        buf.write(u"\u00ce\3\2\2\2\u00cd\u00c8\3\2\2\2\u00ce\u00d1\3\2\2")
        buf.write(u"\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\37\3")
        buf.write(u"\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\5\"\22\2\u00d3")
        buf.write(u"\u00d4\7\6\2\2\u00d4\u00d5\5\34\17\2\u00d5\u00d6\b\21")
        buf.write(u"\1\2\u00d6!\3\2\2\2\u00d7\u00da\7\"\2\2\u00d8\u00d9\7")
        buf.write(u"\7\2\2\u00d9\u00db\7\"\2\2\u00da\u00d8\3\2\2\2\u00da")
        buf.write(u"\u00db\3\2\2\2\u00db#\3\2\2\2\u00dc\u00dd\7\35\2\2\u00dd")
        buf.write(u"\u00e1\5\36\20\2\u00de\u00e0\7&\2\2\u00df\u00de\3\2\2")
        buf.write(u"\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2")
        buf.write(u"\3\2\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4")
        buf.write(u"\u00e8\7\4\2\2\u00e5\u00e7\7&\2\2\u00e6\u00e5\3\2\2\2")
        buf.write(u"\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9")
        buf.write(u"\3\2\2\2\u00e9\u00f3\3\2\2\2\u00ea\u00e8\3\2\2\2\u00eb")
        buf.write(u"\u00ec\5 \21\2\u00ec\u00f0\b\23\1\2\u00ed\u00ef\7&\2")
        buf.write(u"\2\u00ee\u00ed\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee")
        buf.write(u"\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2")
        buf.write(u"\u00f0\3\2\2\2\u00f3\u00eb\3\2\2\2\u00f4\u00f5\3\2\2")
        buf.write(u"\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7")
        buf.write(u"\3\2\2\2\u00f7\u00fb\7\5\2\2\u00f8\u00fa\7&\2\2\u00f9")
        buf.write(u"\u00f8\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2")
        buf.write(u"\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00fb")
        buf.write(u"\3\2\2\2\u00fe\u0125\b\23\1\2\u00ff\u0100\7\36\2\2\u0100")
        buf.write(u"\u0104\5\36\20\2\u0101\u0103\7&\2\2\u0102\u0101\3\2\2")
        buf.write(u"\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105")
        buf.write(u"\3\2\2\2\u0105\u0107\3\2\2\2\u0106\u0104\3\2\2\2\u0107")
        buf.write(u"\u010b\7\4\2\2\u0108\u010a\7&\2\2\u0109\u0108\3\2\2\2")
        buf.write(u"\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c")
        buf.write(u"\3\2\2\2\u010c\u0116\3\2\2\2\u010d\u010b\3\2\2\2\u010e")
        buf.write(u"\u010f\5 \21\2\u010f\u0113\b\23\1\2\u0110\u0112\7&\2")
        buf.write(u"\2\u0111\u0110\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111")
        buf.write(u"\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0117\3\2\2\2\u0115")
        buf.write(u"\u0113\3\2\2\2\u0116\u010e\3\2\2\2\u0117\u0118\3\2\2")
        buf.write(u"\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a")
        buf.write(u"\3\2\2\2\u011a\u011e\7\5\2\2\u011b\u011d\7&\2\2\u011c")
        buf.write(u"\u011b\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2")
        buf.write(u"\2\u011e\u011f\3\2\2\2\u011f\u0121\3\2\2\2\u0120\u011e")
        buf.write(u"\3\2\2\2\u0121\u0122\b\23\1\2\u0122\u0124\3\2\2\2\u0123")
        buf.write(u"\u00ff\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2")
        buf.write(u"\2\u0125\u0126\3\2\2\2\u0126\u014a\3\2\2\2\u0127\u0125")
        buf.write(u"\3\2\2\2\u0128\u012c\7\37\2\2\u0129\u012b\7&\2\2\u012a")
        buf.write(u"\u0129\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2")
        buf.write(u"\2\u012c\u012d\3\2\2\2\u012d\u012f\3\2\2\2\u012e\u012c")
        buf.write(u"\3\2\2\2\u012f\u0133\7\4\2\2\u0130\u0132\7&\2\2\u0131")
        buf.write(u"\u0130\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2")
        buf.write(u"\2\u0133\u0134\3\2\2\2\u0134\u013e\3\2\2\2\u0135\u0133")
        buf.write(u"\3\2\2\2\u0136\u0137\5 \21\2\u0137\u013b\b\23\1\2\u0138")
        buf.write(u"\u013a\7&\2\2\u0139\u0138\3\2\2\2\u013a\u013d\3\2\2\2")
        buf.write(u"\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013f")
        buf.write(u"\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u0136\3\2\2\2\u013f")
        buf.write(u"\u0140\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2")
        buf.write(u"\2\u0141\u0142\3\2\2\2\u0142\u0144\7\5\2\2\u0143\u0145")
        buf.write(u"\7&\2\2\u0144\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write(u"\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\3\2\2")
        buf.write(u"\2\u0148\u0149\b\23\1\2\u0149\u014b\3\2\2\2\u014a\u0128")
        buf.write(u"\3\2\2\2\u014a\u014b\3\2\2\2\u014b%\3\2\2\2()/\66;AK")
        buf.write(u"PT\\mw\u008a\u008e\u0098\u009f\u00aa\u00b6\u00b8\u00c6")
        buf.write(u"\u00cf\u00da\u00e1\u00e8\u00f0\u00f5\u00fb\u0104\u010b")
        buf.write(u"\u0113\u0118\u011e\u0125\u012c\u0133\u013b\u0140\u0146")
        buf.write(u"\u014a")
        return buf.getvalue()


class VarDefParser ( Parser ):

    grammarFileName = "VarDef.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"','", u"'{'", u"'}'", u"'='", u"'.'", 
                     u"'('", u"')'", u"'>'", u"'>='", u"'<'", u"'<='", u"'=='", 
                     u"'!='", u"<INVALID>", u"'@'", u"<INVALID>", u"'*'", 
                     u"'/'", u"'+'", u"'-'", u"' and '", u"' or '", u"'include'", 
                     u"'vardef'", u"'end'", u"'array'", u"'if'", u"'elseif'", 
                     u"'else'", u"'units'", u"'capacity'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"LINE_COMMENT", u"T", 
                      u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", u"AND", u"OR", 
                      u"INCLUDE", u"VARDEF", u"END", u"ARRAY", u"IF", u"ELSEIF", 
                      u"ELSE", u"UNITS", u"CAPACITY", u"ID", u"FLOAT", u"INT", 
                      u"STRING", u"NL", u"WS" ]

    RULE_prog = 0
    RULE_vardef = 1
    RULE_field = 2
    RULE_new_var = 3
    RULE_array = 4
    RULE_array_var = 5
    RULE_array_cluster = 6
    RULE_include = 7
    RULE_var_path = 8
    RULE_var_meta = 9
    RULE_metaKey = 10
    RULE_metaValue = 11
    RULE_stat = 12
    RULE_ee = 13
    RULE_compare = 14
    RULE_assign = 15
    RULE_id2 = 16
    RULE_if_stat = 17

    ruleNames =  [ u"prog", u"vardef", u"field", u"new_var", u"array", u"array_var", 
                   u"array_cluster", u"include", u"var_path", u"var_meta", 
                   u"metaKey", u"metaValue", u"stat", u"ee", u"compare", 
                   u"assign", u"id2", u"if_stat" ]

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
    INCLUDE=23
    VARDEF=24
    END=25
    ARRAY=26
    IF=27
    ELSEIF=28
    ELSE=29
    UNITS=30
    CAPACITY=31
    ID=32
    FLOAT=33
    INT=34
    STRING=35
    NL=36
    WS=37

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


    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

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
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 36
                self.match(VarDefParser.NL)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.vardef()
                self.state = 45 
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
        self.enterRule(localctx, 2, self.RULE_vardef)

        self.varPathMap=collections.OrderedDict();
        self.varExprMap=collections.OrderedDict();
        self.tempVarList=[];
        self.ifsMap=collections.OrderedDict();
        self.newArrayMap=collections.OrderedDict();
        self.ifid=0;

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(VarDefParser.VARDEF)
            self.state = 48
            localctx.name = self.match(VarDefParser.ID)
            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self.match(VarDefParser.NL)
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.field()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ARRAY) | (1 << VarDefParser.IF) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 59
            self.match(VarDefParser.END)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.match(VarDefParser.NL)
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self._ctx.stop = self._input.LT(-1)
            groupName=str((None if localctx.name is None else localctx.name.text)).lower();
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
        self.enterRule(localctx, 4, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 65
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 66
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 67
                self.stat()
                pass

            elif la_ == 4:
                self.state = 68
                self.if_stat()
                self.ifid=self.ifid+1;
                pass

            elif la_ == 5:
                self.state = 71
                self.new_var()
                pass

            elif la_ == 6:
                self.state = 72
                self.include()
                pass


            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 75
                self.match(VarDefParser.NL)
                self.state = 78 
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
        self.enterRule(localctx, 6, self.RULE_new_var)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
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
        self.enterRule(localctx, 8, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(VarDefParser.ARRAY)
            self.state = 85
            self.array_var()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 86
                self.match(VarDefParser.T__0)
                self.state = 87
                self.array_var()
                self.state = 92
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
        self.enterRule(localctx, 10, self.RULE_array_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
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
        self.enterRule(localctx, 12, self.RULE_array_cluster)
        header='';subvar=[];
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(VarDefParser.ARRAY)
            self.state = 97
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 99
            self.match(VarDefParser.T__1)
            self.state = 100
            localctx.i = self.match(VarDefParser.ID)
            subvar.append(str((None if localctx.i is None else localctx.i.text)));
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 102
                self.match(VarDefParser.T__0)
                self.state = 103
                localctx.i = self.match(VarDefParser.ID)
                subvar.append(str((None if localctx.i is None else localctx.i.text)));
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
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
        self.enterRule(localctx, 14, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(VarDefParser.INCLUDE)
            self.state = 113
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

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

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
        self.enterRule(localctx, 16, self.RULE_var_path)
        isTemp=False 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 115
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 119
            localctx.i = self.match(VarDefParser.ID)
            self.state = 120
            self.match(VarDefParser.T__3)
            self.state = 121
            localctx.p = self.match(VarDefParser.PATH)
            p =str((None if localctx.p is None else localctx.p.text)); t = Var(p); 
            name=str((None if localctx.i is None else localctx.i.text)).lower(); self.varPathMap[name]=t;
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
        self.enterRule(localctx, 18, self.RULE_var_meta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            localctx.i = self.id2()
            self.state = 125
            self.match(VarDefParser.T__4)
            self.state = 126
            localctx.m = self.metaKey()
            self.state = 127
            self.match(VarDefParser.T__3)
            self.state = 128
            localctx.inf = self.metaValue()
            name=str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop)))).lower();mk=str((None if localctx.m is None else self._input.getText((localctx.m.start,localctx.m.stop))));c=str((None if localctx.inf is None else self._input.getText((localctx.inf.start,localctx.inf.stop))));
            if name in self.varPathMap:
            	self.varPathMap[name].metaData[mk]=c; 
            elif name in self.varExprMap:
            	self.varExprMap[name].metaData[mk]=c; 
            elif name in self.newArrayMap:
            	self.newArrayMap[name].metaData[mk]=c; 
            else:
            	print ('#Error: '+name+'.'+mk+'='+c+' variable \"'+name+'\" not found!')

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
        self.enterRule(localctx, 20, self.RULE_metaKey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
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
        self.enterRule(localctx, 22, self.RULE_metaValue)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                localctx.i = self.match(VarDefParser.FLOAT)
                pass
            elif token in [VarDefParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(VarDefParser.INT)
                pass
            elif token in [VarDefParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
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
        self.enterRule(localctx, 24, self.RULE_stat)
        isTemp=False 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 138
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 142
            localctx.i = self.match(VarDefParser.ID)
            self.state = 143
            self.match(VarDefParser.T__3)
            self.state = 144
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                s=''
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 148
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 152
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 155
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 159
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 161
                localctx.i = self.match(VarDefParser.ID)
                localctx.x=self.ifsAppend+"['"+str((None if localctx.i is None else localctx.i.text))+"']"+"[i]"
                pass

            elif la_ == 4:
                self.state = 163
                self.match(VarDefParser.T__5)
                self.state = 164
                localctx.a = self.ee(0)
                self.state = 165
                self.match(VarDefParser.T__6)
                localctx.x="("+str(localctx.a.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 182
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 180
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 170
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 171
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 172
                        localctx.b = self.ee(7)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 175
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 176
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 177
                        localctx.b = self.ee(6)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 184
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_compare, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 186
                localctx.a = self.ee(0)
                self.state = 187
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__7) | (1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10) | (1 << VarDefParser.T__11) | (1 << VarDefParser.T__12))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 188
                localctx.b = self.ee(0)
                localctx.x=str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 191
                self.match(VarDefParser.T__5)
                self.state = 192
                localctx.c = self.compare(0)
                self.state = 193
                self.match(VarDefParser.T__6)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VarDefParser.CompareContext(self, _parentctx, _parentState)
                    localctx.c1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare)
                    self.state = 198
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 199
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 200
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            localctx.i = self.id2()
            self.state = 209
            self.match(VarDefParser.T__3)
            self.state = 210
            localctx.a = self.ee(0)
            localctx.x=self.ifsNewAppend+"['"+str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop))))+"'][i]="+localctx.a.x
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
        self.enterRule(localctx, 32, self.RULE_id2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(VarDefParser.ID)
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 214
                self.match(VarDefParser.T__4)
                self.state = 215
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
        self.enterRule(localctx, 34, self.RULE_if_stat)
        ifs=collections.OrderedDict();al=[];
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(VarDefParser.IF)
            self.state = 219
            localctx.c = self.compare(0)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 220
                self.match(VarDefParser.NL)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 226
            self.match(VarDefParser.T__1)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 227
                self.match(VarDefParser.NL)
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 233
                localctx.a = self.assign()
                t=str(localctx.a.x).lower();al.append(t)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 235
                    self.match(VarDefParser.NL)
                    self.state = 240
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 245
            self.match(VarDefParser.T__2)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 246
                    self.match(VarDefParser.NL) 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 253
                self.match(VarDefParser.ELSEIF)
                self.state = 254
                localctx.c = self.compare(0)
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 255
                    self.match(VarDefParser.NL)
                    self.state = 260
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 261
                self.match(VarDefParser.T__1)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 262
                    self.match(VarDefParser.NL)
                    self.state = 267
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 276 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 268
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 273
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 270
                        self.match(VarDefParser.NL)
                        self.state = 275
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 278 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 280
                self.match(VarDefParser.T__2)
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 281
                        self.match(VarDefParser.NL) 
                    self.state = 286
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 294
                self.match(VarDefParser.ELSE)
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 295
                    self.match(VarDefParser.NL)
                    self.state = 300
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 301
                self.match(VarDefParser.T__1)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 302
                    self.match(VarDefParser.NL)
                    self.state = 307
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 316 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 308
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 313
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 310
                        self.match(VarDefParser.NL)
                        self.state = 315
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 318 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 320
                self.match(VarDefParser.T__2)
                self.state = 322 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 321
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 324 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self._predicates[13] = self.ee_sempred
        self._predicates[14] = self.compare_sempred
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
         




