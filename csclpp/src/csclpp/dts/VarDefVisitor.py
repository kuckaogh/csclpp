# Generated from VarDef.g4 by ANTLR 4.6
from antlr4 import *

from Study import Study
from Var import Var
import Temp as T
from collections import defaultdict


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


    # Visit a parse tree produced by VarDefParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#ee.
    def visitEe(self, ctx):
        return self.visitChildren(ctx)


