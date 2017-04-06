import sys


class Var:

	isTemp = False;   # True if @ before name
	path = ''
	expr = ''
	ts = []       # timeseries
	metaData = {}	

	def __init__(self, path):
		self.path = path

