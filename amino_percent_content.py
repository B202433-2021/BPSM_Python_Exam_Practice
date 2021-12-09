#!/usr/local/bin/python3

def content(sequence, aminos = ["A", "I", "L", "M", "F", "W", "Y", "V"]):
	total = 0
	sequence, aminos = sequence.upper()
	for amino in aminos:
		a_count = sequence.count(amino)
		total += a_count
	percent = total * 100 / len(sequence)
	return percent

assert round(content("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(content("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(content("MSRSLLLRFLLFLLLLPPLP")) == 65


protein = input("Enter a protein sequence
