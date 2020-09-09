Author          : Patricia P. Asico
Course and Year : BSIT-1
Filename        : asico_e2.py
Description     : In this exercise you will have to demonstrate your knowledge in creating and using Python data structures (containers, in particular).
Honor Code      : I have not given nor received any unathorized help in
                   completing this exercise. I am also well aware of the 
                   policies stipulated in the AdNU student handbook.

data = {"Complete name" : "Patricia P. Asico.", "Spirit animal" : "Owl, " ,  "Why You Think It Represents You" : "because just like an owl, I like to observe my surroundings and I have a quiet demeanor.",
      "Hobbies" : ["play video games", "draw", "sing"] , "Profession" : "Software engineer" }
print("I am ", data['Complete name'])
print("My spirit animal is an ", data['Spirit animal'], data['Why You Think It Represents You'])
print("When not in school, I love to: ")
print(data['Hobbies'][0])
print(data['Hobbies'][1])
print(data['Hobbies'][2])
print("I dream of being a/an", data['Profession'], "in the future.")
