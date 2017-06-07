# Generated from Expr.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from Study import Study
from Var import Var
import ParserTools as P

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\16,\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\6\2\r\n")
        buf.write(u"\2\r\2\16\2\16\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\5\3\33\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\7\3\'\n\3\f\3\16\3*\13\3\3\3\2\3\4\4\2\4\2\5\4\2\n\n")
        buf.write(u"\f\f\3\2\6\7\3\2\b\t.\2\f\3\2\2\2\4\32\3\2\2\2\6\7\7")
        buf.write(u"\13\2\2\7\b\7\3\2\2\b\t\5\4\3\2\t\n\7\r\2\2\n\13\b\2")
        buf.write(u"\1\2\13\r\3\2\2\2\f\6\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2")
        buf.write(u"\2\16\17\3\2\2\2\17\3\3\2\2\2\20\21\b\3\1\2\21\22\t\2")
        buf.write(u"\2\2\22\33\b\3\1\2\23\24\7\13\2\2\24\33\b\3\1\2\25\26")
        buf.write(u"\7\4\2\2\26\27\5\4\3\2\27\30\7\5\2\2\30\31\b\3\1\2\31")
        buf.write(u"\33\3\2\2\2\32\20\3\2\2\2\32\23\3\2\2\2\32\25\3\2\2\2")
        buf.write(u"\33(\3\2\2\2\34\35\f\7\2\2\35\36\t\3\2\2\36\37\5\4\3")
        buf.write(u"\b\37 \b\3\1\2 \'\3\2\2\2!\"\f\6\2\2\"#\t\4\2\2#$\5\4")
        buf.write(u"\3\7$%\b\3\1\2%\'\3\2\2\2&\34\3\2\2\2&!\3\2\2\2\'*\3")
        buf.write(u"\2\2\2(&\3\2\2\2()\3\2\2\2)\5\3\2\2\2*(\3\2\2\2\6\16")
        buf.write(u"\32&(")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"'('", u"')'", u"'*'", u"'/'", 
                     u"'+'", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"MUL", u"DIV", u"ADD", u"SUB", u"FLOAT", u"ID", u"INT", 
                      u"NEWLINE", u"WS" ]

    RULE_expression = 0
    RULE_ee = 1

    ruleNames =  [ u"expression", u"ee" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    MUL=4
    DIV=5
    ADD=6
    SUB=7
    FLOAT=8
    ID=9
    INT=10
    NEWLINE=11
    WS=12

    def __init__(self, input):
        super(ExprParser, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    varTs={}

    def evaluate(self, left, op, right):
        if   ExprParser.MUL == op.type:
            return left * right
        elif ExprParser.DIV == op.type:
            return left / right
        elif ExprParser.ADD == op.type:
            return left + right
        elif ExprParser.SUB == op.type:
            return left - right
        else:
            return 0


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i = None # Token
            self._ee = None # EeContext

        def ee(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.EeContext)
            else:
                return self.getTypedRuleContext(ExprParser.EeContext,i)


        def NEWLINE(self, i=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def ID(self, i=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def getRuleIndex(self):
            return ExprParser.RULE_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitExpression"):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ExprParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                localctx.i = self.match(ExprParser.ID)
                self.state = 5
                self.match(ExprParser.T__0)
                self.state = 6
                localctx._ee = self.ee(0)
                self.state = 7
                self.match(ExprParser.NEWLINE)
                id = str((None if localctx.i is None else localctx.i.text));self.varTs[id] = localctx._ee.v
                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ExprParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.EeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.a = None # EeContext
            self.number = None # Token
            self.i = None # Token
            self._ee = None # EeContext
            self.op = None # Token
            self.b = None # EeContext

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ee(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.EeContext)
            else:
                return self.getTypedRuleContext(ExprParser.EeContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_ee

        def accept(self, visitor):
            if hasattr(visitor, "visitEe"):
                return visitor.visitEe(self)
            else:
                return visitor.visitChildren(self)



    def ee(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.EeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_ee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.FLOAT, ExprParser.INT]:
                self.state = 15
                localctx.number = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ExprParser.FLOAT or _la==ExprParser.INT):
                    localctx.number = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.v = float((None if localctx.number is None else localctx.number.text))
                pass
            elif token in [ExprParser.ID]:
                self.state = 17
                localctx.i = self.match(ExprParser.ID)

                id = str((None if localctx.i is None else localctx.i.text));localctx.v =  self.varTs[id]
                    
                pass
            elif token in [ExprParser.T__1]:
                self.state = 19
                self.match(ExprParser.T__1)
                self.state = 20
                localctx._ee = self.ee(0)
                self.state = 21
                self.match(ExprParser.T__2)
                localctx.v = localctx._ee.v
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 26
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 27
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.MUL or _la==ExprParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        localctx.b = localctx._ee = self.ee(6)
                        localctx.v = self.evaluate(localctx.a.v, localctx.op, localctx.b.v)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.EeContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ee)
                        self.state = 31
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 32
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.ADD or _la==ExprParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        localctx.b = localctx._ee = self.ee(5)
                        localctx.v = self.evaluate(localctx.a.v, localctx.op, localctx.b.v)
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self._predicates[1] = self.ee_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def ee_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




