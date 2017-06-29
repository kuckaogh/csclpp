# Generated from VarDef.g4 by ANTLR 4.6
from antlr4 import *

from Study import Study
from Var import Var
from collections import defaultdict
import collections
from antlr4.error import Err
import numpy as np


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


    # Visit a parse tree produced by VarDefParser#constant.
    def visitConstant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#intConst.
    def visitIntConst(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#floatConst.
    def visitFloatConst(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#floatConstVar.
    def visitFloatConstVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#intConstVar.
    def visitIntConstVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#strArray.
    def visitStrArray(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#strArrayCluster.
    def visitStrArrayCluster(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#strArrayLone.
    def visitStrArrayLone(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#strArrayVar.
    def visitStrArrayVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#intArray.
    def visitIntArray(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#intArrayCluster.
    def visitIntArrayCluster(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#intArrayLone.
    def visitIntArrayLone(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#intArrayVar.
    def visitIntArrayVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#floatArray.
    def visitFloatArray(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#floatArrayCluster.
    def visitFloatArrayCluster(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#floatArrayLone.
    def visitFloatArrayLone(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#floatArrayVar.
    def visitFloatArrayVar(self, ctx):
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


    # Visit a parse tree produced by VarDefParser#metaDict.
    def visitMetaDict(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#dict_pair.
    def visitDict_pair(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VarDefParser#number.
    def visitNumber(self, ctx):
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


