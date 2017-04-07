import sys
import dts.Parser as P
from dts.Study import Study
from dts.Var import Var
import dts.Setting as S
import dts.Temp as T
import dts.Workflow as W
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *


studyMap = W.setupReference('./example_data/sample.setting')


# take a look at the var maps

for k in studyMap:
    print 'studyName:', k
    for d in studyMap[k].data_src:
        print 'dss data src:', d
    for p in studyMap[k].varPathMap:
        print '  var:  '+p+'= '+studyMap[k].varPathMap[p].path
    for p in studyMap[k].varExprMap:
        print '  dts:  '+p+'= '+studyMap[k].varExprMap[p].expr



# read timeseries data  into Var() holder
for k in studyMap:
    for d in studyMap[k].data_src:
        print 'open data src:', d
        #file = "hist19902014_droughtstudy.dss"
                     
        for p in studyMap[k].varPathMap:
            path =  studyMap[k].varPathMap[p].path
            #print path
            try:
                ts = dss_retrieve_ts(d,selector=path,unique=True) 
                print 'found  var:  '+p+'= '+studyMap[k].varPathMap[p].path
            except:
                print 'mssing! '+studyMap[k].varPathMap[p].path
                #print 'Missing  var:  '+p+'= '+studyMap[k].varPathMap[p].path
 


# 
# for s in S.fileVarGroupMap:
#     print s
# 
# m= S.fileVarGroupMap['calsim2']['xyz']['delta_inflow'].expr
# 
# print m