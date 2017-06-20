# Generated from Setting.g4 by ANTLR 4.6
from antlr4 import *

from Study import Study
from Var import Var
import Setting as S
import copy


# This class defines a complete generic visitor for a parse tree produced by SettingParser.

class SettingVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SettingParser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SettingParser#sty.
    def visitSty(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SettingParser#field.
    def visitField(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SettingParser#data.
    def visitData(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SettingParser#vardef.
    def visitVardef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SettingParser#vardef_old.
    def visitVardef_old(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SettingParser#meta.
    def visitMeta(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SettingParser#wresl.
    def visitWresl(self, ctx):
        return self.visitChildren(ctx)


