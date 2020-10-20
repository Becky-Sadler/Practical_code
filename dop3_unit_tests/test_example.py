#import investigate_sequence
import pytest
import os

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

class Testing():

	def test_file_exists(self):
		my_file = 'fasta.fa'
		assert os.path.isfile(my_file) == True

	def test_open_to_read(self):
		f = open('fasta.fa', 'r')
		assert f.mode == 'r'

	def test_sign_before_identifier_removed(self):
		for i in identifiers:
			assert i.startswith('>') == False

	def test_all_within_sequence_are_AGCT(self):
		for x in reverse:
			assert x == 'A' or x == 'C' or x == 'G' or x =='T'

	def test_number_greater_or_equal_to_0(self):
		assert a_count >= 0 
		assert g_count >= 0 
		assert c_count >= 0 
		assert t_count >= 0 

	def test_number_less_than(self):
		assert a_count <= 64
		assert g_count <= 64 
		assert c_count <= 64 
		assert t_count <= 64 



