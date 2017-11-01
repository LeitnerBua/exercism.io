import logging, re

logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

def word_count(sentence):
	c_word = {}
	list_sentence = re.sub('[\W_]', ' ', sentence.lower()).split()
	for word in list_sentence:
		c_word.setdefault(word, 0)
		c_word[word] = c_word[word] + 1

	logging.debug(list_sentence)
	logging.debug(c_word)
	return c_word