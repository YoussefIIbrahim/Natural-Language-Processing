import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_txt = state_union.raw("2005-GWBush.txt")
sample_txt = state_union.raw("2006-GWBush.txt")

custom_sent_tokenize = PunktSentenceTokenizer(train_txt)

tokenized = custom_sent_tokenize.tokenize(sample_txt)


def process_content():
    try:
        for w in tokenized:
            words = nltk.word_tokenize(w)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))


process_content()
