# Generated from Setting.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
import Setting as S
import copy

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\22_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2")
        buf.write(u"\6\2\32\n\2\r\2\16\2\33\3\3\3\3\3\3\6\3!\n\3\r\3\16\3")
        buf.write(u"\"\3\3\6\3&\n\3\r\3\16\3\'\3\3\3\3\6\3,\n\3\r\3\16\3")
        buf.write(u"-\3\4\3\4\3\4\3\4\5\4\64\n\4\3\4\6\4\67\n\4\r\4\16\4")
        buf.write(u"8\3\5\3\5\5\5=\n\5\3\5\3\5\3\5\3\5\3\5\7\5D\n\5\f\5\16")
        buf.write(u"\5G\13\5\3\6\3\6\5\6K\n\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\2\2")
        buf.write(u"\n\2\4\6\b\n\f\16\20\2\2b\2\25\3\2\2\2\4\35\3\2\2\2\6")
        buf.write(u"\63\3\2\2\2\b:\3\2\2\2\nH\3\2\2\2\fO\3\2\2\2\16V\3\2")
        buf.write(u"\2\2\20Z\3\2\2\2\22\24\7\21\2\2\23\22\3\2\2\2\24\27\3")
        buf.write(u"\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\31\3\2\2\2\27\25")
        buf.write(u"\3\2\2\2\30\32\5\4\3\2\31\30\3\2\2\2\32\33\3\2\2\2\33")
        buf.write(u"\31\3\2\2\2\33\34\3\2\2\2\34\3\3\2\2\2\35\36\7\t\2\2")
        buf.write(u"\36 \7\16\2\2\37!\7\21\2\2 \37\3\2\2\2!\"\3\2\2\2\" ")
        buf.write(u"\3\2\2\2\"#\3\2\2\2#%\3\2\2\2$&\5\6\4\2%$\3\2\2\2&\'")
        buf.write(u"\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)+\7\b\2\2*,")
        buf.write(u"\7\21\2\2+*\3\2\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\5")
        buf.write(u"\3\2\2\2/\64\5\b\5\2\60\64\5\n\6\2\61\64\5\16\b\2\62")
        buf.write(u"\64\5\20\t\2\63/\3\2\2\2\63\60\3\2\2\2\63\61\3\2\2\2")
        buf.write(u"\63\62\3\2\2\2\64\66\3\2\2\2\65\67\7\21\2\2\66\65\3\2")
        buf.write(u"\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29\7\3\2\2\2:<\7")
        buf.write(u"\n\2\2;=\7\3\2\2<;\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\7\7")
        buf.write(u"\2\2?E\b\5\1\2@A\7\4\2\2AB\7\7\2\2BD\b\5\1\2C@\3\2\2")
        buf.write(u"\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\t\3\2\2\2GE\3\2\2\2")
        buf.write(u"HJ\7\13\2\2IK\7\3\2\2JI\3\2\2\2JK\3\2\2\2KL\3\2\2\2L")
        buf.write(u"M\7\7\2\2MN\b\6\1\2N\13\3\2\2\2OP\7\13\2\2PQ\7\3\2\2")
        buf.write(u"QR\7\16\2\2RS\7\5\2\2ST\7\13\2\2TU\b\7\1\2U\r\3\2\2\2")
        buf.write(u"VW\7\f\2\2WX\7\3\2\2XY\7\7\2\2Y\17\3\2\2\2Z[\7\r\2\2")
        buf.write(u"[\\\7\3\2\2\\]\7\7\2\2]\21\3\2\2\2\f\25\33\"\'-\638<")
        buf.write(u"EJ")
        return buf.getvalue()


class SettingParser ( Parser ):

    grammarFileName = "Setting.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"','", u"'.'", u"<INVALID>", 
                     u"<INVALID>", u"'end'", u"'study'", u"'data'", u"'dt'", 
                     u"'metadata'", u"'wresl'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"LINE_COMMENT", u"STRING", u"END", u"STUDY", u"DATA", 
                      u"VARDEF", u"METADATA", u"WRESL", u"ID", u"FLOAT", 
                      u"INT", u"NL", u"WS" ]

    RULE_prog = 0
    RULE_sty = 1
    RULE_field = 2
    RULE_data = 3
    RULE_vardef = 4
    RULE_vardef_old = 5
    RULE_meta = 6
    RULE_wresl = 7

    ruleNames =  [ u"prog", u"sty", u"field", u"data", u"vardef", u"vardef_old", 
                   u"meta", u"wresl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    LINE_COMMENT=4
    STRING=5
    END=6
    STUDY=7
    DATA=8
    VARDEF=9
    METADATA=10
    WRESL=11
    ID=12
    FLOAT=13
    INT=14
    NL=15
    WS=16

    def __init__(self, input):
        super(SettingParser, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    styobj=None
    thisFile='';


    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SettingParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i=None):
            if i is None:
                return self.getTokens(SettingParser.NL)
            else:
                return self.getToken(SettingParser.NL, i)

        def sty(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SettingParser.StyContext)
            else:
                return self.getTypedRuleContext(SettingParser.StyContext,i)


        def getRuleIndex(self):
            return SettingParser.RULE_prog

        def accept(self, visitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SettingParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        S.studyMap={}
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SettingParser.NL:
                self.state = 16
                self.match(SettingParser.NL)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.sty()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SettingParser.STUDY):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SettingParser.StyContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def STUDY(self):
            return self.getToken(SettingParser.STUDY, 0)

        def END(self):
            return self.getToken(SettingParser.END, 0)

        def ID(self):
            return self.getToken(SettingParser.ID, 0)

        def NL(self, i=None):
            if i is None:
                return self.getTokens(SettingParser.NL)
            else:
                return self.getToken(SettingParser.NL, i)

        def field(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SettingParser.FieldContext)
            else:
                return self.getTypedRuleContext(SettingParser.FieldContext,i)


        def getRuleIndex(self):
            return SettingParser.RULE_sty

        def accept(self, visitor):
            if hasattr(visitor, "visitSty"):
                return visitor.visitSty(self)
            else:
                return visitor.visitChildren(self)




    def sty(self):

        localctx = SettingParser.StyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sty)
        self.styobj=Study()
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(SettingParser.STUDY)
            self.state = 28
            localctx.name = self.match(SettingParser.ID)
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self.match(SettingParser.NL)
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SettingParser.NL):
                    break

            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.field()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SettingParser.DATA) | (1 << SettingParser.VARDEF) | (1 << SettingParser.METADATA) | (1 << SettingParser.WRESL))) != 0)):
                    break

            self.state = 39
            self.match(SettingParser.END)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.match(SettingParser.NL)
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SettingParser.NL):
                    break

            self._ctx.stop = self._input.LT(-1)
            stycopy=copy.deepcopy(self.styobj);styName=str((None if localctx.name is None else localctx.name.text)); S.studyMap[styName]=stycopy;
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SettingParser.FieldContext, self).__init__(parent, invokingState)
            self.parser = parser

        def data(self):
            return self.getTypedRuleContext(SettingParser.DataContext,0)


        def vardef(self):
            return self.getTypedRuleContext(SettingParser.VardefContext,0)


        def meta(self):
            return self.getTypedRuleContext(SettingParser.MetaContext,0)


        def wresl(self):
            return self.getTypedRuleContext(SettingParser.WreslContext,0)


        def NL(self, i=None):
            if i is None:
                return self.getTokens(SettingParser.NL)
            else:
                return self.getToken(SettingParser.NL, i)

        def getRuleIndex(self):
            return SettingParser.RULE_field

        def accept(self, visitor):
            if hasattr(visitor, "visitField"):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = SettingParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SettingParser.DATA]:
                self.state = 45
                self.data()
                pass
            elif token in [SettingParser.VARDEF]:
                self.state = 46
                self.vardef()
                pass
            elif token in [SettingParser.METADATA]:
                self.state = 47
                self.meta()
                pass
            elif token in [SettingParser.WRESL]:
                self.state = 48
                self.wresl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.match(SettingParser.NL)
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SettingParser.NL):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SettingParser.DataContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.s1 = None # Token
            self.s2 = None # Token

        def DATA(self):
            return self.getToken(SettingParser.DATA, 0)

        def STRING(self, i=None):
            if i is None:
                return self.getTokens(SettingParser.STRING)
            else:
                return self.getToken(SettingParser.STRING, i)

        def getRuleIndex(self):
            return SettingParser.RULE_data

        def accept(self, visitor):
            if hasattr(visitor, "visitData"):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = SettingParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(SettingParser.DATA)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SettingParser.T__0:
                self.state = 57
                self.match(SettingParser.T__0)


            self.state = 60
            localctx.s1 = self.match(SettingParser.STRING)
            s1=(None if localctx.s1 is None else localctx.s1.text)[1:-1];self.styobj.data_src.append(str(s1))
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SettingParser.T__1:
                self.state = 62
                self.match(SettingParser.T__1)
                self.state = 63
                localctx.s2 = self.match(SettingParser.STRING)
                s2=(None if localctx.s2 is None else localctx.s2.text)[1:-1];self.styobj.data_src.append(str(s2))
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SettingParser.VardefContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.s1 = None # Token

        def VARDEF(self):
            return self.getToken(SettingParser.VARDEF, 0)

        def STRING(self):
            return self.getToken(SettingParser.STRING, 0)

        def getRuleIndex(self):
            return SettingParser.RULE_vardef

        def accept(self, visitor):
            if hasattr(visitor, "visitVardef"):
                return visitor.visitVardef(self)
            else:
                return visitor.visitChildren(self)




    def vardef(self):

        localctx = SettingParser.VardefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(SettingParser.VARDEF)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SettingParser.T__0:
                self.state = 71
                self.match(SettingParser.T__0)


            self.state = 74
            localctx.s1 = self.match(SettingParser.STRING)
            s=(None if localctx.s1 is None else localctx.s1.text)[1:-1];self.styobj.varFile=s;
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Vardef_oldContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SettingParser.Vardef_oldContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.f = None # Token

        def VARDEF(self, i=None):
            if i is None:
                return self.getTokens(SettingParser.VARDEF)
            else:
                return self.getToken(SettingParser.VARDEF, i)

        def ID(self):
            return self.getToken(SettingParser.ID, 0)

        def getRuleIndex(self):
            return SettingParser.RULE_vardef_old

        def accept(self, visitor):
            if hasattr(visitor, "visitVardef_old"):
                return visitor.visitVardef_old(self)
            else:
                return visitor.visitChildren(self)




    def vardef_old(self):

        localctx = SettingParser.Vardef_oldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardef_old)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(SettingParser.VARDEF)
            self.state = 78
            self.match(SettingParser.T__0)
            self.state = 79
            localctx.f = self.match(SettingParser.ID)
            self.state = 80
            self.match(SettingParser.T__2)
            self.state = 81
            self.match(SettingParser.VARDEF)
            f=str((None if localctx.f is None else localctx.f.text));self.styobj.varFile=f;
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetaContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SettingParser.MetaContext, self).__init__(parent, invokingState)
            self.parser = parser

        def METADATA(self):
            return self.getToken(SettingParser.METADATA, 0)

        def STRING(self):
            return self.getToken(SettingParser.STRING, 0)

        def getRuleIndex(self):
            return SettingParser.RULE_meta

        def accept(self, visitor):
            if hasattr(visitor, "visitMeta"):
                return visitor.visitMeta(self)
            else:
                return visitor.visitChildren(self)




    def meta(self):

        localctx = SettingParser.MetaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_meta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(SettingParser.METADATA)
            self.state = 85
            self.match(SettingParser.T__0)
            self.state = 86
            self.match(SettingParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WreslContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SettingParser.WreslContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WRESL(self):
            return self.getToken(SettingParser.WRESL, 0)

        def STRING(self):
            return self.getToken(SettingParser.STRING, 0)

        def getRuleIndex(self):
            return SettingParser.RULE_wresl

        def accept(self, visitor):
            if hasattr(visitor, "visitWresl"):
                return visitor.visitWresl(self)
            else:
                return visitor.visitChildren(self)




    def wresl(self):

        localctx = SettingParser.WreslContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_wresl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(SettingParser.WRESL)
            self.state = 89
            self.match(SettingParser.T__0)
            self.state = 90
            self.match(SettingParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





