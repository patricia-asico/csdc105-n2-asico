#Author				:	Patricia P. Asico
#Course and Year	:	1-BSIT
#Filename			:	emmet.py
#Description		: 	A class that converts code into html code and a class 
#						that checks if the operators and html tags are valid
#Honor Code			:	I have not given nor received any unauthorized help in
#						completing this exercise. I am also well aware of the
#						policies stipulated in the Adnu student handbook.
class Emmet():
	def __init__(self, raw):
		self.raw = raw
		self.parent = self.raw.split("+")			#this line splits the strings when there is a parent operator ('+')
		
	def __str__(self):
		HtmlOutput = ""								#to store the final html output
		for i in range(len(self.parent)):			#this line splits the strings when a child operator('>') is encountered 
			split = self.parent[i].split(">")
			
			for x in range(len(split)):
				HtmlOutput =+  "\t" *x +"<{}>".format(split[x])+"\n"
				
			for y in range(len(split)-1,-1,-1):
				HtmlOutput =+ "\t| * y + "</{}>".format(split[y]) + "\n"
			
		return HtmlOutput				 

class Valid():
	def __init__(self,raw):
		self.raw = raw
		self.ValidOrInvalid(self)

	def ValidOrInvalid(self):
		ValidStrings = ["div", "nav", "p", "span", ">", "+"]		# ValidStrings contains the valid html tags and operatorss
		InvalidStrings = ["<", ">>", "+>", ">+", "++"]				# this line contains the invalid strings 
		
		if any (x in self.raw for x in InvalidStrings):				#statements that checks whether the strings are valid
			return False
		else:
			return True
			
