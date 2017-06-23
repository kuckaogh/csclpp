import sys
import numpy as np


class Var:

	isTemp=False
	path = ''
	expr = ''
	const = None
	metaData = {}; 
	metaDataPost = []


	def __init__(self, path):
		self.isTemp=False
		self.path = path
		self.expr=''
		self.const = None
		self.metaData={}
		self.metaData['_dataType']=np.float # str, int, datetime
		self.metaDataPost =[]


