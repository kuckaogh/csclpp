# Generated from Expr.g4 by ANTLR 4.6
from antlr4 import *

from Study import Study
from Var import Var
import ParserTools as P


# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ee.
    def visitEe(self, ctx):
        return self.visitChildren(ctx)


