#!/usr/local/bin/python3

def percent_content(dna, base1, base2):
    base1_count = dna.count(base1)
    base2_count = dna.count(base2)
    total_count = base1_count + base2_count
    total_percent = total_count * 100 / len(dna)
    return total_percent

seq = "ATGCGTCAAATTCGATA"
b1, b2 = input("Enter two bases separated by a comma: ").split(", ")
print(percent_content(seq, b1, b2))

