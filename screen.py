from random import *
import os

#creates game board
class Screen:
	"""Screen Class to create Board and Board Functions"""
	def __init__(self):
		self.__score=0
		self._a=[['X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X',	' ',	' ',	' ',	' ',	' ',	' ',	'Q',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'H',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'H',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	' ',	'X'],
['X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X',	'X']]
		
#Prints the Game Board after every Move	
	def printScreen(self):
		for i in range(0,30):
 			for j in range(0,80):
				if(self._a[i][j]=='D'):
					print ('\033[1m'+'\033[91m' + 'D' + '\033[0m'),
				elif(self._a[i][j]=='P'):
					print ('\033[1m'+'\033[94m' + 'P' + '\033[0m'),
				elif(self._a[i][j]=='X'):
					print ('\033[1m'+'\033[92m' + 'X' + '\033[0m'),
				elif(self._a[i][j]=='O'):
					print ('\033[1m'+'\033[95m' + 'O' + '\033[0m'),
				elif(self._a[i][j]=='H'):
					print ('\033[1m'+'\033[95m' + 'H' + '\033[0m'),
				elif(self._a[i][j]=='C'):
					print ('\033[1m'+'\033[93m' + 'C' + '\033[0m'),
				elif(self._a[i][j]=='Q'):
					print ('\033[1m'+'\033[96m' + 'Q' + '\033[0m'),
				else:	
					print self._a[i][j],
			print ""

#prints player in correct position after every move
	def printpm(self,x,y,ch,pm):
		if(self._a[x][y]=='C'):
			self.collectCoin(x,y)
			self._a[x][y]=ch
		elif(ch!=' '):
			if(self._a[x][y]=='H'):
				pm.setflag(1)
			self._a[x][y]=ch
			
		else:
			if(pm.getflag()==1 ):
				self._a[x][y]='H'
				pm.setflag(0)
			else:
				self._a[x][y]=ch
				pm.setflag(0)	

#prints donkey in correct position after every move
	def printg(self,x,y,ch,g):
		if(ch==' '):
			if(g.getFlag()==1):
				self._a[x][y]='C'
			elif(g.getFlag()==2):
				self._a[x][y]='H'
			else:
				self._a[x][y]=ch
			g.setFlag(0)
		else:
			if(self._a[x][y]=='H'):
				g.setFlag(2)
			elif(self._a[x][y]=='C'):
				g.setFlag(1)
			self._a[x][y]=ch

#prints fireball in correct position after every move

	def printfb(self,x,y,ch,fb,i):
		if(ch==' '):
			if(fb.getflag()==[1,i]):
				if(self._a[x][y]!='D'):
					self._a[x][y]='C'
			elif(fb.getflag()==[2,i]):
				if(self._a[x][y]!='D'):
					self._a[x][y]='H'
			elif(fb.getflag()==[3,i]):
				pass
			else:
				self._a[x][y]=ch
			fb.setflag(0,i)
		else:
			if(self._a[x][y]=='C'):
				fb.setflag(1,i)
			elif(self._a[x][y]=='H'):
				fb.setflag(2,i)
			elif(self._a[x][y]=='O'):
				fb.setflag(3,i)
			
			self._a[x][y]=ch

	

#checks if the fireball reached the initial position of the player

	def checkend(self,x,y):
		if((x,y)==(28,1)):
			return True
		else:
			return False
		
	

#Increments Score everytime Player gets a Coin	
	def collectCoin(self,x,y):
		self.__score+=5

#checks if there are stairs in that position

	def checkstairs(self,x,y):
		if(self._a[x][y]=='H'):
			return True
		else:
			return False
#checks if the position below is the end of the stairs

	def endofstairs(self,x,y):
		if(self._a[x][y-1]=='X' or self._a[x][y+1]=='X'):
			return True
		else:
			return False	

#checks if there is a wall
	def checkWall(self,x,y):
		if(self._a[x][y]=='X'):
			return False
		else:
			return True

#checks if there is any base (ladder or wall)

	def checkbase(self,x,y):
		if(self._a[x+1][y]=='X' or self._a[x+1][y]=='H'):
			return True
		else:
			return False
#checks if there is any base wall

	def checkbasex(self,x,y):
		if(self._a[x+1][y]=='X'):
			return True
		else:
			return False

#Generate Coins randomly on the board 

	def genCoins(self):
		count=20
		i=0
		j=0
		while(count!=0):
			i=randint(0,29)
			j=randint(0,79)
			if(self._a[i][j]==' '):
				if(self._a[i+1][j]=='X'):	
					self._a[i][j]='C'
					count-=1
#Get Score
	def getScore(self):
		return (self.__score)
	
		
#checks the collision of fireball with the player		
	
	def checkCollision(self,p,fb,ch,i):
		if(p.getX()==fb.getX() and p.getY()==fb.getY()):
			os.system("clear")
			self.printScreen()
			print "Score : ",
			print self.getScore()
			return 'q'

		elif(p.getX()==fb.getX()):
			if((p.getY()-1)==fb.getY() and (ch=='d'or ch=='D') and fb.state==[3,i]):
				os.system("clear")
				self.printpm(p.getX(),p.getY(),' ',p)
				self.printScreen()
				print "Score : ",

				print self.getScore()

				return 'q'

			elif((p.getY()+1)==fb.getY() and (ch=='a'or ch=='A') and fb.state==[2,i]):

				os.system("clear")

				self.printpm(p.getX(),p.getY(),' ',p)

				self.printScreen()
				print "Score : ",
				print self.getScore()
				return 'q'
			else:
				return 'a'
		elif(p.getY()==fb.getY()):
			if((p.getX()-1)==fb.getX() and (ch=='s'or ch=='S') and fb.state==[1,i]):
				os.system("clear")
				self.printpm(p.getX(),p.getY(),' ',p)
				self.printScreen()
				print "Score : ",

				print self.getScore()

				return 'q'

			
			else:
				return 'a'
		else:

			return 'a'


#Checks if the Ghost catches the Player
	def checkGhost(self,p,g,ch,rand):
		if(p.getX()==g.getX() and p.getY()==g.getY()):
			os.system("clear")
			self.printScreen()
			print "Score : ",
			print self.getScore()
			return 'q'
		elif(p.getX()==g.getX()):
			if((p.getY()-1)==g.getY() and (ch=='d'or ch=='D') and rand==3):
				os.system("clear")
				self.printpm(p.getX(),p.getY(),' ',p)
				self.printScreen()
				print "Score : ",
				print self.getScore()
				return 'q'
			elif((p.getY()+1)==g.getY() and (ch=='a'or ch=='A') and rand==4):
				os.system("clear")
				self.printpm(p.getX(),p.getY(),' ',p)
				self.printScreen()
				print "Score : ",
				print self.getScore()
				return 'q'
			else:
				return 'a'
		
		else:
			return 'a'


