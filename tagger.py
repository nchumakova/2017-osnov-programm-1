# objective of the program:
# read the output of the tokeniser and give each word
# the most likely tag according to our language model
import sys

frequent_tag = 'X'
count = 0	
fd = open('model.tsv')
for line in fd.readlines():
	line = line.strip('\n')
	line = line.split('\t') # ['0.4', 5, 'ADJ', '_']
	if int(line[1]) > count:
		count = int(line[1])	  
		frequent_tag = line[2]

print(frequent_tag)
input = sys.stdin.readlines()



for line in input:
	line = line.strip()
	if '\t' not in line:
		continue
	# 
	row = line.split('\t')
	# set the default tag to the most frequent	
	row[3] = frequent_tag
	
	print('\t'.join(row))

