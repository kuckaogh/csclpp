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
        buf.write(u"%\u0124\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\2\6\2$\n\2")
        buf.write(u"\r\2\16\2%\3\3\3\3\3\3\6\3+\n\3\r\3\16\3,\3\3\6\3\60")
        buf.write(u"\n\3\r\3\16\3\61\3\3\3\3\6\3\66\n\3\r\3\16\3\67\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4B\n\4\3\4\6\4E\n\4\r\4")
        buf.write(u"\16\4F\3\5\3\5\3\5\3\5\3\5\3\5\7\5O\n\5\f\5\16\5R\13")
        buf.write(u"\5\3\6\3\6\3\6\3\7\3\7\5\7Y\n\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\5\nk\n\n\3")
        buf.write(u"\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13u\n\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\5\13|\n\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\5\13\u0087\n\13\3\13\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u0093\n\13\f\13")
        buf.write(u"\16\13\u0096\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\5\f\u00a3\n\f\3\f\3\f\3\f\3\f\3\f\7\f\u00aa")
        buf.write(u"\n\f\f\f\16\f\u00ad\13\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write(u"\3\16\7\16\u00b7\n\16\f\16\16\16\u00ba\13\16\3\16\3\16")
        buf.write(u"\7\16\u00be\n\16\f\16\16\16\u00c1\13\16\3\16\3\16\3\16")
        buf.write(u"\7\16\u00c6\n\16\f\16\16\16\u00c9\13\16\6\16\u00cb\n")
        buf.write(u"\16\r\16\16\16\u00cc\3\16\3\16\7\16\u00d1\n\16\f\16\16")
        buf.write(u"\16\u00d4\13\16\3\16\3\16\3\16\3\16\7\16\u00da\n\16\f")
        buf.write(u"\16\16\16\u00dd\13\16\3\16\3\16\7\16\u00e1\n\16\f\16")
        buf.write(u"\16\16\u00e4\13\16\3\16\3\16\3\16\7\16\u00e9\n\16\f\16")
        buf.write(u"\16\16\u00ec\13\16\6\16\u00ee\n\16\r\16\16\16\u00ef\3")
        buf.write(u"\16\3\16\7\16\u00f4\n\16\f\16\16\16\u00f7\13\16\3\16")
        buf.write(u"\3\16\7\16\u00fb\n\16\f\16\16\16\u00fe\13\16\3\16\3\16")
        buf.write(u"\7\16\u0102\n\16\f\16\16\16\u0105\13\16\3\16\3\16\7\16")
        buf.write(u"\u0109\n\16\f\16\16\16\u010c\13\16\3\16\3\16\3\16\7\16")
        buf.write(u"\u0111\n\16\f\16\16\16\u0114\13\16\6\16\u0116\n\16\r")
        buf.write(u"\16\16\16\u0117\3\16\3\16\6\16\u011c\n\16\r\16\16\16")
        buf.write(u"\u011d\3\16\3\16\5\16\u0122\n\16\3\16\2\4\24\26\17\2")
        buf.write(u"\4\6\b\n\f\16\20\22\24\26\30\32\2\7\3\2!#\3\2\23\24\3")
        buf.write(u"\2\25\26\3\2\b\r\3\2\27\30\u013e\2\37\3\2\2\2\4\'\3\2")
        buf.write(u"\2\2\6A\3\2\2\2\bH\3\2\2\2\nS\3\2\2\2\fX\3\2\2\2\16_")
        buf.write(u"\3\2\2\2\20f\3\2\2\2\22j\3\2\2\2\24\u0086\3\2\2\2\26")
        buf.write(u"\u00a2\3\2\2\2\30\u00ae\3\2\2\2\32\u00b3\3\2\2\2\34\36")
        buf.write(u"\7$\2\2\35\34\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3")
        buf.write(u"\2\2\2 #\3\2\2\2!\37\3\2\2\2\"$\5\4\3\2#\"\3\2\2\2$%")
        buf.write(u"\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\3\3\2\2\2\'(\7\32\2\2(")
        buf.write(u"*\7 \2\2)+\7$\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2")
        buf.write(u"\2\2-/\3\2\2\2.\60\5\6\4\2/.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write(u"/\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\65\7\33\2\2")
        buf.write(u"\64\66\7$\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2")
        buf.write(u"\2\678\3\2\2\28\5\3\2\2\29B\5\f\7\2:B\5\16\b\2;B\5\22")
        buf.write(u"\n\2<=\5\32\16\2=>\b\4\1\2>B\3\2\2\2?B\5\b\5\2@B\5\n")
        buf.write(u"\6\2A9\3\2\2\2A:\3\2\2\2A;\3\2\2\2A<\3\2\2\2A?\3\2\2")
        buf.write(u"\2A@\3\2\2\2BD\3\2\2\2CE\7$\2\2DC\3\2\2\2EF\3\2\2\2F")
        buf.write(u"D\3\2\2\2FG\3\2\2\2G\7\3\2\2\2HI\7\34\2\2IJ\7 \2\2JP")
        buf.write(u"\b\5\1\2KL\7\3\2\2LM\7 \2\2MO\b\5\1\2NK\3\2\2\2OR\3\2")
        buf.write(u"\2\2PN\3\2\2\2PQ\3\2\2\2Q\t\3\2\2\2RP\3\2\2\2ST\7\31")
        buf.write(u"\2\2TU\7 \2\2U\13\3\2\2\2VW\7\21\2\2WY\b\7\1\2XV\3\2")
        buf.write(u"\2\2XY\3\2\2\2YZ\3\2\2\2Z[\7 \2\2[\\\7\4\2\2\\]\7\22")
        buf.write(u"\2\2]^\b\7\1\2^\r\3\2\2\2_`\7 \2\2`a\7\5\2\2ab\7 \2\2")
        buf.write(u"bc\7\4\2\2cd\5\20\t\2de\b\b\1\2e\17\3\2\2\2fg\t\2\2\2")
        buf.write(u"g\21\3\2\2\2hi\7\21\2\2ik\b\n\1\2jh\3\2\2\2jk\3\2\2\2")
        buf.write(u"kl\3\2\2\2lm\7 \2\2mn\7\4\2\2no\5\24\13\2o\23\3\2\2\2")
        buf.write(u"pq\b\13\1\2qt\b\13\1\2rs\7\26\2\2su\b\13\1\2tr\3\2\2")
        buf.write(u"\2tu\3\2\2\2uv\3\2\2\2vw\7\"\2\2w\u0087\b\13\1\2x{\b")
        buf.write(u"\13\1\2yz\7\26\2\2z|\b\13\1\2{y\3\2\2\2{|\3\2\2\2|}\3")
        buf.write(u"\2\2\2}~\7!\2\2~\u0087\b\13\1\2\177\u0080\7 \2\2\u0080")
        buf.write(u"\u0087\b\13\1\2\u0081\u0082\7\6\2\2\u0082\u0083\5\24")
        buf.write(u"\13\2\u0083\u0084\7\7\2\2\u0084\u0085\b\13\1\2\u0085")
        buf.write(u"\u0087\3\2\2\2\u0086p\3\2\2\2\u0086x\3\2\2\2\u0086\177")
        buf.write(u"\3\2\2\2\u0086\u0081\3\2\2\2\u0087\u0094\3\2\2\2\u0088")
        buf.write(u"\u0089\f\b\2\2\u0089\u008a\t\3\2\2\u008a\u008b\5\24\13")
        buf.write(u"\t\u008b\u008c\b\13\1\2\u008c\u0093\3\2\2\2\u008d\u008e")
        buf.write(u"\f\7\2\2\u008e\u008f\t\4\2\2\u008f\u0090\5\24\13\b\u0090")
        buf.write(u"\u0091\b\13\1\2\u0091\u0093\3\2\2\2\u0092\u0088\3\2\2")
        buf.write(u"\2\u0092\u008d\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092")
        buf.write(u"\3\2\2\2\u0094\u0095\3\2\2\2\u0095\25\3\2\2\2\u0096\u0094")
        buf.write(u"\3\2\2\2\u0097\u0098\b\f\1\2\u0098\u0099\5\24\13\2\u0099")
        buf.write(u"\u009a\t\5\2\2\u009a\u009b\5\24\13\2\u009b\u009c\b\f")
        buf.write(u"\1\2\u009c\u00a3\3\2\2\2\u009d\u009e\7\6\2\2\u009e\u009f")
        buf.write(u"\5\26\f\2\u009f\u00a0\7\7\2\2\u00a0\u00a1\b\f\1\2\u00a1")
        buf.write(u"\u00a3\3\2\2\2\u00a2\u0097\3\2\2\2\u00a2\u009d\3\2\2")
        buf.write(u"\2\u00a3\u00ab\3\2\2\2\u00a4\u00a5\f\3\2\2\u00a5\u00a6")
        buf.write(u"\t\6\2\2\u00a6\u00a7\5\26\f\4\u00a7\u00a8\b\f\1\2\u00a8")
        buf.write(u"\u00aa\3\2\2\2\u00a9\u00a4\3\2\2\2\u00aa\u00ad\3\2\2")
        buf.write(u"\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\27\3")
        buf.write(u"\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af\7 \2\2\u00af\u00b0")
        buf.write(u"\7\4\2\2\u00b0\u00b1\5\24\13\2\u00b1\u00b2\b\r\1\2\u00b2")
        buf.write(u"\31\3\2\2\2\u00b3\u00b4\7\35\2\2\u00b4\u00b8\5\26\f\2")
        buf.write(u"\u00b5\u00b7\7$\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3")
        buf.write(u"\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write(u"\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bf\7\16\2")
        buf.write(u"\2\u00bc\u00be\7$\2\2\u00bd\u00bc\3\2\2\2\u00be\u00c1")
        buf.write(u"\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0")
        buf.write(u"\u00ca\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c3\5\30\r")
        buf.write(u"\2\u00c3\u00c7\b\16\1\2\u00c4\u00c6\7$\2\2\u00c5\u00c4")
        buf.write(u"\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write(u"\u00c8\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2")
        buf.write(u"\2\u00ca\u00c2\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ca")
        buf.write(u"\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write(u"\u00d2\7\17\2\2\u00cf\u00d1\7$\2\2\u00d0\u00cf\3\2\2")
        buf.write(u"\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3")
        buf.write(u"\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5")
        buf.write(u"\u00fc\b\16\1\2\u00d6\u00d7\7\36\2\2\u00d7\u00db\5\26")
        buf.write(u"\f\2\u00d8\u00da\7$\2\2\u00d9\u00d8\3\2\2\2\u00da\u00dd")
        buf.write(u"\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write(u"\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e2\7\16\2")
        buf.write(u"\2\u00df\u00e1\7$\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e4")
        buf.write(u"\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write(u"\u00ed\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6\5\30\r")
        buf.write(u"\2\u00e6\u00ea\b\16\1\2\u00e7\u00e9\7$\2\2\u00e8\u00e7")
        buf.write(u"\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea")
        buf.write(u"\u00eb\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2")
        buf.write(u"\2\u00ed\u00e5\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00ed")
        buf.write(u"\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1")
        buf.write(u"\u00f5\7\17\2\2\u00f2\u00f4\7$\2\2\u00f3\u00f2\3\2\2")
        buf.write(u"\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6")
        buf.write(u"\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8")
        buf.write(u"\u00f9\b\16\1\2\u00f9\u00fb\3\2\2\2\u00fa\u00d6\3\2\2")
        buf.write(u"\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd")
        buf.write(u"\3\2\2\2\u00fd\u0121\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff")
        buf.write(u"\u0103\7\37\2\2\u0100\u0102\7$\2\2\u0101\u0100\3\2\2")
        buf.write(u"\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104")
        buf.write(u"\3\2\2\2\u0104\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0106")
        buf.write(u"\u010a\7\16\2\2\u0107\u0109\7$\2\2\u0108\u0107\3\2\2")
        buf.write(u"\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b")
        buf.write(u"\3\2\2\2\u010b\u0115\3\2\2\2\u010c\u010a\3\2\2\2\u010d")
        buf.write(u"\u010e\5\30\r\2\u010e\u0112\b\16\1\2\u010f\u0111\7$\2")
        buf.write(u"\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110")
        buf.write(u"\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0116\3\2\2\2\u0114")
        buf.write(u"\u0112\3\2\2\2\u0115\u010d\3\2\2\2\u0116\u0117\3\2\2")
        buf.write(u"\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119")
        buf.write(u"\3\2\2\2\u0119\u011b\7\17\2\2\u011a\u011c\7$\2\2\u011b")
        buf.write(u"\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011b\3\2\2")
        buf.write(u"\2\u011d\u011e\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120")
        buf.write(u"\b\16\1\2\u0120\u0122\3\2\2\2\u0121\u00ff\3\2\2\2\u0121")
        buf.write(u"\u0122\3\2\2\2\u0122\33\3\2\2\2$\37%,\61\67AFPXjt{\u0086")
        buf.write(u"\u0092\u0094\u00a2\u00ab\u00b8\u00bf\u00c7\u00cc\u00d2")
        buf.write(u"\u00db\u00e2\u00ea\u00ef\u00f5\u00fc\u0103\u010a\u0112")
        buf.write(u"\u0117\u011d\u0121")
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
            if vn in self.varPathMap:
            	self.varPathMap[vn].metaData[pn]=c; 
            elif vn in self.varExprMap:
            	self.varExprMap[vn].metaData[pn]=c; 
            else:
            	print ('#Error: '+vn+'.'+pn+'='+c+' variable \"'+vn+'\" not found!')

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

        def FLOAT(self):
            return self.getToken(VarDefParser.FLOAT, 0)

        def INT(self):
            return self.getToken(VarDefParser.INT, 0)

        def STRING(self):
            return self.getToken(VarDefParser.STRING, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.FLOAT) | (1 << VarDefParser.INT) | (1 << VarDefParser.STRING))) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_stat)
        isTemp=False 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 102
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 106
            localctx.i = self.match(VarDefParser.ID)
            self.state = 107
            self.match(VarDefParser.T__1)
            self.state = 108
            localctx.e = self.ee(0)
            self._ctx.stop = self._input.LT(-1)

            v = Var('');
            e=str((None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop))));v.expr=e;
            e_mod=str(localctx.e.x);v.expr_mod=e_mod; 
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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                s=''
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 112
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 116
                localctx.i = self.match(VarDefParser.INT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 2:
                s=''
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.SUB:
                    self.state = 119
                    self.match(VarDefParser.SUB)
                    s='-'


                self.state = 123
                localctx.i = self.match(VarDefParser.FLOAT)
                localctx.x=s+str((None if localctx.i is None else localctx.i.text))
                pass

            elif la_ == 3:
                self.state = 125
                localctx.i = self.match(VarDefParser.ID)
                localctx.x=self.ifsAppend+"['"+str((None if localctx.i is None else localctx.i.text))+"']"+"[i]"
                pass

            elif la_ == 4:
                self.state = 127
                self.match(VarDefParser.T__3)
                self.state = 128
                localctx.a = self.ee(0)
                self.state = 129
                self.match(VarDefParser.T__4)
                localctx.x="("+str(localctx.a.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 144
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 134
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 135
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 136
                        localctx.b = self.ee(7)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 139
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 140
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 141
                        localctx.b = self.ee(6)
                        localctx.x = str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                        pass

             
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 150
                localctx.a = self.ee(0)
                self.state = 151
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T__5) | (1 << VarDefParser.T__6) | (1 << VarDefParser.T__7) | (1 << VarDefParser.T__8) | (1 << VarDefParser.T__9) | (1 << VarDefParser.T__10))) != 0)):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 152
                localctx.b = self.ee(0)
                localctx.x=str(localctx.a.x)+str((None if localctx.o is None else localctx.o.text))+str(localctx.b.x)
                pass

            elif la_ == 2:
                self.state = 155
                self.match(VarDefParser.T__3)
                self.state = 156
                localctx.c = self.compare(0)
                self.state = 157
                self.match(VarDefParser.T__4)
                localctx.x="("+str(localctx.c.x)+")"
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VarDefParser.CompareContext(self, _parentctx, _parentState)
                    localctx.c1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare)
                    self.state = 162
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 163
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==VarDefParser.AND or _la==VarDefParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 164
                    localctx.c2 = self.compare(2)
                    localctx.x=str(localctx.c1.x)+str((None if localctx.op is None else localctx.op.text))+str(localctx.c2.x) 
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 172
            localctx.i = self.match(VarDefParser.ID)
            self.state = 173
            self.match(VarDefParser.T__1)
            self.state = 174
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
            self.state = 177
            self.match(VarDefParser.IF)
            self.state = 178
            localctx.c = self.compare(0)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 179
                self.match(VarDefParser.NL)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self.match(VarDefParser.T__11)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 186
                self.match(VarDefParser.NL)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 192
                localctx.a = self.assign()
                t=str((None if localctx.a is None else self._input.getText((localctx.a.start,localctx.a.stop))));al.append(t)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 194
                    self.match(VarDefParser.NL)
                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 202 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.ID):
                    break

            self.state = 204
            self.match(VarDefParser.T__12)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 205
                    self.match(VarDefParser.NL) 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            k=str((None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop)))); ifs[k]=al;al=[]
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.ELSEIF:
                self.state = 212
                self.match(VarDefParser.ELSEIF)
                self.state = 213
                localctx.c = self.compare(0)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 214
                    self.match(VarDefParser.NL)
                    self.state = 219
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 220
                self.match(VarDefParser.T__11)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 221
                    self.match(VarDefParser.NL)
                    self.state = 226
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 235 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 227
                    localctx.a = self.assign()
                    t=str((None if localctx.a is None else self._input.getText((localctx.a.start,localctx.a.stop))));al.append(t)
                    self.state = 232
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 229
                        self.match(VarDefParser.NL)
                        self.state = 234
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 237 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 239
                self.match(VarDefParser.T__12)
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 240
                        self.match(VarDefParser.NL) 
                    self.state = 245
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                k=str((None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop)))); ifs[k]=al;al=[]
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.ELSE:
                self.state = 253
                self.match(VarDefParser.ELSE)
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 254
                    self.match(VarDefParser.NL)
                    self.state = 259
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 260
                self.match(VarDefParser.T__11)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VarDefParser.NL:
                    self.state = 261
                    self.match(VarDefParser.NL)
                    self.state = 266
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 275 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 267
                    localctx.a = self.assign()
                    t=str((None if localctx.a is None else self._input.getText((localctx.a.start,localctx.a.stop))));al.append(t)
                    self.state = 272
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==VarDefParser.NL:
                        self.state = 269
                        self.match(VarDefParser.NL)
                        self.state = 274
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 277 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==VarDefParser.ID):
                        break

                self.state = 279
                self.match(VarDefParser.T__12)
                self.state = 281 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 280
                        self.match(VarDefParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 283 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
         




