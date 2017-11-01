import string
def rotate(text, rot):
	res = ''
	abc = string.ascii_lowercase *2
	ABC = string.ascii_uppercase *2
	for character in text:
		if character in abc or character in ABC:
			if character.islower():
				i = abc.index(character)
				res += abc[i+rot]
			else:
				i = ABC.index(character)
				res += ABC[i+rot]
		else:
			res += character


	return res