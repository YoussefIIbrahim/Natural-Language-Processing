from nltk import sent_tokenize, word_tokenize
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great," \
               " and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
#
# print(sent_tokenize(EXAMPLE_TEXT))
#
# print(word_tokenize(EXAMPLE_TEXT))

for i in word_tokenize(EXAMPLE_TEXT):
    print(i)
