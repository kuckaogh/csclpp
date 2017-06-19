from dts.Study import Study
from dts.Var import Var
import dts.Setting as S
import dts.Workflow as W
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *
import collections

d='./example_data/callite2.dss'
path =  '//S_OROVL/STORAGE//1MON//'
print path
c = dss_catalog(d) 
for e in c:
    print e
ts = dss_retrieve_ts(d,selector=path,unique=True) 



d='./example_data/callite1.dss'
path =  '//S_Folsm/STORAGE//1MON//'
print path
ts = dss_retrieve_ts(d,selector=path,unique=True) 
c = dss_catalog(d) 
# for e in c:
#     print e

print ts.times
print ts.props
print ts.props['unit']
print ts.start, ts.end
print ts.start.strftime('%Y%m')

d2='./example_data/callite2.dss'
path2 =  '//S_orovl/STORAGE//1MON//'
print path2
ts2 = dss_retrieve_ts(d2,selector=path2,unique=True) 

print ts2.times
print ts2.props
print ts2.start, ts2.end
print ts2.start.strftime('%Y%m')

print ts.data
print ts2.data
print ts.data+ts2.data