# Author          : Patricia P. Asico
# Course and Year : BSIT-1
# Filename        : csdc105-n2-asico/exercise3/asico_e3.py
# Description     : In this exercise you will have to demonstrate your knowledge in writing a complete Python program which can read inputs 
#                   from the command line and uses conditionals or branching statements.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

import sys

if len(sys.argv) <= 1 or len(sys.argv) == 2 or len(sys.argv) > 3:
	print("Usage: ", sys.argv[0], "<activity or sector> <quarantine classification>")
	exit(1)
	
if (sys.argv[1] == "people"):
	if (sys.argv[2] == "ecq"):
		print("100% stay at home; Exception for workers in offices or industries permitted to operate")
	elif (sys.argv[2] == "mecq"):
		print("100% stay at home; Restricted movement, only for accessing essential goods and services; Exception for workers in offices or industries permitted to operate; Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home")
	elif (sys.argv[2] == "gcq"):
		print("Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home")
	elif (sys.argv[2] == "mgcq"):
		print("Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contractingthe COVID-19 disease are required to stay home")
	else:
		print("Error: Invalid input")
		
elif (sys.argv[1] == "transport"):
	if (sys.argv[2] == "ecq"):
		print("No domestic flights, with limited international flights; Public transportation is not allowed; Shuttle services for employees of permitted offices or establishments, as well as point-to-point transport service, granted permission to operate by the government, with healthcare workers and other frontliners given priority")
	elif (sys.argv[2] == "mecq"):
		print("No domestic flights, with limited international flights; Controlled inbound flights; No inter-island travel; Public transportation is not allowed; Private transportation such as company shuttles and personal vehicles allowed subject to the guidelines provided by the Department of Transportation (DOTr); Biking and non-motorized transport encouraged")
	elif (sys.argv[2] == "gcq"):
		print("Public transport is allowed with strict social distancing; Inter-island travel from GCQ to GCQ allowed with safety protocols.")
	elif (sys.argv[2]== "mgcq"):
		print("Public transport is allowed with strict social distancing Inter-island travel from GCQ to GCQ allowed with safety protocols.")
	else:
		print("Error: Invalid input")
		
elif (sys.argv[1] == "gatherings"):
	if (sys.argv[2] == "ecq"):
		print("Mass gatherings are not allowed; Only mass gatherings that are essential for the provision of government services or authorized humanitarian activities permitted")
	elif (sys.argv[2] == "mecq"):
		print("Highly restricted (maximum of 5); Non-essential work gatherings are prohibited.")
	elif (sys.argv[2] == "gcq"):
		print("Gatherings are limited to not more than ten (10) persons; Non-essential work gatherings are prohibited")
	elif (sys.argv[2] == "mgcq"):
		print("Fifty percent (50%) of the seating or venue capacity for movie screenings, concerts, sporting events, and other entertainment activities, religious services, and work conferences.")
	else:
		print("Error: Invalid input")
		
elif (sys.argv[1] == "schools"):
	if (sys.argv[2] == "ecq"):
		print("School premises are closed.")
	elif (sys.argv[2] == "mecq"):
		print("School premises are closed.")
	elif (sys.argv[2] == "gcq"):
		print("Skeletal workforce permitted in schools; Face-to-face or in-person classes are suspended.")
	elif (sys.argv[2] == "mgcq"):
		print("Limited face-to-face or in-person classes may be conducted; strict compliance with minimum public health standards and consultations with local government units (LGUs) and guidelines set by the Commission on Higher Education (CHED)")
	else:
		print("Error: Invalid input")
		
elif (sys.argv[1] == "work"):
	if (sys.argv[2] == "ecq"):
		print("Select industry workers permitted")
	elif (sys.argv[2] == "mecq"):
		print("Essential industries permitted to work at full capacity, with others operating at a fifty percent (50%) capacity; Work-from-home and other flexible work arrangements encouraged")
	elif (sys.argv[2] == "gcq"):
		print("Alternative work arrangements")
	elif (sys.argv[2] == "mgcq"):
		print("Full operating capacity for work in all public and private offices; Alternative work arrangements for persons who are sixty (60) years old and above, or those with other health risks")
	else:
		print("Error: Invalid input")
		
elif (sys.argv[1] == "government"):
	if (sys.argv[2] == "ecq"):
		print("Skeletal workforce onsite;Work from home arrangements")
	elif (sys.argv[2] == "mecq"):
		print("Skeletal workforce onsite; Work from home arrangements")
	elif (sys.argv[2] == "gcq"):
		print("Work in all government offices under alternative work arrangements")
	elif (sys.argv[2] == "mgcq"):
		print("Work in government offices may be at full operational capacity, or under alternative work arrangements  Exercise and Sports")
	else:
		print("Error: Invalid input")
    
else:
	print("Error: Invalid input")
