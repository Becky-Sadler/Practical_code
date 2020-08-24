import xml.etree.ElementTree as ET 

class ETParser():

	def __init__(self, file):
		tree = ET.parse(file)
		self.root = tree.getroot()
		self.start = []
		self.end = []
		self.label = [] 
		self.chrom = None
		self.chromstart = None
		self.chromend = None

	def exon_find(self):
	''' Find the start and end points of the exons.
	Args: 
		uses tree root and input
	Returns:
		Two lists of strings. 
	'''
		for exon in self.root.findall(".//fixed_annotation/transcript/exon"):
			self.label.append(exon.get('label'))
			global coordinates
			coordinates = exon.find('coordinates')
			self.start.append(coordinates.get('start'))
			self.end.append(coordinates.get('end'))
		
		self.start = list(map(int, self.start))
		self.end = list(map(int, self.end))
		return self.start, self.end 

	def chromosome_find(self):
	''' Find the chromosome number and the genomic coordinates for
	the start and end of the gene.
	Args: 
		Uses the tree root
	Returns:
		Values for the chromosome number as well as the start and
		end of the gene as strings
	'''
		for annotation_set in self.root.findall(".//updatable_annotation/annotation_set[@type='lrg']"):
			mapping = annotation_set.find('mapping')
			global chrom
			self.chrom = mapping.get('other_name')
			global chromstart
			self.chromstart = mapping.get('other_start')
			global chromend
			self.chromend = mapping.get('other_end')
		return self.chrom, self.chromstart, self.chromend

	def list_converter(self, list, chromposition):
	''' Converts the start and ends of each exon into genomic
	coordinates.
	Args:
		List of integers
	Returns:
		List of integers
	'''
		for i in range(len(list)):
			list[i] = list[i] + int(chromposition)
		return self.start

	def create_BED(self, bed_file, chrom, start, end):
	''' Creation of a .bed file using the values calculated
	in the other ETParser methods
	Args:
		Bed_file name - Str
		chromosome number - Str/int
		start - list of int
		end - list of int
	Returns:
		a . bed file in the directory
	'''
		bed_file = 'LRG_1.bed'
		f = open(bed_file, "w")
		f.write("Chrom" + "\t" + "Start" + "\t" + "End" + "\n")
		for i in range(len(start)):
			f.write(str(chrom) + "\t" + str(start[i]) + "\t" + str(end[i]) + "\n")
		f.close()


treeparse = ETParser('LRG_1.xml')
exon = treeparse.exon_find()
start, end = exon
chromosome = treeparse.chromosome_find()
chrom, chromstart, chromend = chromosome
start = treeparse.list_converter(start, chromstart)
end = treeparse.list_converter(end, chromstart)
treeparse.create_BED('LRG1.bed', chrom, start, end)

