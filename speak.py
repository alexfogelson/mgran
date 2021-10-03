import sys
from training import *
from load_data import *

filename = "input.txt"
n = 3 #default
length = 1000

argc = len(sys.argv)
if (argc > 1):
    filename = sys.argv[1]

if (argc > 2):
    if (sys.argv[2].isdigit()):
        n = int(sys.argv[2])
    else:
        raise Exception("Invalid n value.")


f = open(filename, 'r')
corpus = clean_corpus(f.read())

models = [{}]

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

print(output)
            
