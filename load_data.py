import regex as re


def clean_corpus(corpus):
    corpus = corpus.lower()
    periods_as_words = re.sub("\. ", " . ", corpus)
    commas_as_words = re.sub("\, ", " , ", corpus)
    questions_as_words = re.sub("\? ", " ? ", corpus)
    exclamation_as_words = re.sub("\! ", " ! ", corpus)

    chunks = exclamation_as_words.split(' ')
    words = list(filter(lambda x: len(re.findall("[^a-zA-Z\.,!?]+", x)) == 0, chunks))
    return words

