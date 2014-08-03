import re
import sys

input_filename = sys.argv[1]

try:
	output_filename = sys.argv[2]
except Exception:
	output_filename = 'output.txt'

regs = [
	
	(			r'[\[\]]'	        ,				''				),
	(        r'\bnvarchar[ ]*\((.)*\) '      ,			'string '			),
	(		r'\bdecimal[ ]*\((.)*\)'			,			'decimal'			),

	(		r'\buniqueidentifier\b' , 			'string'			),
	(		r'\bNOT NULL\b'			, 				''					),
	(		r'\bNULL\b'				,				''				),
	(		r'\bdatetime\b'			,			'timestamp'			),
	(		r'\bmoney\b'			,			'decimal'			),
	(		r'\bbit\b'				,			'boolean'			),
	# (		r'^\b[^ ]+'	   ,          	''  				)



]

input = open(input_filename)
output = open(output_filename,'w')


lines = input.readlines()

for line in lines:
	for (k,v) in regs:
		print k
		line = re.sub(k,v,line)


	output.write(line)
	# print line

output.close()












# for (k,v) in regs:
# 	test = re.sub(k,v,test)
# 	print "matching" + k + "\t" +test


# if match:
# 	print match.group()
# else :
# 	print "No match"

