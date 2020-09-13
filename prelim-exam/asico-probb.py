 # Author          : {Your complete came}
 # Course and Year : {Your course and year}
 # Filename        : {The name of your source file}
 # Description     : {A brief description of what this program does}
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
	first=0
	second = 1
	third = 0
	temp = 0
	T = T - 1
	i = i + 1
print(string_fibo)

