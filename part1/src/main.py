import os.path
import sys

from solvers import *

if __name__ == '__main__':
	if len(sys.argv) <= 2:
		print("Usage: python main.py <algorithm> <graph_filename> <tabVerif>")
		exit(1)
	algorithm = sys.argv[1]
	filename = sys.argv[2]
	if os.path.exists(filename) is False:
		print("File not found.")
		exit(1)
	solv = None
	if algorithm == "backtracking":
		solv = solvBackTracking
	elif algorithm == "random":
		solv = solvRandom
	elif algorithm == "lawler":
		solv = solvLawler
	elif algorithm == "verif":
		colorList = eval(sys.argv[3])
		print(colorList)
		print(verificateur(reader(filename), colorList))
		exit(0)
	else:
		print("Algorithm not found.")
		exit(1)
	res = solv(filename)
	print(res)
