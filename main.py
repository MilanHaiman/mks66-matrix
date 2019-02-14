from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

# TESTING
matrix = new_matrix()
ident(matrix)

print("\ntesting matrix stuff:\n")
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
matrix_mult(A,B)
print_matrix(A)
print_matrix(B)
matrix_mult(B,A)  
print_matrix(A)
print_matrix(B)
matrix_mult(matrix,A)
print_matrix(A)

# MORE TESTING

matrix = new_matrix(4,0)

add_edge(matrix, 1, 100, 0, 100, 200, 1)
add_edge(matrix, 1, 200, 0, 10, 200, 1)
add_edge(matrix, 1, 300, 0, 100, 200, 1)
add_edge(matrix, 400, 100, 0, 200, 200, 1)

print("testing adding edges:\n")
print_matrix(matrix)
draw_lines( matrix, screen, color )
display(screen)
# save_extension(screen, 'img.png')

