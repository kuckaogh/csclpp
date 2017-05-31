import sys


class Var:

	path = ''
	expr = ''
	expr_mod = ''
	metaData = {}	

	def __init__(self, path):
		self.isTemp=False
		self.path = path
		self.expr=''
		self.expr_mod=''
		self.metaData={}

