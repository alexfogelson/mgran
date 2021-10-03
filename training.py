import pickle
import sys
import random
import regex as re


def train_n_gram(corpus, n, padding = .05):
    if (n <= 0):
        raise Exception("Invalid n value" + str(n))

    model = dict()
    
    for i in range(len(corpus)):
        if (i < n):
            continue
        prev_words = tuple(corpus[i-n:i])
        if (model.get(prev_words) == None):
            model[prev_words] = []
        model[prev_words].append(corpus[i])
    
    for key in model:
        value = model[key]
        for i in range(int(len(value)*padding)):
            value.append(None)
        
        model[key] = value

    return model

def get_next_word(prev_words, model):
    if (type(prev_words) != tuple):
        prev_words = tuple(prev_words)
    
    if (model.get(prev_words) == None):
        return None
    
    possible_words = model[prev_words]
    random_index = random.randint(0, len(possible_words)-1)
    random_word = possible_words[random_index]

    return random_word





