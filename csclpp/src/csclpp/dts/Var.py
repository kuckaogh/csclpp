import sys
import numpy as np


class Var:

	isTemp=False
	path = ''
	const = None
	metaData = {}; 
	metaDataPost = []


	def __init__(self, path):
		self.isTemp=False
		self.path = path
		self.const = None
		self.metaData={}
		self.metaDataPost =[]


