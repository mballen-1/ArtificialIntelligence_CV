import numpy as np

mat = np.array([np.array([' ',' ',' ']),np.array([' ',' ',' ']),np.array([' ',' ',' '])])

lineas = [[0,0, 0,1, 0,2],
		  [1,0, 1,1, 1,2],
		  [2,0, 2,1, 2,2],
		  [0,0, 1,0, 2,0],
		  [0,1, 1,1, 2,1],
		  [0,2, 1,2, 2,2],
		  [0,0, 1,1, 2,2], 
		  [2,0, 1,1, 0,2]]


def utility(copy_board):

	sum = 0
	for l in lineas:		
		for val in xrange(2):
			x = l[2*val]
			y =  l[2*val+1]

			if(copy_board[x][y] == 'X'):
				sum-=1
			elif(copy_board[x][y] == 'O'):
				sum+=1
	return sum

def human():
	
	cas = input("Ingrese el numero de la casilla que desea jugar... \n ")	

	if (cas>9 or cas<1):
		print "Casilla debe estar entre uno y nueve"
		main()
	else:
		cas -= 1
		x = cas/3
		y = cas%3

		mat[x][y] = 'X'

def agent():

	options = []

	for x in xrange(3):
		for y in xrange(3):
			if (mat[x][y] == 0):
				options.append([x,y])

	
	best_coord = [-1,-1]
	max_utility = -10000

	for opt in options:
		
		copy_board = np.copy(mat)
		
		x = opt[0]
		y = opt[1]

		copy_board[x][y] = 'O'
		util = utility(copy_board)
		
		if(util > max_utility):
			max_utility  = util
			best_coord = [x, y]


	mat[best_coord[0]][best_coord[1]] = 'O'



def main():

	finished = False
	print mat
	human()
	
	for play in xrange(7):
		agent()
		print "Agent played... \n \n", mat
		human()	
		print "Human played... \n \n", mat

main() #:v


	



