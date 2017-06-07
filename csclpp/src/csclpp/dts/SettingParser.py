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
        buf.write(u"\22T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\6\2\30\n")
        buf.write(u"\2\r\2\16\2\31\3\3\3\3\3\3\6\3\37\n\3\r\3\16\3 \3\3\6")
        buf.write(u"\3$\n\3\r\3\16\3%\3\3\3\3\6\3*\n\3\r\3\16\3+\3\4\3\4")
        buf.write(u"\3\4\3\4\5\4\62\n\4\3\4\6\4\65\n\4\r\4\16\4\66\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\5\7\5@\n\5\f\5\16\5C\13\5\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write(u"\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2V\2\23\3\2\2\2\4\33\3")
        buf.write(u"\2\2\2\6\61\3\2\2\2\b8\3\2\2\2\nD\3\2\2\2\fK\3\2\2\2")
        buf.write(u"\16O\3\2\2\2\20\22\7\21\2\2\21\20\3\2\2\2\22\25\3\2\2")
        buf.write(u"\2\23\21\3\2\2\2\23\24\3\2\2\2\24\27\3\2\2\2\25\23\3")
        buf.write(u"\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27")
        buf.write(u"\3\2\2\2\31\32\3\2\2\2\32\3\3\2\2\2\33\34\7\t\2\2\34")
        buf.write(u"\36\7\16\2\2\35\37\7\21\2\2\36\35\3\2\2\2\37 \3\2\2\2")
        buf.write(u" \36\3\2\2\2 !\3\2\2\2!#\3\2\2\2\"$\5\6\4\2#\"\3\2\2")
        buf.write(u"\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\')\7\b\2")
        buf.write(u"\2(*\7\21\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2")
        buf.write(u",\5\3\2\2\2-\62\5\b\5\2.\62\5\n\6\2/\62\5\f\7\2\60\62")
        buf.write(u"\5\16\b\2\61-\3\2\2\2\61.\3\2\2\2\61/\3\2\2\2\61\60\3")
        buf.write(u"\2\2\2\62\64\3\2\2\2\63\65\7\21\2\2\64\63\3\2\2\2\65")
        buf.write(u"\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67\7\3\2\2\2")
        buf.write(u"89\7\n\2\29:\7\3\2\2:;\7\7\2\2;A\b\5\1\2<=\7\4\2\2=>")
        buf.write(u"\7\7\2\2>@\b\5\1\2?<\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3")
        buf.write(u"\2\2\2B\t\3\2\2\2CA\3\2\2\2DE\7\13\2\2EF\7\3\2\2FG\7")
        buf.write(u"\16\2\2GH\7\5\2\2HI\7\16\2\2IJ\b\6\1\2J\13\3\2\2\2KL")
        buf.write(u"\7\f\2\2LM\7\3\2\2MN\7\7\2\2N\r\3\2\2\2OP\7\r\2\2PQ\7")
        buf.write(u"\3\2\2QR\7\7\2\2R\17\3\2\2\2\n\23\31 %+\61\66A")
        return buf.getvalue()


class SettingParser ( Parser ):

    grammarFileName = "Setting.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"','", u"'.'", u"<INVALID>", 
                     u"<INVALID>", u"'end'", u"'study'", u"'data'", u"'vardef'", 
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
    RULE_meta = 5
    RULE_wresl = 6

    ruleNames =  [ u"prog", u"sty", u"field", u"data", u"vardef", u"meta", 
                   u"wresl" ]

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SettingParser.NL:
                self.state = 14
                self.match(SettingParser.NL)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.sty()
                self.state = 23 
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
            self.state = 25
            self.match(SettingParser.STUDY)
            self.state = 26
            localctx.name = self.match(SettingParser.ID)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.match(SettingParser.NL)
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SettingParser.NL):
                    break

            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.field()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SettingParser.DATA) | (1 << SettingParser.VARDEF) | (1 << SettingParser.METADATA) | (1 << SettingParser.WRESL))) != 0)):
                    break

            self.state = 37
            self.match(SettingParser.END)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.match(SettingParser.NL)
                self.state = 41 
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
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SettingParser.DATA]:
                self.state = 43
                self.data()
                pass
            elif token in [SettingParser.VARDEF]:
                self.state = 44
                self.vardef()
                pass
            elif token in [SettingParser.METADATA]:
                self.state = 45
                self.meta()
                pass
            elif token in [SettingParser.WRESL]:
                self.state = 46
                self.wresl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self.match(SettingParser.NL)
                self.state = 52 
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
            self.state = 54
            self.match(SettingParser.DATA)
            self.state = 55
            self.match(SettingParser.T__0)
            self.state = 56
            localctx.s1 = self.match(SettingParser.STRING)
            s1=(None if localctx.s1 is None else localctx.s1.text)[1:-1];self.styobj.data_src.append(str(s1))
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SettingParser.T__1:
                self.state = 58
                self.match(SettingParser.T__1)
                self.state = 59
                localctx.s2 = self.match(SettingParser.STRING)
                s2=(None if localctx.s2 is None else localctx.s2.text)[1:-1];self.styobj.data_src.append(str(s2))
                self.state = 65
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
            self.f = None # Token
            self.d = None # Token

        def VARDEF(self):
            return self.getToken(SettingParser.VARDEF, 0)

        def ID(self, i=None):
            if i is None:
                return self.getTokens(SettingParser.ID)
            else:
                return self.getToken(SettingParser.ID, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(SettingParser.VARDEF)
            self.state = 67
            self.match(SettingParser.T__0)
            self.state = 68
            localctx.f = self.match(SettingParser.ID)
            self.state = 69
            self.match(SettingParser.T__2)
            self.state = 70
            localctx.d = self.match(SettingParser.ID)
            f=str((None if localctx.f is None else localctx.f.text));d=str((None if localctx.d is None else localctx.d.text));self.styobj.varFile=f;self.styobj.varDef=d;
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
        self.enterRule(localctx, 10, self.RULE_meta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SettingParser.METADATA)
            self.state = 74
            self.match(SettingParser.T__0)
            self.state = 75
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
        self.enterRule(localctx, 12, self.RULE_wresl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(SettingParser.WRESL)
            self.state = 78
            self.match(SettingParser.T__0)
            self.state = 79
            self.match(SettingParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





