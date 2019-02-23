# Prog. Name: prog_py
# Author: Ryan Ellis
# Class: CS344 - Operating Systems
# Description: Script that executes the following 1) creates 3 files
# 2) loads 10 random, lowercase characters into each file 3) prints
# the contents of those 3 files to stdout 4) generates 2 random integers
# and prints those integers to stdout 5) procduct of those integers
# to stdout.

from random import seed, randint
import sys

CHARMIN = 97
CHARMAX = 122
NUMMIN = 1
NUMMAX = 42

def main():

	# Name of files
	fileList = ["myfile1", "myfile2", "myfile3"]

	# Initialize random number generator
	seed()

	# Create files and print rand ints
	for fileName in fileList:
		
		with open(fileName, 'w') as file:
			for i in range(0, 10):
				randNum = randint(CHARMIN, CHARMAX)
				print(chr(randNum), end='', file=file)
				sys.stdout.write(chr(randNum));
			print(file=file)
			sys.stdout.write('\n')
			sys.stdout.flush()

	# Two random ints and their product
	rand1 = randint(NUMMIN, NUMMAX)
	rand2 = randint(NUMMIN, NUMMAX)
	randProd = rand1 * rand2

	print(rand1)
	print(rand2)
	print(randProd)

	return 0

if __name__ == "__main__":
	main()
