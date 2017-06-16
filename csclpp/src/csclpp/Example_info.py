from dts.Study import Study
from dts.Var import Var
import dts.Setting as S
import dts.Workflow as W
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *
import collections

studyMap = W.readReference('./example_data/easy.setting')


# take a look at the var maps

for k, sv in studyMap.iteritems():
    
    print '\nstudyName:', k, ' vardef:', sv.varDef
    for d in studyMap[k].data_src:
        print 'dss data src:', d
        
    print ''
    for p, v in studyMap[k].varPathMap.iteritems():
        print '  var:  '+p+'= '+v.path
        if v.metaData: 
            print v.metaData   #print units, capacity
        if v.metaDataPost:
            print v.metaDataPost
    
    print ''
    for p, v in studyMap[k].varExprMap.iteritems():
        print '  dts:  '+p+'= '+v.expr
        if v.metaData: 
            print v.metaData   #print units, capacity
        if v.metaDataPost:
            print v.metaDataPost
#     for p in studyMap[k].ifsMap:
#         print '  if statement id:  '+str(p)
#         print studyMap[k].ifsMap[p] 
    
    print ''
    print '  temp vars:', studyMap[k].tempVarList

    print ''
    for p, v in studyMap[k].newArrayMap.iteritems():
        print '  new array:  '+p
        if v.metaData: 
            print v.metaData   #print units, capacity
        if v.metaDataPost:
            print v.metaDataPost

    print ''
    for p, v in studyMap[k].newConstMap.iteritems():
        print '  new const:  '+p+'= ', v.const
        if v.metaData: 
            print v.metaData   #print units, capacity
        if v.metaDataPost:
            print v.metaDataPost
