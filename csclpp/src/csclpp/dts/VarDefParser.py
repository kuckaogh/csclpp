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
        buf.write(u".\u0207\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\3")
        buf.write(u"\2\7\2;\n\2\f\2\16\2>\13\2\3\2\6\2A\n\2\r\2\16\2B\3\3")
        buf.write(u"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\6\4M\n\4\r\4\16\4N\3\4\6")
        buf.write(u"\4R\n\4\r\4\16\4S\3\4\3\4\6\4X\n\4\r\4\16\4Y\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write(u"j\n\5\3\5\6\5m\n\5\r\5\16\5n\3\6\3\6\5\6s\n\6\3\7\3\7")
        buf.write(u"\3\7\3\7\7\7y\n\7\f\7\16\7|\13\7\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\5\b\u0086\n\b\3\b\3\b\3\t\3\t\5\t\u008c")
        buf.write(u"\n\t\3\t\3\t\3\t\3\t\7\t\u0092\n\t\f\t\16\t\u0095\13")
        buf.write(u"\t\3\n\3\n\5\n\u0099\n\n\3\n\3\n\3\n\3\13\3\13\5\13\u00a0")
        buf.write(u"\n\13\3\13\3\13\3\13\5\13\u00a5\n\13\3\13\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\5\13\u00ad\n\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\5\13\u00b5\n\13\3\13\3\13\7\13\u00b9\n\13\f\13")
        buf.write(u"\16\13\u00bc\13\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\5\r")
        buf.write(u"\u00c5\n\r\3\r\3\r\3\r\3\r\3\r\5\r\u00cc\n\r\3\r\3\r")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5")
        buf.write(u"\16\u00da\n\16\3\16\3\16\3\16\5\16\u00df\n\16\3\16\3")
        buf.write(u"\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00ea\n\17")
        buf.write(u"\f\17\16\17\u00ed\13\17\3\17\3\17\3\20\3\20\5\20\u00f3")
        buf.write(u"\n\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00fb\n\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0105\n\20")
        buf.write(u"\3\20\3\20\3\21\3\21\3\22\3\22\3\22\5\22\u010e\n\22\3")
        buf.write(u"\22\3\22\3\22\3\22\3\23\3\23\5\23\u0116\n\23\3\23\3\23")
        buf.write(u"\3\23\3\23\3\24\3\24\3\24\3\24\5\24\u0120\n\24\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\5\24\u0127\n\24\3\24\3\24\3\24\3\24")
        buf.write(u"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0134\n\24\3")
        buf.write(u"\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24")
        buf.write(u"\u0140\n\24\f\24\16\24\u0143\13\24\3\25\3\25\3\25\3\25")
        buf.write(u"\5\25\u0149\n\25\3\25\3\25\3\25\3\25\3\25\5\25\u0150")
        buf.write(u"\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5")
        buf.write(u"\25\u015b\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\5\25\u0165\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\7\25\u0171\n\25\f\25\16\25\u0174\13\25")
        buf.write(u"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write(u"\26\5\26\u0181\n\26\3\26\3\26\3\26\3\26\3\26\7\26\u0188")
        buf.write(u"\n\26\f\26\16\26\u018b\13\26\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\30\3\30\3\30\5\30\u0195\n\30\3\31\3\31\3\31\7\31\u019a")
        buf.write(u"\n\31\f\31\16\31\u019d\13\31\3\31\3\31\7\31\u01a1\n\31")
        buf.write(u"\f\31\16\31\u01a4\13\31\3\31\3\31\3\31\7\31\u01a9\n\31")
        buf.write(u"\f\31\16\31\u01ac\13\31\6\31\u01ae\n\31\r\31\16\31\u01af")
        buf.write(u"\3\31\3\31\7\31\u01b4\n\31\f\31\16\31\u01b7\13\31\3\31")
        buf.write(u"\3\31\3\31\3\31\7\31\u01bd\n\31\f\31\16\31\u01c0\13\31")
        buf.write(u"\3\31\3\31\7\31\u01c4\n\31\f\31\16\31\u01c7\13\31\3\31")
        buf.write(u"\3\31\3\31\7\31\u01cc\n\31\f\31\16\31\u01cf\13\31\6\31")
        buf.write(u"\u01d1\n\31\r\31\16\31\u01d2\3\31\3\31\7\31\u01d7\n\31")
        buf.write(u"\f\31\16\31\u01da\13\31\3\31\3\31\7\31\u01de\n\31\f\31")
        buf.write(u"\16\31\u01e1\13\31\3\31\3\31\7\31\u01e5\n\31\f\31\16")
        buf.write(u"\31\u01e8\13\31\3\31\3\31\7\31\u01ec\n\31\f\31\16\31")
        buf.write(u"\u01ef\13\31\3\31\3\31\3\31\7\31\u01f4\n\31\f\31\16\31")
        buf.write(u"\u01f7\13\31\6\31\u01f9\n\31\r\31\16\31\u01fa\3\31\3")
        buf.write(u"\31\6\31\u01ff\n\31\r\31\16\31\u0200\3\31\3\31\5\31\u0205")
        buf.write(u"\n\31\3\31\2\5&(*\32\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write(u"\34\36 \"$&(*,.\60\2\7\4\2))++\3\2\24\25\3\2\26\27\3")
        buf.write(u"\2\13\20\3\2\30\31\u023e\2\65\3\2\2\2\4D\3\2\2\2\6H\3")
        buf.write(u"\2\2\2\bi\3\2\2\2\nr\3\2\2\2\ft\3\2\2\2\16}\3\2\2\2\20")
        buf.write(u"\u008b\3\2\2\2\22\u0098\3\2\2\2\24\u009f\3\2\2\2\26\u00bf")
        buf.write(u"\3\2\2\2\30\u00c4\3\2\2\2\32\u00cf\3\2\2\2\34\u00e2\3")
        buf.write(u"\2\2\2\36\u00fa\3\2\2\2 \u0108\3\2\2\2\"\u010a\3\2\2")
        buf.write(u"\2$\u0115\3\2\2\2&\u0133\3\2\2\2(\u0164\3\2\2\2*\u0180")
        buf.write(u"\3\2\2\2,\u018c\3\2\2\2.\u0191\3\2\2\2\60\u0196\3\2\2")
        buf.write(u"\2\62\64\7-\2\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63\3\2")
        buf.write(u"\2\2\65\66\3\2\2\2\668\3\2\2\2\67\65\3\2\2\28<\5\4\3")
        buf.write(u"\29;\7-\2\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=")
        buf.write(u"@\3\2\2\2><\3\2\2\2?A\5\6\4\2@?\3\2\2\2AB\3\2\2\2B@\3")
        buf.write(u"\2\2\2BC\3\2\2\2C\3\3\2\2\2DE\7\32\2\2EF\7*\2\2FG\b\3")
        buf.write(u"\1\2G\5\3\2\2\2HI\7\34\2\2IJ\7*\2\2JL\b\4\1\2KM\7-\2")
        buf.write(u"\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2")
        buf.write(u"PR\5\b\5\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TU")
        buf.write(u"\3\2\2\2UW\7\35\2\2VX\7-\2\2WV\3\2\2\2XY\3\2\2\2YW\3")
        buf.write(u"\2\2\2YZ\3\2\2\2Z\7\3\2\2\2[j\5\30\r\2\\j\5\32\16\2]")
        buf.write(u"^\5$\23\2^_\b\5\1\2_j\3\2\2\2`a\5\"\22\2ab\b\5\1\2bj")
        buf.write(u"\3\2\2\2cd\5\60\31\2de\b\5\1\2ej\3\2\2\2fj\5\n\6\2gj")
        buf.write(u"\5\26\f\2hj\5\f\7\2i[\3\2\2\2i\\\3\2\2\2i]\3\2\2\2i`")
        buf.write(u"\3\2\2\2ic\3\2\2\2if\3\2\2\2ig\3\2\2\2ih\3\2\2\2jl\3")
        buf.write(u"\2\2\2km\7-\2\2lk\3\2\2\2mn\3\2\2\2nl\3\2\2\2no\3\2\2")
        buf.write(u"\2o\t\3\2\2\2ps\5\20\t\2qs\5\24\13\2rp\3\2\2\2rq\3\2")
        buf.write(u"\2\2s\13\3\2\2\2tu\7&\2\2uz\5\16\b\2vw\7\3\2\2wy\5\16")
        buf.write(u"\b\2xv\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\r\3\2\2")
        buf.write(u"\2|z\3\2\2\2}~\7*\2\2~\u0085\7\4\2\2\177\u0080\7)\2\2")
        buf.write(u"\u0080\u0086\b\b\1\2\u0081\u0082\7+\2\2\u0082\u0086\b")
        buf.write(u"\b\1\2\u0083\u0084\7,\2\2\u0084\u0086\b\b\1\2\u0085\177")
        buf.write(u"\3\2\2\2\u0085\u0081\3\2\2\2\u0085\u0083\3\2\2\2\u0086")
        buf.write(u"\u0087\3\2\2\2\u0087\u0088\b\b\1\2\u0088\17\3\2\2\2\u0089")
        buf.write(u"\u008c\7#\2\2\u008a\u008c\7$\2\2\u008b\u0089\3\2\2\2")
        buf.write(u"\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d")
        buf.write(u"\3\2\2\2\u008d\u008e\7\36\2\2\u008e\u0093\5\22\n\2\u008f")
        buf.write(u"\u0090\7\3\2\2\u0090\u0092\5\22\n\2\u0091\u008f\3\2\2")
        buf.write(u"\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094")
        buf.write(u"\3\2\2\2\u0094\21\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097")
        buf.write(u"\7\22\2\2\u0097\u0099\b\n\1\2\u0098\u0096\3\2\2\2\u0098")
        buf.write(u"\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\7*\2\2")
        buf.write(u"\u009b\u009c\b\n\1\2\u009c\23\3\2\2\2\u009d\u00a0\7#")
        buf.write(u"\2\2\u009e\u00a0\7$\2\2\u009f\u009d\3\2\2\2\u009f\u009e")
        buf.write(u"\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write(u"\u00a4\7\36\2\2\u00a2\u00a3\7\22\2\2\u00a3\u00a5\b\13")
        buf.write(u"\1\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6")
        buf.write(u"\3\2\2\2\u00a6\u00a7\7*\2\2\u00a7\u00a8\b\13\1\2\u00a8")
        buf.write(u"\u00a9\7\5\2\2\u00a9\u00ac\b\13\1\2\u00aa\u00ab\7\22")
        buf.write(u"\2\2\u00ab\u00ad\b\13\1\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad")
        buf.write(u"\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\7*\2\2\u00af")
        buf.write(u"\u00ba\b\13\1\2\u00b0\u00b1\7\3\2\2\u00b1\u00b4\b\13")
        buf.write(u"\1\2\u00b2\u00b3\7\22\2\2\u00b3\u00b5\b\13\1\2\u00b4")
        buf.write(u"\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2")
        buf.write(u"\2\u00b6\u00b7\7*\2\2\u00b7\u00b9\b\13\1\2\u00b8\u00b0")
        buf.write(u"\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write(u"\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3\2\2")
        buf.write(u"\2\u00bd\u00be\7\6\2\2\u00be\25\3\2\2\2\u00bf\u00c0\7")
        buf.write(u"\33\2\2\u00c0\u00c1\7*\2\2\u00c1\27\3\2\2\2\u00c2\u00c3")
        buf.write(u"\7\22\2\2\u00c3\u00c5\b\r\1\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write(u"\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\7*\2\2")
        buf.write(u"\u00c7\u00c8\7\4\2\2\u00c8\u00cb\7\23\2\2\u00c9\u00ca")
        buf.write(u"\7\3\2\2\u00ca\u00cc\7,\2\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write(u"\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\b\r\1")
        buf.write(u"\2\u00ce\31\3\2\2\2\u00cf\u00d0\5.\30\2\u00d0\u00d1\7")
        buf.write(u"\7\2\2\u00d1\u00d2\7*\2\2\u00d2\u00de\7\4\2\2\u00d3\u00d4")
        buf.write(u"\7)\2\2\u00d4\u00da\b\16\1\2\u00d5\u00d6\7+\2\2\u00d6")
        buf.write(u"\u00da\b\16\1\2\u00d7\u00d8\7,\2\2\u00d8\u00da\b\16\1")
        buf.write(u"\2\u00d9\u00d3\3\2\2\2\u00d9\u00d5\3\2\2\2\u00d9\u00d7")
        buf.write(u"\3\2\2\2\u00da\u00df\3\2\2\2\u00db\u00dc\5\34\17\2\u00dc")
        buf.write(u"\u00dd\b\16\1\2\u00dd\u00df\3\2\2\2\u00de\u00d9\3\2\2")
        buf.write(u"\2\u00de\u00db\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1")
        buf.write(u"\b\16\1\2\u00e1\33\3\2\2\2\u00e2\u00e3\7\5\2\2\u00e3")
        buf.write(u"\u00e4\5\36\20\2\u00e4\u00eb\b\17\1\2\u00e5\u00e6\7\3")
        buf.write(u"\2\2\u00e6\u00e7\5\36\20\2\u00e7\u00e8\b\17\1\2\u00e8")
        buf.write(u"\u00ea\3\2\2\2\u00e9\u00e5\3\2\2\2\u00ea\u00ed\3\2\2")
        buf.write(u"\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ee")
        buf.write(u"\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef\7\6\2\2\u00ef")
        buf.write(u"\35\3\2\2\2\u00f0\u00f3\7*\2\2\u00f1\u00f3\7(\2\2\u00f2")
        buf.write(u"\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f4\3\2\2")
        buf.write(u"\2\u00f4\u00fb\b\20\1\2\u00f5\u00f6\7,\2\2\u00f6\u00fb")
        buf.write(u"\b\20\1\2\u00f7\u00f8\5 \21\2\u00f8\u00f9\b\20\1\2\u00f9")
        buf.write(u"\u00fb\3\2\2\2\u00fa\u00f2\3\2\2\2\u00fa\u00f5\3\2\2")
        buf.write(u"\2\u00fa\u00f7\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u0104")
        buf.write(u"\7\b\2\2\u00fd\u00fe\7*\2\2\u00fe\u0105\b\20\1\2\u00ff")
        buf.write(u"\u0100\7,\2\2\u0100\u0105\b\20\1\2\u0101\u0102\5 \21")
        buf.write(u"\2\u0102\u0103\b\20\1\2\u0103\u0105\3\2\2\2\u0104\u00fd")
        buf.write(u"\3\2\2\2\u0104\u00ff\3\2\2\2\u0104\u0101\3\2\2\2\u0105")
        buf.write(u"\u0106\3\2\2\2\u0106\u0107\b\20\1\2\u0107\37\3\2\2\2")
        buf.write(u"\u0108\u0109\t\2\2\2\u0109!\3\2\2\2\u010a\u010d\7\36")
        buf.write(u"\2\2\u010b\u010c\7\22\2\2\u010c\u010e\b\22\1\2\u010d")
        buf.write(u"\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\3\2\2")
        buf.write(u"\2\u010f\u0110\7*\2\2\u0110\u0111\7\4\2\2\u0111\u0112")
        buf.write(u"\5(\25\2\u0112#\3\2\2\2\u0113\u0114\7\22\2\2\u0114\u0116")
        buf.write(u"\b\23\1\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write(u"\u0117\3\2\2\2\u0117\u0118\7*\2\2\u0118\u0119\7\4\2\2")
        buf.write(u"\u0119\u011a\5(\25\2\u011a%\3\2\2\2\u011b\u011c\b\24")
        buf.write(u"\1\2\u011c\u011f\b\24\1\2\u011d\u011e\7\27\2\2\u011e")
        buf.write(u"\u0120\b\24\1\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2")
        buf.write(u"\2\u0120\u0121\3\2\2\2\u0121\u0122\7+\2\2\u0122\u0134")
        buf.write(u"\b\24\1\2\u0123\u0126\b\24\1\2\u0124\u0125\7\27\2\2\u0125")
        buf.write(u"\u0127\b\24\1\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2")
        buf.write(u"\2\u0127\u0128\3\2\2\2\u0128\u0129\7)\2\2\u0129\u0134")
        buf.write(u"\b\24\1\2\u012a\u012b\7*\2\2\u012b\u0134\b\24\1\2\u012c")
        buf.write(u"\u012d\7\t\2\2\u012d\u012e\5&\24\2\u012e\u012f\7\n\2")
        buf.write(u"\2\u012f\u0130\b\24\1\2\u0130\u0134\3\2\2\2\u0131\u0132")
        buf.write(u"\7,\2\2\u0132\u0134\b\24\1\2\u0133\u011b\3\2\2\2\u0133")
        buf.write(u"\u0123\3\2\2\2\u0133\u012a\3\2\2\2\u0133\u012c\3\2\2")
        buf.write(u"\2\u0133\u0131\3\2\2\2\u0134\u0141\3\2\2\2\u0135\u0136")
        buf.write(u"\f\t\2\2\u0136\u0137\t\3\2\2\u0137\u0138\5&\24\n\u0138")
        buf.write(u"\u0139\b\24\1\2\u0139\u0140\3\2\2\2\u013a\u013b\f\b\2")
        buf.write(u"\2\u013b\u013c\t\4\2\2\u013c\u013d\5&\24\t\u013d\u013e")
        buf.write(u"\b\24\1\2\u013e\u0140\3\2\2\2\u013f\u0135\3\2\2\2\u013f")
        buf.write(u"\u013a\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2")
        buf.write(u"\2\u0141\u0142\3\2\2\2\u0142\'\3\2\2\2\u0143\u0141\3")
        buf.write(u"\2\2\2\u0144\u0145\b\25\1\2\u0145\u0148\b\25\1\2\u0146")
        buf.write(u"\u0147\7\27\2\2\u0147\u0149\b\25\1\2\u0148\u0146\3\2")
        buf.write(u"\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b")
        buf.write(u"\7+\2\2\u014b\u0165\b\25\1\2\u014c\u014f\b\25\1\2\u014d")
        buf.write(u"\u014e\7\27\2\2\u014e\u0150\b\25\1\2\u014f\u014d\3\2")
        buf.write(u"\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152")
        buf.write(u"\7)\2\2\u0152\u0165\b\25\1\2\u0153\u0154\7\'\2\2\u0154")
        buf.write(u"\u0165\b\25\1\2\u0155\u0156\7(\2\2\u0156\u0165\b\25\1")
        buf.write(u"\2\u0157\u015a\7*\2\2\u0158\u0159\7\7\2\2\u0159\u015b")
        buf.write(u"\7*\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write(u"\u015c\3\2\2\2\u015c\u0165\b\25\1\2\u015d\u015e\7\t\2")
        buf.write(u"\2\u015e\u015f\5(\25\2\u015f\u0160\7\n\2\2\u0160\u0161")
        buf.write(u"\b\25\1\2\u0161\u0165\3\2\2\2\u0162\u0163\7,\2\2\u0163")
        buf.write(u"\u0165\b\25\1\2\u0164\u0144\3\2\2\2\u0164\u014c\3\2\2")
        buf.write(u"\2\u0164\u0153\3\2\2\2\u0164\u0155\3\2\2\2\u0164\u0157")
        buf.write(u"\3\2\2\2\u0164\u015d\3\2\2\2\u0164\u0162\3\2\2\2\u0165")
        buf.write(u"\u0172\3\2\2\2\u0166\u0167\f\13\2\2\u0167\u0168\t\3\2")
        buf.write(u"\2\u0168\u0169\5(\25\f\u0169\u016a\b\25\1\2\u016a\u0171")
        buf.write(u"\3\2\2\2\u016b\u016c\f\n\2\2\u016c\u016d\t\4\2\2\u016d")
        buf.write(u"\u016e\5(\25\13\u016e\u016f\b\25\1\2\u016f\u0171\3\2")
        buf.write(u"\2\2\u0170\u0166\3\2\2\2\u0170\u016b\3\2\2\2\u0171\u0174")
        buf.write(u"\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write(u")\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176\b\26\1\2\u0176")
        buf.write(u"\u0177\5(\25\2\u0177\u0178\t\5\2\2\u0178\u0179\5(\25")
        buf.write(u"\2\u0179\u017a\b\26\1\2\u017a\u0181\3\2\2\2\u017b\u017c")
        buf.write(u"\7\t\2\2\u017c\u017d\5*\26\2\u017d\u017e\7\n\2\2\u017e")
        buf.write(u"\u017f\b\26\1\2\u017f\u0181\3\2\2\2\u0180\u0175\3\2\2")
        buf.write(u"\2\u0180\u017b\3\2\2\2\u0181\u0189\3\2\2\2\u0182\u0183")
        buf.write(u"\f\3\2\2\u0183\u0184\t\6\2\2\u0184\u0185\5*\26\4\u0185")
        buf.write(u"\u0186\b\26\1\2\u0186\u0188\3\2\2\2\u0187\u0182\3\2\2")
        buf.write(u"\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a")
        buf.write(u"\3\2\2\2\u018a+\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d")
        buf.write(u"\5.\30\2\u018d\u018e\7\4\2\2\u018e\u018f\5(\25\2\u018f")
        buf.write(u"\u0190\b\27\1\2\u0190-\3\2\2\2\u0191\u0194\7*\2\2\u0192")
        buf.write(u"\u0193\7\7\2\2\u0193\u0195\7*\2\2\u0194\u0192\3\2\2\2")
        buf.write(u"\u0194\u0195\3\2\2\2\u0195/\3\2\2\2\u0196\u0197\7\37")
        buf.write(u"\2\2\u0197\u019b\5*\26\2\u0198\u019a\7-\2\2\u0199\u0198")
        buf.write(u"\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write(u"\u019c\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u019b\3\2\2")
        buf.write(u"\2\u019e\u01a2\7\5\2\2\u019f\u01a1\7-\2\2\u01a0\u019f")
        buf.write(u"\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write(u"\u01a3\3\2\2\2\u01a3\u01ad\3\2\2\2\u01a4\u01a2\3\2\2")
        buf.write(u"\2\u01a5\u01a6\5,\27\2\u01a6\u01aa\b\31\1\2\u01a7\u01a9")
        buf.write(u"\7-\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa")
        buf.write(u"\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ae\3\2\2")
        buf.write(u"\2\u01ac\u01aa\3\2\2\2\u01ad\u01a5\3\2\2\2\u01ae\u01af")
        buf.write(u"\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write(u"\u01b1\3\2\2\2\u01b1\u01b5\7\6\2\2\u01b2\u01b4\7-\2\2")
        buf.write(u"\u01b3\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3")
        buf.write(u"\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7")
        buf.write(u"\u01b5\3\2\2\2\u01b8\u01df\b\31\1\2\u01b9\u01ba\7 \2")
        buf.write(u"\2\u01ba\u01be\5*\26\2\u01bb\u01bd\7-\2\2\u01bc\u01bb")
        buf.write(u"\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be")
        buf.write(u"\u01bf\3\2\2\2\u01bf\u01c1\3\2\2\2\u01c0\u01be\3\2\2")
        buf.write(u"\2\u01c1\u01c5\7\5\2\2\u01c2\u01c4\7-\2\2\u01c3\u01c2")
        buf.write(u"\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5")
        buf.write(u"\u01c6\3\2\2\2\u01c6\u01d0\3\2\2\2\u01c7\u01c5\3\2\2")
        buf.write(u"\2\u01c8\u01c9\5,\27\2\u01c9\u01cd\b\31\1\2\u01ca\u01cc")
        buf.write(u"\7-\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd")
        buf.write(u"\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d1\3\2\2")
        buf.write(u"\2\u01cf\u01cd\3\2\2\2\u01d0\u01c8\3\2\2\2\u01d1\u01d2")
        buf.write(u"\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write(u"\u01d4\3\2\2\2\u01d4\u01d8\7\6\2\2\u01d5\u01d7\7-\2\2")
        buf.write(u"\u01d6\u01d5\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6")
        buf.write(u"\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01db\3\2\2\2\u01da")
        buf.write(u"\u01d8\3\2\2\2\u01db\u01dc\b\31\1\2\u01dc\u01de\3\2\2")
        buf.write(u"\2\u01dd\u01b9\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd")
        buf.write(u"\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u0204\3\2\2\2\u01e1")
        buf.write(u"\u01df\3\2\2\2\u01e2\u01e6\7!\2\2\u01e3\u01e5\7-\2\2")
        buf.write(u"\u01e4\u01e3\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4")
        buf.write(u"\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e9\3\2\2\2\u01e8")
        buf.write(u"\u01e6\3\2\2\2\u01e9\u01ed\7\5\2\2\u01ea\u01ec\7-\2\2")
        buf.write(u"\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb")
        buf.write(u"\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f8\3\2\2\2\u01ef")
        buf.write(u"\u01ed\3\2\2\2\u01f0\u01f1\5,\27\2\u01f1\u01f5\b\31\1")
        buf.write(u"\2\u01f2\u01f4\7-\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f7")
        buf.write(u"\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write(u"\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01f0\3\2\2")
        buf.write(u"\2\u01f9\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb")
        buf.write(u"\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fe\7\6\2\2\u01fd")
        buf.write(u"\u01ff\7-\2\2\u01fe\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2")
        buf.write(u"\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0202")
        buf.write(u"\3\2\2\2\u0202\u0203\b\31\1\2\u0203\u0205\3\2\2\2\u0204")
        buf.write(u"\u01e2\3\2\2\2\u0204\u0205\3\2\2\2\u0205\61\3\2\2\2>")
        buf.write(u"\65<BNSYinrz\u0085\u008b\u0093\u0098\u009f\u00a4\u00ac")
        buf.write(u"\u00b4\u00ba\u00c4\u00cb\u00d9\u00de\u00eb\u00f2\u00fa")
        buf.write(u"\u0104\u010d\u0115\u011f\u0126\u0133\u013f\u0141\u0148")
        buf.write(u"\u014f\u015a\u0164\u0170\u0172\u0180\u0189\u0194\u019b")
        buf.write(u"\u01a2\u01aa\u01af\u01b5\u01be\u01c5\u01cd\u01d2\u01d8")
        buf.write(u"\u01df\u01e6\u01ed\u01f5\u01fa\u0200\u0204")
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
                     u"'int'", u"'float'", u"'const'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"LINE_COMMENT", 
                      u"T", u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", u"AND", 
                      u"OR", u"USE", u"INCLUDE", u"VARDEF", u"END", u"ARRAY", 
                      u"IF", u"ELSEIF", u"ELSE", u"GROUP", u"STRING_L", 
                      u"INT_L", u"FLOAT_L", u"CONST", u"SYSARRAY", u"SYSCONST", 
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
    RULE_stat_define = 16
    RULE_stat = 17
    RULE_ee_dts = 18
    RULE_ee = 19
    RULE_compare = 20
    RULE_assign = 21
    RULE_id2 = 22
    RULE_if_stat = 23

    ruleNames =  [ u"prog", u"use", u"vardef", u"field", u"new_var", u"constant", 
                   u"const_var", u"array", u"array_var", u"array_cluster", 
                   u"include", u"var_path", u"var_meta", u"metaDict", u"dict_pair", 
                   u"number", u"stat_define", u"stat", u"ee_dts", u"ee", 
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
    systemVars=['year','month','oct','nov','dec','jan','feb','mar','apr','may','jun','jul','aug','sep'];
    allVars=[];


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
        self.allVars=list(self.systemVars);

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ARRAY) | (1 << VarDefParser.IF) | (1 << VarDefParser.STRING_L) | (1 << VarDefParser.INT_L) | (1 << VarDefParser.CONST) | (1 << VarDefParser.ID))) != 0)):
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


        def stat_define(self):
            return self.getTypedRuleContext(VarDefParser.Stat_defineContext,0)


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
            self.state = 103
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
                self.ifid=self.ifid+1;
                pass

            elif la_ == 4:
                self.state = 94
                self.stat_define()
                self.ifid=self.ifid+1;
                pass

            elif la_ == 5:
                self.state = 97
                self.if_stat()
                self.ifid=self.ifid+1;
                pass

            elif la_ == 6:
                self.state = 100
                self.new_var()
                pass

            elif la_ == 7:
                self.state = 101
                self.include()
                pass

            elif la_ == 8:
                self.state = 102
                self.constant()
                pass


            self.state = 106 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 105
                self.match(VarDefParser.NL)
                self.state = 108 
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
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
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
            self.state = 114
            self.match(VarDefParser.CONST)
            self.state = 115
            self.const_var()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 116
                self.match(VarDefParser.T__0)
                self.state = 117
                self.const_var()
                self.state = 122
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
            self.state = 123
            localctx.i = self.match(VarDefParser.ID)
            self.state = 124
            self.match(VarDefParser.T__1)
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT]:
                self.state = 125
                localctx.c = self.match(VarDefParser.FLOAT)
                v.const=float((None if localctx.c is None else localctx.c.text))
                pass
            elif token in [VarDefParser.INT]:
                self.state = 127
                localctx.c = self.match(VarDefParser.INT)
                v.const=int((None if localctx.c is None else localctx.c.text));v.metaData['_dataType']=np.int;
                pass
            elif token in [VarDefParser.STRING]:
                self.state = 129
                localctx.c = self.match(VarDefParser.STRING)
                v.const=str((None if localctx.c is None else localctx.c.text));v.metaData['_dataType']=np.str;
                pass
            else:
                raise NoViableAltException(self)

            name=str((None if localctx.i is None else localctx.i.text)).lower();self.newConstMap[name]=v;
            if name in self.allVars:
            	Err.addError(name+' is already defined.', self.vardefFile, self.vardefName)
            else:
            	self.allVars.append(name)	

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
            self.g = None # Token

        def ARRAY(self):
            return self.getToken(VarDefParser.ARRAY, 0)

        def array_var(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.Array_varContext)
            else:
                return self.getTypedRuleContext(VarDefParser.Array_varContext,i)


        def STRING_L(self):
            return self.getToken(VarDefParser.STRING_L, 0)

        def INT_L(self):
            return self.getToken(VarDefParser.INT_L, 0)

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
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.STRING_L]:
                self.state = 135
                localctx.l = self.match(VarDefParser.STRING_L)
                pass
            elif token in [VarDefParser.INT_L]:
                self.state = 136
                localctx.g = self.match(VarDefParser.INT_L)
                pass
            elif token in [VarDefParser.ARRAY]:
                pass
            else:
                raise NoViableAltException(self)
            self.state = 139
            self.match(VarDefParser.ARRAY)
            self.state = 140
            self.array_var(localctx.l!=None,localctx.g!=None)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 141
                self.match(VarDefParser.T__0)
                self.state = 142
                self.array_var(localctx.l!=None,localctx.g!=None)
                self.state = 147
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

        def __init__(self, parser, parent=None, invokingState=-1, isStr=None, isInt=None):
            super(VarDefParser.Array_varContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.isStr = None
            self.isInt = None
            self.i = None # Token
            self.isStr = isStr
            self.isInt = isInt

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




    def array_var(self, isStr, isInt):

        localctx = VarDefParser.Array_varContext(self, self._ctx, self.state, isStr, isInt)
        self.enterRule(localctx, 16, self.RULE_array_var)
        isTemp=False;
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 148
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 152
            localctx.i = self.match(VarDefParser.ID)
            v = Var('');name=str((None if localctx.i is None else localctx.i.text)).lower();
            if name in self.allVars:
            	Err.addError(name+' is already defined.', self.vardefFile, self.vardefName)
            else:
            	self.allVars.append(name)
            if isStr:
            	v.metaData['_dataType']=np.str
            	print (name+' is string')
            if isInt:
            	v.metaData['_dataType']=np.int
            	print (name+' is integer')
            if not isStr and not isInt:
            	print (name+' is float')
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
            self.g = None # Token
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

        def INT_L(self):
            return self.getToken(VarDefParser.INT_L, 0)

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
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.STRING_L]:
                self.state = 155
                localctx.l = self.match(VarDefParser.STRING_L)
                pass
            elif token in [VarDefParser.INT_L]:
                self.state = 156
                localctx.g = self.match(VarDefParser.INT_L)
                pass
            elif token in [VarDefParser.ARRAY]:
                pass
            else:
                raise NoViableAltException(self)
            self.state = 159
            self.match(VarDefParser.ARRAY)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 160
                self.match(VarDefParser.T)
                isGroupTemp=True


            self.state = 164
            localctx.i = self.match(VarDefParser.ID)
            header=str((None if localctx.i is None else localctx.i.text));
            self.state = 166
            self.match(VarDefParser.T__2)
            isTemp=False;
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 168
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 172
            localctx.i = self.match(VarDefParser.ID)
            subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 174
                self.match(VarDefParser.T__0)
                isTemp=False;
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 176
                    self.match(VarDefParser.T)
                    isTemp=True


                self.state = 180
                localctx.i = self.match(VarDefParser.ID)
                subvar[str((None if localctx.i is None else localctx.i.text))]=isTemp;
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(VarDefParser.T__3)
            self._ctx.stop = self._input.LT(-1)

            for k in subvar.keys():
            	o = Var('')
            	name=header.lower()+'.'+k.lower()
            	if name in self.allVars:
            		Err.addError(name+' is already defined.', self.vardefFile, self.vardefName)
            	else:
            		self.allVars.append(name)
            	if localctx.l!=None: 
            		o.metaData['_dataType']=np.str;
            		print (name+' is string')
            	if localctx.g!=None: 
            		o.metaData['_dataType']=np.int;
            		print (name+' is int')
            	if localctx.g==None and localctx.l==None:
            		print (name+' is float')
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
            self.state = 189
            self.match(VarDefParser.INCLUDE)
            self.state = 190
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
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 192
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 196
            localctx.i = self.match(VarDefParser.ID)
            self.state = 197
            self.match(VarDefParser.T__1)
            self.state = 198
            localctx.p = self.match(VarDefParser.PATH)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T__0:
                self.state = 199
                self.match(VarDefParser.T__0)
                self.state = 200
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
        self.enterRule(localctx, 24, self.RULE_var_meta)
        ha=False
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            localctx.i = self.id2()
            self.state = 206
            self.match(VarDefParser.T__4)
            self.state = 207
            localctx.m = self.match(VarDefParser.ID)
            self.state = 208
            self.match(VarDefParser.T__1)
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT, VarDefParser.INT, VarDefParser.STRING]:
                self.state = 215
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VarDefParser.FLOAT]:
                    self.state = 209
                    localctx.k = self.match(VarDefParser.FLOAT)
                    c=float((None if localctx.k is None else localctx.k.text))
                    pass
                elif token in [VarDefParser.INT]:
                    self.state = 211
                    localctx.k = self.match(VarDefParser.INT)
                    c=int((None if localctx.k is None else localctx.k.text))
                    pass
                elif token in [VarDefParser.STRING]:
                    self.state = 213
                    localctx.k = self.match(VarDefParser.STRING)
                    c=str((None if localctx.k is None else localctx.k.text))[1:-1].lower()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [VarDefParser.T__2]:
                self.state = 217
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
            self.state = 224
            self.match(VarDefParser.T__2)
            self.state = 225
            localctx.d = self.dict_pair()
            if localctx.d.hasV: localctx.hasV = True
            localctx.x = localctx.d.x	

            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 227
                self.match(VarDefParser.T__0)
                self.state = 228
                localctx.d = self.dict_pair()
                if localctx.d.hasV: localctx.hasV = True
                localctx.x = localctx.x+','+localctx.d.x	

                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 236
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
        self.enterRule(localctx, 28, self.RULE_dict_pair)
        r1='';r2=''
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.SYSCONST, VarDefParser.ID]:
                self.state = 240
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VarDefParser.ID]:
                    self.state = 238
                    localctx.i1 = self.match(VarDefParser.ID)
                    pass
                elif token in [VarDefParser.SYSCONST]:
                    self.state = 239
                    localctx.i1 = self.match(VarDefParser.SYSCONST)
                    pass
                else:
                    raise NoViableAltException(self)

                localctx.hasV = True 
                r1='_cm[\''+str((None if localctx.i1 is None else localctx.i1.text))+'\'].const'

                pass
            elif token in [VarDefParser.STRING]:
                self.state = 243
                localctx.s1 = self.match(VarDefParser.STRING)
                r1=str((None if localctx.s1 is None else localctx.s1.text))
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 245
                localctx.s11 = self.number()
                r1=str((None if localctx.s11 is None else self._input.getText((localctx.s11.start,localctx.s11.stop))))
                pass
            else:
                raise NoViableAltException(self)

            self.state = 250
            self.match(VarDefParser.T__5)
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.ID]:
                self.state = 251
                localctx.i2 = self.match(VarDefParser.ID)
                localctx.hasV = True 
                r2='_cm[\''+str((None if localctx.i2 is None else localctx.i2.text))+'\'].const'

                pass
            elif token in [VarDefParser.STRING]:
                self.state = 253
                localctx.s2 = self.match(VarDefParser.STRING)
                r2=str((None if localctx.s2 is None else localctx.s2.text))
                pass
            elif token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.state = 255
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
            self.state = 262
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

    class Stat_defineContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.Stat_defineContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self.e = None # EeContext

        def ARRAY(self):
            return self.getToken(VarDefParser.ARRAY, 0)

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def ee(self):
            return self.getTypedRuleContext(VarDefParser.EeContext,0)


        def T(self):
            return self.getToken(VarDefParser.T, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_stat_define

        def accept(self, visitor):
            if hasattr(visitor, "visitStat_define"):
                return visitor.visitStat_define(self)
            else:
                return visitor.visitChildren(self)




    def stat_define(self):

        localctx = VarDefParser.Stat_defineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stat_define)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(VarDefParser.ARRAY)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 265
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 269
            localctx.i = self.match(VarDefParser.ID)
            self.state = 270
            self.match(VarDefParser.T__1)
            self.state = 271
            localctx.e = self.ee(0)
            self._ctx.stop = self._input.LT(-1)

            v = Var('');
            e=str((None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))).lower();v.expr=e;
            name=str((None if localctx.i is None else localctx.i.text)).lower(); self.varExprMap[name]=v; 
            if name in self.allVars:
            	Err.addError(name+' is already defined.', self.vardefFile, self.vardefName)
            else:
            	self.allVars.append(name)
            e2=str(localctx.e.x).lower()
            name2=self.ifsAppend+"['"+str((None if localctx.i is None else localctx.i.text)).lower()+"'][i]"
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
        self.enterRule(localctx, 34, self.RULE_stat)
        isTemp=False;ifs=collections.OrderedDict();k='';
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 273
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 277
            localctx.i = self.match(VarDefParser.ID)
            self.state = 278
            self.match(VarDefParser.T__1)
            self.state = 279
            localctx.e = self.ee(0)
            self._ctx.stop = self._input.LT(-1)

            e=str((None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))).lower();
            name=str((None if localctx.i is None else localctx.i.text)).lower(); 
            if name not in self.allVars:
            	Err.addError(name+' not defined.', self.vardefFile, self.vardefName)

            e2=str(localctx.e.x).lower()
            name2=self.ifsAppend+"['"+str((None if localctx.i is None else localctx.i.text)).lower()+"'][i]"
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_ee_dts, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                s=''
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 283
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 287
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 290
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 294
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 296
                localctx.i = self.match(VarDefParser.ID)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();
                if vName in self.newArrayMap.keys() or vName in self.varPathMap.keys() or vName in self.varExprMap.keys():
                	localctx.x = self.ifsAppend+"['"+vName+"']"
                	#print (vName) 
                else:
                	Err.addError(vName+' not defined.', self.vardefFile, self.vardefName)

                pass

            elif la_ == 4:
                self.state = 298
                self.match(VarDefParser.T__6)
                self.state = 299
                localctx.a = self.ee_dts(0)
                self.state = 300
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.a.x)+")"
                pass

            elif la_ == 5:
                self.state = 303
                localctx.i = self.match(VarDefParser.STRING)
                localctx.x=  str((None if localctx.i is None else localctx.i.text)) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 317
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.Ee_dtsContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee_dts)
                        self.state = 307
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 308
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 309
                        localctx.b = self.ee_dts(8)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.Ee_dtsContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee_dts)
                        self.state = 312
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 313
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 314
                        localctx.b = self.ee_dts(7)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                s=''
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 324
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 328
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 331
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 335
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 337
                localctx.i = self.match(VarDefParser.SYSARRAY)
                vName=str((None if localctx.i is None else localctx.i.text)).lower();localctx.x=self.ifsAppend+"['"+vName+"']"+"[i]"
                pass

            elif la_ == 4:
                self.state = 339
                localctx.i = self.match(VarDefParser.SYSCONST)
                localctx.x=str((None if localctx.i is None else localctx.i.text)).lower()
                pass

            elif la_ == 5:
                self.state = 341
                localctx.i = self.match(VarDefParser.ID)
                self.state = 344
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 342
                    self.match(VarDefParser.T__4)
                    self.state = 343
                    localctx.j = self.match(VarDefParser.ID)


                vName=str((None if localctx.i is None else localctx.i.text)).lower();
                if localctx.j!=None: vName=str((None if localctx.i is None else localctx.i.text)).lower()+'.'+str((None if localctx.j is None else localctx.j.text)).lower();
                if vName in self.newArrayMap.keys() or vName in self.varPathMap.keys() or vName in self.varExprMap.keys():
                	localctx.x = self.ifsAppend+"['"+vName+"']"+"[i]"
                	#print (vName) 
                else:
                	Err.addError(vName+' not defined.', self.vardefFile, self.vardefName)

                pass

            elif la_ == 6:
                self.state = 347
                self.match(VarDefParser.T__6)
                self.state = 348
                localctx.a = self.ee(0)
                self.state = 349
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.a.x)+")"
                pass

            elif la_ == 7:
                self.state = 352
                localctx.i = self.match(VarDefParser.STRING)
                localctx.x=  str((None if localctx.i is None else localctx.i.text)) 
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
                    self.state = 366
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 356
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 357
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 358
                        localctx.b = self.ee(10)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 361
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 362
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 363
                        localctx.b = self.ee(9)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
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
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 372
                localctx.a = self.ee(0)
                self.state = 373
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10) | (1 << VarDefParser.T__11) | (1 << VarDefParser.T__12) | (1 << VarDefParser.T__13))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 374
                localctx.b = self.ee(0)
                localctx.x=str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 377
                self.match(VarDefParser.T__6)
                self.state = 378
                localctx.c = self.compare(0)
                self.state = 379
                self.match(VarDefParser.T__7)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VarDefParser.CompareContext(self, _parentctx, _parentState)
                    localctx.c1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare)
                    self.state = 384
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 385
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 386
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 393
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
            self.state = 394
            localctx.i = self.id2()
            self.state = 395
            self.match(VarDefParser.T__1)
            self.state = 396
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
        self.enterRule(localctx, 44, self.RULE_id2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(VarDefParser.ID)
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 400
                self.match(VarDefParser.T__4)
                self.state = 401
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
            self.state = 404
            self.match(VarDefParser.IF)
            self.state = 405
            localctx.c = self.compare(0)
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 406
                self.match(VarDefParser.NL)
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 412
            self.match(VarDefParser.T__2)
            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 413
                self.match(VarDefParser.NL)
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 427 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 419
                localctx.a = self.assign()
                t=str(localctx.a.x).lower();al.append(t)
                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 421
                    self.match(VarDefParser.NL)
                    self.state = 426
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 429 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 431
            self.match(VarDefParser.T__3)
            self.state = 435
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 432
                    self.match(VarDefParser.NL) 
                self.state = 437
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

            k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 439
                self.match(VarDefParser.ELSEIF)
                self.state = 440
                localctx.c = self.compare(0)
                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 441
                    self.match(VarDefParser.NL)
                    self.state = 446
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 447
                self.match(VarDefParser.T__2)
                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 448
                    self.match(VarDefParser.NL)
                    self.state = 453
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 462 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 454
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 459
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 456
                        self.match(VarDefParser.NL)
                        self.state = 461
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 464 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 466
                self.match(VarDefParser.T__3)
                self.state = 470
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 467
                        self.match(VarDefParser.NL) 
                    self.state = 472
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

                k=str(localctx.c.x).lower(); ifs[k]=al;al=[]
                self.state = 479
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 480
                self.match(VarDefParser.ELSE)
                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 481
                    self.match(VarDefParser.NL)
                    self.state = 486
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 487
                self.match(VarDefParser.T__2)
                self.state = 491
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 488
                    self.match(VarDefParser.NL)
                    self.state = 493
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 502 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 494
                    localctx.a = self.assign()
                    t=str(localctx.a.x).lower();al.append(t)
                    self.state = 499
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 496
                        self.match(VarDefParser.NL)
                        self.state = 501
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 504 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 506
                self.match(VarDefParser.T__3)
                self.state = 508 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 507
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 510 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

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
        self._predicates[18] = self.ee_dts_sempred
        self._predicates[19] = self.ee_sempred
        self._predicates[20] = self.compare_sempred
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
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

    def compare_sempred(self, localctx, predIndex):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




