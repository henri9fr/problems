##############################
#Pig Latin
#
#Example Input
#
#"HeLLo World! I can't wait to explore your VAST forests. The-End!"
#Example Output
#
#"ElLOhay Orldway! I antca'y aitway otay exploreway ouryay ASTVay orestfay. Hetay-Endway!"
#
#HFR 2017
#####

def PigLatinEA(string):
	pigdone=""
	vowels='aeiouAEIOU'
	punct = '?!,.:;'
	suffix='way'
	hyp='-'
	hstring=''

	#remove hyphen and treat as 2 words
	if hyp in string:
		newstring=string.split('-')
		lnew=len(newstring)
		for i in range(lnew):
			hstring += newstring[i] + " - "

		string = hstring.rstrip()
		string = string[:-1]
		string = string.rstrip()
			
	piglist = string.split(' ')
	lp=len(piglist)
	    	
	for i in range(lp):
		word= piglist[i]
		#single letter word not modified
		if len(word)==1:
			newpig=word
		elif word[0].islower():
			
			if (word[0] in vowels and word[-1] not in punct):
				newpig=word[:] + "way"
			elif  (word[0] not in vowels and word[-1] not in punct):
				newpig=word[1:] + word[0] + "ay"
			elif (word[0] in vowels  and word[-1] in punct):
				newpig=word[:-1] + "way" + word[-1]
			elif  (word[0] not in vowels  and word[-1] in punct):
				newpig=word[1:-1] + word[0] + "ay" +  word[-1]	
			else:
				continue
			#word ending with way not modified
			if (word.endswith(suffix) or (word[-1] in punct and word[:-1].endswith(suffix))):
				newpig=word	

		else:
			if (word[0] in vowels and word[-1] not in punct):
				newpig=word[:] + "way"
			elif  (word[0] not in vowels and word[-1] not in punct):
				newpig=word[1].upper() + word[2:] + word[0].lower() + "ay"
			elif (word[0] in vowels and word[-1] in punct):
				newpig=word[:-1] + "way" + word[-1]
			elif  (word[0] not in vowels and word[-1] in punct):
				newpig=word[1].upper() + word[2:-1] + word[0].lower() + "ay" +  word[-1]
			else:
				continue
			#word ending with way not modified
			if (word.endswith(suffix) or (word[-1] in punct and word[:-1].endswith(suffix))):
				newpig=word	


		pigdone += newpig + (" ")
	#add hyphen back 
	if hyp in pigdone:
		hstring=''
		newpigdone=pigdone.split(' - ')
		lnew=len(newpigdone)
		for i in range(lnew):
			newpigdone[i] = newpigdone[i].strip()
			hstring += newpigdone[i] + "-"
		

		pigdone = hstring.rstrip()
		pigdone = pigdone[:-1]
		pigdone = pigdone.rstrip()
		
	return pigdone
#Driver
sentence="Hello EA World! I am amazing. A word with way: tramway. You should hire-hire me and I can't wait! The-End!"
#sentence="The-End"
print sentence
print "piglatin..."
print PigLatinEA(sentence)	
