def count_words(file_contents):

	x = file_contents.split()

	return len(x)

def count_characters(file_contents):

	letter_dict = {

		'a': 0,
		'b': 0,
		'c': 0,
		'd': 0,
		'e': 0,
		'f': 0,
		'g': 0,
		'h': 0,
		'i': 0,
		'j': 0,
		'k': 0,
		'l': 0,
		'm': 0,
		'n': 0,
		'o': 0,
		'p': 0,
		'q': 0,
		'r': 0,
		's': 0,
		't': 0,
		'u': 0,
		'v': 0,
		'w': 0,
		'x': 0,
		'y': 0,
		'z': 0

	}

	for character in file_contents:

		char = character.lower()

		if char == 'a':
			letter_dict['a'] += 1

		if char == 'b':
			letter_dict['b'] += 1

		if char == 'c':
			letter_dict['c'] += 1

		if char == 'd':
			letter_dict['d'] += 1
	
		if char == 'e':
			letter_dict['e'] += 1

		if char == 'f':
			letter_dict['f'] += 1

		if char == 'g':
			letter_dict['g'] += 1

		if char == 'h':
			letter_dict['h'] += 1

		if char == 'i':
			letter_dict['i'] += 1

		if char == 'j':
			letter_dict['j'] += 1

		if char == 'k':
			letter_dict['k'] += 1

		if char == 'l':
			letter_dict['l'] += 1

		if char == 'm':
			letter_dict['m'] += 1

		if char == 'n':
			letter_dict['n'] += 1

		if char == 'o':
			letter_dict['o'] += 1

		if char == 'p':
			letter_dict['p'] += 1

		if char == 'q':
			letter_dict['q'] += 1

		if char == 'r':
			letter_dict['r'] += 1

		if char == 's':
			letter_dict['s'] += 1

		if char == 't':
			letter_dict['t'] += 1

		if char == 'u':
			letter_dict['u'] += 1

		if char == 'v':
			letter_dict['v'] += 1

		if char == 'w':
			letter_dict['w'] += 1

		if char == 'x':
			letter_dict['x'] += 1

		if char == 'y':
			letter_dict['y'] += 1

		if char == 'z':
			letter_dict['z'] += 1

	return letter_dict

def main():

	with open("books/frankenstein.txt") as f:
	
		file_contents = f.read()

		print(file_contents)

	print("--- Begin report of books/frankenstein.txt ---")
	print(count_words(file_contents), "words found in the document")

	d = count_characters(file_contents)
	
	for key in d.keys():

		print("The letter",key,"was found", d[key], "times")

main()



