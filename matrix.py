"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
	for row in matrix:
		print_row(row)
	print( "")


def print_row( row ):
	toprint = ""
	for el in row:
		toprint += str(el) + "\t"
	print(toprint)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			matrix[i][j] = 0
		matrix[i][i] = 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for col_index in range(len(m2[0])):
    	column = [m2[i][col_index] for i in range(len(m2))]
    	for i in range(len(m2)):
    		m2[i][col_index]=dot(m1[i],column)

def dot( v1, v2):
	tot = 0
	for i in range(len(v1)):
		tot+=v1[i]*v2[i]
	return tot


def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m
