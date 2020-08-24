# Code to give the reverse complement of a dna sequence. 
# Starts by opening a text file that contains the DNA seq.
f= open("dna.txt", "r")
# Checking that it is opened to read, then reading the file and assigning it to varaible named dna
if f.mode == 'r':
	dna = f.read()

# Taking the dna string, turning it into a list and reversing it
reverse = (list(reversed(dna)))

# Creating a new list called complement to hold the reverse complement dna
complement = []

# Doing the complement of the reverse dna string using a simple for loop. 
for x in reverse: 
	if x == 'A':
		complement.append('T')
	if x == 'G':
		complement.append('C')
	if x == 'C':
		complement.append('G')
	if x == 'T':
		complement.append('A')

# Joining all the dna nucleotides in the list into one coherant string (with no separator - which is why there is '')
reverse_complement = ''.join(complement)

# Creates a new .txt file containing the reverse_complement
f = open("reverse_complement.txt", "w+")
for x in reverse_complement:
	f.write(x)

f.close()

print('The DNA sequence is ' + dna)
print('The reverse complement sequence is ' + reverse_complement)