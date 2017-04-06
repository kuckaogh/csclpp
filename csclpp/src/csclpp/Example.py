import sys
import dts.Parser as P
from dts.Study import Study
from dts.Var import Var
import dts.Setting as S
import dts.Temp as T
import dts.Workflow as W


studyMap = W.setupReference('./example_data/sample.setting')

for k in studyMap:
    print k, studyMap[k].data_src





# 
# print T.varGroupMap
# 
# print T.varGroupMap['base']['s_trinity'].metaData
# 
# m= T.varGroupMap['base']['s_trinity'].metaData
# 
# print m.keys()
# 
# m= S.studyMap['calsim2Name2'].varMap['delta_inflow'].expr
# 
# print m
# 
# for s in S.fileVarGroupMap:
#     print s
# 
# m= S.fileVarGroupMap['calsim2']['xyz']['delta_inflow'].expr
# 
# print m