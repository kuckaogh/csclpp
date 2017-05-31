import sys
import dts.Parser as P
from dts.Study import Study
from dts.Var import Var
import dts.Setting as S
import dts.Workflow as W
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *

d='./example_data/callite1.dss'
path =  '//S_Folsm/STORAGE//1MON//'
print path
ts = dss_retrieve_ts(d,selector=path,unique=True) 

print ts

