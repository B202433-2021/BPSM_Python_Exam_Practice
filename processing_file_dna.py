#!/usr/local/bin/python3

with open ("/localdisk/data/BPSM/Lecture12/input.txt") as infile:
	with open ("trimmed_seqs.txt", "w") as outfile:
		for line in infile:
			line = line.replace("\n", "")
			trimmed = line[14:]
			print(trimmed)
			outfile.write(trimmed + "\n")
			print(len(trimmed))
