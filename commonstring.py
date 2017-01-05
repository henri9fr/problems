#########################
#Given two strings, write a program that efficiently finds the longest common subsequence.
#Example Input
#
#"Everything is awesome!"
#"Hello World is awesome!"
#Output
#
#is awesome!
#HFR 2017
####################

def commonsubstringEA(string1,string2):
	
	match = []
	answer = ""
	length = 0

	if string1 == string2:
		print "same string !!"
		return string1

	if (len(string1)==0 or len(string2)==0):
		answer="one string empty, no match"
		return answer	 

	ls1 = list(string1) + [" "]
	ls2 = list(string2)	+ [" "]

	for i in range(0,len(ls1)):
		if ls1[i] in ls2:
			match.append(ls1[i])
			for j in range(i+1,len(ls1)):
				if ''.join(ls1[i:j]) in string2:
					match.append(''.join(ls1[i:j]))
						
	for string in match:
		if length < len(list(string)):
			length = len(list(string))		
			answer = string


	return answer		
			
#Driver
print commonsubstringEA("Hello World is awesome!","Everything is awesome!")
print commonsubstringEA("Hello World is awesome!","Hello World is awesome!")
print commonsubstringEA("Hello World is awesome!","")

