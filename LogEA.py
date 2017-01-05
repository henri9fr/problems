#########################
#Logs
#Create a program that parses Logs.txt and allows the user to search inclusivly and exclusivly by the following:
#
#OS
#Browser
#IP
#Date and Time
#File Requested
#Referer
#Example Input
#
#Logs.txt
#
#HFR 2017
############################################

try:
	# input file name
	filename = "Logs.txt"	
	num_lines = sum(1 for line in open('Logs.txt'))
	while True:
		f = open(filename, "r")
		choice = raw_input("Enter\n 1.Search Inclusively\n 2.Search Exclusively\n or '0' to exit!\n ")
		if choice == '1':
			searchimp = raw_input("Enter a string to be included in the results\n Sample:OS,Browser,IP,Date and Time,File Requested,Referer\n Search: ")
			i = 0
			for line in f:
				if searchimp in line:
					#return full line
					print line
					i +=1
				else:
					continue
			#end for loop / end of file . print number of occurences
			if i == 0:
				print "Not found"
			else: 	
				i=str(i)
				num_lines=str(num_lines)
				print searchimp + " found " +  i + " time(s) in " + num_lines + " lines"
				
		
		elif choice == '2':
			searchimp = raw_input("Enter a string to be excluded in the results\n Sample:OS,Browser,IP,Date and Time,File Requested,Referer\n Search: ")
			i = 0
			for line in f:
				if searchimp not in line:
					#return full line
					print line
					i +=1
							
				else:
					continue
			#end for loop / end of file . print number of occurences		
			if (i == 0 or i == num_lines):
				print searchimp + " was not found in the file"
			else:
				ex=str(num_lines-i)
				num_lines=str(num_lines)

				print searchimp + " excluded " + ex +" time(s) in " + num_lines + " lines"		
		elif choice == '0':
			break
		
		else: 
		# choice <> 0, 1 or :
			print choice + " is not valid !"	
		continue

except IOError:
	print 'cannot open', filename