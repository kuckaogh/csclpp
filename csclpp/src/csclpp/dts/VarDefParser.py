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
        buf.write(u"%\u0127\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\2\6\2$\n\2")
        buf.write(u"\r\2\16\2%\3\3\3\3\3\3\6\3+\n\3\r\3\16\3,\3\3\6\3\60")
        buf.write(u"\n\3\r\3\16\3\61\3\3\3\3\6\3\66\n\3\r\3\16\3\67\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4B\n\4\3\4\6\4E\n\4\r\4")
        buf.write(u"\16\4F\3\5\3\5\3\5\3\5\3\5\3\5\7\5O\n\5\f\5\16\5R\13")
        buf.write(u"\5\3\6\3\6\3\6\3\7\3\7\5\7Y\n\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\tj\n\t\3\n\3")
        buf.write(u"\n\5\nn\n\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13")
        buf.write(u"x\n\13\3\13\3\13\3\13\3\13\3\13\5\13\177\n\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u008a\n\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7")
        buf.write(u"\13\u0096\n\13\f\13\16\13\u0099\13\13\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00a6\n\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\7\f\u00ad\n\f\f\f\16\f\u00b0\13\f\3\r\3\r")
        buf.write(u"\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u00ba\n\16\f\16\16\16")
        buf.write(u"\u00bd\13\16\3\16\3\16\7\16\u00c1\n\16\f\16\16\16\u00c4")
        buf.write(u"\13\16\3\16\3\16\3\16\7\16\u00c9\n\16\f\16\16\16\u00cc")
        buf.write(u"\13\16\6\16\u00ce\n\16\r\16\16\16\u00cf\3\16\3\16\7\16")
        buf.write(u"\u00d4\n\16\f\16\16\16\u00d7\13\16\3\16\3\16\3\16\3\16")
        buf.write(u"\7\16\u00dd\n\16\f\16\16\16\u00e0\13\16\3\16\3\16\7\16")
        buf.write(u"\u00e4\n\16\f\16\16\16\u00e7\13\16\3\16\3\16\3\16\7\16")
        buf.write(u"\u00ec\n\16\f\16\16\16\u00ef\13\16\6\16\u00f1\n\16\r")
        buf.write(u"\16\16\16\u00f2\3\16\3\16\7\16\u00f7\n\16\f\16\16\16")
        buf.write(u"\u00fa\13\16\3\16\3\16\7\16\u00fe\n\16\f\16\16\16\u0101")
        buf.write(u"\13\16\3\16\3\16\7\16\u0105\n\16\f\16\16\16\u0108\13")
        buf.write(u"\16\3\16\3\16\7\16\u010c\n\16\f\16\16\16\u010f\13\16")
        buf.write(u"\3\16\3\16\3\16\7\16\u0114\n\16\f\16\16\16\u0117\13\16")
        buf.write(u"\6\16\u0119\n\16\r\16\16\16\u011a\3\16\3\16\6\16\u011f")
        buf.write(u"\n\16\r\16\16\16\u0120\3\16\3\16\5\16\u0125\n\16\3\16")
        buf.write(u"\2\4\24\26\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\6\3")
        buf.write(u"\2\23\24\3\2\25\26\3\2\b\r\3\2\27\30\u0143\2\37\3\2\2")
        buf.write(u"\2\4\'\3\2\2\2\6A\3\2\2\2\bH\3\2\2\2\nS\3\2\2\2\fX\3")
        buf.write(u"\2\2\2\16_\3\2\2\2\20i\3\2\2\2\22m\3\2\2\2\24\u0089\3")
        buf.write(u"\2\2\2\26\u00a5\3\2\2\2\30\u00b1\3\2\2\2\32\u00b6\3\2")
        buf.write(u"\2\2\34\36\7$\2\2\35\34\3\2\2\2\36!\3\2\2\2\37\35\3\2")
        buf.write(u"\2\2\37 \3\2\2\2 #\3\2\2\2!\37\3\2\2\2\"$\5\4\3\2#\"")
        buf.write(u"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\3\3\2\2\2\'(")
        buf.write(u"\7\32\2\2(*\7 \2\2)+\7$\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2")
        buf.write(u"\2\2,-\3\2\2\2-/\3\2\2\2.\60\5\6\4\2/.\3\2\2\2\60\61")
        buf.write(u"\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\65")
        buf.write(u"\7\33\2\2\64\66\7$\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67")
        buf.write(u"\65\3\2\2\2\678\3\2\2\28\5\3\2\2\29B\5\f\7\2:B\5\16\b")
        buf.write(u"\2;B\5\22\n\2<=\5\32\16\2=>\b\4\1\2>B\3\2\2\2?B\5\b\5")
        buf.write(u"\2@B\5\n\6\2A9\3\2\2\2A:\3\2\2\2A;\3\2\2\2A<\3\2\2\2")
        buf.write(u"A?\3\2\2\2A@\3\2\2\2BD\3\2\2\2CE\7$\2\2DC\3\2\2\2EF\3")
        buf.write(u"\2\2\2FD\3\2\2\2FG\3\2\2\2G\7\3\2\2\2HI\7\34\2\2IJ\7")
        buf.write(u" \2\2JP\b\5\1\2KL\7\3\2\2LM\7 \2\2MO\b\5\1\2NK\3\2\2")
        buf.write(u"\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\t\3\2\2\2RP\3\2\2\2")
        buf.write(u"ST\7\31\2\2TU\7 \2\2U\13\3\2\2\2VW\7\21\2\2WY\b\7\1\2")
        buf.write(u"XV\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z[\7 \2\2[\\\7\4\2\2\\")
        buf.write(u"]\7\22\2\2]^\b\7\1\2^\r\3\2\2\2_`\7 \2\2`a\7\5\2\2ab")
        buf.write(u"\7 \2\2bc\7\4\2\2cd\5\20\t\2de\b\b\1\2e\17\3\2\2\2fj")
        buf.write(u"\7!\2\2gj\7\"\2\2hj\7 \2\2if\3\2\2\2ig\3\2\2\2ih\3\2")
        buf.write(u"\2\2j\21\3\2\2\2kl\7\21\2\2ln\b\n\1\2mk\3\2\2\2mn\3\2")
        buf.write(u"\2\2no\3\2\2\2op\7 \2\2pq\7\4\2\2qr\5\24\13\2r\23\3\2")
        buf.write(u"\2\2st\b\13\1\2tw\b\13\1\2uv\7\26\2\2vx\b\13\1\2wu\3")
        buf.write(u"\2\2\2wx\3\2\2\2xy\3\2\2\2yz\7\"\2\2z\u008a\b\13\1\2")
        buf.write(u"{~\b\13\1\2|}\7\26\2\2}\177\b\13\1\2~|\3\2\2\2~\177\3")
        buf.write(u"\2\2\2\177\u0080\3\2\2\2\u0080\u0081\7!\2\2\u0081\u008a")
        buf.write(u"\b\13\1\2\u0082\u0083\7 \2\2\u0083\u008a\b\13\1\2\u0084")
        buf.write(u"\u0085\7\6\2\2\u0085\u0086\5\24\13\2\u0086\u0087\7\7")
        buf.write(u"\2\2\u0087\u0088\b\13\1\2\u0088\u008a\3\2\2\2\u0089s")
        buf.write(u"\3\2\2\2\u0089{\3\2\2\2\u0089\u0082\3\2\2\2\u0089\u0084")
        buf.write(u"\3\2\2\2\u008a\u0097\3\2\2\2\u008b\u008c\f\b\2\2\u008c")
        buf.write(u"\u008d\t\2\2\2\u008d\u008e\5\24\13\t\u008e\u008f\b\13")
        buf.write(u"\1\2\u008f\u0096\3\2\2\2\u0090\u0091\f\7\2\2\u0091\u0092")
        buf.write(u"\t\3\2\2\u0092\u0093\5\24\13\b\u0093\u0094\b\13\1\2\u0094")
        buf.write(u"\u0096\3\2\2\2\u0095\u008b\3\2\2\2\u0095\u0090\3\2\2")
        buf.write(u"\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098")
        buf.write(u"\3\2\2\2\u0098\25\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b")
        buf.write(u"\b\f\1\2\u009b\u009c\5\24\13\2\u009c\u009d\t\4\2\2\u009d")
        buf.write(u"\u009e\5\24\13\2\u009e\u009f\b\f\1\2\u009f\u00a6\3\2")
        buf.write(u"\2\2\u00a0\u00a1\7\6\2\2\u00a1\u00a2\5\26\f\2\u00a2\u00a3")
        buf.write(u"\7\7\2\2\u00a3\u00a4\b\f\1\2\u00a4\u00a6\3\2\2\2\u00a5")
        buf.write(u"\u009a\3\2\2\2\u00a5\u00a0\3\2\2\2\u00a6\u00ae\3\2\2")
        buf.write(u"\2\u00a7\u00a8\f\3\2\2\u00a8\u00a9\t\5\2\2\u00a9\u00aa")
        buf.write(u"\5\26\f\4\u00aa\u00ab\b\f\1\2\u00ab\u00ad\3\2\2\2\u00ac")
        buf.write(u"\u00a7\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2")
        buf.write(u"\2\u00ae\u00af\3\2\2\2\u00af\27\3\2\2\2\u00b0\u00ae\3")
        buf.write(u"\2\2\2\u00b1\u00b2\7 \2\2\u00b2\u00b3\7\4\2\2\u00b3\u00b4")
        buf.write(u"\5\24\13\2\u00b4\u00b5\b\r\1\2\u00b5\31\3\2\2\2\u00b6")
        buf.write(u"\u00b7\7\35\2\2\u00b7\u00bb\5\26\f\2\u00b8\u00ba\7$\2")
        buf.write(u"\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9")
        buf.write(u"\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd")
        buf.write(u"\u00bb\3\2\2\2\u00be\u00c2\7\16\2\2\u00bf\u00c1\7$\2")
        buf.write(u"\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0")
        buf.write(u"\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00cd\3\2\2\2\u00c4")
        buf.write(u"\u00c2\3\2\2\2\u00c5\u00c6\5\30\r\2\u00c6\u00ca\b\16")
        buf.write(u"\1\2\u00c7\u00c9\7$\2\2\u00c8\u00c7\3\2\2\2\u00c9\u00cc")
        buf.write(u"\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write(u"\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00c5\3\2\2")
        buf.write(u"\2\u00ce\u00cf\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0")
        buf.write(u"\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d5\7\17\2\2\u00d2")
        buf.write(u"\u00d4\7$\2\2\u00d3\u00d2\3\2\2\2\u00d4\u00d7\3\2\2\2")
        buf.write(u"\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8")
        buf.write(u"\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00ff\b\16\1\2\u00d9")
        buf.write(u"\u00da\7\36\2\2\u00da\u00de\5\26\f\2\u00db\u00dd\7$\2")
        buf.write(u"\2\u00dc\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc")
        buf.write(u"\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write(u"\u00de\3\2\2\2\u00e1\u00e5\7\16\2\2\u00e2\u00e4\7$\2")
        buf.write(u"\2\u00e3\u00e2\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3")
        buf.write(u"\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00f0\3\2\2\2\u00e7")
        buf.write(u"\u00e5\3\2\2\2\u00e8\u00e9\5\30\r\2\u00e9\u00ed\b\16")
        buf.write(u"\1\2\u00ea\u00ec\7$\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef")
        buf.write(u"\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee")
        buf.write(u"\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00e8\3\2\2")
        buf.write(u"\2\u00f1\u00f2\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3")
        buf.write(u"\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f8\7\17\2\2\u00f5")
        buf.write(u"\u00f7\7$\2\2\u00f6\u00f5\3\2\2\2\u00f7\u00fa\3\2\2\2")
        buf.write(u"\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fb")
        buf.write(u"\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fc\b\16\1\2\u00fc")
        buf.write(u"\u00fe\3\2\2\2\u00fd\u00d9\3\2\2\2\u00fe\u0101\3\2\2")
        buf.write(u"\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0124")
        buf.write(u"\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0106\7\37\2\2\u0103")
        buf.write(u"\u0105\7$\2\2\u0104\u0103\3\2\2\2\u0105\u0108\3\2\2\2")
        buf.write(u"\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0109")
        buf.write(u"\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u010d\7\16\2\2\u010a")
        buf.write(u"\u010c\7$\2\2\u010b\u010a\3\2\2\2\u010c\u010f\3\2\2\2")
        buf.write(u"\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0118")
        buf.write(u"\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111\5\30\r\2\u0111")
        buf.write(u"\u0115\b\16\1\2\u0112\u0114\7$\2\2\u0113\u0112\3\2\2")
        buf.write(u"\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116")
        buf.write(u"\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0118")
        buf.write(u"\u0110\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u0118\3\2\2")
        buf.write(u"\2\u011a\u011b\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011e")
        buf.write(u"\7\17\2\2\u011d\u011f\7$\2\2\u011e\u011d\3\2\2\2\u011f")
        buf.write(u"\u0120\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2")
        buf.write(u"\2\u0121\u0122\3\2\2\2\u0122\u0123\b\16\1\2\u0123\u0125")
        buf.write(u"\3\2\2\2\u0124\u0102\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write(u"\33\3\2\2\2%\37%,\61\67AFPXimw~\u0089\u0095\u0097\u00a5")
        buf.write(u"\u00ae\u00bb\u00c2\u00ca\u00cf\u00d5\u00de\u00e5\u00ed")
        buf.write(u"\u00f2\u00f8\u00ff\u0106\u010d\u0115\u011a\u0120\u0124")
        return buf.getvalue()


class VarDefParser ( Parser ):

    grammarFileName = "VarDef.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"','", u"'='", u"'.'", u"'('", u"')'", 
                     u"'>'", u"'>='", u"'<'", u"'<='", u"'=='", u"'!='", 
                     u"'{'", u"'}'", u"<INVALID>", u"'@'", u"<INVALID>", 
                     u"'*'", u"'/'", u"'+'", u"'-'", u"' and '", u"' or '", 
                     u"'include'", u"'vardef'", u"'end'", u"'array'", u"'if'", 
                     u"'elseif'", u"'else'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"LINE_COMMENT", u"T", 
                      u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", u"AND", u"OR", 
                      u"INCLUDE", u"VARDEF", u"END", u"ARRAY", u"IF", u"ELSEIF", 
                      u"ELSE", u"ID", u"FLOAT", u"INT", u"STRING", u"NL", 
                      u"WS" ]

    RULE_prog = 0
    RULE_vardef = 1
    RULE_field = 2
    RULE_new_var = 3
    RULE_include = 4
    RULE_var_path = 5
    RULE_var_meta = 6
    RULE_info = 7
    RULE_stat = 8
    RULE_ee = 9
    RULE_compare = 10
    RULE_assign = 11
    RULE_if_stat = 12

    ruleNames =  [ u"prog", u"vardef", u"field", u"new_var", u"include", 
                   u"var_path", u"var_meta", u"info", u"stat", u"ee", u"compare", 
                   u"assign", u"if_stat" ]

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
    ID=30
    FLOAT=31
    INT=32
    STRING=33
    NL=34
    WS=35

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
    newArrayGroupList={};
    varPathMap={};
    varExprMap={};
    tempVarList=[];
    newArrayList=[];
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
        ifsMapGroupMap={};newArrayGroupList={};

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 26
                self.match(VarDefParser.NL)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.vardef()
                self.state = 35 
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

        self.varPathMap={};self.varExprMap={};self.tempVarList=[];
        self.ifsMap=collections.OrderedDict();self.newArrayList=[];
        self.ifid=0;

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(VarDefParser.VARDEF)
            self.state = 38
            localctx.name = self.match(VarDefParser.ID)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.match(VarDefParser.NL)
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.field()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ARRAY) | (1 << VarDefParser.IF) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 49
            self.match(VarDefParser.END)
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

            self._ctx.stop = self._input.LT(-1)
            groupName=(None if localctx.name is None else localctx.name.text);
            self.varPathGroupMap[groupName]=self.varPathMap;
            self.varExprGroupMap[groupName]=self.varExprMap;
            self.tempVarGroupList[groupName]=self.tempVarList;	
            self.ifsMapGroupMap[groupName]=self.ifsMap;
            self.newArrayGroupList[groupName]=self.newArrayList;

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
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 55
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 56
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 57
                self.stat()
                pass

            elif la_ == 4:
                self.state = 58
                self.if_stat()
                self.ifid=self.ifid+1;
                pass

            elif la_ == 5:
                self.state = 61
                self.new_var()
                pass

            elif la_ == 6:
                self.state = 62
                self.include()
                pass


            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.match(VarDefParser.NL)
                self.state = 68 
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
            self.i = None # Token

        def ARRAY(self):
            return self.getToken(VarDefParser.ARRAY, 0)

        def ID(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.ID)
            else:
                return self.getToken(VarDefParser.ID, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(VarDefParser.ARRAY)
            self.state = 71
            localctx.i = self.match(VarDefParser.ID)
            name=str((None if localctx.i is None else localctx.i.text)); self.newArrayList.append(name);
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.T__0:
                self.state = 73
                self.match(VarDefParser.T__0)
                self.state = 74
                localctx.i = self.match(VarDefParser.ID)
                name=str((None if localctx.i is None else localctx.i.text)); self.newArrayList.append(name);
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 8, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(VarDefParser.INCLUDE)
            self.state = 82
            localctx.g = self.match(VarDefParser.ID)
            self._ctx.stop = self._input.LT(-1)
            gn=(None if localctx.g is None else localctx.g.text);
            if gn: 
            	self.varPathMap.update(self.varPathGroupMap[gn])
            	self.varExprMap.update(self.varExprGroupMap[gn])
            	self.tempVarList.extend(self.tempVarGroupList[gn])
            	self.ifsMap.update(self.ifsMapGroupMap[gn])
            	self.newArrayList.extend(self.newArrayGroupList[gn])

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
        self.enterRule(localctx, 10, self.RULE_var_path)
        isTemp=False 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 84
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 88
            localctx.i = self.match(VarDefParser.ID)
            self.state = 89
            self.match(VarDefParser.T__1)
            self.state = 90
            localctx.p = self.match(VarDefParser.PATH)
            p =str((None if localctx.p is None else localctx.p.text)); t = Var(p); 
            name=str((None if localctx.i is None else localctx.i.text)); self.varPathMap[name]=t;
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
            self.v = None # Token
            self.p = None # Token
            self.inf = None # InfoContext

        def ID(self, i=None):
            if i is None:
                return self.getTokens(VarDefParser.ID)
            else:
                return self.getToken(VarDefParser.ID, i)

        def info(self):
            return self.getTypedRuleContext(VarDefParser.InfoContext,0)


        def getRuleIndex(self):
            return VarDefParser.RULE_var_meta

        def accept(self, visitor):
            if hasattr(visitor, "visitVar_meta"):
                return visitor.visitVar_meta(self)
            else:
                return visitor.visitChildren(self)




    def var_meta(self):

        localctx = VarDefParser.Var_metaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_meta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            localctx.v = self.match(VarDefParser.ID)
            self.state = 94
            self.match(VarDefParser.T__2)
            self.state = 95
            localctx.p = self.match(VarDefParser.ID)
            self.state = 96
            self.match(VarDefParser.T__1)
            self.state = 97
            localctx.inf = self.info()
            vn=str((None if localctx.v is None else localctx.v.text));pn=str((None if localctx.p is None else localctx.p.text));c=str((None if localctx.inf is None else self._input.getText((localctx.inf.start,localctx.inf.stop))));
            	
            if pn in self.varMetaKeys:
            	if vn in self.varPathMap:
            		self.varPathMap[vn].metaData[pn]=c; 
            	elif vn in self.varExprMap:
            		self.varExprMap[vn].metaData[pn]=c; 
            	else:
            		print ('#Error: '+vn+'.'+pn+'='+c+' variable \"'+vn+'\" not found!')
            else:
            	print ('#Error: '+vn+'.'+pn+'='+c+' metadata keyword \"'+pn+'\" not recognized!')

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InfoContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.InfoContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token

        def FLOAT(self):
            return self.getToken(VarDefParser.FLOAT, 0)

        def INT(self):
            return self.getToken(VarDefParser.INT, 0)

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

        def getRuleIndex(self):
            return VarDefParser.RULE_info

        def accept(self, visitor):
            if hasattr(visitor, "visitInfo"):
                return visitor.visitInfo(self)
            else:
                return visitor.visitChildren(self)




    def info(self):

        localctx = VarDefParser.InfoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_info)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                localctx.i = self.match(VarDefParser.FLOAT)
                pass
            elif token in [VarDefParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(VarDefParser.INT)
                pass
            elif token in [VarDefParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
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
        self.enterRule(localctx, 16, self.RULE_stat)
        isTemp=False 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 105
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 109
            localctx.i = self.match(VarDefParser.ID)
            self.state = 110
            self.match(VarDefParser.T__1)
            self.state = 111
            localctx.e = self.ee(0)
            self._ctx.stop = self._input.LT(-1)

            v = Var('');
            e=str((None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop))));v.expr=e;
            name=str((None if localctx.i is None else localctx.i.text)); self.varExprMap[name]=v; 
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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                s=''
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 115
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 119
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 122
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 126
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 128
                localctx.i = self.match(VarDefParser.ID)
                localctx.x=self.ifsAppend+"['"+str((None if localctx.i is None else localctx.i.text))+"']"+"[i]"
                pass

            elif la_ == 4:
                self.state = 130
                self.match(VarDefParser.T__3)
                self.state = 131
                localctx.a = self.ee(0)
                self.state = 132
                self.match(VarDefParser.T__4)
                localctx.x="("+str(localctx.a.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 147
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 137
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 138
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 139
                        localctx.b = self.ee(7)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 142
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 143
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 144
                        localctx.b = self.ee(6)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_compare, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 153
                localctx.a = self.ee(0)
                self.state = 154
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__5) | (1 << VarDefParser.T__6) | (1 << VarDefParser.T__7) | (1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                localctx.b = self.ee(0)
                localctx.x=str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 158
                self.match(VarDefParser.T__3)
                self.state = 159
                localctx.c = self.compare(0)
                self.state = 160
                self.match(VarDefParser.T__4)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VarDefParser.CompareContext(self, _parentctx, _parentState)
                    localctx.c1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare)
                    self.state = 165
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 166
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 167
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.i = None # Token
            self.a = None # EeContext

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)

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
        self.enterRule(localctx, 22, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            localctx.i = self.match(VarDefParser.ID)
            self.state = 176
            self.match(VarDefParser.T__1)
            self.state = 177
            localctx.a = self.ee(0)
            localctx.x=self.ifsNewAppend+"['"+str((None if localctx.i is None else localctx.i.text))+"'][i]="+localctx.a.x
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
        self.enterRule(localctx, 24, self.RULE_if_stat)
        ifs=collections.OrderedDict();al=[];
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(VarDefParser.IF)
            self.state = 181
            localctx.c = self.compare(0)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 182
                self.match(VarDefParser.NL)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self.match(VarDefParser.T__11)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 189
                self.match(VarDefParser.NL)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 195
                localctx.a = self.assign()
                t=str(localctx.a.x);al.append(t)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 197
                    self.match(VarDefParser.NL)
                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 205 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 207
            self.match(VarDefParser.T__12)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 208
                    self.match(VarDefParser.NL) 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            k=str(localctx.c.x); ifs[k]=al;al=[]
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 215
                self.match(VarDefParser.ELSEIF)
                self.state = 216
                localctx.c = self.compare(0)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 217
                    self.match(VarDefParser.NL)
                    self.state = 222
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 223
                self.match(VarDefParser.T__11)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 224
                    self.match(VarDefParser.NL)
                    self.state = 229
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 238 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 230
                    localctx.a = self.assign()
                    t=str(localctx.a.x);al.append(t)
                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 232
                        self.match(VarDefParser.NL)
                        self.state = 237
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 240 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 242
                self.match(VarDefParser.T__12)
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 243
                        self.match(VarDefParser.NL) 
                    self.state = 248
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                k=str(localctx.c.x); ifs[k]=al;al=[]
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 256
                self.match(VarDefParser.ELSE)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 257
                    self.match(VarDefParser.NL)
                    self.state = 262
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 263
                self.match(VarDefParser.T__11)
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 264
                    self.match(VarDefParser.NL)
                    self.state = 269
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 278 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 270
                    localctx.a = self.assign()
                    t=str(localctx.a.x);al.append(t)
                    self.state = 275
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 272
                        self.match(VarDefParser.NL)
                        self.state = 277
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 280 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 282
                self.match(VarDefParser.T__12)
                self.state = 284 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 283
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 286 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        self._predicates[9] = self.ee_sempred
        self._predicates[10] = self.compare_sempred
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
         




