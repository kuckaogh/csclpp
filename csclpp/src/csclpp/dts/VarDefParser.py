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
        buf.write(u"+\u014e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\3\2\7\2(\n\2\f\2\16\2+\13\2\3\2\6\2.\n\2\r\2")
        buf.write(u"\16\2/\3\3\3\3\3\3\3\3\6\3\66\n\3\r\3\16\3\67\3\3\6\3")
        buf.write(u";\n\3\r\3\16\3<\3\3\3\3\6\3A\n\3\r\3\16\3B\3\4\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\4\5\4M\n\4\3\4\6\4P\n\4\r\4\16\4")
        buf.write(u"Q\3\5\3\5\5\5V\n\5\3\6\3\6\3\6\3\6\7\6\\\n\6\f\6\16\6")
        buf.write(u"_\13\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write(u"\b\7\bm\n\b\f\b\16\bp\13\b\3\b\3\b\3\t\3\t\3\t\3\n\3")
        buf.write(u"\n\5\ny\n\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\5\r\u008c\n\r\3\16")
        buf.write(u"\3\16\5\16\u0090\n\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write(u"\17\3\17\5\17\u009a\n\17\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write(u"\u00a1\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\5\17\u00ac\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\7\17\u00b8\n\17\f\17\16\17\u00bb\13\17")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\5\20\u00c8\n\20\3\20\3\20\3\20\3\20\3\20\7\20\u00cf")
        buf.write(u"\n\20\f\20\16\20\u00d2\13\20\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\22\3\22\3\22\5\22\u00dc\n\22\3\23\3\23\3\23\7\23\u00e1")
        buf.write(u"\n\23\f\23\16\23\u00e4\13\23\3\23\3\23\7\23\u00e8\n\23")
        buf.write(u"\f\23\16\23\u00eb\13\23\3\23\3\23\3\23\7\23\u00f0\n\23")
        buf.write(u"\f\23\16\23\u00f3\13\23\6\23\u00f5\n\23\r\23\16\23\u00f6")
        buf.write(u"\3\23\3\23\7\23\u00fb\n\23\f\23\16\23\u00fe\13\23\3\23")
        buf.write(u"\3\23\3\23\3\23\7\23\u0104\n\23\f\23\16\23\u0107\13\23")
        buf.write(u"\3\23\3\23\7\23\u010b\n\23\f\23\16\23\u010e\13\23\3\23")
        buf.write(u"\3\23\3\23\7\23\u0113\n\23\f\23\16\23\u0116\13\23\6\23")
        buf.write(u"\u0118\n\23\r\23\16\23\u0119\3\23\3\23\7\23\u011e\n\23")
        buf.write(u"\f\23\16\23\u0121\13\23\3\23\3\23\7\23\u0125\n\23\f\23")
        buf.write(u"\16\23\u0128\13\23\3\23\3\23\7\23\u012c\n\23\f\23\16")
        buf.write(u"\23\u012f\13\23\3\23\3\23\7\23\u0133\n\23\f\23\16\23")
        buf.write(u"\u0136\13\23\3\23\3\23\3\23\7\23\u013b\n\23\f\23\16\23")
        buf.write(u"\u013e\13\23\6\23\u0140\n\23\r\23\16\23\u0141\3\23\3")
        buf.write(u"\23\6\23\u0146\n\23\r\23\16\23\u0147\3\23\3\23\5\23\u014c")
        buf.write(u"\n\23\3\23\2\4\34\36\24\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write(u"\32\34\36 \"$\2\7\3\2 !\3\2\23\24\3\2\25\26\3\2\n\17")
        buf.write(u"\3\2\27\30\u0168\2)\3\2\2\2\4\61\3\2\2\2\6L\3\2\2\2\b")
        buf.write(u"U\3\2\2\2\nW\3\2\2\2\f`\3\2\2\2\16c\3\2\2\2\20s\3\2\2")
        buf.write(u"\2\22x\3\2\2\2\24\177\3\2\2\2\26\u0086\3\2\2\2\30\u008b")
        buf.write(u"\3\2\2\2\32\u008f\3\2\2\2\34\u00ab\3\2\2\2\36\u00c7\3")
        buf.write(u"\2\2\2 \u00d3\3\2\2\2\"\u00d8\3\2\2\2$\u00dd\3\2\2\2")
        buf.write(u"&(\7*\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*")
        buf.write(u"-\3\2\2\2+)\3\2\2\2,.\5\4\3\2-,\3\2\2\2./\3\2\2\2/-\3")
        buf.write(u"\2\2\2/\60\3\2\2\2\60\3\3\2\2\2\61\62\7\32\2\2\62\63")
        buf.write(u"\7\'\2\2\63\65\b\3\1\2\64\66\7*\2\2\65\64\3\2\2\2\66")
        buf.write(u"\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28:\3\2\2\29;\5\6")
        buf.write(u"\4\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=>\3\2\2")
        buf.write(u"\2>@\7\33\2\2?A\7*\2\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2")
        buf.write(u"BC\3\2\2\2C\5\3\2\2\2DM\5\22\n\2EM\5\24\13\2FM\5\32\16")
        buf.write(u"\2GH\5$\23\2HI\b\4\1\2IM\3\2\2\2JM\5\b\5\2KM\5\20\t\2")
        buf.write(u"LD\3\2\2\2LE\3\2\2\2LF\3\2\2\2LG\3\2\2\2LJ\3\2\2\2LK")
        buf.write(u"\3\2\2\2MO\3\2\2\2NP\7*\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2")
        buf.write(u"\2\2QR\3\2\2\2R\7\3\2\2\2SV\5\n\6\2TV\5\16\b\2US\3\2")
        buf.write(u"\2\2UT\3\2\2\2V\t\3\2\2\2WX\7\34\2\2X]\5\f\7\2YZ\7\3")
        buf.write(u"\2\2Z\\\5\f\7\2[Y\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2")
        buf.write(u"\2\2^\13\3\2\2\2_]\3\2\2\2`a\7\'\2\2ab\b\7\1\2b\r\3\2")
        buf.write(u"\2\2cd\7\34\2\2de\7\'\2\2ef\b\b\1\2fg\7\4\2\2gh\7\'\2")
        buf.write(u"\2hn\b\b\1\2ij\7\3\2\2jk\7\'\2\2km\b\b\1\2li\3\2\2\2")
        buf.write(u"mp\3\2\2\2nl\3\2\2\2no\3\2\2\2oq\3\2\2\2pn\3\2\2\2qr")
        buf.write(u"\7\5\2\2r\17\3\2\2\2st\7\31\2\2tu\7\'\2\2u\21\3\2\2\2")
        buf.write(u"vw\7\21\2\2wy\b\n\1\2xv\3\2\2\2xy\3\2\2\2yz\3\2\2\2z")
        buf.write(u"{\7\'\2\2{|\7\6\2\2|}\7\22\2\2}~\b\n\1\2~\23\3\2\2\2")
        buf.write(u"\177\u0080\5\"\22\2\u0080\u0081\7\7\2\2\u0081\u0082\5")
        buf.write(u"\26\f\2\u0082\u0083\7\6\2\2\u0083\u0084\5\30\r\2\u0084")
        buf.write(u"\u0085\b\13\1\2\u0085\25\3\2\2\2\u0086\u0087\t\2\2\2")
        buf.write(u"\u0087\27\3\2\2\2\u0088\u008c\7&\2\2\u0089\u008c\7(\2")
        buf.write(u"\2\u008a\u008c\7\'\2\2\u008b\u0088\3\2\2\2\u008b\u0089")
        buf.write(u"\3\2\2\2\u008b\u008a\3\2\2\2\u008c\31\3\2\2\2\u008d\u008e")
        buf.write(u"\7\21\2\2\u008e\u0090\b\16\1\2\u008f\u008d\3\2\2\2\u008f")
        buf.write(u"\u0090\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\7\'\2")
        buf.write(u"\2\u0092\u0093\7\6\2\2\u0093\u0094\5\34\17\2\u0094\33")
        buf.write(u"\3\2\2\2\u0095\u0096\b\17\1\2\u0096\u0099\b\17\1\2\u0097")
        buf.write(u"\u0098\7\26\2\2\u0098\u009a\b\17\1\2\u0099\u0097\3\2")
        buf.write(u"\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c")
        buf.write(u"\7(\2\2\u009c\u00ac\b\17\1\2\u009d\u00a0\b\17\1\2\u009e")
        buf.write(u"\u009f\7\26\2\2\u009f\u00a1\b\17\1\2\u00a0\u009e\3\2")
        buf.write(u"\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3")
        buf.write(u"\7&\2\2\u00a3\u00ac\b\17\1\2\u00a4\u00a5\7\'\2\2\u00a5")
        buf.write(u"\u00ac\b\17\1\2\u00a6\u00a7\7\b\2\2\u00a7\u00a8\5\34")
        buf.write(u"\17\2\u00a8\u00a9\7\t\2\2\u00a9\u00aa\b\17\1\2\u00aa")
        buf.write(u"\u00ac\3\2\2\2\u00ab\u0095\3\2\2\2\u00ab\u009d\3\2\2")
        buf.write(u"\2\u00ab\u00a4\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ac\u00b9")
        buf.write(u"\3\2\2\2\u00ad\u00ae\f\b\2\2\u00ae\u00af\t\3\2\2\u00af")
        buf.write(u"\u00b0\5\34\17\t\u00b0\u00b1\b\17\1\2\u00b1\u00b8\3\2")
        buf.write(u"\2\2\u00b2\u00b3\f\7\2\2\u00b3\u00b4\t\4\2\2\u00b4\u00b5")
        buf.write(u"\5\34\17\b\u00b5\u00b6\b\17\1\2\u00b6\u00b8\3\2\2\2\u00b7")
        buf.write(u"\u00ad\3\2\2\2\u00b7\u00b2\3\2\2\2\u00b8\u00bb\3\2\2")
        buf.write(u"\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\35\3")
        buf.write(u"\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd\b\20\1\2\u00bd")
        buf.write(u"\u00be\5\34\17\2\u00be\u00bf\t\5\2\2\u00bf\u00c0\5\34")
        buf.write(u"\17\2\u00c0\u00c1\b\20\1\2\u00c1\u00c8\3\2\2\2\u00c2")
        buf.write(u"\u00c3\7\b\2\2\u00c3\u00c4\5\36\20\2\u00c4\u00c5\7\t")
        buf.write(u"\2\2\u00c5\u00c6\b\20\1\2\u00c6\u00c8\3\2\2\2\u00c7\u00bc")
        buf.write(u"\3\2\2\2\u00c7\u00c2\3\2\2\2\u00c8\u00d0\3\2\2\2\u00c9")
        buf.write(u"\u00ca\f\3\2\2\u00ca\u00cb\t\6\2\2\u00cb\u00cc\5\36\20")
        buf.write(u"\4\u00cc\u00cd\b\20\1\2\u00cd\u00cf\3\2\2\2\u00ce\u00c9")
        buf.write(u"\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0")
        buf.write(u"\u00d1\3\2\2\2\u00d1\37\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3")
        buf.write(u"\u00d4\5\"\22\2\u00d4\u00d5\7\6\2\2\u00d5\u00d6\5\34")
        buf.write(u"\17\2\u00d6\u00d7\b\21\1\2\u00d7!\3\2\2\2\u00d8\u00db")
        buf.write(u"\7\'\2\2\u00d9\u00da\7\7\2\2\u00da\u00dc\7\'\2\2\u00db")
        buf.write(u"\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc#\3\2\2\2\u00dd")
        buf.write(u"\u00de\7\35\2\2\u00de\u00e2\5\36\20\2\u00df\u00e1\7*")
        buf.write(u"\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0")
        buf.write(u"\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4")
        buf.write(u"\u00e2\3\2\2\2\u00e5\u00e9\7\4\2\2\u00e6\u00e8\7*\2\2")
        buf.write(u"\u00e7\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7")
        buf.write(u"\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00f4\3\2\2\2\u00eb")
        buf.write(u"\u00e9\3\2\2\2\u00ec\u00ed\5 \21\2\u00ed\u00f1\b\23\1")
        buf.write(u"\2\u00ee\u00f0\7*\2\2\u00ef\u00ee\3\2\2\2\u00f0\u00f3")
        buf.write(u"\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2")
        buf.write(u"\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00ec\3\2\2")
        buf.write(u"\2\u00f5\u00f6\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7")
        buf.write(u"\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00fc\7\5\2\2\u00f9")
        buf.write(u"\u00fb\7*\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2")
        buf.write(u"\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff")
        buf.write(u"\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0126\b\23\1\2\u0100")
        buf.write(u"\u0101\7\36\2\2\u0101\u0105\5\36\20\2\u0102\u0104\7*")
        buf.write(u"\2\2\u0103\u0102\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103")
        buf.write(u"\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108\3\2\2\2\u0107")
        buf.write(u"\u0105\3\2\2\2\u0108\u010c\7\4\2\2\u0109\u010b\7*\2\2")
        buf.write(u"\u010a\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a")
        buf.write(u"\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u0117\3\2\2\2\u010e")
        buf.write(u"\u010c\3\2\2\2\u010f\u0110\5 \21\2\u0110\u0114\b\23\1")
        buf.write(u"\2\u0111\u0113\7*\2\2\u0112\u0111\3\2\2\2\u0113\u0116")
        buf.write(u"\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115")
        buf.write(u"\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u010f\3\2\2")
        buf.write(u"\2\u0118\u0119\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a")
        buf.write(u"\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011f\7\5\2\2\u011c")
        buf.write(u"\u011e\7*\2\2\u011d\u011c\3\2\2\2\u011e\u0121\3\2\2\2")
        buf.write(u"\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122")
        buf.write(u"\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0123\b\23\1\2\u0123")
        buf.write(u"\u0125\3\2\2\2\u0124\u0100\3\2\2\2\u0125\u0128\3\2\2")
        buf.write(u"\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u014b")
        buf.write(u"\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012d\7\37\2\2\u012a")
        buf.write(u"\u012c\7*\2\2\u012b\u012a\3\2\2\2\u012c\u012f\3\2\2\2")
        buf.write(u"\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130")
        buf.write(u"\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0134\7\4\2\2\u0131")
        buf.write(u"\u0133\7*\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2")
        buf.write(u"\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u013f")
        buf.write(u"\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0138\5 \21\2\u0138")
        buf.write(u"\u013c\b\23\1\2\u0139\u013b\7*\2\2\u013a\u0139\3\2\2")
        buf.write(u"\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d")
        buf.write(u"\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013f")
        buf.write(u"\u0137\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2")
        buf.write(u"\2\u0141\u0142\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145")
        buf.write(u"\7\5\2\2\u0144\u0146\7*\2\2\u0145\u0144\3\2\2\2\u0146")
        buf.write(u"\u0147\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2")
        buf.write(u"\2\u0148\u0149\3\2\2\2\u0149\u014a\b\23\1\2\u014a\u014c")
        buf.write(u"\3\2\2\2\u014b\u0129\3\2\2\2\u014b\u014c\3\2\2\2\u014c")
        buf.write(u"%\3\2\2\2()/\67<BLQU]nx\u008b\u008f\u0099\u00a0\u00ab")
        buf.write(u"\u00b7\u00b9\u00c7\u00d0\u00db\u00e2\u00e9\u00f1\u00f6")
        buf.write(u"\u00fc\u0105\u010c\u0114\u0119\u011f\u0126\u012d\u0134")
        buf.write(u"\u013c\u0141\u0147\u014b")
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
                     u"'else'", u"'units'", u"'capacity'", u"'group'", u"'string'", 
                     u"'int'", u"'float'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"LINE_COMMENT", u"T", 
                      u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", u"AND", u"OR", 
                      u"INCLUDE", u"VARDEF", u"END", u"ARRAY", u"IF", u"ELSEIF", 
                      u"ELSE", u"UNITS", u"CAPACITY", u"GROUP", u"STRING_L", 
                      u"INT_L", u"FLOAT_L", u"FLOAT", u"ID", u"INT", u"STRING", 
                      u"NL", u"WS" ]

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
    GROUP=32
    STRING_L=33
    INT_L=34
    FLOAT_L=35
    FLOAT=36
    ID=37
    INT=38
    STRING=39
    NL=40
    WS=41

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
            groupName=str((None if localctx.name is None else localctx.name.text)).lower();self.vardefName=groupName;
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.match(VarDefParser.NL)
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.field()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ARRAY) | (1 << VarDefParser.IF) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 60
            self.match(VarDefParser.END)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.match(VarDefParser.NL)
                self.state = 64 
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
        self.enterRule(localctx, 4, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 66
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 67
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 68
                self.stat()
                pass

            elif la_ == 4:
                self.state = 69
                self.if_stat()
                self.ifid=self.ifid+1;
                pass

            elif la_ == 5:
                self.state = 72
                self.new_var()
                pass

            elif la_ == 6:
                self.state = 73
                self.include()
                pass


            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.match(VarDefParser.NL)
                self.state = 79 
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
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
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
            self.state = 85
            self.match(VarDefParser.ARRAY)
            self.state = 86
            self.array_var()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 87
                self.match(VarDefParser.T__0)
                self.state = 88
                self.array_var()
                self.state = 93
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
            self.state = 94
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
            self.state = 97
            self.match(VarDefParser.ARRAY)
            self.state = 98
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 100
            self.match(VarDefParser.T__1)
            self.state = 101
            localctx.i = self.match(VarDefParser.ID)
            subvar.append(str((None if localctx.i is None else localctx.i.text)));
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 103
                self.match(VarDefParser.T__0)
                self.state = 104
                localctx.i = self.match(VarDefParser.ID)
                subvar.append(str((None if localctx.i is None else localctx.i.text)));
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
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
            self.state = 113
            self.match(VarDefParser.INCLUDE)
            self.state = 114
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
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 116
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 120
            localctx.i = self.match(VarDefParser.ID)
            self.state = 121
            self.match(VarDefParser.T__3)
            self.state = 122
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
            self.state = 125
            localctx.i = self.id2()
            self.state = 126
            self.match(VarDefParser.T__4)
            self.state = 127
            localctx.m = self.metaKey()
            self.state = 128
            self.match(VarDefParser.T__3)
            self.state = 129
            localctx.inf = self.metaValue()
            name=str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop)))).lower();mk=str((None if localctx.m is None else self._input.getText((localctx.m.start,localctx.m.stop))));c=str((None if localctx.inf is None else self._input.getText((localctx.inf.start,localctx.inf.stop))));
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
        self.enterRule(localctx, 20, self.RULE_metaKey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
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
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                localctx.i = self.match(VarDefParser.FLOAT)
                pass
            elif token in [VarDefParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(VarDefParser.INT)
                pass
            elif token in [VarDefParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
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
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 139
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 143
            localctx.i = self.match(VarDefParser.ID)
            self.state = 144
            self.match(VarDefParser.T__3)
            self.state = 145
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                s=''
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 149
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 153
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 156
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 160
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 162
                localctx.i = self.match(VarDefParser.ID)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();
                if vName in self.newArrayMap.keys() or vName in self.varPathMap.keys() or vName in self.varExprMap.keys():
                	localctx.x = self.ifsAppend+"['"+vName+"']"+"[i]"
                	#print (vName) 
                else:
                	Err.addError(vName+' not defined.', self.vardefFile, self.vardefName)

                pass

            elif la_ == 4:
                self.state = 164
                self.match(VarDefParser.T__5)
                self.state = 165
                localctx.a = self.ee(0)
                self.state = 166
                self.match(VarDefParser.T__6)
                localctx.x="("+str(localctx.a.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 181
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 171
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 172
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 173
                        localctx.b = self.ee(7)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 176
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 177
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 178
                        localctx.b = self.ee(6)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 185
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
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 187
                localctx.a = self.ee(0)
                self.state = 188
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__7) | (1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10) | (1 << VarDefParser.T__11) | (1 << VarDefParser.T__12))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 189
                localctx.b = self.ee(0)
                localctx.x=str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 192
                self.match(VarDefParser.T__5)
                self.state = 193
                localctx.c = self.compare(0)
                self.state = 194
                self.match(VarDefParser.T__6)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 206
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
                    self.state = 199
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 200
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 201
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 208
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
            self.state = 209
            localctx.i = self.id2()
            self.state = 210
            self.match(VarDefParser.T__3)
            self.state = 211
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
        self.enterRule(localctx, 32, self.RULE_id2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(VarDefParser.ID)
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 215
                self.match(VarDefParser.T__4)
                self.state = 216
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
            self.state = 219
            self.match(VarDefParser.IF)
            self.state = 220
            localctx.c = self.compare(0)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 221
                self.match(VarDefParser.NL)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self.match(VarDefParser.T__1)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 228
                self.match(VarDefParser.NL)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 234
                localctx.a = self.assign()
                t=str(localctx.a.x).lower();al.append(t)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 236
                    self.match(VarDefParser.NL)
                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 244 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 246
            self.match(VarDefParser.T__2)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 247
                    self.match(VarDefParser.NL) 
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 254
                self.match(VarDefParser.ELSEIF)
                self.state = 255
                localctx.c = self.compare(0)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 256
                    self.match(VarDefParser.NL)
                    self.state = 261
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 262
                self.match(VarDefParser.T__1)
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 263
                    self.match(VarDefParser.NL)
                    self.state = 268
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 277 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 269
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 274
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 271
                        self.match(VarDefParser.NL)
                        self.state = 276
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 279 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 281
                self.match(VarDefParser.T__2)
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 282
                        self.match(VarDefParser.NL) 
                    self.state = 287
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 295
                self.match(VarDefParser.ELSE)
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 296
                    self.match(VarDefParser.NL)
                    self.state = 301
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 302
                self.match(VarDefParser.T__1)
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 303
                    self.match(VarDefParser.NL)
                    self.state = 308
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 317 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 309
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 314
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 311
                        self.match(VarDefParser.NL)
                        self.state = 316
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 319 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 321
                self.match(VarDefParser.T__2)
                self.state = 323 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 322
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 325 
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
         




