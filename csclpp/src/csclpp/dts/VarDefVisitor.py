# Generated from VarDef.g4 by ANTLR 4.6
from antlr4 import *

from Study import Study
from Var import Var
from collections import defaultdict
import collections
from antlr4.error import Err


# This class defines a complete generic visitor for a parse tree produced by VarDefParser.

class VarDefVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VarDefParser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#use.
    def visitUse(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#vardef.
    def visitVardef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#field.
    def visitField(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#new_var.
    def visitNew_var(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#array.
    def visitArray(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#array_var.
    def visitArray_var(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#array_cluster.
    def visitArray_cluster(self, ctx):
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


    # Visit a parse tree produced by VarDefParser#metaKey.
    def visitMetaKey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#metaValue.
    def visitMetaValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#ee.
    def visitEe(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#compare.
    def visitCompare(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#assign.
    def visitAssign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#id2.
    def visitId2(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#if_stat.
    def visitIf_stat(self, ctx):
        return self.visitChildren(ctx)


