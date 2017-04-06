# Generated from VarDef.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
import Temp as T

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\26w\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2")
        buf.write(u"\16\2\33\13\2\3\2\6\2\36\n\2\r\2\16\2\37\3\3\3\3\3\3")
        buf.write(u"\6\3%\n\3\r\3\16\3&\3\3\6\3*\n\3\r\3\16\3+\3\3\3\3\6")
        buf.write(u"\3\60\n\3\r\3\16\3\61\3\4\3\4\3\4\3\4\5\48\n\4\3\4\6")
        buf.write(u"\4;\n\4\r\4\16\4<\3\5\3\5\3\5\3\6\3\6\5\6D\n\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5")
        buf.write(u"\bT\n\b\3\t\3\t\5\tX\n\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write(u"\5\na\n\n\3\n\3\n\3\n\3\n\3\n\5\nh\n\n\3\n\3\n\3\n\3")
        buf.write(u"\n\3\n\3\n\7\np\n\n\f\n\16\ns\13\n\3\13\3\13\3\13\2\3")
        buf.write(u"\22\f\2\4\6\b\n\f\16\20\22\24\2\5\3\2\r\16\3\2\17\20")
        buf.write(u"\3\2\23\24}\2\31\3\2\2\2\4!\3\2\2\2\6\67\3\2\2\2\b>\3")
        buf.write(u"\2\2\2\nC\3\2\2\2\fJ\3\2\2\2\16S\3\2\2\2\20W\3\2\2\2")
        buf.write(u"\22g\3\2\2\2\24t\3\2\2\2\26\30\7\25\2\2\27\26\3\2\2\2")
        buf.write(u"\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\35\3\2")
        buf.write(u"\2\2\33\31\3\2\2\2\34\36\5\4\3\2\35\34\3\2\2\2\36\37")
        buf.write(u"\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \3\3\2\2\2!\"\7\n")
        buf.write(u"\2\2\"$\7\21\2\2#%\7\25\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2")
        buf.write(u"\2\2&\'\3\2\2\2\')\3\2\2\2(*\5\6\4\2)(\3\2\2\2*+\3\2")
        buf.write(u"\2\2+)\3\2\2\2+,\3\2\2\2,-\3\2\2\2-/\7\13\2\2.\60\7\25")
        buf.write(u"\2\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2")
        buf.write(u"\2\62\5\3\2\2\2\638\5\n\6\2\648\5\f\7\2\658\5\20\t\2")
        buf.write(u"\668\5\b\5\2\67\63\3\2\2\2\67\64\3\2\2\2\67\65\3\2\2")
        buf.write(u"\2\67\66\3\2\2\28:\3\2\2\29;\7\25\2\2:9\3\2\2\2;<\3\2")
        buf.write(u"\2\2<:\3\2\2\2<=\3\2\2\2=\7\3\2\2\2>?\7\t\2\2?@\7\21")
        buf.write(u"\2\2@\t\3\2\2\2AB\7\b\2\2BD\b\6\1\2CA\3\2\2\2CD\3\2\2")
        buf.write(u"\2DE\3\2\2\2EF\7\21\2\2FG\7\3\2\2GH\7\f\2\2HI\b\6\1\2")
        buf.write(u"I\13\3\2\2\2JK\7\21\2\2KL\7\4\2\2LM\7\21\2\2MN\7\3\2")
        buf.write(u"\2NO\5\16\b\2OP\b\7\1\2P\r\3\2\2\2QT\5\24\13\2RT\7\22")
        buf.write(u"\2\2SQ\3\2\2\2SR\3\2\2\2T\17\3\2\2\2UV\7\b\2\2VX\b\t")
        buf.write(u"\1\2WU\3\2\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\21\2\2Z[\7\3\2")
        buf.write(u"\2[\\\5\22\n\2\\\21\3\2\2\2]^\b\n\1\2^h\5\24\13\2_a\7")
        buf.write(u"\b\2\2`_\3\2\2\2`a\3\2\2\2ab\3\2\2\2bh\7\21\2\2cd\7\5")
        buf.write(u"\2\2de\5\22\n\2ef\7\6\2\2fh\3\2\2\2g]\3\2\2\2g`\3\2\2")
        buf.write(u"\2gc\3\2\2\2hq\3\2\2\2ij\f\7\2\2jk\t\2\2\2kp\5\22\n\b")
        buf.write(u"lm\f\6\2\2mn\t\3\2\2np\5\22\n\7oi\3\2\2\2ol\3\2\2\2p")
        buf.write(u"s\3\2\2\2qo\3\2\2\2qr\3\2\2\2r\23\3\2\2\2sq\3\2\2\2t")
        buf.write(u"u\t\4\2\2u\25\3\2\2\2\20\31\37&+\61\67<CSW`goq")
        return buf.getvalue()


class VarDefParser ( Parser ):

    grammarFileName = "VarDef.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"'.'", u"'('", u"')'", u"<INVALID>", 
                     u"'@'", u"'include'", u"'vardef'", u"'end'", u"<INVALID>", 
                     u"'*'", u"'/'", u"'+'", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"LINE_COMMENT", u"T", u"INCLUDE", u"VARDEF", 
                      u"END", u"PATH", u"MUL", u"DIV", u"ADD", u"SUB", u"ID", 
                      u"STRING", u"FLOAT", u"INT", u"NL", u"WS" ]

    RULE_prog = 0
    RULE_vardef = 1
    RULE_field = 2
    RULE_include = 3
    RULE_var_path = 4
    RULE_var_meta = 5
    RULE_info = 6
    RULE_stat = 7
    RULE_expr = 8
    RULE_number = 9

    ruleNames =  [ u"prog", u"vardef", u"field", u"include", u"var_path", 
                   u"var_meta", u"info", u"stat", u"expr", u"number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    LINE_COMMENT=5
    T=6
    INCLUDE=7
    VARDEF=8
    END=9
    PATH=10
    MUL=11
    DIV=12
    ADD=13
    SUB=14
    ID=15
    STRING=16
    FLOAT=17
    INT=18
    NL=19
    WS=20

    def __init__(self, input):
        super(VarDefParser, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



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
        T.varGroupMap={}
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 20
                self.match(VarDefParser.NL)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.vardef()
                self.state = 29 
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
        T.varMap={}
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(VarDefParser.VARDEF)
            self.state = 32
            localctx.name = self.match(VarDefParser.ID)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.match(VarDefParser.NL)
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.field()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 43
            self.match(VarDefParser.END)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.match(VarDefParser.NL)
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self._ctx.stop = self._input.LT(-1)
            vm=T.varMap.copy(); groupName=(None if localctx.name is None else localctx.name.text); T.varGroupMap[groupName]=vm;
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
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 49
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 50
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 51
                self.stat()
                pass

            elif la_ == 4:
                self.state = 52
                self.include()
                pass


            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.match(VarDefParser.NL)
                self.state = 58 
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
        self.enterRule(localctx, 6, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(VarDefParser.INCLUDE)
            self.state = 61
            localctx.g = self.match(VarDefParser.ID)
            self._ctx.stop = self._input.LT(-1)
            gn=(None if localctx.g is None else localctx.g.text);T.varMap.update(T.varGroupMap[gn]); 
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
        self.enterRule(localctx, 8, self.RULE_var_path)
        isTemp=False 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 63
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 67
            localctx.i = self.match(VarDefParser.ID)
            self.state = 68
            self.match(VarDefParser.T__0)
            self.state = 69
            localctx.p = self.match(VarDefParser.PATH)
            p =(None if localctx.p is None else localctx.p.text); t = Var(p);t.isTemp=isTemp; 
            name=(None if localctx.i is None else localctx.i.text); T.varMap[name]=t; 	

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
        self.enterRule(localctx, 10, self.RULE_var_meta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            localctx.v = self.match(VarDefParser.ID)
            self.state = 73
            self.match(VarDefParser.T__1)
            self.state = 74
            localctx.p = self.match(VarDefParser.ID)
            self.state = 75
            self.match(VarDefParser.T__0)
            self.state = 76
            localctx.inf = self.info()
            vn=(None if localctx.v is None else localctx.v.text);pn=(None if localctx.p is None else localctx.p.text);T.varMap[vn].metaData[pn]=(None if localctx.inf is None else self._input.getText((localctx.inf.start,localctx.inf.stop)));
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

        def number(self):
            return self.getTypedRuleContext(VarDefParser.NumberContext,0)


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
        self.enterRule(localctx, 12, self.RULE_info)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT, VarDefParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.number()
                pass
            elif token in [VarDefParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(VarDefParser.STRING)
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


        def getRuleIndex(self):
            return VarDefParser.RULE_stat

     
        def copyFrom(self, ctx):
            super(VarDefParser.StatContext, self).copyFrom(ctx)



    class AssignContext(StatContext):

        def __init__(self, parser, ctx): # actually a VarDefParser.StatContext)
            super(VarDefParser.AssignContext, self).__init__(parser)
            self.i = None # Token
            self.e = None # ExprContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(VarDefParser.ExprContext,0)

        def T(self):
            return self.getToken(VarDefParser.T, 0)

        def accept(self, visitor):
            if hasattr(visitor, "visitAssign"):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = VarDefParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stat)
        isTemp=False 
        self._la = 0 # Token type
        try:
            localctx = VarDefParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 83
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 87
            localctx.i = self.match(VarDefParser.ID)
            self.state = 88
            self.match(VarDefParser.T__0)
            self.state = 89
            localctx.e = self.expr(0)
            self._ctx.stop = self._input.LT(-1)
            v = Var('');v.isTemp=isTemp;e=(None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)));v.expr=e; 
            name=(None if localctx.i is None else localctx.i.text); T.varMap[name]=v; 	

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDefParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VarDefParser.RULE_expr

     
        def copyFrom(self, ctx):
            super(VarDefParser.ExprContext, self).copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx): # actually a VarDefParser.ExprContext)
            super(VarDefParser.ParensContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(VarDefParser.ExprContext,0)


        def accept(self, visitor):
            if hasattr(visitor, "visitParens"):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx): # actually a VarDefParser.ExprContext)
            super(VarDefParser.MulDivContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.ExprContext)
            else:
                return self.getTypedRuleContext(VarDefParser.ExprContext,i)


        def accept(self, visitor):
            if hasattr(visitor, "visitMulDiv"):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx): # actually a VarDefParser.ExprContext)
            super(VarDefParser.AddSubContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDefParser.ExprContext)
            else:
                return self.getTypedRuleContext(VarDefParser.ExprContext,i)


        def accept(self, visitor):
            if hasattr(visitor, "visitAddSub"):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx): # actually a VarDefParser.ExprContext)
            super(VarDefParser.IdContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(VarDefParser.ID, 0)
        def T(self):
            return self.getToken(VarDefParser.T, 0)

        def accept(self, visitor):
            if hasattr(visitor, "visitId"):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx): # actually a VarDefParser.ExprContext)
            super(VarDefParser.IntContext, self).__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(VarDefParser.NumberContext,0)


        def accept(self, visitor):
            if hasattr(visitor, "visitInt"):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VarDefParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.FLOAT, VarDefParser.INT]:
                localctx = VarDefParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 92
                self.number()
                pass
            elif token in [VarDefParser.T, VarDefParser.ID]:
                localctx = VarDefParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==VarDefParser.T:
                    self.state = 93
                    self.match(VarDefParser.T)


                self.state = 96
                self.match(VarDefParser.ID)
                pass
            elif token in [VarDefParser.T__2]:
                localctx = VarDefParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(VarDefParser.T__2)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(VarDefParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 109
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.MulDivContext(self, VarDefParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 104
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 105
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.AddSubContext(self, VarDefParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 106
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 107
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 108
                        self.expr(5)
                        pass

             
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 18, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
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



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




