import sys


class Var:

	path = ''
	expr = ''
	metaData = {}	

	def __init__(self, path):
		self.isTemp=False
		self.path = path
		self.expr=''
		self.metaData={}

