#!/usr/local/bin/python3

info_dict = {}

name = input("What is your name?\n\t>")
info_dict["n"] = name

age = input("How old are you?\n\t>")
while True:
	try:
		age = int(age)
		break
	except:
		age = input("Invalid input, please enter a number\n\t>")
info_dict["a"] = age

if info_dict["n"] == "Robert":
	print("Good luck at GSK")
else:
	print("Unlucky mate")

if info_dict["a"] != 22:
	print("Taylors not happy")

