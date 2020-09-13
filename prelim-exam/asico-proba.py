# Author : Patricia P. Asico
# Course and Year : BSIT-1
# Filename : asico-proba.py
# Description : Write a program that prints a triangle
#               shape composed of specific ASCII character.
# Honor Code : I have not given nor received any unathorized help in
#              completing this exercise. I am also well aware of the
#              policies stipulated in the AdNU student handbook.

#PROBLEM A: TRIANGLES
T = int(input("Enter number of test cases: "))              #asks user for input for no of test cases
string_tri = ""
n = 1

while T > 0:                                                #loop that enables to input height and character based on T
	k, c = input().split()                                    #user inputs the height(k) and character(c)
	k = int(k)
	string_tri = string_tri + ("CASE ") + str(n) + (":\n") 
	for i in range(0,k):                                      #loop for height
		for j in range(0,k-i):                                  #loop for the spaces before characters
			string_tri = string_tri + (" ")       
		for j in range(0,2*i+1):                                #loop for the character
			string_tri = string_tri + (c)
		string_tri = string_tri + ("\n")
	n = n + 1                                                 #for case number
	T = T - 1                                                 #for test cases
print()
print(string_tri)                                           #outputs the triangle for each case
