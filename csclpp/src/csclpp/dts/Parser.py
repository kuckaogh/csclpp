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
ifsTsDictName='_ts'
ifsNewDictName=ifsTsDictName
varMetaKeys=['units','capacity']

def parseVarDef(f, sysConstMap):

    input_stream = FileStream(f)
    lexer = VarDefLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    p = VarDefParser(token_stream)
    p.ifsAppend=ifsTsDictName
    p.ifsNewAppend=ifsNewDictName
    p.varMetaKeys=varMetaKeys
    p.vardefFile=f
    p.systemConstMap=sysConstMap
    tree = p.prog()
    #print(tree.toStringTree(recog=p))
    return p.vardefDefault, p.varPathGroupMap, \
        p.tempVarGroupList, p.ifsMapGroupMap, \
        p.strArrayGroupMap, p.intArrayGroupMap, p.floatArrayGroupMap, p.constGroupMap
    
#     visitor = DtsVisitor()
#     visitor.visit(tree)


def parseSetting(f):
 
    input_stream = FileStream(f)
    lexer = SettingLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SettingParser(token_stream)
    parser.thisFile=f
    s=parser.prog()


def evaluateDTS(varTs, line):
    
    istream = InputStream(line)
    lexer = ExprLexer(istream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    parser.varTs = varTs
    parser.expression()


# def evaluateDTS(f):
#  
#     input_stream = FileStream(f)
#     lexer = EvalLexer(input_stream)
#     token_stream = CommonTokenStream(lexer)
#     parser = EvalParser(token_stream)
#     s=parser.prog()
    
    
    
    