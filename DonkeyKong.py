"""DonkeyKong Game"""

from random import *
import os
import time
from person import *
from fireball import *
from screen import * 

def getchar():
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch







"""Main Function"""
def main():
	screen=Screen()
	flag=0
	i=0
	j=0
	pm=player(28,1)
	fb=[fireball(4,2)]
	screen.printfb(4,2,'O',fb[0],0)
	screen.printpm(28,1,'P',pm)
	d=Ghost(4,1)
	screen.printg(4,1,'D',d)
	os.system("clear")
	screen.genCoins()
	screen.printScreen()
	count=0
	while(1):
		if(count%20==0 and count!=0):
			fb=fb+[fireball(d.getX(),d.getY())]
			
		print "Enter your  Move  :",
		ch=getchar()
		if(ch==' '):
			
			ch1=getchar()
			i=1
			for i in range(5):
				
				pm.jump(ch1,screen,pm,i)
				os.system("clear")
				screen.printScreen()
				
				time.sleep(0.1)
				i+=1
			i=0
		if(ch=='q'):
			break
		pm.move(ch,screen,pm)
		i=0
		
		rand1=randint(3,4)
		prevX=d.getX()
		prevY=d.getY()
		d.move(rand1,screen,d)
		nextX=d.getX()
		nextY=d.getY()
		while(prevX==nextX and prevY==nextY):
			rand1=randint(3,4)
			d.move(rand1,screen,d)
			nextX=d.getX()
			nextY=d.getY()
		for i in range(len(fb)):
			
			rand2=randint(2,3)
			fb[i].move(screen,fb[i],rand2,i)
			i+=1
		print ""
		os.system("clear")
		screen.printScreen()
		print "Score :",
		print screen.getScore()
		check1=screen.checkGhost(pm,d,ch,rand1)
		i=0
		for i in range(len(fb)):
			
			check2=screen.checkCollision(pm,fb[i],ch,i)
			
			i+=1
			if(check2=='q'):
				break
		if(check1=='q' or check2=='q'):
			break
		elif( pm.getX()==1 and pm.getY()==31):
			flag=1
			break
		else:
			flag=0
		count+=1
	print ""
	print "Game Over!!! Your Final Score is:",
	if(flag==0):
		print screen.getScore()
	else:
		print screen.getScore()+50
if __name__ == "__main__":
	main()
