import sys
import dts.Parser as P
from dts.Study import Study
from dts.Var import Var
import dts.Setting as S
import dts.Workflow as W
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *


studyMap = W.readReference('./example_data/if_statement.setting')


# take a look at the var maps

for k in studyMap:
    print 'studyName:', k
    for d in studyMap[k].data_src:
        print 'dss data src:', d
    for p in studyMap[k].varPathMap:
        print '  var:  '+p+'= '+studyMap[k].varPathMap[p].path
    for p in studyMap[k].varExprMap:
        print '  dts:  '+p+'= '+studyMap[k].varExprMap[p].expr  
    for p in studyMap[k].newArrayList:
        print '  new arrays: '+p
    print '  temp vars:', studyMap[k].tempVarList,'\n'
    
    for p in studyMap[k].ifsMap:
        ifs = studyMap[k].ifsMap[p]
        print 'if statement ID: '+ str(p)
        for condition in ifs:
            print ' ', condition,':',ifs[condition]

