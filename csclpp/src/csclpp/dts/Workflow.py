import sys
import Parser as P
from Study import Study
from Var import Var
import Setting as S
import Temp as T
import os

def setupReference(fs):
    
    ds = os.path.dirname(fs)
    
    P.parseSetting(fs)
    
    for s in S.studyMap:
        sty = S.studyMap[s]
        varFile=sty.varFile
        varDef =sty.varDef
        #print varFile, varDef
        
        vf=os.path.join(ds,varFile+'.vardef')
        P.parseVarDef(vf)
#         S.fileVarPathGroupMap[varFile]=T.varPathGroupMap
#         S.fileVarExprGroupMap[varFile]=T.varExprGroupMap
        sty.varPathMap=T.varPathGroupMap[varDef]
        sty.varExprMap=T.varExprGroupMap[varDef]
        
    return S.studyMap
#     for s in S.studyMap:
#         sty = S.studyMap[s]
#         for k in sty.varMap:
#             v=sty.varMap[k]
#             print k, v.isTemp, v.path, v.expr
            
def getPathReference():
    
    for s in S.studyMap:
        varMap = S.studyMap[s].varMap
        for name in varMap:
            c = varMap[name]
            if c.path:
                print name, c.path
        
        
        
        