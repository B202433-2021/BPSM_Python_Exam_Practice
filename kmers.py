#!/usr/local/bin/python3

import sys 

def kmer_counter(dna, k_length, min):
	
	kmers = []
	for i in range(len(dna) - k_length):
		start = i
		end = i + k_length
		kmer = dna[start:end]
		kmers.append(kmer)
	
	kmers_above_threshold = []
	for k in kmers:
		if kmers.count(k) > min:
			kmers_above_threshold.append(k)
	kmers_above_threshold_set = set(kmers_above_threshold)

	return kmers_above_threshold_set


dna = str(sys.argv[1])
k_length = int(sys.argv[2])
min = int(sys.argv[3])

ks = kmer_counter(dna, k_length, min)
print(ks)
			
