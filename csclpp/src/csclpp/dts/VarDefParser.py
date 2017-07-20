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
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u".\u0277\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2")
        buf.write(u"\7\2H\n\2\f\2\16\2K\13\2\3\2\3\2\7\2O\n\2\f\2\16\2R\13")
        buf.write(u"\2\3\2\6\2U\n\2\r\2\16\2V\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write(u"\3\4\6\4a\n\4\r\4\16\4b\3\4\6\4f\n\4\r\4\16\4g\3\4\3")
        buf.write(u"\4\7\4l\n\4\f\4\16\4o\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\5\5z\n\5\3\5\6\5}\n\5\r\5\16\5~\3\6\3\6\3")
        buf.write(u"\6\5\6\u0084\n\6\3\7\3\7\5\7\u0088\n\7\3\b\3\b\3\b\3")
        buf.write(u"\b\3\b\7\b\u008f\n\b\f\b\16\b\u0092\13\b\3\t\3\t\3\t")
        buf.write(u"\3\t\7\t\u0098\n\t\f\t\16\t\u009b\13\t\3\n\3\n\3\n\3")
        buf.write(u"\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00a9\n\f")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u00b3\n\r\3\16\3")
        buf.write(u"\16\3\16\3\16\5\16\u00b9\n\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\5\16\u00c1\n\16\3\16\3\16\3\16\3\16\3\16\3\16\5")
        buf.write(u"\16\u00c9\n\16\3\16\3\16\7\16\u00cd\n\16\f\16\16\16\u00d0")
        buf.write(u"\13\16\3\16\3\16\3\16\3\16\3\16\5\16\u00d7\n\16\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\7\17\u00de\n\17\f\17\16\17\u00e1")
        buf.write(u"\13\17\3\20\3\20\5\20\u00e5\n\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\5\20\u00ed\n\20\3\21\3\21\5\21\u00f1\n\21")
        buf.write(u"\3\22\3\22\3\22\3\22\5\22\u00f7\n\22\3\22\3\22\3\22\3")
        buf.write(u"\22\3\22\3\22\5\22\u00ff\n\22\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\5\22\u0107\n\22\3\22\3\22\7\22\u010b\n\22\f\22")
        buf.write(u"\16\22\u010e\13\22\3\22\3\22\3\22\3\22\3\22\5\22\u0115")
        buf.write(u"\n\22\3\23\3\23\3\23\3\23\3\23\7\23\u011c\n\23\f\23\16")
        buf.write(u"\23\u011f\13\23\3\24\3\24\5\24\u0123\n\24\3\24\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\5\24\u012b\n\24\3\25\3\25\5\25\u012f")
        buf.write(u"\n\25\3\26\3\26\3\26\5\26\u0134\n\26\3\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\5\26\u013c\n\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\5\26\u0144\n\26\3\26\3\26\7\26\u0148\n\26\f\26")
        buf.write(u"\16\26\u014b\13\26\3\26\3\26\3\26\3\26\3\26\5\26\u0152")
        buf.write(u"\n\26\3\27\3\27\3\27\3\27\7\27\u0158\n\27\f\27\16\27")
        buf.write(u"\u015b\13\27\3\30\3\30\5\30\u015f\n\30\3\30\3\30\3\30")
        buf.write(u"\3\30\3\30\3\30\5\30\u0167\n\30\3\31\3\31\3\31\3\32\3")
        buf.write(u"\32\5\32\u016e\n\32\3\32\3\32\3\32\3\32\3\32\5\32\u0175")
        buf.write(u"\n\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\5\33\u0183\n\33\3\33\3\33\3\33\5\33\u0188")
        buf.write(u"\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7")
        buf.write(u"\34\u0193\n\34\f\34\16\34\u0196\13\34\3\34\3\34\3\35")
        buf.write(u"\3\35\5\35\u019c\n\35\3\35\3\35\3\35\3\35\3\35\3\35\5")
        buf.write(u"\35\u01a4\n\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write(u"\5\35\u01ae\n\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3")
        buf.write(u"\37\5\37\u01b8\n\37\3\37\3\37\3\37\3\37\3\37\5\37\u01bf")
        buf.write(u"\n\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(u"\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write(u"\5\37\u01d5\n\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(u"\37\3\37\3\37\7\37\u01e1\n\37\f\37\16\37\u01e4\13\37")
        buf.write(u"\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u01f1\n \3 \3 \3")
        buf.write(u" \3 \3 \7 \u01f8\n \f \16 \u01fb\13 \3!\3!\3!\3!\3!\3")
        buf.write(u"\"\3\"\3\"\5\"\u0205\n\"\3#\3#\3#\7#\u020a\n#\f#\16#")
        buf.write(u"\u020d\13#\3#\3#\7#\u0211\n#\f#\16#\u0214\13#\3#\3#\3")
        buf.write(u"#\7#\u0219\n#\f#\16#\u021c\13#\6#\u021e\n#\r#\16#\u021f")
        buf.write(u"\3#\3#\7#\u0224\n#\f#\16#\u0227\13#\3#\3#\3#\3#\7#\u022d")
        buf.write(u"\n#\f#\16#\u0230\13#\3#\3#\7#\u0234\n#\f#\16#\u0237\13")
        buf.write(u"#\3#\3#\3#\7#\u023c\n#\f#\16#\u023f\13#\6#\u0241\n#\r")
        buf.write(u"#\16#\u0242\3#\3#\7#\u0247\n#\f#\16#\u024a\13#\3#\3#")
        buf.write(u"\7#\u024e\n#\f#\16#\u0251\13#\3#\3#\7#\u0255\n#\f#\16")
        buf.write(u"#\u0258\13#\3#\3#\7#\u025c\n#\f#\16#\u025f\13#\3#\3#")
        buf.write(u"\3#\7#\u0264\n#\f#\16#\u0267\13#\6#\u0269\n#\r#\16#\u026a")
        buf.write(u"\3#\3#\6#\u026f\n#\r#\16#\u0270\3#\3#\5#\u0275\n#\3#")
        buf.write(u"\2\4<>$\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write(u"*,.\60\62\64\668:<>@BD\2\7\4\2))++\3\2\24\25\3\2\26\27")
        buf.write(u"\3\2\13\20\3\2\30\31\u02ac\2I\3\2\2\2\4X\3\2\2\2\6\\")
        buf.write(u"\3\2\2\2\by\3\2\2\2\n\u0083\3\2\2\2\f\u0087\3\2\2\2\16")
        buf.write(u"\u0089\3\2\2\2\20\u0093\3\2\2\2\22\u009c\3\2\2\2\24\u00a1")
        buf.write(u"\3\2\2\2\26\u00a8\3\2\2\2\30\u00b2\3\2\2\2\32\u00b4\3")
        buf.write(u"\2\2\2\34\u00d8\3\2\2\2\36\u00e4\3\2\2\2 \u00f0\3\2\2")
        buf.write(u"\2\"\u00f2\3\2\2\2$\u0116\3\2\2\2&\u0122\3\2\2\2(\u012e")
        buf.write(u"\3\2\2\2*\u0130\3\2\2\2,\u0153\3\2\2\2.\u015e\3\2\2\2")
        buf.write(u"\60\u0168\3\2\2\2\62\u016d\3\2\2\2\64\u0178\3\2\2\2\66")
        buf.write(u"\u018b\3\2\2\28\u01a3\3\2\2\2:\u01b1\3\2\2\2<\u01d4\3")
        buf.write(u"\2\2\2>\u01f0\3\2\2\2@\u01fc\3\2\2\2B\u0201\3\2\2\2D")
        buf.write(u"\u0206\3\2\2\2FH\7-\2\2GF\3\2\2\2HK\3\2\2\2IG\3\2\2\2")
        buf.write(u"IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LP\5\4\3\2MO\7-\2\2NM\3")
        buf.write(u"\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QT\3\2\2\2RP\3\2")
        buf.write(u"\2\2SU\5\6\4\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2")
        buf.write(u"\2W\3\3\2\2\2XY\7\32\2\2YZ\7*\2\2Z[\b\3\1\2[\5\3\2\2")
        buf.write(u"\2\\]\7\34\2\2]^\7*\2\2^`\b\4\1\2_a\7-\2\2`_\3\2\2\2")
        buf.write(u"ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2ce\3\2\2\2df\5\b\5\2ed")
        buf.write(u"\3\2\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2im\7")
        buf.write(u"\35\2\2jl\7-\2\2kj\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2")
        buf.write(u"\2\2n\7\3\2\2\2om\3\2\2\2pz\5\62\32\2qz\5\64\33\2rz\5")
        buf.write(u"\26\f\2st\5D#\2tu\b\5\1\2uz\3\2\2\2vz\5\n\6\2wz\5\60")
        buf.write(u"\31\2xz\5\f\7\2yp\3\2\2\2yq\3\2\2\2yr\3\2\2\2ys\3\2\2")
        buf.write(u"\2yv\3\2\2\2yw\3\2\2\2yx\3\2\2\2z|\3\2\2\2{}\7-\2\2|")
        buf.write(u"{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\t\3\2")
        buf.write(u"\2\2\u0080\u0084\5\30\r\2\u0081\u0084\5 \21\2\u0082\u0084")
        buf.write(u"\5(\25\2\u0083\u0080\3\2\2\2\u0083\u0081\3\2\2\2\u0083")
        buf.write(u"\u0082\3\2\2\2\u0084\13\3\2\2\2\u0085\u0088\5\20\t\2")
        buf.write(u"\u0086\u0088\5\16\b\2\u0087\u0085\3\2\2\2\u0087\u0086")
        buf.write(u"\3\2\2\2\u0088\r\3\2\2\2\u0089\u008a\7$\2\2\u008a\u008b")
        buf.write(u"\7&\2\2\u008b\u0090\5\24\13\2\u008c\u008d\7\3\2\2\u008d")
        buf.write(u"\u008f\5\24\13\2\u008e\u008c\3\2\2\2\u008f\u0092\3\2")
        buf.write(u"\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\17")
        buf.write(u"\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094\7&\2\2\u0094")
        buf.write(u"\u0099\5\22\n\2\u0095\u0096\7\3\2\2\u0096\u0098\5\22")
        buf.write(u"\n\2\u0097\u0095\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097")
        buf.write(u"\3\2\2\2\u0099\u009a\3\2\2\2\u009a\21\3\2\2\2\u009b\u0099")
        buf.write(u"\3\2\2\2\u009c\u009d\7*\2\2\u009d\u009e\7\4\2\2\u009e")
        buf.write(u"\u009f\5<\37\2\u009f\u00a0\b\n\1\2\u00a0\23\3\2\2\2\u00a1")
        buf.write(u"\u00a2\7*\2\2\u00a2\u00a3\7\4\2\2\u00a3\u00a4\5<\37\2")
        buf.write(u"\u00a4\u00a5\b\13\1\2\u00a5\25\3\2\2\2\u00a6\u00a7\7")
        buf.write(u"\22\2\2\u00a7\u00a9\b\f\1\2\u00a8\u00a6\3\2\2\2\u00a8")
        buf.write(u"\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\7*\2\2")
        buf.write(u"\u00ab\u00ac\b\f\1\2\u00ac\u00ad\7\4\2\2\u00ad\u00ae")
        buf.write(u"\5<\37\2\u00ae\u00af\b\f\1\2\u00af\27\3\2\2\2\u00b0\u00b3")
        buf.write(u"\5\32\16\2\u00b1\u00b3\5\34\17\2\u00b2\u00b0\3\2\2\2")
        buf.write(u"\u00b2\u00b1\3\2\2\2\u00b3\31\3\2\2\2\u00b4\u00b5\7#")
        buf.write(u"\2\2\u00b5\u00b8\7\36\2\2\u00b6\u00b7\7\22\2\2\u00b7")
        buf.write(u"\u00b9\b\16\1\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2")
        buf.write(u"\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\7*\2\2\u00bb\u00bc")
        buf.write(u"\b\16\1\2\u00bc\u00bd\7\5\2\2\u00bd\u00c0\b\16\1\2\u00be")
        buf.write(u"\u00bf\7\22\2\2\u00bf\u00c1\b\16\1\2\u00c0\u00be\3\2")
        buf.write(u"\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3")
        buf.write(u"\7*\2\2\u00c3\u00ce\b\16\1\2\u00c4\u00c5\7\3\2\2\u00c5")
        buf.write(u"\u00c8\b\16\1\2\u00c6\u00c7\7\22\2\2\u00c7\u00c9\b\16")
        buf.write(u"\1\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca")
        buf.write(u"\3\2\2\2\u00ca\u00cb\7*\2\2\u00cb\u00cd\b\16\1\2\u00cc")
        buf.write(u"\u00c4\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2")
        buf.write(u"\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce")
        buf.write(u"\3\2\2\2\u00d1\u00d6\7\6\2\2\u00d2\u00d3\7\4\2\2\u00d3")
        buf.write(u"\u00d4\5<\37\2\u00d4\u00d5\b\16\1\2\u00d5\u00d7\3\2\2")
        buf.write(u"\2\u00d6\u00d2\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\33\3")
        buf.write(u"\2\2\2\u00d8\u00d9\7#\2\2\u00d9\u00da\7\36\2\2\u00da")
        buf.write(u"\u00df\5\36\20\2\u00db\u00dc\7\3\2\2\u00dc\u00de\5\36")
        buf.write(u"\20\2\u00dd\u00db\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd")
        buf.write(u"\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\35\3\2\2\2\u00e1\u00df")
        buf.write(u"\3\2\2\2\u00e2\u00e3\7\22\2\2\u00e3\u00e5\b\20\1\2\u00e4")
        buf.write(u"\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\3\2\2")
        buf.write(u"\2\u00e6\u00e7\7*\2\2\u00e7\u00ec\b\20\1\2\u00e8\u00e9")
        buf.write(u"\7\4\2\2\u00e9\u00ea\5<\37\2\u00ea\u00eb\b\20\1\2\u00eb")
        buf.write(u"\u00ed\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ec\u00ed\3\2\2")
        buf.write(u"\2\u00ed\37\3\2\2\2\u00ee\u00f1\5\"\22\2\u00ef\u00f1")
        buf.write(u"\5$\23\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1")
        buf.write(u"!\3\2\2\2\u00f2\u00f3\7$\2\2\u00f3\u00f6\7\36\2\2\u00f4")
        buf.write(u"\u00f5\7\22\2\2\u00f5\u00f7\b\22\1\2\u00f6\u00f4\3\2")
        buf.write(u"\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9")
        buf.write(u"\7*\2\2\u00f9\u00fa\b\22\1\2\u00fa\u00fb\7\5\2\2\u00fb")
        buf.write(u"\u00fe\b\22\1\2\u00fc\u00fd\7\22\2\2\u00fd\u00ff\b\22")
        buf.write(u"\1\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100")
        buf.write(u"\3\2\2\2\u0100\u0101\7*\2\2\u0101\u010c\b\22\1\2\u0102")
        buf.write(u"\u0103\7\3\2\2\u0103\u0106\b\22\1\2\u0104\u0105\7\22")
        buf.write(u"\2\2\u0105\u0107\b\22\1\2\u0106\u0104\3\2\2\2\u0106\u0107")
        buf.write(u"\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\7*\2\2\u0109")
        buf.write(u"\u010b\b\22\1\2\u010a\u0102\3\2\2\2\u010b\u010e\3\2\2")
        buf.write(u"\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010f")
        buf.write(u"\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0114\7\6\2\2\u0110")
        buf.write(u"\u0111\7\4\2\2\u0111\u0112\5<\37\2\u0112\u0113\b\22\1")
        buf.write(u"\2\u0113\u0115\3\2\2\2\u0114\u0110\3\2\2\2\u0114\u0115")
        buf.write(u"\3\2\2\2\u0115#\3\2\2\2\u0116\u0117\7$\2\2\u0117\u0118")
        buf.write(u"\7\36\2\2\u0118\u011d\5&\24\2\u0119\u011a\7\3\2\2\u011a")
        buf.write(u"\u011c\5&\24\2\u011b\u0119\3\2\2\2\u011c\u011f\3\2\2")
        buf.write(u"\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e%\3\2")
        buf.write(u"\2\2\u011f\u011d\3\2\2\2\u0120\u0121\7\22\2\2\u0121\u0123")
        buf.write(u"\b\24\1\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write(u"\u0124\3\2\2\2\u0124\u0125\7*\2\2\u0125\u012a\b\24\1")
        buf.write(u"\2\u0126\u0127\7\4\2\2\u0127\u0128\5<\37\2\u0128\u0129")
        buf.write(u"\b\24\1\2\u0129\u012b\3\2\2\2\u012a\u0126\3\2\2\2\u012a")
        buf.write(u"\u012b\3\2\2\2\u012b\'\3\2\2\2\u012c\u012f\5*\26\2\u012d")
        buf.write(u"\u012f\5,\27\2\u012e\u012c\3\2\2\2\u012e\u012d\3\2\2")
        buf.write(u"\2\u012f)\3\2\2\2\u0130\u0133\7\36\2\2\u0131\u0132\7")
        buf.write(u"\22\2\2\u0132\u0134\b\26\1\2\u0133\u0131\3\2\2\2\u0133")
        buf.write(u"\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\7*\2\2")
        buf.write(u"\u0136\u0137\b\26\1\2\u0137\u0138\7\5\2\2\u0138\u013b")
        buf.write(u"\b\26\1\2\u0139\u013a\7\22\2\2\u013a\u013c\b\26\1\2\u013b")
        buf.write(u"\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2")
        buf.write(u"\2\u013d\u013e\7*\2\2\u013e\u0149\b\26\1\2\u013f\u0140")
        buf.write(u"\7\3\2\2\u0140\u0143\b\26\1\2\u0141\u0142\7\22\2\2\u0142")
        buf.write(u"\u0144\b\26\1\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2")
        buf.write(u"\2\u0144\u0145\3\2\2\2\u0145\u0146\7*\2\2\u0146\u0148")
        buf.write(u"\b\26\1\2\u0147\u013f\3\2\2\2\u0148\u014b\3\2\2\2\u0149")
        buf.write(u"\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014c\3\2\2")
        buf.write(u"\2\u014b\u0149\3\2\2\2\u014c\u0151\7\6\2\2\u014d\u014e")
        buf.write(u"\7\4\2\2\u014e\u014f\5<\37\2\u014f\u0150\b\26\1\2\u0150")
        buf.write(u"\u0152\3\2\2\2\u0151\u014d\3\2\2\2\u0151\u0152\3\2\2")
        buf.write(u"\2\u0152+\3\2\2\2\u0153\u0154\7\36\2\2\u0154\u0159\5")
        buf.write(u".\30\2\u0155\u0156\7\3\2\2\u0156\u0158\5.\30\2\u0157")
        buf.write(u"\u0155\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2")
        buf.write(u"\2\u0159\u015a\3\2\2\2\u015a-\3\2\2\2\u015b\u0159\3\2")
        buf.write(u"\2\2\u015c\u015d\7\22\2\2\u015d\u015f\b\30\1\2\u015e")
        buf.write(u"\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2")
        buf.write(u"\2\u0160\u0161\7*\2\2\u0161\u0166\b\30\1\2\u0162\u0163")
        buf.write(u"\7\4\2\2\u0163\u0164\5<\37\2\u0164\u0165\b\30\1\2\u0165")
        buf.write(u"\u0167\3\2\2\2\u0166\u0162\3\2\2\2\u0166\u0167\3\2\2")
        buf.write(u"\2\u0167/\3\2\2\2\u0168\u0169\7\33\2\2\u0169\u016a\7")
        buf.write(u"*\2\2\u016a\61\3\2\2\2\u016b\u016c\7\22\2\2\u016c\u016e")
        buf.write(u"\b\32\1\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write(u"\u016f\3\2\2\2\u016f\u0170\7*\2\2\u0170\u0171\7\4\2\2")
        buf.write(u"\u0171\u0174\7\23\2\2\u0172\u0173\7\3\2\2\u0173\u0175")
        buf.write(u"\7,\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write(u"\u0176\3\2\2\2\u0176\u0177\b\32\1\2\u0177\63\3\2\2\2")
        buf.write(u"\u0178\u0179\5B\"\2\u0179\u017a\7\7\2\2\u017a\u017b\7")
        buf.write(u"*\2\2\u017b\u0187\7\4\2\2\u017c\u017d\7)\2\2\u017d\u0183")
        buf.write(u"\b\33\1\2\u017e\u017f\7+\2\2\u017f\u0183\b\33\1\2\u0180")
        buf.write(u"\u0181\7,\2\2\u0181\u0183\b\33\1\2\u0182\u017c\3\2\2")
        buf.write(u"\2\u0182\u017e\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0188")
        buf.write(u"\3\2\2\2\u0184\u0185\5\66\34\2\u0185\u0186\b\33\1\2\u0186")
        buf.write(u"\u0188\3\2\2\2\u0187\u0182\3\2\2\2\u0187\u0184\3\2\2")
        buf.write(u"\2\u0188\u0189\3\2\2\2\u0189\u018a\b\33\1\2\u018a\65")
        buf.write(u"\3\2\2\2\u018b\u018c\7\5\2\2\u018c\u018d\58\35\2\u018d")
        buf.write(u"\u0194\b\34\1\2\u018e\u018f\7\3\2\2\u018f\u0190\58\35")
        buf.write(u"\2\u0190\u0191\b\34\1\2\u0191\u0193\3\2\2\2\u0192\u018e")
        buf.write(u"\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0194")
        buf.write(u"\u0195\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u0194\3\2\2")
        buf.write(u"\2\u0197\u0198\7\6\2\2\u0198\67\3\2\2\2\u0199\u019c\7")
        buf.write(u"*\2\2\u019a\u019c\7(\2\2\u019b\u0199\3\2\2\2\u019b\u019a")
        buf.write(u"\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u01a4\b\35\1\2\u019e")
        buf.write(u"\u019f\7,\2\2\u019f\u01a4\b\35\1\2\u01a0\u01a1\5:\36")
        buf.write(u"\2\u01a1\u01a2\b\35\1\2\u01a2\u01a4\3\2\2\2\u01a3\u019b")
        buf.write(u"\3\2\2\2\u01a3\u019e\3\2\2\2\u01a3\u01a0\3\2\2\2\u01a4")
        buf.write(u"\u01a5\3\2\2\2\u01a5\u01ad\7\b\2\2\u01a6\u01a7\7*\2\2")
        buf.write(u"\u01a7\u01ae\b\35\1\2\u01a8\u01a9\7,\2\2\u01a9\u01ae")
        buf.write(u"\b\35\1\2\u01aa\u01ab\5:\36\2\u01ab\u01ac\b\35\1\2\u01ac")
        buf.write(u"\u01ae\3\2\2\2\u01ad\u01a6\3\2\2\2\u01ad\u01a8\3\2\2")
        buf.write(u"\2\u01ad\u01aa\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0")
        buf.write(u"\b\35\1\2\u01b09\3\2\2\2\u01b1\u01b2\t\2\2\2\u01b2;\3")
        buf.write(u"\2\2\2\u01b3\u01b4\b\37\1\2\u01b4\u01b7\b\37\1\2\u01b5")
        buf.write(u"\u01b6\7\27\2\2\u01b6\u01b8\b\37\1\2\u01b7\u01b5\3\2")
        buf.write(u"\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba")
        buf.write(u"\7+\2\2\u01ba\u01d5\b\37\1\2\u01bb\u01be\b\37\1\2\u01bc")
        buf.write(u"\u01bd\7\27\2\2\u01bd\u01bf\b\37\1\2\u01be\u01bc\3\2")
        buf.write(u"\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1")
        buf.write(u"\7)\2\2\u01c1\u01d5\b\37\1\2\u01c2\u01c3\7\'\2\2\u01c3")
        buf.write(u"\u01d5\b\37\1\2\u01c4\u01c5\7(\2\2\u01c5\u01d5\b\37\1")
        buf.write(u"\2\u01c6\u01c7\7*\2\2\u01c7\u01d5\b\37\1\2\u01c8\u01c9")
        buf.write(u"\7*\2\2\u01c9\u01ca\7\7\2\2\u01ca\u01cb\7*\2\2\u01cb")
        buf.write(u"\u01cc\3\2\2\2\u01cc\u01d5\b\37\1\2\u01cd\u01ce\7\t\2")
        buf.write(u"\2\u01ce\u01cf\5<\37\2\u01cf\u01d0\7\n\2\2\u01d0\u01d1")
        buf.write(u"\b\37\1\2\u01d1\u01d5\3\2\2\2\u01d2\u01d3\7,\2\2\u01d3")
        buf.write(u"\u01d5\b\37\1\2\u01d4\u01b3\3\2\2\2\u01d4\u01bb\3\2\2")
        buf.write(u"\2\u01d4\u01c2\3\2\2\2\u01d4\u01c4\3\2\2\2\u01d4\u01c6")
        buf.write(u"\3\2\2\2\u01d4\u01c8\3\2\2\2\u01d4\u01cd\3\2\2\2\u01d4")
        buf.write(u"\u01d2\3\2\2\2\u01d5\u01e2\3\2\2\2\u01d6\u01d7\f\f\2")
        buf.write(u"\2\u01d7\u01d8\t\3\2\2\u01d8\u01d9\5<\37\r\u01d9\u01da")
        buf.write(u"\b\37\1\2\u01da\u01e1\3\2\2\2\u01db\u01dc\f\13\2\2\u01dc")
        buf.write(u"\u01dd\t\4\2\2\u01dd\u01de\5<\37\f\u01de\u01df\b\37\1")
        buf.write(u"\2\u01df\u01e1\3\2\2\2\u01e0\u01d6\3\2\2\2\u01e0\u01db")
        buf.write(u"\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write(u"\u01e3\3\2\2\2\u01e3=\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5")
        buf.write(u"\u01e6\b \1\2\u01e6\u01e7\5<\37\2\u01e7\u01e8\t\5\2\2")
        buf.write(u"\u01e8\u01e9\5<\37\2\u01e9\u01ea\b \1\2\u01ea\u01f1\3")
        buf.write(u"\2\2\2\u01eb\u01ec\7\t\2\2\u01ec\u01ed\5> \2\u01ed\u01ee")
        buf.write(u"\7\n\2\2\u01ee\u01ef\b \1\2\u01ef\u01f1\3\2\2\2\u01f0")
        buf.write(u"\u01e5\3\2\2\2\u01f0\u01eb\3\2\2\2\u01f1\u01f9\3\2\2")
        buf.write(u"\2\u01f2\u01f3\f\3\2\2\u01f3\u01f4\t\6\2\2\u01f4\u01f5")
        buf.write(u"\5> \4\u01f5\u01f6\b \1\2\u01f6\u01f8\3\2\2\2\u01f7\u01f2")
        buf.write(u"\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9")
        buf.write(u"\u01fa\3\2\2\2\u01fa?\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc")
        buf.write(u"\u01fd\5B\"\2\u01fd\u01fe\7\4\2\2\u01fe\u01ff\5<\37\2")
        buf.write(u"\u01ff\u0200\b!\1\2\u0200A\3\2\2\2\u0201\u0204\7*\2\2")
        buf.write(u"\u0202\u0203\7\7\2\2\u0203\u0205\7*\2\2\u0204\u0202\3")
        buf.write(u"\2\2\2\u0204\u0205\3\2\2\2\u0205C\3\2\2\2\u0206\u0207")
        buf.write(u"\7\37\2\2\u0207\u020b\5> \2\u0208\u020a\7-\2\2\u0209")
        buf.write(u"\u0208\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2")
        buf.write(u"\2\u020b\u020c\3\2\2\2\u020c\u020e\3\2\2\2\u020d\u020b")
        buf.write(u"\3\2\2\2\u020e\u0212\7\5\2\2\u020f\u0211\7-\2\2\u0210")
        buf.write(u"\u020f\3\2\2\2\u0211\u0214\3\2\2\2\u0212\u0210\3\2\2")
        buf.write(u"\2\u0212\u0213\3\2\2\2\u0213\u021d\3\2\2\2\u0214\u0212")
        buf.write(u"\3\2\2\2\u0215\u0216\5@!\2\u0216\u021a\b#\1\2\u0217\u0219")
        buf.write(u"\7-\2\2\u0218\u0217\3\2\2\2\u0219\u021c\3\2\2\2\u021a")
        buf.write(u"\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021e\3\2\2")
        buf.write(u"\2\u021c\u021a\3\2\2\2\u021d\u0215\3\2\2\2\u021e\u021f")
        buf.write(u"\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220")
        buf.write(u"\u0221\3\2\2\2\u0221\u0225\7\6\2\2\u0222\u0224\7-\2\2")
        buf.write(u"\u0223\u0222\3\2\2\2\u0224\u0227\3\2\2\2\u0225\u0223")
        buf.write(u"\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0228\3\2\2\2\u0227")
        buf.write(u"\u0225\3\2\2\2\u0228\u024f\b#\1\2\u0229\u022a\7 \2\2")
        buf.write(u"\u022a\u022e\5> \2\u022b\u022d\7-\2\2\u022c\u022b\3\2")
        buf.write(u"\2\2\u022d\u0230\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022f")
        buf.write(u"\3\2\2\2\u022f\u0231\3\2\2\2\u0230\u022e\3\2\2\2\u0231")
        buf.write(u"\u0235\7\5\2\2\u0232\u0234\7-\2\2\u0233\u0232\3\2\2\2")
        buf.write(u"\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236")
        buf.write(u"\3\2\2\2\u0236\u0240\3\2\2\2\u0237\u0235\3\2\2\2\u0238")
        buf.write(u"\u0239\5@!\2\u0239\u023d\b#\1\2\u023a\u023c\7-\2\2\u023b")
        buf.write(u"\u023a\3\2\2\2\u023c\u023f\3\2\2\2\u023d\u023b\3\2\2")
        buf.write(u"\2\u023d\u023e\3\2\2\2\u023e\u0241\3\2\2\2\u023f\u023d")
        buf.write(u"\3\2\2\2\u0240\u0238\3\2\2\2\u0241\u0242\3\2\2\2\u0242")
        buf.write(u"\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0244\3\2\2")
        buf.write(u"\2\u0244\u0248\7\6\2\2\u0245\u0247\7-\2\2\u0246\u0245")
        buf.write(u"\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0248")
        buf.write(u"\u0249\3\2\2\2\u0249\u024b\3\2\2\2\u024a\u0248\3\2\2")
        buf.write(u"\2\u024b\u024c\b#\1\2\u024c\u024e\3\2\2\2\u024d\u0229")
        buf.write(u"\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f")
        buf.write(u"\u0250\3\2\2\2\u0250\u0274\3\2\2\2\u0251\u024f\3\2\2")
        buf.write(u"\2\u0252\u0256\7!\2\2\u0253\u0255\7-\2\2\u0254\u0253")
        buf.write(u"\3\2\2\2\u0255\u0258\3\2\2\2\u0256\u0254\3\2\2\2\u0256")
        buf.write(u"\u0257\3\2\2\2\u0257\u0259\3\2\2\2\u0258\u0256\3\2\2")
        buf.write(u"\2\u0259\u025d\7\5\2\2\u025a\u025c\7-\2\2\u025b\u025a")
        buf.write(u"\3\2\2\2\u025c\u025f\3\2\2\2\u025d\u025b\3\2\2\2\u025d")
        buf.write(u"\u025e\3\2\2\2\u025e\u0268\3\2\2\2\u025f\u025d\3\2\2")
        buf.write(u"\2\u0260\u0261\5@!\2\u0261\u0265\b#\1\2\u0262\u0264\7")
        buf.write(u"-\2\2\u0263\u0262\3\2\2\2\u0264\u0267\3\2\2\2\u0265\u0263")
        buf.write(u"\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0269\3\2\2\2\u0267")
        buf.write(u"\u0265\3\2\2\2\u0268\u0260\3\2\2\2\u0269\u026a\3\2\2")
        buf.write(u"\2\u026a\u0268\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u026c")
        buf.write(u"\3\2\2\2\u026c\u026e\7\6\2\2\u026d\u026f\7-\2\2\u026e")
        buf.write(u"\u026d\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u026e\3\2\2")
        buf.write(u"\2\u0270\u0271\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u0273")
        buf.write(u"\b#\1\2\u0273\u0275\3\2\2\2\u0274\u0252\3\2\2\2\u0274")
        buf.write(u"\u0275\3\2\2\2\u0275E\3\2\2\2KIPVbgmy~\u0083\u0087\u0090")
        buf.write(u"\u0099\u00a8\u00b2\u00b8\u00c0\u00c8\u00ce\u00d6\u00df")
        buf.write(u"\u00e4\u00ec\u00f0\u00f6\u00fe\u0106\u010c\u0114\u011d")
        buf.write(u"\u0122\u012a\u012e\u0133\u013b\u0143\u0149\u0151\u0159")
        buf.write(u"\u015e\u0166\u016d\u0174\u0182\u0187\u0194\u019b\u01a3")
        buf.write(u"\u01ad\u01b7\u01be\u01d4\u01e0\u01e2\u01f0\u01f9\u0204")
        buf.write(u"\u020b\u0212\u021a\u021f\u0225\u022e\u0235\u023d\u0242")
        buf.write(u"\u0248\u024f\u0256\u025d\u0265\u026a\u0270\u0274")
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
                     u"'use'", u"'include'", u"'dt'", u"'end'", u"'array'", 
                     u"'if'", u"'elseif'", u"'else'", u"'group'", u"'str'", 
                     u"'int'", u"'float'", u"'const'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"LINE_COMMENT", 
                      u"T", u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", u"AND", 
                      u"OR", u"USE", u"INCLUDE", u"VARDEF", u"END", u"ARRAY", 
                      u"IF", u"ELSEIF", u"ELSE", u"GROUP", u"STR_L", u"INT_L", 
                      u"FLOAT_L", u"CONST", u"SYSARRAY", u"SYSCONST", u"FLOAT", 
                      u"ID", u"INT", u"STRING", u"NL", u"WS" ]

    RULE_prog = 0
    RULE_use = 1
    RULE_vardef = 2
    RULE_field = 3
    RULE_new_var = 4
    RULE_constant = 5
    RULE_intConst = 6
    RULE_floatConst = 7
    RULE_floatConstVar = 8
    RULE_intConstVar = 9
    RULE_stat = 10
    RULE_strArray = 11
    RULE_strArrayCluster = 12
    RULE_strArrayLone = 13
    RULE_strArrayVar = 14
    RULE_intArray = 15
    RULE_intArrayCluster = 16
    RULE_intArrayLone = 17
    RULE_intArrayVar = 18
    RULE_floatArray = 19
    RULE_floatArrayCluster = 20
    RULE_floatArrayLone = 21
    RULE_floatArrayVar = 22
    RULE_include = 23
    RULE_var_path = 24
    RULE_var_meta = 25
    RULE_metaDict = 26
    RULE_dict_pair = 27
    RULE_number = 28
    RULE_ee = 29
    RULE_compare = 30
    RULE_assign = 31
    RULE_id2 = 32
    RULE_if_stat = 33

    ruleNames =  [ u"prog", u"use", u"vardef", u"field", u"new_var", u"constant", 
                   u"intConst", u"floatConst", u"floatConstVar", u"intConstVar", 
                   u"stat", u"strArray", u"strArrayCluster", u"strArrayLone", 
                   u"strArrayVar", u"intArray", u"intArrayCluster", u"intArrayLone", 
                   u"intArrayVar", u"floatArray", u"floatArrayCluster", 
                   u"floatArrayLone", u"floatArrayVar", u"include", u"var_path", 
                   u"var_meta", u"metaDict", u"dict_pair", u"number", u"ee", 
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
    STR_L=33
    INT_L=34
    FLOAT_L=35
    CONST=36
    SYSARRAY=37
    SYSCONST=38
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

    tempVarGroupList={};
    ifsMapGroupMap={};
    strArrayGroupMap={};
    intArrayGroupMap={};
    floatArrayGroupMap={};
    constGroupMap={};
    varPathMap=collections.OrderedDict();
    allVarsGroupList={}

    tempVarList=[];
    strArrayMap=collections.OrderedDict();
    intArrayMap=collections.OrderedDict();
    floatArrayMap=collections.OrderedDict();
    constMap=collections.OrderedDict();
    ifsMap=collections.OrderedDict(); # (if statement ID, (condition, assignments)) 
    vardefName='';
    vardefFile='';
    vardefDefault='';
    systemVars=['year','month','oct','nov','dec','jan','feb','mar','apr','may','jun','jul','aug','sep'];
    systemConstMap=collections.OrderedDict();
    allVars=[];

    def isConst(self, name):
    	if name in self.constMap.keys():
    		return True
    	else:
    		return False

    def checkDup(self, name):
    	if name in self.allVars:
    		msg=name+' is already defined.'
    		Err.addError(msg, self.vardefFile, self.vardefName)
    	else:
    		self.allVars.append(name)
    		
    def checkExist(self, name):
    	if name not in self.allVars:
    		msg=name+' is not defined.'
    		Err.addError(msg, self.vardefFile, self.vardefName)
    		


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

        self.tempVarGroupList={};
        self.ifsMapGroupMap={};
        self.strArrayGroupMap={};
        self.intArrayGroupMap={};
        self.floatArrayGroupMap={};
        self.constGroupMap={};
        self.allVarsGroupList={};
        self.ifid=0;

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 68
                self.match(VarDefParser.NL)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.use()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 75
                self.match(VarDefParser.NL)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.vardef()
                self.state = 84 
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
            self.state = 86
            self.match(VarDefParser.USE)
            self.state = 87
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

        self.tempVarList=[];
        self.ifsMap=collections.OrderedDict();
        self.strArrayMap=collections.OrderedDict();
        self.intArrayMap=collections.OrderedDict();
        self.floatArrayMap=collections.OrderedDict();
        self.constMap=self.systemConstMap;
        self.allVars=self.systemVars[:];

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(VarDefParser.VARDEF)
            self.state = 91
            localctx.name = self.match(VarDefParser.ID)
            groupName=str((None if localctx.name is None else localctx.name.text)).lower();self.vardefName=groupName;
            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.match(VarDefParser.NL)
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.field()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ARRAY) | (1 << VarDefParser.IF) | (1 << VarDefParser.STR_L) | (1 << VarDefParser.INT_L) | (1 << VarDefParser.CONST) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 103
            self.match(VarDefParser.END)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 104
                self.match(VarDefParser.NL)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self._ctx.stop = self._input.LT(-1)

            self.varPathGroupMap[groupName]=self.varPathMap;

            self.tempVarGroupList[groupName]=self.tempVarList;	
            self.ifsMapGroupMap[groupName]=self.ifsMap;
            self.strArrayGroupMap[groupName]=self.strArrayMap;
            self.intArrayGroupMap[groupName]=self.intArrayMap;
            self.floatArrayGroupMap[groupName]=self.floatArrayMap;
            self.constGroupMap[groupName]=self.constMap;
            self.allVarsGroupList[groupName]=self.allVars;
            #print(groupName, self.allVars)

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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 110
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 111
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 112
                self.stat()
                pass

            elif la_ == 4:
                self.state = 113
                self.if_stat()
                self.ifid=self.ifid+1;
                pass

            elif la_ == 5:
                self.state = 116
                self.new_var()
                pass

            elif la_ == 6:
                self.state = 117
                self.include()
                pass

            elif la_ == 7:
                self.state = 118
                self.constant()
                pass


            self.state = 122 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 121
                self.match(VarDefParser.NL)
                self.state = 124 
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

        def strArray(self):
            return self.getTypedRuleContext(VarDefParser.StrArrayContext,0)


        def intArray(self):
            return self.getTypedRuleContext(VarDefParser.IntArrayContext,0)


        def floatArray(self):
            return self.getTypedRuleContext(VarDefParser.FloatArrayContext,0)


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
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.STR_L]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.strArray()
                pass
            elif token in [VarDefParser.INT_L]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.intArray()
                pass
            elif token in [VarDefParser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.floatArray()
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

    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.ConstantContext, self).__init__(parent, invokingState)
            self.parser = parser

        def floatConst(self):
            return self.getTypedRuleContext(VarDefParser.FloatConstContext,0)


        def intConst(self):
            return self.getTypedRuleContext(VarDefParser.IntConstContext,0)


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
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.floatConst()
                pass
            elif token in [VarDefParser.INT_L]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.intConst()
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

    class IntConstContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.IntConstContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT_L(self):
            return self.getToken(VarDefParser.INT_L, 0)

        def CONST(self):
            return self.getToken(VarDefParser.CONST, 0)

        def intConstVar(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.IntConstVarContext)
            else:
                return self.getTypedRuleContext(VarDefParser.IntConstVarContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_intConst

        def accept(self, visitor):
            if hasattr(visitor, "visitIntConst"):
                return visitor.visitIntConst(self)
            else:
                return visitor.visitChildren(self)




    def intConst(self):

        localctx = VarDefParser.IntConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_intConst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(VarDefParser.INT_L)
            self.state = 136
            self.match(VarDefParser.CONST)
            self.state = 137
            self.intConstVar()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 138
                self.match(VarDefParser.T__0)
                self.state = 139
                self.intConstVar()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FloatConstContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.FloatConstContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(VarDefParser.CONST, 0)

        def floatConstVar(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.FloatConstVarContext)
            else:
                return self.getTypedRuleContext(VarDefParser.FloatConstVarContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_floatConst

        def accept(self, visitor):
            if hasattr(visitor, "visitFloatConst"):
                return visitor.visitFloatConst(self)
            else:
                return visitor.visitChildren(self)




    def floatConst(self):

        localctx = VarDefParser.FloatConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_floatConst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(VarDefParser.CONST)
            self.state = 146
            self.floatConstVar()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 147
                self.match(VarDefParser.T__0)
                self.state = 148
                self.floatConstVar()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FloatConstVarContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.FloatConstVarContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.e = None # EeContext

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_floatConstVar

        def accept(self, visitor):
            if hasattr(visitor, "visitFloatConstVar"):
                return visitor.visitFloatConstVar(self)
            else:
                return visitor.visitChildren(self)




    def floatConstVar(self):

        localctx = VarDefParser.FloatConstVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_floatConstVar)
        v = Var('');
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            localctx.i = self.match(VarDefParser.ID)
            self.state = 155
            self.match(VarDefParser.T__1)
            self.state = 156
            localctx.e = self.ee(0)
            name=str((None if localctx.i is None else localctx.i.text)).lower();
            self.checkDup(name);
            v.const='('+str(localctx.e.x)+')';v.metaData['_dataType']=np.float;
            self.constMap[name]=v;

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntConstVarContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.IntConstVarContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.e = None # EeContext

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_intConstVar

        def accept(self, visitor):
            if hasattr(visitor, "visitIntConstVar"):
                return visitor.visitIntConstVar(self)
            else:
                return visitor.visitChildren(self)




    def intConstVar(self):

        localctx = VarDefParser.IntConstVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_intConstVar)
        v = Var('');
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            localctx.i = self.match(VarDefParser.ID)
            self.state = 160
            self.match(VarDefParser.T__1)
            self.state = 161
            localctx.e = self.ee(0)
            name=str((None if localctx.i is None else localctx.i.text)).lower();
            self.checkDup(name);
            v.const='int('+str(localctx.e.x)+')';v.metaData['_dataType']=np.int;
            self.constMap[name]=v;

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
        self.enterRule(localctx, 20, self.RULE_stat)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 164
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 168
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();self.checkExist(name);
            self.state = 170
            self.match(VarDefParser.T__1)
            self.state = 171
            localctx.e = self.ee(0)
            e2=str(localctx.e.x).lower()
            name2=self.ifsAppend+"['"+str((None if localctx.i is None else localctx.i.text)).lower()+"'][i]"
            k='!'+name2+'='+e2;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StrArrayContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.StrArrayContext, self).__init__(parent, invokingState)
            self.parser = parser

        def strArrayCluster(self):
            return self.getTypedRuleContext(VarDefParser.StrArrayClusterContext,0)


        def strArrayLone(self):
            return self.getTypedRuleContext(VarDefParser.StrArrayLoneContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_strArray

        def accept(self, visitor):
            if hasattr(visitor, "visitStrArray"):
                return visitor.visitStrArray(self)
            else:
                return visitor.visitChildren(self)




    def strArray(self):

        localctx = VarDefParser.StrArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_strArray)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.strArrayCluster()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.strArrayLone()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StrArrayClusterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.StrArrayClusterContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.e = None # EeContext

        def STR_L(self):
            return self.getToken(VarDefParser.STR_L, 0)

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

        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_strArrayCluster

        def accept(self, visitor):
            if hasattr(visitor, "visitStrArrayCluster"):
                return visitor.visitStrArrayCluster(self)
            else:
                return visitor.visitChildren(self)




    def strArrayCluster(self):

        localctx = VarDefParser.StrArrayClusterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_strArrayCluster)
        header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;
        expr='';ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(VarDefParser.STR_L)
            self.state = 179
            self.match(VarDefParser.ARRAY)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 180
                self.match(VarDefParser.T)
                isGroupTemp=True


            self.state = 184
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 186
            self.match(VarDefParser.T__2)
            isTemp=False;
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 188
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 192
            localctx.i = self.match(VarDefParser.ID)
            subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 194
                self.match(VarDefParser.T__0)
                isTemp=False;
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 196
                    self.match(VarDefParser.T)
                    isTemp=True


                self.state = 200
                localctx.i = self.match(VarDefParser.ID)
                subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self.match(VarDefParser.T__3)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 208
                self.match(VarDefParser.T__1)
                self.state = 209
                localctx.e = self.ee(0)
                expr=str(localctx.e.x).lower()


            self._ctx.stop = self._input.LT(-1)

            for k in subvar.keys():
            	o = Var('')
            	name=header.lower()+'.'+k.lower()
            	self.checkDup(name)	
            	print (name+' is string')
            	self.strArrayMap[name]=o;
            	if isGroupTemp or subvar[k]:
            		self.tempVarList.append(name);
            	if expr:
            		name2=self.ifsAppend+"['"+name+"'][i]"
            		k='!'+name2+'='+expr;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StrArrayLoneContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.StrArrayLoneContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STR_L(self):
            return self.getToken(VarDefParser.STR_L, 0)

        def ARRAY(self):
            return self.getToken(VarDefParser.ARRAY, 0)

        def strArrayVar(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.StrArrayVarContext)
            else:
                return self.getTypedRuleContext(VarDefParser.StrArrayVarContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_strArrayLone

        def accept(self, visitor):
            if hasattr(visitor, "visitStrArrayLone"):
                return visitor.visitStrArrayLone(self)
            else:
                return visitor.visitChildren(self)




    def strArrayLone(self):

        localctx = VarDefParser.StrArrayLoneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_strArrayLone)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(VarDefParser.STR_L)
            self.state = 215
            self.match(VarDefParser.ARRAY)
            self.state = 216
            self.strArrayVar()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 217
                self.match(VarDefParser.T__0)
                self.state = 218
                self.strArrayVar()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StrArrayVarContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.StrArrayVarContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.e = None # EeContext

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def T(self):
            return self.getToken(VarDefParser.T, 0)

        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_strArrayVar

        def accept(self, visitor):
            if hasattr(visitor, "visitStrArrayVar"):
                return visitor.visitStrArrayVar(self)
            else:
                return visitor.visitChildren(self)




    def strArrayVar(self):

        localctx = VarDefParser.StrArrayVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_strArrayVar)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 224
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 228
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();
            self.checkDup(name);self.strArrayMap[name]=v;
            if isTemp: self.tempVarList.append(name); 
            print (name+' is string')

            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 230
                self.match(VarDefParser.T__1)
                self.state = 231
                localctx.e = self.ee(0)
                e2=str(localctx.e.x).lower()
                name2=self.ifsAppend+"['"+str((None if localctx.i is None else localctx.i.text)).lower()+"'][i]"
                k='!'+name2+'='+e2;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntArrayContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.IntArrayContext, self).__init__(parent, invokingState)
            self.parser = parser

        def intArrayCluster(self):
            return self.getTypedRuleContext(VarDefParser.IntArrayClusterContext,0)


        def intArrayLone(self):
            return self.getTypedRuleContext(VarDefParser.IntArrayLoneContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_intArray

        def accept(self, visitor):
            if hasattr(visitor, "visitIntArray"):
                return visitor.visitIntArray(self)
            else:
                return visitor.visitChildren(self)




    def intArray(self):

        localctx = VarDefParser.IntArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_intArray)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.intArrayCluster()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.intArrayLone()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntArrayClusterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.IntArrayClusterContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.e = None # EeContext

        def INT_L(self):
            return self.getToken(VarDefParser.INT_L, 0)

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

        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_intArrayCluster

        def accept(self, visitor):
            if hasattr(visitor, "visitIntArrayCluster"):
                return visitor.visitIntArrayCluster(self)
            else:
                return visitor.visitChildren(self)




    def intArrayCluster(self):

        localctx = VarDefParser.IntArrayClusterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_intArrayCluster)
        header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;
        expr='';ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(VarDefParser.INT_L)
            self.state = 241
            self.match(VarDefParser.ARRAY)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 242
                self.match(VarDefParser.T)
                isGroupTemp=True


            self.state = 246
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 248
            self.match(VarDefParser.T__2)
            isTemp=False;
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 250
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 254
            localctx.i = self.match(VarDefParser.ID)
            subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 256
                self.match(VarDefParser.T__0)
                isTemp=False;
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 258
                    self.match(VarDefParser.T)
                    isTemp=True


                self.state = 262
                localctx.i = self.match(VarDefParser.ID)
                subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 269
            self.match(VarDefParser.T__3)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 270
                self.match(VarDefParser.T__1)
                self.state = 271
                localctx.e = self.ee(0)
                expr=str(localctx.e.x).lower()


            self._ctx.stop = self._input.LT(-1)

            for k in subvar.keys():
            	o = Var('')
            	name=header.lower()+'.'+k.lower()
            	self.checkDup(name)	
            	print (name+' is integer')
            	self.intArrayMap[name]=o;
            	if isGroupTemp or subvar[k]:
            		self.tempVarList.append(name);
            	if expr:
            		name2=self.ifsAppend+"['"+name+"'][i]"
            		k='!'+name2+'='+expr;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntArrayLoneContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.IntArrayLoneContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT_L(self):
            return self.getToken(VarDefParser.INT_L, 0)

        def ARRAY(self):
            return self.getToken(VarDefParser.ARRAY, 0)

        def intArrayVar(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.IntArrayVarContext)
            else:
                return self.getTypedRuleContext(VarDefParser.IntArrayVarContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_intArrayLone

        def accept(self, visitor):
            if hasattr(visitor, "visitIntArrayLone"):
                return visitor.visitIntArrayLone(self)
            else:
                return visitor.visitChildren(self)




    def intArrayLone(self):

        localctx = VarDefParser.IntArrayLoneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_intArrayLone)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(VarDefParser.INT_L)
            self.state = 277
            self.match(VarDefParser.ARRAY)
            self.state = 278
            self.intArrayVar()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 279
                self.match(VarDefParser.T__0)
                self.state = 280
                self.intArrayVar()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntArrayVarContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.IntArrayVarContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.e = None # EeContext

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def T(self):
            return self.getToken(VarDefParser.T, 0)

        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_intArrayVar

        def accept(self, visitor):
            if hasattr(visitor, "visitIntArrayVar"):
                return visitor.visitIntArrayVar(self)
            else:
                return visitor.visitChildren(self)




    def intArrayVar(self):

        localctx = VarDefParser.IntArrayVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_intArrayVar)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 286
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 290
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();
            self.checkDup(name);self.intArrayMap[name]=v;
            if isTemp: self.tempVarList.append(name); 
            print (name+' is integer')
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 292
                self.match(VarDefParser.T__1)
                self.state = 293
                localctx.e = self.ee(0)
                e2=str(localctx.e.x).lower()
                name2=self.ifsAppend+"['"+str((None if localctx.i is None else localctx.i.text)).lower()+"'][i]"
                k='!'+name2+'='+e2;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FloatArrayContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.FloatArrayContext, self).__init__(parent, invokingState)
            self.parser = parser

        def floatArrayCluster(self):
            return self.getTypedRuleContext(VarDefParser.FloatArrayClusterContext,0)


        def floatArrayLone(self):
            return self.getTypedRuleContext(VarDefParser.FloatArrayLoneContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_floatArray

        def accept(self, visitor):
            if hasattr(visitor, "visitFloatArray"):
                return visitor.visitFloatArray(self)
            else:
                return visitor.visitChildren(self)




    def floatArray(self):

        localctx = VarDefParser.FloatArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_floatArray)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.floatArrayCluster()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.floatArrayLone()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FloatArrayClusterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.FloatArrayClusterContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.e = None # EeContext

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

        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_floatArrayCluster

        def accept(self, visitor):
            if hasattr(visitor, "visitFloatArrayCluster"):
                return visitor.visitFloatArrayCluster(self)
            else:
                return visitor.visitChildren(self)




    def floatArrayCluster(self):

        localctx = VarDefParser.FloatArrayClusterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_floatArrayCluster)
        header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;
        expr='';ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(VarDefParser.ARRAY)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 303
                self.match(VarDefParser.T)
                isGroupTemp=True


            self.state = 307
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 309
            self.match(VarDefParser.T__2)
            isTemp=False;
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 311
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 315
            localctx.i = self.match(VarDefParser.ID)
            subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 317
                self.match(VarDefParser.T__0)
                isTemp=False;
                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 319
                    self.match(VarDefParser.T)
                    isTemp=True


                self.state = 323
                localctx.i = self.match(VarDefParser.ID)
                subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 330
            self.match(VarDefParser.T__3)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 331
                self.match(VarDefParser.T__1)
                self.state = 332
                localctx.e = self.ee(0)
                expr=str(localctx.e.x).lower()


            self._ctx.stop = self._input.LT(-1)

            for k in subvar.keys():
            	o = Var('')
            	name=header.lower()+'.'+k.lower()
            	self.checkDup(name)	
            	print (name+' is float')
            	self.floatArrayMap[name]=o;
            	if isGroupTemp or subvar[k]:
            		self.tempVarList.append(name);
            	if expr:
            		name2=self.ifsAppend+"['"+name+"'][i]"
            		k='!'+name2+'='+expr;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FloatArrayLoneContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.FloatArrayLoneContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(VarDefParser.ARRAY, 0)

        def floatArrayVar(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.FloatArrayVarContext)
            else:
                return self.getTypedRuleContext(VarDefParser.FloatArrayVarContext,i)


        def getRuleIndex(self):
            return VarDefParser.RULE_floatArrayLone

        def accept(self, visitor):
            if hasattr(visitor, "visitFloatArrayLone"):
                return visitor.visitFloatArrayLone(self)
            else:
                return visitor.visitChildren(self)




    def floatArrayLone(self):

        localctx = VarDefParser.FloatArrayLoneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_floatArrayLone)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(VarDefParser.ARRAY)
            self.state = 338
            self.floatArrayVar()
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 339
                self.match(VarDefParser.T__0)
                self.state = 340
                self.floatArrayVar()
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FloatArrayVarContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.FloatArrayVarContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.e = None # EeContext

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def T(self):
            return self.getToken(VarDefParser.T, 0)

        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_floatArrayVar

        def accept(self, visitor):
            if hasattr(visitor, "visitFloatArrayVar"):
                return visitor.visitFloatArrayVar(self)
            else:
                return visitor.visitChildren(self)




    def floatArrayVar(self):

        localctx = VarDefParser.FloatArrayVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_floatArrayVar)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 346
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 350
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();
            self.checkDup(name);self.floatArrayMap[name]=v;
            if isTemp: self.tempVarList.append(name); 
            print (name+' is float')
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 352
                self.match(VarDefParser.T__1)
                self.state = 353
                localctx.e = self.ee(0)
                e2=str(localctx.e.x).lower()
                name2=self.ifsAppend+"['"+str((None if localctx.i is None else localctx.i.text)).lower()+"'][i]"
                k='!'+name2+'='+e2;ifs[k]='hi';self.ifsMap[self.ifid]=ifs;self.ifid=self.ifid+1;


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
        self.enterRule(localctx, 46, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(VarDefParser.INCLUDE)
            self.state = 359
            localctx.g = self.match(VarDefParser.ID)
            self._ctx.stop = self._input.LT(-1)
            gn=str((None if localctx.g is None else localctx.g.text)).lower();
            if gn: 
            	self.varPathMap.update(self.varPathGroupMap[gn])

            	self.tempVarList.extend(self.tempVarGroupList[gn])
            	self.ifsMap.update(self.ifsMapGroupMap[gn])
            	self.strArrayMap.update(self.strArrayGroupMap[gn])
            	self.intArrayMap.update(self.intArrayGroupMap[gn])
            	self.floatArrayMap.update(self.floatArrayGroupMap[gn])
            	self.constMap.update(self.constGroupMap[gn])
            	self.allVars.extend(self.allVarsGroupList[gn])

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
        self.enterRule(localctx, 48, self.RULE_var_path)
        isTemp=False;
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 361
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 365
            localctx.i = self.match(VarDefParser.ID)
            self.state = 366
            self.match(VarDefParser.T__1)
            self.state = 367
            localctx.p = self.match(VarDefParser.PATH)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__0:
                self.state = 368
                self.match(VarDefParser.T__0)
                self.state = 369
                localctx.u = self.match(VarDefParser.STRING)


            p =str((None if localctx.p is None else localctx.p.text)); t = Var(p); 
            name=str((None if localctx.i is None else localctx.i.text)).lower(); self.varPathMap[name]=t; 
            if name in self.allVars:
            	Err.addError(name+' is already defined.', self.vardefFile, self.vardefName)
            else:
            	self.allVars.append(name)
            if localctx.u: self.varPathMap[name].metaData['unit']=str((None if localctx.u is None else localctx.u.text))[1:-1].lower();
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
        self.enterRule(localctx, 50, self.RULE_var_meta)
        ha=False
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            localctx.i = self.id2()
            self.state = 375
            self.match(VarDefParser.T__4)
            self.state = 376
            localctx.m = self.match(VarDefParser.ID)
            self.state = 377
            self.match(VarDefParser.T__1)
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT, VarDefParser.INT, VarDefParser.STRING]:
                self.state = 384
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VarDefParser.FLOAT]:
                    self.state = 378
                    localctx.k = self.match(VarDefParser.FLOAT)
                    c=float((None if localctx.k is None else localctx.k.text))
                    pass
                elif token in [VarDefParser.INT]:
                    self.state = 380
                    localctx.k = self.match(VarDefParser.INT)
                    c=int((None if localctx.k is None else localctx.k.text))
                    pass
                elif token in [VarDefParser.STRING]:
                    self.state = 382
                    localctx.k = self.match(VarDefParser.STRING)
                    c=str((None if localctx.k is None else localctx.k.text))[1:-1].lower()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [VarDefParser.T__2]:
                self.state = 386
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
            elif self.strArrayMap.has_key(name):
            	self.strArrayMap[name].metaData[mk]=c; 
            elif self.intArrayMap.has_key(name):
            	self.intArrayMap[name].metaData[mk]=c; 
            elif self.floatArrayMap.has_key(name):
            	self.floatArrayMap[name].metaData[mk]=c; 
            else:
            	msg=name+'.'+mk+'='+str(c)+' variable \"'+name+'\" not found!'
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
        self.enterRule(localctx, 52, self.RULE_metaDict)
        hasV=False
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(VarDefParser.T__2)
            self.state = 394
            localctx.d = self.dict_pair()
            if localctx.d.hasV: localctx.hasV = True
            localctx.x = localctx.d.x	

            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 396
                self.match(VarDefParser.T__0)
                self.state = 397
                localctx.d = self.dict_pair()
                if localctx.d.hasV: localctx.hasV = True
                localctx.x = localctx.x+','+localctx.d.x	

                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 405
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


        def ID(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.ID)
            else:
                return self.getToken(VarDefParser.ID, i)

        def SYSCONST(self):
            return self.getToken(VarDefParser.SYSCONST, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_dict_pair

        def accept(self, visitor):
            if hasattr(visitor, "visitDict_pair"):
                return visitor.visitDict_pair(self)
            else:
                return visitor.visitChildren(self)




    def dict_pair(self):

        localctx = VarDefParser.Dict_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_dict_pair)
        r1='';r2=''
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.SYSCONST, VarDefParser.ID]:
                self.state = 409
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VarDefParser.ID]:
                    self.state = 407
                    localctx.i1 = self.match(VarDefParser.ID)
                    pass
                elif token in [VarDefParser.SYSCONST]:
                    self.state = 408
                    localctx.i1 = self.match(VarDefParser.SYSCONST)
                    pass
                else:
                    raise NoViableAltException(self)

                localctx.hasV = True 
                r1='_cm[\''+str((None if localctx.i1 is None else localctx.i1.text))+'\'].const'

                pass
            elif token in [VarDefParser.STRING]:
                self.state = 412
                localctx.s1 = self.match(VarDefParser.STRING)
                r1=str((None if localctx.s1 is None else localctx.s1.text))
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 414
                localctx.s11 = self.number()
                r1=str((None if localctx.s11 is None else self._input.getText((localctx.s11.start,localctx.s11.stop))))
                pass
            else:
                raise NoViableAltException(self)

            self.state = 419
            self.match(VarDefParser.T__5)
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.ID]:
                self.state = 420
                localctx.i2 = self.match(VarDefParser.ID)
                localctx.hasV = True 
                r2='_cm[\''+str((None if localctx.i2 is None else localctx.i2.text))+'\'].const'

                pass
            elif token in [VarDefParser.STRING]:
                self.state = 422
                localctx.s2 = self.match(VarDefParser.STRING)
                r2=str((None if localctx.s2 is None else localctx.s2.text))
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 424
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
        self.enterRule(localctx, 56, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
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

        def SYSARRAY(self):
            return self.getToken(VarDefParser.SYSARRAY, 0)

        def SYSCONST(self):
            return self.getToken(VarDefParser.SYSCONST, 0)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                s=''
                self.state = 437
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 435
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 439
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 442
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 446
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 448
                localctx.i = self.match(VarDefParser.SYSARRAY)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();localctx.x = self.ifsAppend+"['"+vName+"']"+"[i]"
                pass

            elif la_ == 4:
                self.state = 450
                localctx.i = self.match(VarDefParser.SYSCONST)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();localctx.x = self.constMap[vName].const
                pass

            elif la_ == 5:
                self.state = 452
                localctx.i = self.match(VarDefParser.ID)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();
                self.checkExist(vName);
                if vName in self.allVars:
                	if vName in self.constMap.keys():
                		localctx.x=self.constMap[vName].const
                	else:
                		localctx.x=self.ifsAppend+"['"+vName+"']"+"[i]"	
                else:
                		print('not found ***',vName, localctx.x)
                		print(self.allVars)

                pass

            elif la_ == 6:
                self.state = 454
                localctx.i = self.match(VarDefParser.ID)
                self.state = 455
                self.match(VarDefParser.T__4)
                self.state = 456
                localctx.j = self.match(VarDefParser.ID)

                name1=str((None if localctx.i is None else localctx.i.text)).lower();name2=str((None if localctx.j is None else localctx.j.text)).lower();vName=name1+'.'+name2; 
                if vName in self.allVars:
                	localctx.x=self.ifsAppend+"['"+vName+"']"+"[i]"
                 
                elif name1 in self.allVars:
                	m=None
                	if name1 in self.varPathMap.keys():
                		m=self.varPathMap[name1].metaData[name2]
                	elif name1 in self.floatArrayMap.keys():
                		m=self.floatArrayMap[name1].metaData[name2]
                	elif name1 in self.intArrayMap.keys():	
                		m=self.intArrayMap[name1].metaData[name2]
                	localctx.x=str(m)

                pass

            elif la_ == 7:
                self.state = 459
                self.match(VarDefParser.T__6)
                self.state = 460
                localctx.a = self.ee(0)
                self.state = 461
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.a.x)+")"
                pass

            elif la_ == 8:
                self.state = 464
                localctx.i = self.match(VarDefParser.STRING)
                localctx.x=  str((None if localctx.i is None else localctx.i.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 480
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 478
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 468
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 469
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 470
                        localctx.b = self.ee(11)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 473
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 474
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 475
                        localctx.b = self.ee(10)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 482
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_compare, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 484
                localctx.a = self.ee(0)
                self.state = 485
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10) | (1 << VarDefParser.T__11) | (1 << VarDefParser.T__12) | (1 << VarDefParser.T__13))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 486
                localctx.b = self.ee(0)
                localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 489
                self.match(VarDefParser.T__6)
                self.state = 490
                localctx.c = self.compare(0)
                self.state = 491
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 503
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VarDefParser.CompareContext(self, _parentctx, _parentState)
                    localctx.c1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare)
                    self.state = 496
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 497
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 498
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 505
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

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
        self.enterRule(localctx, 62, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            localctx.i = self.id2()
            self.state = 507
            self.match(VarDefParser.T__1)
            self.state = 508
            localctx.a = self.ee(0)
            vName=str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop)))).lower();
            if vName in self.allVars:
            	localctx.x = self.ifsNewAppend+"['"+str((None if localctx.i is None else self._input.getText((localctx.i.start,localctx.i.stop))))+"'][i]="+localctx.a.x
            	#print (vName) 
            else:
            	Err.addError(vName+' not defined yet.', self.vardefFile, self.vardefName)

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
        self.enterRule(localctx, 64, self.RULE_id2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(VarDefParser.ID)
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 512
                self.match(VarDefParser.T__4)
                self.state = 513
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
        self.enterRule(localctx, 66, self.RULE_if_stat)
        ifs=collections.OrderedDict();al=[];
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(VarDefParser.IF)
            self.state = 517
            localctx.c = self.compare(0)
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 518
                self.match(VarDefParser.NL)
                self.state = 523
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 524
            self.match(VarDefParser.T__2)
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 525
                self.match(VarDefParser.NL)
                self.state = 530
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 539 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 531
                localctx.a = self.assign()
                t=str(localctx.a.x).lower();al.append(t)
                self.state = 536
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 533
                    self.match(VarDefParser.NL)
                    self.state = 538
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 541 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 543
            self.match(VarDefParser.T__3)
            self.state = 547
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 544
                    self.match(VarDefParser.NL) 
                self.state = 549
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

            k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
            self.state = 589
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 551
                self.match(VarDefParser.ELSEIF)
                self.state = 552
                localctx.c = self.compare(0)
                self.state = 556
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 553
                    self.match(VarDefParser.NL)
                    self.state = 558
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 559
                self.match(VarDefParser.T__2)
                self.state = 563
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 560
                    self.match(VarDefParser.NL)
                    self.state = 565
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 574 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 566
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 571
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 568
                        self.match(VarDefParser.NL)
                        self.state = 573
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 576 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 578
                self.match(VarDefParser.T__3)
                self.state = 582
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 579
                        self.match(VarDefParser.NL) 
                    self.state = 584
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

                k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 626
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 592
                self.match(VarDefParser.ELSE)
                self.state = 596
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 593
                    self.match(VarDefParser.NL)
                    self.state = 598
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 599
                self.match(VarDefParser.T__2)
                self.state = 603
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 600
                    self.match(VarDefParser.NL)
                    self.state = 605
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 614 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 606
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 611
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 608
                        self.match(VarDefParser.NL)
                        self.state = 613
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 616 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 618
                self.match(VarDefParser.T__3)
                self.state = 620 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 619
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 622 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

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
        self._predicates[29] = self.ee_sempred
        self._predicates[30] = self.compare_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def ee_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

    def compare_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




