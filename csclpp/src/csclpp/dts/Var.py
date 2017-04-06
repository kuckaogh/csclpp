import sys


class Var:

	isTemp = False;   # True if @ before name
	path = ''
	expr = ''
	#ts = []       # timeseries
	metaData = {}	

	def __init__(self, path):
		self.isTemp=False
		self.path = path
		self.expr=''
		self.metaData={}

