from training import *

def mimic(corpus, n, length = 1000):
    models = []

    for i in range(1, n+1):
        models.append(train_n_gram(corpus, i))

    models.reverse()

    output = "folks"

    starting_text = [output]


    word_found = True

    words_added = 0
    while (word_found and words_added < length):
        word_found = False
        for model in models:
            result = get_next_word(starting_text, model)
            if (result != None):
                output = output + " " + result
                starting_text.append(result)
                starting_text = starting_text[-1*n:]
                word_found = True
                break
            
        words_added += 1

    return output

def apply_capitalization(text):
    words = text.split(' ')
    words[0] = words[0][0].upper() + words[0][1:]
    for i in range(1, len(words)):
        if (words[i-1][-1] == "."):
            words[i] = words[i][0].upper() + words[i][1:]

    return ' '.join(words)