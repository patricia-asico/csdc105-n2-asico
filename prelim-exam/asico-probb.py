 # Author          : Patricia P. Asico
 # Course and Year : BSIT -1 
 # Filename        : asico-probb.py
 # Description     : Write a program that reads an integer and prints the sequence of Fibonacci numbers
 #                   as a comma-separated list on a single line.
 # Honor Code      : I have not given nor received any unathorized help in
 #                   completing this exercise. I am also well aware of the 
 #                   policies stipulated in the AdNU student handbook.




# PROGRAM B: FIBONACCI
T = int(input("Enter number of test cases: "))  #prompt user to enter number of test cases
first=0                                         
second = 1
third = 0
i=1
string_fibo = ""

while T>0:                                      #loop for entering the values
	n=int(input("n: "))
	string_fibo += ("CASE ") + str(i) + (": ")    #prints CASE (i): 
	while third < n+1:                            
			string_fibo += str(first) + " "           #stores the number in string
			temp = first + second                     #formula for fibonacci
			first = second
			second = temp
			third += 1
	string_fibo += "\n"	
	first=0							#resets fibo
	second = 1
	third = 0
	temp = 0
	T = T - 1						#for T
	i = i + 1						#for case number
print(string_fibo)						#prints the fibonacci for each case						

