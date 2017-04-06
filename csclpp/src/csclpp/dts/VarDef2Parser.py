# Generated from VarDef2.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\r-\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\27\n\3\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\4\5\4 \n\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write(u"\4\7\4(\n\4\f\4\16\4+\13\4\3\4\2\3\6\5\2\4\6\2\4\3\2")
        buf.write(u"\6\7\3\2\b\t\60\2\t\3\2\2\2\4\26\3\2\2\2\6\37\3\2\2\2")
        buf.write(u"\b\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13")
        buf.write(u"\f\3\2\2\2\f\3\3\2\2\2\r\16\5\6\4\2\16\17\7\f\2\2\17")
        buf.write(u"\27\3\2\2\2\20\21\7\n\2\2\21\22\7\3\2\2\22\23\5\6\4\2")
        buf.write(u"\23\24\7\f\2\2\24\27\3\2\2\2\25\27\7\f\2\2\26\r\3\2\2")
        buf.write(u"\2\26\20\3\2\2\2\26\25\3\2\2\2\27\5\3\2\2\2\30\31\b\4")
        buf.write(u"\1\2\31 \7\13\2\2\32 \7\n\2\2\33\34\7\4\2\2\34\35\5\6")
        buf.write(u"\4\2\35\36\7\5\2\2\36 \3\2\2\2\37\30\3\2\2\2\37\32\3")
        buf.write(u"\2\2\2\37\33\3\2\2\2 )\3\2\2\2!\"\f\7\2\2\"#\t\2\2\2")
        buf.write(u"#(\5\6\4\b$%\f\6\2\2%&\t\3\2\2&(\5\6\4\7\'!\3\2\2\2\'")
        buf.write(u"$\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\7\3\2\2\2+")
        buf.write(u")\3\2\2\2\7\13\26\37\')")
        return buf.getvalue()


class VarDef2Parser ( Parser ):

    grammarFileName = "VarDef2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"'('", u"')'", u"'*'", u"'/'", 
                     u"'+'", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"MUL", u"DIV", u"ADD", u"SUB", u"ID", u"INT", u"NEWLINE", 
                      u"WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ u"prog", u"stat", u"expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    MUL=4
    DIV=5
    ADD=6
    SUB=7
    ID=8
    INT=9
    NEWLINE=10
    WS=11

    def __init__(self, input):
        super(VarDef2Parser, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDef2Parser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDef2Parser.StatContext)
            else:
                return self.getTypedRuleContext(VarDef2Parser.StatContext,i)


        def getRuleIndex(self):
            return VarDef2Parser.RULE_prog

        def accept(self, visitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = VarDef2Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VarDef2Parser.T__1) | (1 << VarDef2Parser.ID) | (1 << VarDef2Parser.INT) | (1 << VarDef2Parser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDef2Parser.StatContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VarDef2Parser.RULE_stat

     
        def copyFrom(self, ctx):
            super(VarDef2Parser.StatContext, self).copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx): # actually a VarDef2Parser.StatContext)
            super(VarDef2Parser.BlankContext, self).__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(VarDef2Parser.NEWLINE, 0)

        def accept(self, visitor):
            if hasattr(visitor, "visitBlank"):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx): # actually a VarDef2Parser.StatContext)
            super(VarDef2Parser.PrintExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(VarDef2Parser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(VarDef2Parser.NEWLINE, 0)

        def accept(self, visitor):
            if hasattr(visitor, "visitPrintExpr"):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx): # actually a VarDef2Parser.StatContext)
            super(VarDef2Parser.AssignContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(VarDef2Parser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(VarDef2Parser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(VarDef2Parser.NEWLINE, 0)

        def accept(self, visitor):
            if hasattr(visitor, "visitAssign"):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = VarDef2Parser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = VarDef2Parser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(VarDef2Parser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = VarDef2Parser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(VarDef2Parser.ID)
                self.state = 15
                self.match(VarDef2Parser.T__0)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(VarDef2Parser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = VarDef2Parser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(VarDef2Parser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(VarDef2Parser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VarDef2Parser.RULE_expr

     
        def copyFrom(self, ctx):
            super(VarDef2Parser.ExprContext, self).copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx): # actually a VarDef2Parser.ExprContext)
            super(VarDef2Parser.ParensContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(VarDef2Parser.ExprContext,0)


        def accept(self, visitor):
            if hasattr(visitor, "visitParens"):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx): # actually a VarDef2Parser.ExprContext)
            super(VarDef2Parser.MulDivContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDef2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(VarDef2Parser.ExprContext,i)


        def accept(self, visitor):
            if hasattr(visitor, "visitMulDiv"):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx): # actually a VarDef2Parser.ExprContext)
            super(VarDef2Parser.AddSubContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(VarDef2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(VarDef2Parser.ExprContext,i)


        def accept(self, visitor):
            if hasattr(visitor, "visitAddSub"):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx): # actually a VarDef2Parser.ExprContext)
            super(VarDef2Parser.IdContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(VarDef2Parser.ID, 0)

        def accept(self, visitor):
            if hasattr(visitor, "visitId"):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx): # actually a VarDef2Parser.ExprContext)
            super(VarDef2Parser.IntContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(VarDef2Parser.INT, 0)

        def accept(self, visitor):
            if hasattr(visitor, "visitInt"):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VarDef2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VarDef2Parser.INT]:
                localctx = VarDef2Parser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(VarDef2Parser.INT)
                pass
            elif token in [VarDef2Parser.ID]:
                localctx = VarDef2Parser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(VarDef2Parser.ID)
                pass
            elif token in [VarDef2Parser.T__1]:
                localctx = VarDef2Parser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(VarDef2Parser.T__1)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(VarDef2Parser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = VarDef2Parser.MulDivContext(self, VarDef2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 32
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDef2Parser.MUL or _la==VarDef2Parser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = VarDef2Parser.AddSubContext(self, VarDef2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 35
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==VarDef2Parser.ADD or _la==VarDef2Parser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        self.expr(5)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self._predicates[2] = self.expr_sempred
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
         




