# Author : {Patricia P. Asico}
# Course and Year : {1-BSIT}
# Filename : {asico_e4.py}
# Description : {Reads 3 comma separated numbers, checks the lengths if it is valid and then computes
#                for the perimeter and area using the function in geometry.py and displays the results.
#                If the lengths given by the user is invalid, the program issues an error.}
# Honor Code : I have not given nor received any unathorized help in
#              completing this exercise. I am also well aware of the
#              policies stipulated in the AdNU student handbook.

from geometry import perimeter, triange_heronsarea

def check ():
  if float(a + b) <= float(c):
    return True
   else
    return False
    
print("Enter sides of the triangle:")    
a = input("a: ")
b = input("b: ")
c = input("c: ")

if check():
  P = perimeter(side_length)
  A = triangle_heronsarea(a,b,c)
  print("Perimeter: ", P)
  print("Area: ", A)
else:
  print("Error: Invalid input")
