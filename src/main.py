
#this tokenizes the dataset into words.
import nltk
from nltk import ngrams
from Syllable.syllable import parser

#Downloads the punk if not already downloaded.
from Unigram.unigram import unigram_procedure
from ngrams.bi import bigram_runner
from ngrams.uni import unigram_runner

nltk.download('punkt')

#Read File
f=open('5.txt',encoding="utf8")
k=open('02.txt',encoding="utf8")
raw = f.read()
kraw = k.read()

tokens = nltk.word_tokenize(raw)
ktokens = nltk.word_tokenize(kraw)
newraw = ""
knewraw =""

#divide into syllable
for tok in tokens:
    try:
        newraw += parser(tok) + "\n"
    except IndexError:
        1 + 1

for tok in ktokens:
    try:
        knewraw += parser(tok) + "\n"
    except IndexError:
        1+1

#regenerate tokens
newTok = nltk.word_tokenize(newraw)
knewTok = nltk.word_tokenize(knewraw)
text = nltk.Text(newTok)
smalltext = nltk.Text(knewTok)

unigram_runner(text, smalltext)
bigram_runner(text, smalltext)

#for tok in newTok:
 #   print(tok)

#for item in two_gram:
 #   print(item)