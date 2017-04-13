# Generated from VarDef.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
from collections import defaultdict

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\26o\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26\n\2\f\2\16\2\31\13")
        buf.write(u"\2\3\2\6\2\34\n\2\r\2\16\2\35\3\3\3\3\3\3\6\3#\n\3\r")
        buf.write(u"\3\16\3$\3\3\6\3(\n\3\r\3\16\3)\3\3\3\3\6\3.\n\3\r\3")
        buf.write(u"\16\3/\3\4\3\4\3\4\3\4\5\4\66\n\4\3\4\6\49\n\4\r\4\16")
        buf.write(u"\4:\3\5\3\5\3\5\3\6\3\6\5\6B\n\6\3\6\3\6\3\6\3\6\3\6")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\5\tT\n\t")
        buf.write(u"\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n")
        buf.write(u"b\n\n\3\n\3\n\3\n\3\n\3\n\3\n\7\nj\n\n\f\n\16\nm\13\n")
        buf.write(u"\3\n\2\3\22\13\2\4\6\b\n\f\16\20\22\2\5\3\2\22\24\3\2")
        buf.write(u"\r\16\3\2\17\20u\2\27\3\2\2\2\4\37\3\2\2\2\6\65\3\2\2")
        buf.write(u"\2\b<\3\2\2\2\nA\3\2\2\2\fH\3\2\2\2\16O\3\2\2\2\20S\3")
        buf.write(u"\2\2\2\22a\3\2\2\2\24\26\7\25\2\2\25\24\3\2\2\2\26\31")
        buf.write(u"\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\33\3\2\2\2\31")
        buf.write(u"\27\3\2\2\2\32\34\5\4\3\2\33\32\3\2\2\2\34\35\3\2\2\2")
        buf.write(u"\35\33\3\2\2\2\35\36\3\2\2\2\36\3\3\2\2\2\37 \7\n\2\2")
        buf.write(u" \"\7\21\2\2!#\7\25\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2")
        buf.write(u"\2$%\3\2\2\2%\'\3\2\2\2&(\5\6\4\2\'&\3\2\2\2()\3\2\2")
        buf.write(u"\2)\'\3\2\2\2)*\3\2\2\2*+\3\2\2\2+-\7\13\2\2,.\7\25\2")
        buf.write(u"\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\5\3\2")
        buf.write(u"\2\2\61\66\5\n\6\2\62\66\5\f\7\2\63\66\5\20\t\2\64\66")
        buf.write(u"\5\b\5\2\65\61\3\2\2\2\65\62\3\2\2\2\65\63\3\2\2\2\65")
        buf.write(u"\64\3\2\2\2\668\3\2\2\2\679\7\25\2\28\67\3\2\2\29:\3")
        buf.write(u"\2\2\2:8\3\2\2\2:;\3\2\2\2;\7\3\2\2\2<=\7\t\2\2=>\7\21")
        buf.write(u"\2\2>\t\3\2\2\2?@\7\b\2\2@B\b\6\1\2A?\3\2\2\2AB\3\2\2")
        buf.write(u"\2BC\3\2\2\2CD\7\21\2\2DE\7\3\2\2EF\7\f\2\2FG\b\6\1\2")
        buf.write(u"G\13\3\2\2\2HI\7\21\2\2IJ\7\4\2\2JK\7\21\2\2KL\7\3\2")
        buf.write(u"\2LM\5\16\b\2MN\b\7\1\2N\r\3\2\2\2OP\t\2\2\2P\17\3\2")
        buf.write(u"\2\2QR\7\b\2\2RT\b\t\1\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2")
        buf.write(u"\2UV\7\21\2\2VW\7\3\2\2WX\5\22\n\2X\21\3\2\2\2YZ\b\n")
        buf.write(u"\1\2Zb\7\23\2\2[b\7\22\2\2\\b\7\21\2\2]^\7\5\2\2^_\5")
        buf.write(u"\22\n\2_`\7\6\2\2`b\3\2\2\2aY\3\2\2\2a[\3\2\2\2a\\\3")
        buf.write(u"\2\2\2a]\3\2\2\2bk\3\2\2\2cd\f\b\2\2de\t\3\2\2ej\5\22")
        buf.write(u"\n\tfg\f\7\2\2gh\t\4\2\2hj\5\22\n\bic\3\2\2\2if\3\2\2")
        buf.write(u"\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2l\23\3\2\2\2mk\3\2\2")
        buf.write(u"\2\16\27\35$)/\65:ASaik")
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
                      u"FLOAT", u"INT", u"STRING", u"NL", u"WS" ]

    RULE_prog = 0
    RULE_vardef = 1
    RULE_field = 2
    RULE_include = 3
    RULE_var_path = 4
    RULE_var_meta = 5
    RULE_info = 6
    RULE_stat = 7
    RULE_ee = 8

    ruleNames =  [ u"prog", u"vardef", u"field", u"include", u"var_path", 
                   u"var_meta", u"info", u"stat", u"ee" ]

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
    FLOAT=16
    INT=17
    STRING=18
    NL=19
    WS=20

    def __init__(self, input):
        super(VarDefParser, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    varPathGroupMap={};
    varExprGroupMap={};
    tempVarGroupList={};
    varPathMap={};
    varExprMap={};
    tempVarList=[];


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
        self.varPathGroupMap={};self.varExprGroupMap={};self.tempVarGroupList={}
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VarDefParser.NL:
                self.state = 18
                self.match(VarDefParser.NL)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.vardef()
                self.state = 27 
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
        self.varPathMap={};self.varExprMap={};self.tempVarList=[]
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(VarDefParser.VARDEF)
            self.state = 30
            localctx.name = self.match(VarDefParser.ID)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.match(VarDefParser.NL)
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.field()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDefParser.T) | (1 << VarDefParser.INCLUDE) | (1 << VarDefParser.ID))) != 0)):
                    break

            self.state = 41
            self.match(VarDefParser.END)
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.match(VarDefParser.NL)
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VarDefParser.NL):
                    break

            self._ctx.stop = self._input.LT(-1)
            groupName=(None if localctx.name is None else localctx.name.text);
            self.varPathGroupMap[groupName]=self.varPathMap;
            self.varExprGroupMap[groupName]=self.varExprMap;
            self.tempVarGroupList[groupName]=self.tempVarList;	

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
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 47
                self.var_path()
                pass

            elif la_ == 2:
                self.state = 48
                self.var_meta()
                pass

            elif la_ == 3:
                self.state = 49
                self.stat()
                pass

            elif la_ == 4:
                self.state = 50
                self.include()
                pass


            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.match(VarDefParser.NL)
                self.state = 56 
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
            self.state = 58
            self.match(VarDefParser.INCLUDE)
            self.state = 59
            localctx.g = self.match(VarDefParser.ID)
            self._ctx.stop = self._input.LT(-1)
            gn=(None if localctx.g is None else localctx.g.text);
            if gn: 
            	self.varPathMap.update(self.varPathGroupMap[gn])
            	self.varExprMap.update(self.varExprGroupMap[gn])

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
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 61
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 65
            localctx.i = self.match(VarDefParser.ID)
            self.state = 66
            self.match(VarDefParser.T__0)
            self.state = 67
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
        self.enterRule(localctx, 10, self.RULE_var_meta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            localctx.v = self.match(VarDefParser.ID)
            self.state = 71
            self.match(VarDefParser.T__1)
            self.state = 72
            localctx.p = self.match(VarDefParser.ID)
            self.state = 73
            self.match(VarDefParser.T__0)
            self.state = 74
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
        self.enterRule(localctx, 12, self.RULE_info)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
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
        self.enterRule(localctx, 14, self.RULE_stat)
        isTemp=False 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==VarDefParser.T:
                self.state = 79
                self.match(VarDefParser.T)
                isTemp=True


            self.state = 83
            localctx.i = self.match(VarDefParser.ID)
            self.state = 84
            self.match(VarDefParser.T__0)
            self.state = 85
            localctx.e = self.ee(0)
            self._ctx.stop = self._input.LT(-1)
            v = Var('');e=str((None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop))));v.expr=e; 
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
            self.a = None # EeContext
            self.op = None # Token
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDefParser.INT]:
                self.state = 88
                self.match(VarDefParser.INT)
                pass
            elif token in [VarDefParser.FLOAT]:
                self.state = 89
                self.match(VarDefParser.FLOAT)
                pass
            elif token in [VarDefParser.ID]:
                self.state = 90
                self.match(VarDefParser.ID)
                pass
            elif token in [VarDefParser.T__2]:
                self.state = 91
                self.match(VarDefParser.T__2)
                self.state = 92
                self.ee(0)
                self.state = 93
                self.match(VarDefParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 103
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 97
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 98
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.MUL or _la==VarDefParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 99
                        localctx.b = self.ee(7)
                        pass

                    elif la_ == 2:
                        localctx = VarDefParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 100
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 101
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDefParser.ADD or _la==VarDefParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 102
                        localctx.b = self.ee(6)
                        pass

             
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.ee_sempred
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
         




