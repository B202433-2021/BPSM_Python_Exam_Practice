#!/usr/local/bin/python3

import shutil 

#shutil.copy("/localdisk/data/BPSM/Lecture12/genomic_dna2.txt", "/localdisk/home/s2173344/Exam_practice/")
#shutil.copy("/localdisk/data/BPSM/Lecture12/exons.txt", "/localdisk/home/s2173344/Exam_practice/")

with open("genomic_dna2.txt") as gene_infile:
	with open ("exons.txt") as ex_infile:
		with open("output_exons.txt", "w") as outfile:
			sequence = gene_infile.read()
			sequence = sequence.replace("\n", "")
			for line in ex_infile:
				positions = line.split(",")
				start = int(positions[0])
				stop = int(positions[1])
				exon = sequence[start-1:stop]
				outfile.write(f"{exon} from {start} to {stop} with length {len(exon)}\n")
