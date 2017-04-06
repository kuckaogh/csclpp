import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from VarDefLexer import VarDefLexer
from VarDefParser import VarDefParser
from SettingLexer import SettingLexer
from SettingParser import SettingParser
#from DtsVisitor import DtsVisitor


def parseVarDef(f):

    input_stream = FileStream(f)
    lexer = VarDefLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = VarDefParser(token_stream)
    tree = parser.prog()
#     visitor = DtsVisitor()
#     visitor.visit(tree)


def parseSetting(f):
 
    input_stream = FileStream(f)
    lexer = SettingLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SettingParser(token_stream)
    s=parser.prog()
