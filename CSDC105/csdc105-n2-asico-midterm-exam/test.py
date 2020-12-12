#Author				:	Patricia P. Asico
#Course and Year	:	1-BSIT
#Filename			:	emmet.py
#Description		: 	prints the final output
#Honor Code			:	I have not given nor received any unauthorized help in
#						completing this exercise. I am also well aware of the
#						policies stipulated in the Adnu student handbook.
from emmet import Emmet, Valid
while:
	w =input()
	if w == "quit" or w == "exit":	#to terminate and exit the program
		exit()

	check = Valid(w)

	if check == True:			#prints the final output
		E = Emmet(w)
		print(E)
	
	else:
		print("Error: Unrecognized abbreviation\n")		#prints an error message if it returned false
	
