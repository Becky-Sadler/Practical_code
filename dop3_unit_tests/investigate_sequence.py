'''Program should do:
	> Open and read fasta file
	> Split the sequences from the identifiers
	> Have a list of identifiers and sequences
	> Reverse complement the sequences
	> Count the occurances of each nucleotide, save this into lists
	> Complile all information about each into own list
'''
sequence = open('fasta.fa', 'r')
fastaseqs = sequence.read()
sequences = []
identifiers = [] 

lines = fastaseqs.splitlines()

for i in lines:
	if i.startswith('>'):
		identifiers.append(i[1:])
	else:
		sequences.append(i)

count = 0
for i in sequences:
	reverse = list(reversed(i))
	complement = []

	for x in reverse: 
		if x == 'A':
			complement.append('T')
		if x == 'G':
			complement.append('C')
		if x == 'C':
			complement.append('G')
		if x == 'T':
			complement.append('A')

	reverse_complement = ''.join(complement)

	a_count = reverse_complement.count('A')
	g_count = reverse_complement.count('G')
	c_count = reverse_complement.count('C')
	t_count = reverse_complement.count('T')

	data = [identifiers[count], reverse_complement, a_count, g_count, c_count, t_count]
	count += 1
	print(data)