from random import *
import os

#person class

class Person:
	
    

	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y

	def move(self,ch,sc):
	        raise NotImplementedError("Subclass must implement abstract method")

"""Player Class"""

class player(Person):
	
    
	def __init__(self,x,y):	
		self.__x=x
		self.__y=y
		self.__flag=0

	def move(self,ch,sc,pm):
		if(ch=='w' or ch=='W'):
			if(sc.checkstairs(self.__x-1,self.__y)):
				sc.printpm(self.__x,self.__y,'H',pm)
				self.__x-=1
				sc.printpm(self.__x,self.__y,'P',pm)
			elif(sc.endofstairs(self.__x,self.__y)):
				sc.printpm(self.__x,self.__y,' ',pm)
				self.__x-=1
				sc.printpm(self.__x,self.__y,'P',pm)
		elif(ch=='s' or ch=='S'):
			if(sc.checkstairs(self.__x+1,self.__y)):
				sc.printpm(self.__x,self.__y,' ',pm)
				self.__x+=1
				sc.printpm(self.__x,self.__y,'P',pm)
		elif(ch=='a' or ch=='A'):
			if(sc.checkstairs(self.__x,self.__y-1)):
				sc.printpm(self.__x,self.__y,' ',pm)
				self.__y-=1
				sc.printpm(self.__x,self.__y,'P',pm)
			elif(sc.checkWall(self.__x,self.__y-1) and sc.checkbase(self.__x,self.__y-1)):
				sc.printpm(self.__x,self.__y,' ',pm)
				self.__y-=1
				sc.printpm(self.__x,self.__y,'P',pm)
			
		elif(ch=='d' or ch=='D'):
			if(sc.checkstairs(self.__x,self.__y+1)):
				sc.printpm(self.__x,self.__y,' ',pm)
				self.__y+=1
				sc.printpm(self.__x,self.__y,'P',pm)
			elif(sc.checkWall(self.__x,self.__y+1) and sc.checkbase(self.__x,self.__y+1)):
				sc.printpm(self.__x,self.__y,' ',pm)
				self.__y+=1
				sc.printpm(self.__x,self.__y,'P',pm)
	def jump(self,ch,sc,pm,n):
		if(ch=='d' or ch=='D'):
			if(n==1 or n==2):
				sc.printpm(self.__x,self.__y,' ',pm)
				self.__y+=1
				self.__x-=1	
				sc.printpm(self.__x,self.__y,'P',pm)
			
			elif(n==3 or n==4):
				sc.printpm(self.__x,self.__y,' ',pm)
				self.__y+=1
				self.__x+=1	
				sc.printpm(self.__x,self.__y,'P',pm)
		elif(ch=='a' or ch=='A'):
			if(n==1 or n==2):
				sc.printpm(self.__x,self.__y,' ',pm)
				self.__y-=1
				self.__x-=1	
				sc.printpm(self.__x,self.__y,'P',pm)
	
			elif(n==3 or n==4):
				sc.printpm(self.__x,self.__y,' ',pm)
				self.__y-=1
				self.__x+=1	
				sc.printpm(self.__x,self.__y,'P',pm)
	def getX(self):
		return self.__x
	def getY(self):
		return self.__y		
	def getposition(self):
		return (self.__x,self.__y)

	def getflag(self):
		return self.__flag

	def setflag(self,a):
		self.__flag=a

#donkey class
class Ghost(Person):
	
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self.__flag=0

	def move(self,rand,sc,g):
		if(rand==3):
			if(sc.checkWall(self.__x,self.__y-1) ):
				sc.printg(self.__x,self.__y,' ',g)
				self.__y-=1
		elif(rand==4):
			if(sc.checkWall(self.__x,self.__y+1) ):
				sc.printg(self.__x,self.__y,' ',g)
				self.__y+=1

		sc.printg(self.__x,self.__y,'D',g)
	def getX(self):
		return self.__x
	def getY(self):
		return self.__y	

	def getposition(self):
		return (self.__x,self.__y)
	
	def getFlag(self):
		return self.__flag
	
	def setFlag(self,a):
		self.__flag=a
