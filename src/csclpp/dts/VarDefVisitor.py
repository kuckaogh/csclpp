# Generated from VarDef.g4 by ANTLR 4.6
from antlr4 import *

from Study import Study
from Var import Var
import Temp as T


# This class defines a complete generic visitor for a parse tree produced by VarDefParser.

class VarDefVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VarDefParser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#vardef.
    def visitVardef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#field.
    def visitField(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#include.
    def visitInclude(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#var_path.
    def visitVar_path(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#var_meta.
    def visitVar_meta(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#info.
    def visitInfo(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#assign.
    def visitAssign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#parens.
    def visitParens(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#MulDiv.
    def visitMulDiv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#AddSub.
    def visitAddSub(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#id.
    def visitId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#int.
    def visitInt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#number.
    def visitNumber(self, ctx):
        return self.visitChildren(ctx)


