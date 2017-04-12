import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from VarDefLexer import VarDefLexer
from VarDefParser import VarDefParser
from SettingLexer import SettingLexer
from SettingParser import SettingParser
from ExprLexer import ExprLexer
from ExprParser import ExprParser
# from EvalLexer import EvalLexer
# from EvalParser import EvalParser
#from DtsVisitor import DtsVisitor


def parseVarDef(f):

    input_stream = FileStream(f)
    lexer = VarDefLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    p = VarDefParser(token_stream)
    tree = p.prog()
    return p.varPathGroupMap, p.varExprGroupMap, p.tempVarGroupList
    
#     visitor = DtsVisitor()
#     visitor.visit(tree)


def parseSetting(f):
 
    input_stream = FileStream(f)
    lexer = SettingLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SettingParser(token_stream)
    s=parser.prog()


def evaluateDTS(varTs, line):
    
    istream = InputStream(line)
    lexer = ExprLexer(istream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    parser.varTs = varTs
    parser.prog()


# def evaluateDTS(f):
#  
#     input_stream = FileStream(f)
#     lexer = EvalLexer(input_stream)
#     token_stream = CommonTokenStream(lexer)
#     parser = EvalParser(token_stream)
#     s=parser.prog()
    
    
    
    