import sys


class Var:

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
		self.metaDataPost =[]

