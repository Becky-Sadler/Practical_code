import xml.etree.ElementTree as ET 

#First function to create lists for the exon number, and the start and end coordinates of the exons of the region of interest.
def exon_find():
	''' Find the start and end points of the exons.
	Args: 
		uses tree root and input
	Returns:
		Two lists of strings. 
	'''
	for exon in root.findall(".//fixed_annotation/transcript/exon"):
		label.append(exon.get('label'))
		global coordinates
		coordinates = exon.find('coordinates')
		start.append(coordinates.get('start'))
		end.append(coordinates.get('end'))
	return start, end 

#Second function to find the chromosome number, start and end coordinates within the XML file.
def chromosome_find():
	''' Find the chromosome number and the genomic coordinates for
	the start and end of the gene.
	Args: 
		Uses the tree root
	Returns:
		Values for the chromosome number as well as the start and
		end of the gene as strings
	'''
	for annotation_set in root.findall(".//updatable_annotation/annotation_set[@type='lrg']"):
		mapping = annotation_set.find('mapping')
		global chrom
		chrom = mapping.get('other_name')
		global chromstart
		chromstart = mapping.get('other_start')
		global chromend
		chromend = mapping.get('other_end')
	return chrom, chromstart, chromend

# Third function to convert the position to genomic coordinate

def list_converter(list):
	''' Converts the start and ends of each exon into genomic
	coordinates.
	Args:
		List of integers
	Returns:
		List of integers
	'''
	for i in range(len(list)):
		list[i] = list[i] + int(chromstart)

tree = ET.parse('LRG_1.xml')
root = tree.getroot()

#Creation of lists for the exon number, and the start and end coordinates of the exons of the gene of interest using the first function.
start =[]
end = []
label = []

exon_find()

start = list(map(int, start))
end = list(map(int, end))

#Finding the chromosome number, start and end coordinates within the XML file using the second function.
chromosome_find()

# Converting the lists

list_converter(start)
list_converter(end)

#Code to extract the gene name:
for annotation_set in root.findall(".//updatable_annotation/annotation_set[@type='lrg']"):
			lrg_locus = annotation_set.find('lrg_locus')

#This code produces a bed file that contains 3 columns the chr number, the start coordinate of the exons, the end coordinate of the exons.
bed_file = 'LRG_1.bed'
f = open(bed_file, "w")
f.write("Chrom" + "\t" + "Start" + "\t" + "End" + "\n")
for i in range(len(start)):
	f.write(str(chrom) + "\t" + str(start[i]) + "\t" + str(end[i]) + "\n")
f.close()


