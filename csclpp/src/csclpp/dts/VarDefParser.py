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
        buf.write(u".\u0264\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \3\2\7\2B\n\2\f\2\16\2E")
        buf.write(u"\13\2\3\2\3\2\7\2I\n\2\f\2\16\2L\13\2\3\2\6\2O\n\2\r")
        buf.write(u"\2\16\2P\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\6\4[\n\4\r\4")
        buf.write(u"\16\4\\\3\4\6\4`\n\4\r\4\16\4a\3\4\3\4\6\4f\n\4\r\4\16")
        buf.write(u"\4g\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5s\n\5\3\5")
        buf.write(u"\6\5v\n\5\r\5\16\5w\3\6\3\6\3\6\5\6}\n\6\3\7\3\7\3\7")
        buf.write(u"\3\7\7\7\u0083\n\7\f\7\16\7\u0086\13\7\3\b\3\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\5\b\u0090\n\b\3\b\3\b\3\t\3\t\5\t")
        buf.write(u"\u0096\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u00a0")
        buf.write(u"\n\n\3\13\3\13\3\13\3\13\5\13\u00a6\n\13\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\5\13\u00ae\n\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\5\13\u00b6\n\13\3\13\3\13\7\13\u00ba\n\13")
        buf.write(u"\f\13\16\13\u00bd\13\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write(u"\u00c4\n\13\3\f\3\f\3\f\3\f\3\f\7\f\u00cb\n\f\f\f\16")
        buf.write(u"\f\u00ce\13\f\3\r\3\r\5\r\u00d2\n\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\5\r\u00da\n\r\3\16\3\16\5\16\u00de\n\16\3\17\3")
        buf.write(u"\17\3\17\3\17\5\17\u00e4\n\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\5\17\u00ec\n\17\3\17\3\17\3\17\3\17\3\17\3\17\5")
        buf.write(u"\17\u00f4\n\17\3\17\3\17\7\17\u00f8\n\17\f\17\16\17\u00fb")
        buf.write(u"\13\17\3\17\3\17\3\17\3\17\3\17\5\17\u0102\n\17\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\7\20\u0109\n\20\f\20\16\20\u010c")
        buf.write(u"\13\20\3\21\3\21\5\21\u0110\n\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\5\21\u0118\n\21\3\22\3\22\5\22\u011c\n\22")
        buf.write(u"\3\23\3\23\3\23\5\23\u0121\n\23\3\23\3\23\3\23\3\23\3")
        buf.write(u"\23\3\23\5\23\u0129\n\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write(u"\5\23\u0131\n\23\3\23\3\23\7\23\u0135\n\23\f\23\16\23")
        buf.write(u"\u0138\13\23\3\23\3\23\3\23\3\23\3\23\5\23\u013f\n\23")
        buf.write(u"\3\24\3\24\3\24\3\24\7\24\u0145\n\24\f\24\16\24\u0148")
        buf.write(u"\13\24\3\25\3\25\5\25\u014c\n\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\5\25\u0154\n\25\3\26\3\26\3\26\3\27\3\27\5")
        buf.write(u"\27\u015b\n\27\3\27\3\27\3\27\3\27\3\27\5\27\u0162\n")
        buf.write(u"\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write(u"\3\30\3\30\5\30\u0170\n\30\3\30\3\30\3\30\5\30\u0175")
        buf.write(u"\n\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write(u"\31\u0180\n\31\f\31\16\31\u0183\13\31\3\31\3\31\3\32")
        buf.write(u"\3\32\5\32\u0189\n\32\3\32\3\32\3\32\3\32\3\32\3\32\5")
        buf.write(u"\32\u0191\n\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write(u"\5\32\u019b\n\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3")
        buf.write(u"\34\5\34\u01a5\n\34\3\34\3\34\3\34\3\34\3\34\5\34\u01ac")
        buf.write(u"\n\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\5\34\u01c2\n\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\7\34\u01ce\n\34\f\34\16\34\u01d1\13\34")
        buf.write(u"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\5\35\u01de\n\35\3\35\3\35\3\35\3\35\3\35\7\35\u01e5")
        buf.write(u"\n\35\f\35\16\35\u01e8\13\35\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\37\3\37\3\37\5\37\u01f2\n\37\3 \3 \3 \7 \u01f7\n ")
        buf.write(u"\f \16 \u01fa\13 \3 \3 \7 \u01fe\n \f \16 \u0201\13 ")
        buf.write(u"\3 \3 \3 \7 \u0206\n \f \16 \u0209\13 \6 \u020b\n \r")
        buf.write(u" \16 \u020c\3 \3 \7 \u0211\n \f \16 \u0214\13 \3 \3 ")
        buf.write(u"\3 \3 \7 \u021a\n \f \16 \u021d\13 \3 \3 \7 \u0221\n")
        buf.write(u" \f \16 \u0224\13 \3 \3 \3 \7 \u0229\n \f \16 \u022c")
        buf.write(u"\13 \6 \u022e\n \r \16 \u022f\3 \3 \7 \u0234\n \f \16")
        buf.write(u" \u0237\13 \3 \3 \7 \u023b\n \f \16 \u023e\13 \3 \3 ")
        buf.write(u"\7 \u0242\n \f \16 \u0245\13 \3 \3 \7 \u0249\n \f \16")
        buf.write(u" \u024c\13 \3 \3 \3 \7 \u0251\n \f \16 \u0254\13 \6 ")
        buf.write(u"\u0256\n \r \16 \u0257\3 \3 \6 \u025c\n \r \16 \u025d")
        buf.write(u"\3 \3 \5 \u0262\n \3 \2\4\668!\2\4\6\b\n\f\16\20\22\24")
        buf.write(u"\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>\2\7\4\2))++")
        buf.write(u"\3\2\24\25\3\2\26\27\3\2\13\20\3\2\30\31\u029c\2C\3\2")
        buf.write(u"\2\2\4R\3\2\2\2\6V\3\2\2\2\br\3\2\2\2\n|\3\2\2\2\f~\3")
        buf.write(u"\2\2\2\16\u0087\3\2\2\2\20\u0095\3\2\2\2\22\u009f\3\2")
        buf.write(u"\2\2\24\u00a1\3\2\2\2\26\u00c5\3\2\2\2\30\u00d1\3\2\2")
        buf.write(u"\2\32\u00dd\3\2\2\2\34\u00df\3\2\2\2\36\u0103\3\2\2\2")
        buf.write(u" \u010f\3\2\2\2\"\u011b\3\2\2\2$\u011d\3\2\2\2&\u0140")
        buf.write(u"\3\2\2\2(\u014b\3\2\2\2*\u0155\3\2\2\2,\u015a\3\2\2\2")
        buf.write(u".\u0165\3\2\2\2\60\u0178\3\2\2\2\62\u0190\3\2\2\2\64")
        buf.write(u"\u019e\3\2\2\2\66\u01c1\3\2\2\28\u01dd\3\2\2\2:\u01e9")
        buf.write(u"\3\2\2\2<\u01ee\3\2\2\2>\u01f3\3\2\2\2@B\7-\2\2A@\3\2")
        buf.write(u"\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2EC\3\2\2")
        buf.write(u"\2FJ\5\4\3\2GI\7-\2\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2J")
        buf.write(u"K\3\2\2\2KN\3\2\2\2LJ\3\2\2\2MO\5\6\4\2NM\3\2\2\2OP\3")
        buf.write(u"\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\3\3\2\2\2RS\7\32\2\2ST\7")
        buf.write(u"*\2\2TU\b\3\1\2U\5\3\2\2\2VW\7\34\2\2WX\7*\2\2XZ\b\4")
        buf.write(u"\1\2Y[\7-\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2")
        buf.write(u"\2\2]_\3\2\2\2^`\5\b\5\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2")
        buf.write(u"\2ab\3\2\2\2bc\3\2\2\2ce\7\35\2\2df\7-\2\2ed\3\2\2\2")
        buf.write(u"fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\7\3\2\2\2is\5,\27\2j")
        buf.write(u"s\5.\30\2ks\5\20\t\2lm\5> \2mn\b\5\1\2ns\3\2\2\2os\5")
        buf.write(u"\n\6\2ps\5*\26\2qs\5\f\7\2ri\3\2\2\2rj\3\2\2\2rk\3\2")
        buf.write(u"\2\2rl\3\2\2\2ro\3\2\2\2rp\3\2\2\2rq\3\2\2\2su\3\2\2")
        buf.write(u"\2tv\7-\2\2ut\3\2\2\2vw\3\2\2\2wu\3\2\2\2wx\3\2\2\2x")
        buf.write(u"\t\3\2\2\2y}\5\22\n\2z}\5\32\16\2{}\5\"\22\2|y\3\2\2")
        buf.write(u"\2|z\3\2\2\2|{\3\2\2\2}\13\3\2\2\2~\177\7&\2\2\177\u0084")
        buf.write(u"\5\16\b\2\u0080\u0081\7\3\2\2\u0081\u0083\5\16\b\2\u0082")
        buf.write(u"\u0080\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2")
        buf.write(u"\2\u0084\u0085\3\2\2\2\u0085\r\3\2\2\2\u0086\u0084\3")
        buf.write(u"\2\2\2\u0087\u0088\7*\2\2\u0088\u008f\7\4\2\2\u0089\u008a")
        buf.write(u"\7)\2\2\u008a\u0090\b\b\1\2\u008b\u008c\7+\2\2\u008c")
        buf.write(u"\u0090\b\b\1\2\u008d\u008e\7,\2\2\u008e\u0090\b\b\1\2")
        buf.write(u"\u008f\u0089\3\2\2\2\u008f\u008b\3\2\2\2\u008f\u008d")
        buf.write(u"\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\b\b\1\2\u0092")
        buf.write(u"\17\3\2\2\2\u0093\u0094\7\22\2\2\u0094\u0096\b\t\1\2")
        buf.write(u"\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097")
        buf.write(u"\3\2\2\2\u0097\u0098\7*\2\2\u0098\u0099\b\t\1\2\u0099")
        buf.write(u"\u009a\7\4\2\2\u009a\u009b\5\66\34\2\u009b\u009c\b\t")
        buf.write(u"\1\2\u009c\21\3\2\2\2\u009d\u00a0\5\24\13\2\u009e\u00a0")
        buf.write(u"\5\26\f\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0")
        buf.write(u"\23\3\2\2\2\u00a1\u00a2\7#\2\2\u00a2\u00a5\7\36\2\2\u00a3")
        buf.write(u"\u00a4\7\22\2\2\u00a4\u00a6\b\13\1\2\u00a5\u00a3\3\2")
        buf.write(u"\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8")
        buf.write(u"\7*\2\2\u00a8\u00a9\b\13\1\2\u00a9\u00aa\7\5\2\2\u00aa")
        buf.write(u"\u00ad\b\13\1\2\u00ab\u00ac\7\22\2\2\u00ac\u00ae\b\13")
        buf.write(u"\1\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af")
        buf.write(u"\3\2\2\2\u00af\u00b0\7*\2\2\u00b0\u00bb\b\13\1\2\u00b1")
        buf.write(u"\u00b2\7\3\2\2\u00b2\u00b5\b\13\1\2\u00b3\u00b4\7\22")
        buf.write(u"\2\2\u00b4\u00b6\b\13\1\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6")
        buf.write(u"\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\7*\2\2\u00b8")
        buf.write(u"\u00ba\b\13\1\2\u00b9\u00b1\3\2\2\2\u00ba\u00bd\3\2\2")
        buf.write(u"\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be")
        buf.write(u"\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00c3\7\6\2\2\u00bf")
        buf.write(u"\u00c0\7\4\2\2\u00c0\u00c1\5\66\34\2\u00c1\u00c2\b\13")
        buf.write(u"\1\2\u00c2\u00c4\3\2\2\2\u00c3\u00bf\3\2\2\2\u00c3\u00c4")
        buf.write(u"\3\2\2\2\u00c4\25\3\2\2\2\u00c5\u00c6\7#\2\2\u00c6\u00c7")
        buf.write(u"\7\36\2\2\u00c7\u00cc\5\30\r\2\u00c8\u00c9\7\3\2\2\u00c9")
        buf.write(u"\u00cb\5\30\r\2\u00ca\u00c8\3\2\2\2\u00cb\u00ce\3\2\2")
        buf.write(u"\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\27\3")
        buf.write(u"\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7\22\2\2\u00d0")
        buf.write(u"\u00d2\b\r\1\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2")
        buf.write(u"\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\7*\2\2\u00d4\u00d9")
        buf.write(u"\b\r\1\2\u00d5\u00d6\7\4\2\2\u00d6\u00d7\5\66\34\2\u00d7")
        buf.write(u"\u00d8\b\r\1\2\u00d8\u00da\3\2\2\2\u00d9\u00d5\3\2\2")
        buf.write(u"\2\u00d9\u00da\3\2\2\2\u00da\31\3\2\2\2\u00db\u00de\5")
        buf.write(u"\34\17\2\u00dc\u00de\5\36\20\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write(u"\u00dc\3\2\2\2\u00de\33\3\2\2\2\u00df\u00e0\7$\2\2\u00e0")
        buf.write(u"\u00e3\7\36\2\2\u00e1\u00e2\7\22\2\2\u00e2\u00e4\b\17")
        buf.write(u"\1\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5")
        buf.write(u"\3\2\2\2\u00e5\u00e6\7*\2\2\u00e6\u00e7\b\17\1\2\u00e7")
        buf.write(u"\u00e8\7\5\2\2\u00e8\u00eb\b\17\1\2\u00e9\u00ea\7\22")
        buf.write(u"\2\2\u00ea\u00ec\b\17\1\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec")
        buf.write(u"\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\7*\2\2\u00ee")
        buf.write(u"\u00f9\b\17\1\2\u00ef\u00f0\7\3\2\2\u00f0\u00f3\b\17")
        buf.write(u"\1\2\u00f1\u00f2\7\22\2\2\u00f2\u00f4\b\17\1\2\u00f3")
        buf.write(u"\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\3\2\2")
        buf.write(u"\2\u00f5\u00f6\7*\2\2\u00f6\u00f8\b\17\1\2\u00f7\u00ef")
        buf.write(u"\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9")
        buf.write(u"\u00fa\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9\3\2\2")
        buf.write(u"\2\u00fc\u0101\7\6\2\2\u00fd\u00fe\7\4\2\2\u00fe\u00ff")
        buf.write(u"\5\66\34\2\u00ff\u0100\b\17\1\2\u0100\u0102\3\2\2\2\u0101")
        buf.write(u"\u00fd\3\2\2\2\u0101\u0102\3\2\2\2\u0102\35\3\2\2\2\u0103")
        buf.write(u"\u0104\7$\2\2\u0104\u0105\7\36\2\2\u0105\u010a\5 \21")
        buf.write(u"\2\u0106\u0107\7\3\2\2\u0107\u0109\5 \21\2\u0108\u0106")
        buf.write(u"\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a")
        buf.write(u"\u010b\3\2\2\2\u010b\37\3\2\2\2\u010c\u010a\3\2\2\2\u010d")
        buf.write(u"\u010e\7\22\2\2\u010e\u0110\b\21\1\2\u010f\u010d\3\2")
        buf.write(u"\2\2\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112")
        buf.write(u"\7*\2\2\u0112\u0117\b\21\1\2\u0113\u0114\7\4\2\2\u0114")
        buf.write(u"\u0115\5\66\34\2\u0115\u0116\b\21\1\2\u0116\u0118\3\2")
        buf.write(u"\2\2\u0117\u0113\3\2\2\2\u0117\u0118\3\2\2\2\u0118!\3")
        buf.write(u"\2\2\2\u0119\u011c\5$\23\2\u011a\u011c\5&\24\2\u011b")
        buf.write(u"\u0119\3\2\2\2\u011b\u011a\3\2\2\2\u011c#\3\2\2\2\u011d")
        buf.write(u"\u0120\7\36\2\2\u011e\u011f\7\22\2\2\u011f\u0121\b\23")
        buf.write(u"\1\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122")
        buf.write(u"\3\2\2\2\u0122\u0123\7*\2\2\u0123\u0124\b\23\1\2\u0124")
        buf.write(u"\u0125\7\5\2\2\u0125\u0128\b\23\1\2\u0126\u0127\7\22")
        buf.write(u"\2\2\u0127\u0129\b\23\1\2\u0128\u0126\3\2\2\2\u0128\u0129")
        buf.write(u"\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\7*\2\2\u012b")
        buf.write(u"\u0136\b\23\1\2\u012c\u012d\7\3\2\2\u012d\u0130\b\23")
        buf.write(u"\1\2\u012e\u012f\7\22\2\2\u012f\u0131\b\23\1\2\u0130")
        buf.write(u"\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2")
        buf.write(u"\2\u0132\u0133\7*\2\2\u0133\u0135\b\23\1\2\u0134\u012c")
        buf.write(u"\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136")
        buf.write(u"\u0137\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u0136\3\2\2")
        buf.write(u"\2\u0139\u013e\7\6\2\2\u013a\u013b\7\4\2\2\u013b\u013c")
        buf.write(u"\5\66\34\2\u013c\u013d\b\23\1\2\u013d\u013f\3\2\2\2\u013e")
        buf.write(u"\u013a\3\2\2\2\u013e\u013f\3\2\2\2\u013f%\3\2\2\2\u0140")
        buf.write(u"\u0141\7\36\2\2\u0141\u0146\5(\25\2\u0142\u0143\7\3\2")
        buf.write(u"\2\u0143\u0145\5(\25\2\u0144\u0142\3\2\2\2\u0145\u0148")
        buf.write(u"\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write(u"\'\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a\7\22\2\2\u014a")
        buf.write(u"\u014c\b\25\1\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2")
        buf.write(u"\2\u014c\u014d\3\2\2\2\u014d\u014e\7*\2\2\u014e\u0153")
        buf.write(u"\b\25\1\2\u014f\u0150\7\4\2\2\u0150\u0151\5\66\34\2\u0151")
        buf.write(u"\u0152\b\25\1\2\u0152\u0154\3\2\2\2\u0153\u014f\3\2\2")
        buf.write(u"\2\u0153\u0154\3\2\2\2\u0154)\3\2\2\2\u0155\u0156\7\33")
        buf.write(u"\2\2\u0156\u0157\7*\2\2\u0157+\3\2\2\2\u0158\u0159\7")
        buf.write(u"\22\2\2\u0159\u015b\b\27\1\2\u015a\u0158\3\2\2\2\u015a")
        buf.write(u"\u015b\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\7*\2\2")
        buf.write(u"\u015d\u015e\7\4\2\2\u015e\u0161\7\23\2\2\u015f\u0160")
        buf.write(u"\7\3\2\2\u0160\u0162\7,\2\2\u0161\u015f\3\2\2\2\u0161")
        buf.write(u"\u0162\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\b\27\1")
        buf.write(u"\2\u0164-\3\2\2\2\u0165\u0166\5<\37\2\u0166\u0167\7\7")
        buf.write(u"\2\2\u0167\u0168\7*\2\2\u0168\u0174\7\4\2\2\u0169\u016a")
        buf.write(u"\7)\2\2\u016a\u0170\b\30\1\2\u016b\u016c\7+\2\2\u016c")
        buf.write(u"\u0170\b\30\1\2\u016d\u016e\7,\2\2\u016e\u0170\b\30\1")
        buf.write(u"\2\u016f\u0169\3\2\2\2\u016f\u016b\3\2\2\2\u016f\u016d")
        buf.write(u"\3\2\2\2\u0170\u0175\3\2\2\2\u0171\u0172\5\60\31\2\u0172")
        buf.write(u"\u0173\b\30\1\2\u0173\u0175\3\2\2\2\u0174\u016f\3\2\2")
        buf.write(u"\2\u0174\u0171\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177")
        buf.write(u"\b\30\1\2\u0177/\3\2\2\2\u0178\u0179\7\5\2\2\u0179\u017a")
        buf.write(u"\5\62\32\2\u017a\u0181\b\31\1\2\u017b\u017c\7\3\2\2\u017c")
        buf.write(u"\u017d\5\62\32\2\u017d\u017e\b\31\1\2\u017e\u0180\3\2")
        buf.write(u"\2\2\u017f\u017b\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f")
        buf.write(u"\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184\3\2\2\2\u0183")
        buf.write(u"\u0181\3\2\2\2\u0184\u0185\7\6\2\2\u0185\61\3\2\2\2\u0186")
        buf.write(u"\u0189\7*\2\2\u0187\u0189\7(\2\2\u0188\u0186\3\2\2\2")
        buf.write(u"\u0188\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u0191")
        buf.write(u"\b\32\1\2\u018b\u018c\7,\2\2\u018c\u0191\b\32\1\2\u018d")
        buf.write(u"\u018e\5\64\33\2\u018e\u018f\b\32\1\2\u018f\u0191\3\2")
        buf.write(u"\2\2\u0190\u0188\3\2\2\2\u0190\u018b\3\2\2\2\u0190\u018d")
        buf.write(u"\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u019a\7\b\2\2\u0193")
        buf.write(u"\u0194\7*\2\2\u0194\u019b\b\32\1\2\u0195\u0196\7,\2\2")
        buf.write(u"\u0196\u019b\b\32\1\2\u0197\u0198\5\64\33\2\u0198\u0199")
        buf.write(u"\b\32\1\2\u0199\u019b\3\2\2\2\u019a\u0193\3\2\2\2\u019a")
        buf.write(u"\u0195\3\2\2\2\u019a\u0197\3\2\2\2\u019b\u019c\3\2\2")
        buf.write(u"\2\u019c\u019d\b\32\1\2\u019d\63\3\2\2\2\u019e\u019f")
        buf.write(u"\t\2\2\2\u019f\65\3\2\2\2\u01a0\u01a1\b\34\1\2\u01a1")
        buf.write(u"\u01a4\b\34\1\2\u01a2\u01a3\7\27\2\2\u01a3\u01a5\b\34")
        buf.write(u"\1\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6")
        buf.write(u"\3\2\2\2\u01a6\u01a7\7+\2\2\u01a7\u01c2\b\34\1\2\u01a8")
        buf.write(u"\u01ab\b\34\1\2\u01a9\u01aa\7\27\2\2\u01aa\u01ac\b\34")
        buf.write(u"\1\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad")
        buf.write(u"\3\2\2\2\u01ad\u01ae\7)\2\2\u01ae\u01c2\b\34\1\2\u01af")
        buf.write(u"\u01b0\7\'\2\2\u01b0\u01c2\b\34\1\2\u01b1\u01b2\7(\2")
        buf.write(u"\2\u01b2\u01c2\b\34\1\2\u01b3\u01b4\7*\2\2\u01b4\u01c2")
        buf.write(u"\b\34\1\2\u01b5\u01b6\7*\2\2\u01b6\u01b7\7\7\2\2\u01b7")
        buf.write(u"\u01b8\7*\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01c2\b\34\1")
        buf.write(u"\2\u01ba\u01bb\7\t\2\2\u01bb\u01bc\5\66\34\2\u01bc\u01bd")
        buf.write(u"\7\n\2\2\u01bd\u01be\b\34\1\2\u01be\u01c2\3\2\2\2\u01bf")
        buf.write(u"\u01c0\7,\2\2\u01c0\u01c2\b\34\1\2\u01c1\u01a0\3\2\2")
        buf.write(u"\2\u01c1\u01a8\3\2\2\2\u01c1\u01af\3\2\2\2\u01c1\u01b1")
        buf.write(u"\3\2\2\2\u01c1\u01b3\3\2\2\2\u01c1\u01b5\3\2\2\2\u01c1")
        buf.write(u"\u01ba\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01cf\3\2\2")
        buf.write(u"\2\u01c3\u01c4\f\f\2\2\u01c4\u01c5\t\3\2\2\u01c5\u01c6")
        buf.write(u"\5\66\34\r\u01c6\u01c7\b\34\1\2\u01c7\u01ce\3\2\2\2\u01c8")
        buf.write(u"\u01c9\f\13\2\2\u01c9\u01ca\t\4\2\2\u01ca\u01cb\5\66")
        buf.write(u"\34\f\u01cb\u01cc\b\34\1\2\u01cc\u01ce\3\2\2\2\u01cd")
        buf.write(u"\u01c3\3\2\2\2\u01cd\u01c8\3\2\2\2\u01ce\u01d1\3\2\2")
        buf.write(u"\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\67\3")
        buf.write(u"\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3\b\35\1\2\u01d3")
        buf.write(u"\u01d4\5\66\34\2\u01d4\u01d5\t\5\2\2\u01d5\u01d6\5\66")
        buf.write(u"\34\2\u01d6\u01d7\b\35\1\2\u01d7\u01de\3\2\2\2\u01d8")
        buf.write(u"\u01d9\7\t\2\2\u01d9\u01da\58\35\2\u01da\u01db\7\n\2")
        buf.write(u"\2\u01db\u01dc\b\35\1\2\u01dc\u01de\3\2\2\2\u01dd\u01d2")
        buf.write(u"\3\2\2\2\u01dd\u01d8\3\2\2\2\u01de\u01e6\3\2\2\2\u01df")
        buf.write(u"\u01e0\f\3\2\2\u01e0\u01e1\t\6\2\2\u01e1\u01e2\58\35")
        buf.write(u"\4\u01e2\u01e3\b\35\1\2\u01e3\u01e5\3\2\2\2\u01e4\u01df")
        buf.write(u"\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6")
        buf.write(u"\u01e7\3\2\2\2\u01e79\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9")
        buf.write(u"\u01ea\5<\37\2\u01ea\u01eb\7\4\2\2\u01eb\u01ec\5\66\34")
        buf.write(u"\2\u01ec\u01ed\b\36\1\2\u01ed;\3\2\2\2\u01ee\u01f1\7")
        buf.write(u"*\2\2\u01ef\u01f0\7\7\2\2\u01f0\u01f2\7*\2\2\u01f1\u01ef")
        buf.write(u"\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2=\3\2\2\2\u01f3\u01f4")
        buf.write(u"\7\37\2\2\u01f4\u01f8\58\35\2\u01f5\u01f7\7-\2\2\u01f6")
        buf.write(u"\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2")
        buf.write(u"\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01f8")
        buf.write(u"\3\2\2\2\u01fb\u01ff\7\5\2\2\u01fc\u01fe\7-\2\2\u01fd")
        buf.write(u"\u01fc\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff\u01fd\3\2\2")
        buf.write(u"\2\u01ff\u0200\3\2\2\2\u0200\u020a\3\2\2\2\u0201\u01ff")
        buf.write(u"\3\2\2\2\u0202\u0203\5:\36\2\u0203\u0207\b \1\2\u0204")
        buf.write(u"\u0206\7-\2\2\u0205\u0204\3\2\2\2\u0206\u0209\3\2\2\2")
        buf.write(u"\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u020b")
        buf.write(u"\3\2\2\2\u0209\u0207\3\2\2\2\u020a\u0202\3\2\2\2\u020b")
        buf.write(u"\u020c\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2")
        buf.write(u"\2\u020d\u020e\3\2\2\2\u020e\u0212\7\6\2\2\u020f\u0211")
        buf.write(u"\7-\2\2\u0210\u020f\3\2\2\2\u0211\u0214\3\2\2\2\u0212")
        buf.write(u"\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0215\3\2\2")
        buf.write(u"\2\u0214\u0212\3\2\2\2\u0215\u023c\b \1\2\u0216\u0217")
        buf.write(u"\7 \2\2\u0217\u021b\58\35\2\u0218\u021a\7-\2\2\u0219")
        buf.write(u"\u0218\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2")
        buf.write(u"\2\u021b\u021c\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u021b")
        buf.write(u"\3\2\2\2\u021e\u0222\7\5\2\2\u021f\u0221\7-\2\2\u0220")
        buf.write(u"\u021f\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220\3\2\2")
        buf.write(u"\2\u0222\u0223\3\2\2\2\u0223\u022d\3\2\2\2\u0224\u0222")
        buf.write(u"\3\2\2\2\u0225\u0226\5:\36\2\u0226\u022a\b \1\2\u0227")
        buf.write(u"\u0229\7-\2\2\u0228\u0227\3\2\2\2\u0229\u022c\3\2\2\2")
        buf.write(u"\u022a\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022e")
        buf.write(u"\3\2\2\2\u022c\u022a\3\2\2\2\u022d\u0225\3\2\2\2\u022e")
        buf.write(u"\u022f\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2")
        buf.write(u"\2\u0230\u0231\3\2\2\2\u0231\u0235\7\6\2\2\u0232\u0234")
        buf.write(u"\7-\2\2\u0233\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235")
        buf.write(u"\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0238\3\2\2")
        buf.write(u"\2\u0237\u0235\3\2\2\2\u0238\u0239\b \1\2\u0239\u023b")
        buf.write(u"\3\2\2\2\u023a\u0216\3\2\2\2\u023b\u023e\3\2\2\2\u023c")
        buf.write(u"\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u0261\3\2\2")
        buf.write(u"\2\u023e\u023c\3\2\2\2\u023f\u0243\7!\2\2\u0240\u0242")
        buf.write(u"\7-\2\2\u0241\u0240\3\2\2\2\u0242\u0245\3\2\2\2\u0243")
        buf.write(u"\u0241\3\2\2\2\u0243\u0244\3\2\2\2\u0244\u0246\3\2\2")
        buf.write(u"\2\u0245\u0243\3\2\2\2\u0246\u024a\7\5\2\2\u0247\u0249")
        buf.write(u"\7-\2\2\u0248\u0247\3\2\2\2\u0249\u024c\3\2\2\2\u024a")
        buf.write(u"\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u0255\3\2\2")
        buf.write(u"\2\u024c\u024a\3\2\2\2\u024d\u024e\5:\36\2\u024e\u0252")
        buf.write(u"\b \1\2\u024f\u0251\7-\2\2\u0250\u024f\3\2\2\2\u0251")
        buf.write(u"\u0254\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0253\3\2\2")
        buf.write(u"\2\u0253\u0256\3\2\2\2\u0254\u0252\3\2\2\2\u0255\u024d")
        buf.write(u"\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0255\3\2\2\2\u0257")
        buf.write(u"\u0258\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025b\7\6\2")
        buf.write(u"\2\u025a\u025c\7-\2\2\u025b\u025a\3\2\2\2\u025c\u025d")
        buf.write(u"\3\2\2\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e")
        buf.write(u"\u025f\3\2\2\2\u025f\u0260\b \1\2\u0260\u0262\3\2\2\2")
        buf.write(u"\u0261\u023f\3\2\2\2\u0261\u0262\3\2\2\2\u0262?\3\2\2")
        buf.write(u"\2JCJP\\agrw|\u0084\u008f\u0095\u009f\u00a5\u00ad\u00b5")
        buf.write(u"\u00bb\u00c3\u00cc\u00d1\u00d9\u00dd\u00e3\u00eb\u00f3")
        buf.write(u"\u00f9\u0101\u010a\u010f\u0117\u011b\u0120\u0128\u0130")
        buf.write(u"\u0136\u013e\u0146\u014b\u0153\u015a\u0161\u016f\u0174")
        buf.write(u"\u0181\u0188\u0190\u019a\u01a4\u01ab\u01c1\u01cd\u01cf")
        buf.write(u"\u01dd\u01e6\u01f1\u01f8\u01ff\u0207\u020c\u0212\u021b")
        buf.write(u"\u0222\u022a\u022f\u0235\u023c\u0243\u024a\u0252\u0257")
        buf.write(u"\u025d\u0261")
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
    RULE_const_var = 6
    RULE_stat = 7
    RULE_strArray = 8
    RULE_strArrayCluster = 9
    RULE_strArrayLone = 10
    RULE_strArrayVar = 11
    RULE_intArray = 12
    RULE_intArrayCluster = 13
    RULE_intArrayLone = 14
    RULE_intArrayVar = 15
    RULE_floatArray = 16
    RULE_floatArrayCluster = 17
    RULE_floatArrayLone = 18
    RULE_floatArrayVar = 19
    RULE_include = 20
    RULE_var_path = 21
    RULE_var_meta = 22
    RULE_metaDict = 23
    RULE_dict_pair = 24
    RULE_number = 25
    RULE_ee = 26
    RULE_compare = 27
    RULE_assign = 28
    RULE_id2 = 29
    RULE_if_stat = 30

    ruleNames =  [ u"prog", u"use", u"vardef", u"field", u"new_var", u"constant", 
                   u"const_var", u"stat", u"strArray", u"strArrayCluster", 
                   u"strArrayLone", u"strArrayVar", u"intArray", u"intArrayCluster", 
                   u"intArrayLone", u"intArrayVar", u"floatArray", u"floatArrayCluster", 
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
    allVars=[];

    def isConst(self, name):
    	if name in self.constMap.keys():
    		return True
    	else:
    		return False

    def checkDup(self, name, where=None):
    	if name in self.allVars:
    		msg=name+' is already defined.'
    		if where: msg=msg+'@'+where
    		Err.addError(msg, self.vardefFile, self.vardefName)
    	else:
    		self.allVars.append(name)
    		
    def checkExist(self, name, where=None):
    	if name not in self.allVars:
    		msg=name+' is not defined.'
    		if where: msg=msg+'@'+where
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
        self.ifid=0;

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 62
                self.match(VarDefParser.NL)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.use()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 69
                self.match(VarDefParser.NL)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 75
                self.vardef()
                self.state = 78 
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
            self.state = 80
            self.match(VarDefParser.USE)
            self.state = 81
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
        self.constMap=collections.OrderedDict();
        self.allVars=list(self.systemVars);

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(VarDefParser.VARDEF)
            self.state = 85
            localctx.name = self.match(VarDefParser.ID)
            groupName=str((None if localctx.name is None else localctx.name.text)).lower();self.vardefName=groupName;
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                self.match(VarDefParser.NL)
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self.field()
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ARRAY) | (1 << VarDefParser.IF) | (1 << VarDefParser.STR_L) | (1 << VarDefParser.INT_L) | (1 << VarDefParser.CONST) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 97
            self.match(VarDefParser.END)
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.match(VarDefParser.NL)
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self._ctx.stop = self._input.LT(-1)

            self.varPathGroupMap[groupName]=self.varPathMap;

            self.tempVarGroupList[groupName]=self.tempVarList;	
            self.ifsMapGroupMap[groupName]=self.ifsMap;
            self.strArrayGroupMap[groupName]=self.strArrayMap;
            self.intArrayGroupMap[groupName]=self.intArrayMap;
            self.floatArrayGroupMap[groupName]=self.floatArrayMap;
            self.constGroupMap[groupName]=self.constMap;

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
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 103
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 104
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 105
                self.stat()
                pass

            elif la_ == 4:
                self.state = 106
                self.if_stat()
                self.ifid=self.ifid+1;
                pass

            elif la_ == 5:
                self.state = 109
                self.new_var()
                pass

            elif la_ == 6:
                self.state = 110
                self.include()
                pass

            elif la_ == 7:
                self.state = 111
                self.constant()
                pass


            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.match(VarDefParser.NL)
                self.state = 117 
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
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.STR_L]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.strArray()
                pass
            elif token in [VarDefParser.INT_L]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.intArray()
                pass
            elif token in [VarDefParser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
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
            self.state = 124
            self.match(VarDefParser.CONST)
            self.state = 125
            self.const_var()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 126
                self.match(VarDefParser.T__0)
                self.state = 127
                self.const_var()
                self.state = 132
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
            self.state = 133
            localctx.i = self.match(VarDefParser.ID)
            self.state = 134
            self.match(VarDefParser.T__1)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT]:
                self.state = 135
                localctx.c = self.match(VarDefParser.FLOAT)
                v.const=float((None if localctx.c is None else localctx.c.text));v.metaData['_dataType']=np.float;
                pass
            elif token in [VarDefParser.INT]:
                self.state = 137
                localctx.c = self.match(VarDefParser.INT)
                v.const=int((None if localctx.c is None else localctx.c.text));v.metaData['_dataType']=np.int;
                pass
            elif token in [VarDefParser.STRING]:
                self.state = 139
                localctx.c = self.match(VarDefParser.STRING)
                v.const=str((None if localctx.c is None else localctx.c.text));v.metaData['_dataType']=np.str;
                pass
            else:
                raise NoViableAltException(self)

            name=str((None if localctx.i is None else localctx.i.text)).lower();self.constMap[name]=v;self.checkDup(name);
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
        self.enterRule(localctx, 14, self.RULE_stat)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 145
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 149
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();self.checkExist(name);
            self.state = 151
            self.match(VarDefParser.T__1)
            self.state = 152
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
        self.enterRule(localctx, 16, self.RULE_strArray)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.strArrayCluster()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
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
        self.enterRule(localctx, 18, self.RULE_strArrayCluster)
        header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;
        expr='';ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(VarDefParser.STR_L)
            self.state = 160
            self.match(VarDefParser.ARRAY)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 161
                self.match(VarDefParser.T)
                isGroupTemp=True


            self.state = 165
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 167
            self.match(VarDefParser.T__2)
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
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 175
                self.match(VarDefParser.T__0)
                isTemp=False;
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 177
                    self.match(VarDefParser.T)
                    isTemp=True


                self.state = 181
                localctx.i = self.match(VarDefParser.ID)
                subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self.match(VarDefParser.T__3)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 189
                self.match(VarDefParser.T__1)
                self.state = 190
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
        self.enterRule(localctx, 20, self.RULE_strArrayLone)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(VarDefParser.STR_L)
            self.state = 196
            self.match(VarDefParser.ARRAY)
            self.state = 197
            self.strArrayVar()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 198
                self.match(VarDefParser.T__0)
                self.state = 199
                self.strArrayVar()
                self.state = 204
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
        self.enterRule(localctx, 22, self.RULE_strArrayVar)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 205
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 209
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();
            self.checkDup(name);self.strArrayMap[name]=v;
            if isTemp: self.tempVarList.append(name); 
            print (name+' is string')

            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 211
                self.match(VarDefParser.T__1)
                self.state = 212
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
        self.enterRule(localctx, 24, self.RULE_intArray)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.intArrayCluster()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
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
        self.enterRule(localctx, 26, self.RULE_intArrayCluster)
        header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;
        expr='';ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(VarDefParser.INT_L)
            self.state = 222
            self.match(VarDefParser.ARRAY)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 223
                self.match(VarDefParser.T)
                isGroupTemp=True


            self.state = 227
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 229
            self.match(VarDefParser.T__2)
            isTemp=False;
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 231
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 235
            localctx.i = self.match(VarDefParser.ID)
            subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 237
                self.match(VarDefParser.T__0)
                isTemp=False;
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 239
                    self.match(VarDefParser.T)
                    isTemp=True


                self.state = 243
                localctx.i = self.match(VarDefParser.ID)
                subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 250
            self.match(VarDefParser.T__3)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 251
                self.match(VarDefParser.T__1)
                self.state = 252
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
        self.enterRule(localctx, 28, self.RULE_intArrayLone)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(VarDefParser.INT_L)
            self.state = 258
            self.match(VarDefParser.ARRAY)
            self.state = 259
            self.intArrayVar()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 260
                self.match(VarDefParser.T__0)
                self.state = 261
                self.intArrayVar()
                self.state = 266
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
        self.enterRule(localctx, 30, self.RULE_intArrayVar)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 267
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 271
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();
            self.checkDup(name);self.intArrayMap[name]=v;
            if isTemp: self.tempVarList.append(name); 
            print (name+' is integer')
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 273
                self.match(VarDefParser.T__1)
                self.state = 274
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
        self.enterRule(localctx, 32, self.RULE_floatArray)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.floatArrayCluster()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
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
        self.enterRule(localctx, 34, self.RULE_floatArrayCluster)
        header='';subvar=collections.OrderedDict();isTemp=False;isGroupTemp=False;
        expr='';ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(VarDefParser.ARRAY)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 284
                self.match(VarDefParser.T)
                isGroupTemp=True


            self.state = 288
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 290
            self.match(VarDefParser.T__2)
            isTemp=False;
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 292
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 296
            localctx.i = self.match(VarDefParser.ID)
            subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 298
                self.match(VarDefParser.T__0)
                isTemp=False;
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 300
                    self.match(VarDefParser.T)
                    isTemp=True


                self.state = 304
                localctx.i = self.match(VarDefParser.ID)
                subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 311
            self.match(VarDefParser.T__3)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 312
                self.match(VarDefParser.T__1)
                self.state = 313
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
        self.enterRule(localctx, 36, self.RULE_floatArrayLone)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(VarDefParser.ARRAY)
            self.state = 319
            self.floatArrayVar()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 320
                self.match(VarDefParser.T__0)
                self.state = 321
                self.floatArrayVar()
                self.state = 326
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
        self.enterRule(localctx, 38, self.RULE_floatArrayVar)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 327
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 331
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();
            self.checkDup(name);self.floatArrayMap[name]=v;
            if isTemp: self.tempVarList.append(name); 
            print (name+' is float')
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__1:
                self.state = 333
                self.match(VarDefParser.T__1)
                self.state = 334
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
        self.enterRule(localctx, 40, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(VarDefParser.INCLUDE)
            self.state = 340
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
        self.enterRule(localctx, 42, self.RULE_var_path)
        isTemp=False;
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 342
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 346
            localctx.i = self.match(VarDefParser.ID)
            self.state = 347
            self.match(VarDefParser.T__1)
            self.state = 348
            localctx.p = self.match(VarDefParser.PATH)
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__0:
                self.state = 349
                self.match(VarDefParser.T__0)
                self.state = 350
                localctx.u = self.match(VarDefParser.STRING)


            p =str((None if localctx.p is None else localctx.p.text)); t = Var(p); 
            name=str((None if localctx.i is None else localctx.i.text)).lower(); self.varPathMap[name]=t; 
            if name in self.allVars:
            	Err.addError(name+' is already defined.', self.vardefFile, self.vardefName)
            else:
            	self.allVars.append(name)
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
        self.enterRule(localctx, 44, self.RULE_var_meta)
        ha=False
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            localctx.i = self.id2()
            self.state = 356
            self.match(VarDefParser.T__4)
            self.state = 357
            localctx.m = self.match(VarDefParser.ID)
            self.state = 358
            self.match(VarDefParser.T__1)
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT, VarDefParser.INT, VarDefParser.STRING]:
                self.state = 365
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VarDefParser.FLOAT]:
                    self.state = 359
                    localctx.k = self.match(VarDefParser.FLOAT)
                    c=float((None if localctx.k is None else localctx.k.text))
                    pass
                elif token in [VarDefParser.INT]:
                    self.state = 361
                    localctx.k = self.match(VarDefParser.INT)
                    c=int((None if localctx.k is None else localctx.k.text))
                    pass
                elif token in [VarDefParser.STRING]:
                    self.state = 363
                    localctx.k = self.match(VarDefParser.STRING)
                    c=str((None if localctx.k is None else localctx.k.text))[1:-1].lower()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [VarDefParser.T__2]:
                self.state = 367
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
        self.enterRule(localctx, 46, self.RULE_metaDict)
        hasV=False
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(VarDefParser.T__2)
            self.state = 375
            localctx.d = self.dict_pair()
            if localctx.d.hasV: localctx.hasV = True
            localctx.x = localctx.d.x	

            self.state = 383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 377
                self.match(VarDefParser.T__0)
                self.state = 378
                localctx.d = self.dict_pair()
                if localctx.d.hasV: localctx.hasV = True
                localctx.x = localctx.x+','+localctx.d.x	

                self.state = 385
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 386
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
        self.enterRule(localctx, 48, self.RULE_dict_pair)
        r1='';r2=''
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.SYSCONST, VarDefParser.ID]:
                self.state = 390
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VarDefParser.ID]:
                    self.state = 388
                    localctx.i1 = self.match(VarDefParser.ID)
                    pass
                elif token in [VarDefParser.SYSCONST]:
                    self.state = 389
                    localctx.i1 = self.match(VarDefParser.SYSCONST)
                    pass
                else:
                    raise NoViableAltException(self)

                localctx.hasV = True 
                r1='_cm[\''+str((None if localctx.i1 is None else localctx.i1.text))+'\'].const'

                pass
            elif token in [VarDefParser.STRING]:
                self.state = 393
                localctx.s1 = self.match(VarDefParser.STRING)
                r1=str((None if localctx.s1 is None else localctx.s1.text))
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 395
                localctx.s11 = self.number()
                r1=str((None if localctx.s11 is None else self._input.getText((localctx.s11.start,localctx.s11.stop))))
                pass
            else:
                raise NoViableAltException(self)

            self.state = 400
            self.match(VarDefParser.T__5)
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.ID]:
                self.state = 401
                localctx.i2 = self.match(VarDefParser.ID)
                localctx.hasV = True 
                r2='_cm[\''+str((None if localctx.i2 is None else localctx.i2.text))+'\'].const'

                pass
            elif token in [VarDefParser.STRING]:
                self.state = 403
                localctx.s2 = self.match(VarDefParser.STRING)
                r2=str((None if localctx.s2 is None else localctx.s2.text))
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 405
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
        self.enterRule(localctx, 50, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                s=''
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 416
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 420
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 423
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 427
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 429
                localctx.i = self.match(VarDefParser.SYSARRAY)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();localctx.x=self.ifsAppend+"['"+vName+"']"+"[i]"
                pass

            elif la_ == 4:
                self.state = 431
                localctx.i = self.match(VarDefParser.SYSCONST)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();localctx.x=self.ifsAppend+"['"+vName+"']"
                pass

            elif la_ == 5:
                self.state = 433
                localctx.i = self.match(VarDefParser.ID)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();
                if vName in self.allVars:
                	if vName in self.constMap.keys():
                		localctx.x=str((None if localctx.i is None else localctx.i.text)).lower()
                	else:
                		localctx.x=self.ifsAppend+"['"+vName+"']"+"[i]"	

                pass

            elif la_ == 6:
                self.state = 435
                localctx.i = self.match(VarDefParser.ID)
                self.state = 436
                self.match(VarDefParser.T__4)
                self.state = 437
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
                self.state = 440
                self.match(VarDefParser.T__6)
                self.state = 441
                localctx.a = self.ee(0)
                self.state = 442
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.a.x)+")"
                pass

            elif la_ == 8:
                self.state = 445
                localctx.i = self.match(VarDefParser.STRING)
                localctx.x=  str((None if localctx.i is None else localctx.i.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 461
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 459
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 449
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 450
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 451
                        localctx.b = self.ee(11)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 454
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 455
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 456
                        localctx.b = self.ee(10)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 463
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_compare, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 465
                localctx.a = self.ee(0)
                self.state = 466
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10) | (1 << VarDefParser.T__11) | (1 << VarDefParser.T__12) | (1 << VarDefParser.T__13))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 467
                localctx.b = self.ee(0)
                localctx.x=str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 470
                self.match(VarDefParser.T__6)
                self.state = 471
                localctx.c = self.compare(0)
                self.state = 472
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 484
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VarDefParser.CompareContext(self, _parentctx, _parentState)
                    localctx.c1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare)
                    self.state = 477
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 478
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 479
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 486
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

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
        self.enterRule(localctx, 56, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            localctx.i = self.id2()
            self.state = 488
            self.match(VarDefParser.T__1)
            self.state = 489
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
        self.enterRule(localctx, 58, self.RULE_id2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(VarDefParser.ID)
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 493
                self.match(VarDefParser.T__4)
                self.state = 494
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
        self.enterRule(localctx, 60, self.RULE_if_stat)
        ifs=collections.OrderedDict();al=[];
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(VarDefParser.IF)
            self.state = 498
            localctx.c = self.compare(0)
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 499
                self.match(VarDefParser.NL)
                self.state = 504
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 505
            self.match(VarDefParser.T__2)
            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 506
                self.match(VarDefParser.NL)
                self.state = 511
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 520 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 512
                localctx.a = self.assign()
                t=str(localctx.a.x).lower();al.append(t)
                self.state = 517
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 514
                    self.match(VarDefParser.NL)
                    self.state = 519
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 522 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 524
            self.match(VarDefParser.T__3)
            self.state = 528
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 525
                    self.match(VarDefParser.NL) 
                self.state = 530
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

            k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
            self.state = 570
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 532
                self.match(VarDefParser.ELSEIF)
                self.state = 533
                localctx.c = self.compare(0)
                self.state = 537
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 534
                    self.match(VarDefParser.NL)
                    self.state = 539
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 540
                self.match(VarDefParser.T__2)
                self.state = 544
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 541
                    self.match(VarDefParser.NL)
                    self.state = 546
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 555 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 547
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 552
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 549
                        self.match(VarDefParser.NL)
                        self.state = 554
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 557 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 559
                self.match(VarDefParser.T__3)
                self.state = 563
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 560
                        self.match(VarDefParser.NL) 
                    self.state = 565
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

                k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
                self.state = 572
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 573
                self.match(VarDefParser.ELSE)
                self.state = 577
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 574
                    self.match(VarDefParser.NL)
                    self.state = 579
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 580
                self.match(VarDefParser.T__2)
                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 581
                    self.match(VarDefParser.NL)
                    self.state = 586
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 595 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 587
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 592
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 589
                        self.match(VarDefParser.NL)
                        self.state = 594
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 597 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 599
                self.match(VarDefParser.T__3)
                self.state = 601 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 600
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 603 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

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
        self._predicates[26] = self.ee_sempred
        self._predicates[27] = self.compare_sempred
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
         




