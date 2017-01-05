#################################################
#
#Essay Monkey
#
#Given a set of txt files generate an essay.
#The function should take the number of paragraphs to generate.
#The function should take the number of sentences per peragraph to generate.
#Each sentence should be of any reasonable length but each should not be the same length.
#Input
#
#See EssayMonkeyVerbs.txt
#See EssayMonkeyNouns.txt
#See EssayMonkeyAdjectives.txt
#
#HFR 2017
##########################################

def essaymonkeyEA(par,sent):
	#import random gen
	from random import randint
	#open various files
	adj=open('EssayMonkeyAdjectives.txt', 'r')
	nou=open('EssayMonkeyNouns.txt', 'r')
	ver=open('EssayMonkeyVerbs.txt', 'r')
	essay= open('Essay.txt','w')
	# read file, split the words in list, get the lenght of the list 
	adjectives=adj.readline()
	adjectives=adjectives.split(",")
	nouns=nou.readline()
	nouns=nouns.split(",")
	verbs=ver.readline()
	verbs=verbs.split(",")
	la=len(adjectives)
	ln=len(nouns)
	lv=len(verbs)
	

#iteration for paragraph 
	for i in range (par):
		p = str(i+1)
		essay.write('Paragraph ' + p + '\n' )
		#iteration for sentences, random number of words 
		for j in range (sent):
			strn = ""
			for n in range(randint(1,5)):
				strn += nouns[randint(1,ln-1)] + " "
			for v in range(randint(1,5)):
				strn += verbs[randint(1,lv-1)] + " "
			for a in range(randint(1,5)):
				strn += adjectives[randint(1,la-1)] + " "
			#remove trailing space and add .
			strn=strn.rstrip() + "."
			#capitalize 1st letter
			strn=strn[0].upper() + strn[1:]
			#write the sentence 
			essay.write (strn + '\n')
		#new line between paragraph	
		essay.write('\n')		

#closing files 
	adj.close()
	nou.close()
	ver.close()
	essay.close()
	return 

#Driver
essaymonkeyEA(3,5)
