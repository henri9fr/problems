##################################3
#Common Subsequence
#
#You are given two sequences. Write a program to determine the longest common subsequence between the two strings 
#(each string can have a maximum length of 50 characters). 
#NOTE: This subsequence need not be contiguous. The input file may contain empty lines, these need to be ignored. 
#The first argument will be a path to a filename that contains two strings per line, semicolon delimited. 
#You can assume that there is only one unique subsequence per test case.
#
#Example Input
#
#XMJYAUZ;MZJAWXU
#
#Example Output
#
#MJAU
#HFR 2017
##################################################
# 
#for this one I did reseach online to fully understand it , and one I found the function .. I spend time to 
# grab the concept instead 
# I added the read the file part 
# source http://www.geeksforgeeks.org/printing-longest-common-subsequence/
##############

# Returns length of LCS for X[0..m-1], Y[0..n-1] 
def lcs(X, Y, m, n):
    L = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
 
    # Following steps build L[m+1][n+1] in bottom up fashion. Note
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] 
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    # Following code is used to print LCS
    index = L[m][n]
 
    # Create a character array to store the lcs string
    lcs = [""] * (index+1)
    lcs[index] = "\0"
 
    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
 
        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
 
        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
 
    print "LCS of " + X + " and " + Y + " is " + "".join(lcs) 
 

# This code is contributed by BHAVYA JAIN

#The following part of code is from HFR to open and read the file
f = open('sampleFile', 'r')
for line in f:
	if (line <> "" and ";" in line):
		sub=line.split(";")
		X=sub[0]
		Y=sub[1]
		m = len(X)
		n = len(Y)
		lcs(X, Y, m, n)