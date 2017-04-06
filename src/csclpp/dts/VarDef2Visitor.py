# Generated from VarDef2.g4 by ANTLR 4.6
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by VarDef2Parser.

class VarDef2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by VarDef2Parser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDef2Parser#printExpr.
    def visitPrintExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDef2Parser#assign.
    def visitAssign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDef2Parser#blank.
    def visitBlank(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDef2Parser#parens.
    def visitParens(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDef2Parser#MulDiv.
    def visitMulDiv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDef2Parser#AddSub.
    def visitAddSub(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDef2Parser#id.
    def visitId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDef2Parser#int.
    def visitInt(self, ctx):
        return self.visitChildren(ctx)


