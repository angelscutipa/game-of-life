# -*- coding: utf-8 -*-
#By: izanbf1803
#
import os, sys
import random
import time
import threading
from threading import Thread



#---PARAMETERS---#
_sleepTime = 0.5
_clsCMD = "cls"   #If you are in linux change it by "clear"
_Probability_of_no_spawn = 7  #5-10
#----------------#



stopAll = False

def finish():
	global stopAll
	stopAll = True
	sys.exit(0)

def random_range(min, max):
	return round(random.random() * (max - min) + min);

y = 20
x = int(y*2)
matrix = []

for i in range(y):
    matrix.append([0]*x)
    for j in range(x):
    	_temp = random_range(0,_Probability_of_no_spawn)
    	if _temp == 1: matrix[i][j] = 1
    	else: matrix[i][j] = 0

def iterate():
	global stopAll
	while not stopAll:
		time.sleep(_sleepTime)
		_matrix = matrix
		for i,_ in enumerate(matrix):
			for j,_ in enumerate(matrix[i]):
				analyze(i, j, _matrix)

def analyze(x, y, _matrix):
	n = 0
	to_iterate = [
		(x-1,y+1),
		(x,y+1),
		(x+1,y+1),
		(x-1,y),
		(x+1,y),
		(x-1,y-1),
		(x,y-1),
		(x+1,y-1),
	]
	for i,_ in enumerate(to_iterate):
		_x, _y = to_iterate[i]
		try:
			_val = _matrix[_x][_y]
			if _val == 0: n += 1
		except: pass
	if n < 2: _matrix[x][y] = 1
	elif n > 3: _matrix[x][y] = 1
	elif n == 3: _matrix[x][y] = 0
	matrix = _matrix


def draw():
	global stopAll
	while not stopAll:
		lines = "\n\t"
		for i,_ in enumerate(matrix):
			for j,_ in enumerate(matrix[i]):
				if matrix[i][j] == 1:
					lines += " "
				else:
					lines += "·"
			lines += "\n\t"
		os.system(_clsCMD)
		print (lines)
		time.sleep(_sleepTime)

def main():
	t = Thread(target=draw)
	t2 = Thread(target=iterate)
	t.start()
	t2.start()


main()
input()
finish()