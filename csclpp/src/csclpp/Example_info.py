import sys
import dts.Parser as P
from dts.Study import Study
from dts.Var import Var
import dts.Setting as S
import dts.Workflow as W
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *


studyMap = W.readReference('./example_data/sample.setting')


# take a look at the var maps

for k in studyMap:
    print 'studyName:', k
    for d in studyMap[k].data_src:
        print 'dss data src:', d
        
    for p in studyMap[k].varPathMap:
        v=studyMap[k].varPathMap[p]
        print '  var:  '+p+'= '+v.path
        if v.metaData: print v.metaData   #print units, capacity
        
    for p in studyMap[k].varExprMap:
        v=studyMap[k].varExprMap[p]
        print '  dts:  '+p+'= '+v.expr
        if v.metaData: print v.metaData   #print units, capacity
#     for p in studyMap[k].ifsMap:
#         print '  if statement id:  '+str(p)
#         print studyMap[k].ifsMap[p] 
    print '  temp vars:', studyMap[k].tempVarList
    print '  new vars:', studyMap[k].newArrayList

