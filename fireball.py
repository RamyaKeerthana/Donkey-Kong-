from random import *
import os
#fireball class
class fireball:
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self.__flag=[0,0]
		self.state=[0,0]
	def move(self,sc,fb,rand,i):
		if(sc.checkend(self.__x,self.__y)):
			sc.printfb(self.__x,self.__y,' ',fb,i)
		elif(sc.endofstairs(self.__x+1,self.__y) and sc.checkstairs(self.__x+1,self.__y)):
			if(rand==2):
				sc.printfb(self.__x,self.__y,' ',fb,i)
				self.__x+=1
				sc.printfb(self.__x,self.__y,'O',fb,i)
				self.state=[1,i]
			else:
				if(self.__x==4 or self.__x==12 or self.__x==20):
					sc.printfb(self.__x,self.__y,' ',fb,i)
					self.__y+=1
					sc.printfb(self.__x,self.__y,'O',fb,i)
					self.state=[2,i]
				else:
					sc.printfb(self.__x,self.__y,' ',fb,i)
					self.__y-=1
					sc.printfb(self.__x,self.__y,'O',fb,i)
					self.state=[3,i]				
		elif(sc.checkbasex(self.__x,self.__y)):
			if(self.__x==4 or self.__x==12 or self.__x==20):
					sc.printfb(self.__x,self.__y,' ',fb,i)
					self.__y+=1
					sc.printfb(self.__x,self.__y,'O',fb,i)
					self.state=[2,i]
			else:
				sc.printfb(self.__x,self.__y,' ',fb,i)
				self.__y-=1
				sc.printfb(self.__x,self.__y,'O',fb,i)
				self.state=[3,i]
		
		else:
			sc.printfb(self.__x,self.__y,' ',fb,i)
			self.__x+=1
			sc.printfb(self.__x,self.__y,'O',fb,i)
			self.state=[1,i]
	def getposition():
		return (self.__x,self.__y)
	
	def getX(self):
		return self.__x

	def getY(self):
		return self.__y	
	def getflag(self):
		return self.__flag
	
	def setflag(self,a,l):
		self.__flag=[a,l]			
				
		
