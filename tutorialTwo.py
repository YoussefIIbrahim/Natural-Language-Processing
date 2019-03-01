from nltk.corpus import stopwords
from nltk import word_tokenize

EXAMPLE_SENTENCE = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

words = word_tokenize(EXAMPLE_SENTENCE)
#
# filtered_sentence = []
# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)
#
# print(filtered_sentence)

filtered_sentence = [w for w in words if w not in stop_words]
print(filtered_sentence)