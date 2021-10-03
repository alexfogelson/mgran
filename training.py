import pickle
import sys
import regex as re

filename = "input.txt"
n = 3 #default

argc = len(sys.argv)
if (argc > 1):
    filename = sys.argv[1]

if (argc > 2):
    if (sys.argv[2].isdigit()):
        n = int(sys.argv[2])
    else:
        raise Exception("Invalid n value.")

f = open(filename, 'r')
corpus = f.read()

corpus = re.replace(" ^[\s]*^[a-zA-Z\-]+^[\s]* ", " ", corpus)
words = corpus.split(' ')


