from string import ascii_lowercase

def is_pangram(word):
	abc = ascii_lowercase
	word = word.lower()
	for i in abc:
		if i not in word:
			return False
	return True