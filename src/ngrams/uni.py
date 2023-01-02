#Take %95 and %5 text.

#calculate for both:
# 1 - parse them up
# 2 - tokenize
# 3 - count them
# 4 - clear low frequency
# 5 - prepare ngram
import random
from nltk import ngrams

#####################################################################################
class unigram:
    def __init__(self):
        self.wordMatrix = []
        self.countMatrix = []
        self.unigramtable = []
        self.ug = []
        self.total = 0

def unigram_runner(text, smalltext):
    print("You started unigram!")

    print("\nTracing big data: %95")
    big = get_unigram_class(text)

    print("\n\nTracing big data: %5")
    small = get_unigram_class(smalltext)

    #--
    print("\nCalculating unigrams")
    calculate_unigram_table(big)
    calculate_unigram_table(small)

    #--
    print("\nCalculating perplexity with the help of smaller data (%5)")
    calculate_perplexity(big,small)

    #--
    print("\nGenerating random sentences:")
    generate_random(big)


#####################################################################################
def get_unigram_class(text):
    u = unigram()
    u.ug = ngrams(text, 1)
    # get ALL
    for token in u.ug:
        u.total += 1
        i = 0
        found = 0
        for word in u.wordMatrix:
            if token == word:
                u.countMatrix[i] += 1
                found = 1
                break
            i += 1
        if found == 0:
            u.wordMatrix.append(token)
            u.countMatrix.append(1)
    print(f"Read total of {u.total} syllables")

    # deleting low frequent words.
    minOccurence = 7
    print(f"removing occurences lesser than {minOccurence}")
    i = 0
    while True:
        try:
            if u.countMatrix[i] < minOccurence:
                # print(f"deleting {i} {countMatrix[i]} {wordMatrix[i]}")
                u.wordMatrix.__delitem__(i)
                u.countMatrix.__delitem__(i)
            else:
                i += 1
        except IndexError:
            break

    print(f"We have {len(u.wordMatrix)} unique syllables after cleaning up")
    return u
#####################################################################################

def calculate_unigram_table(unig):
    #now it is time to unigram table.
    for i in unig.countMatrix:
        unig.unigramtable.append(i/unig.total)

#####################################################################################

def calculate_perplexity(big,small):
    perplexity = 1
    for i in range(0, len(big.unigramtable)):
        found = False
        index = 0
        for j in range(0,len(small.unigramtable)):
            if(small.unigramtable[j] == big.unigramtable[i]):
                found = True
                index = j
        if found:
            perplexity += big.unigramtable[index]
        else:
            perplexity += big.total/len(big.unigramtable)

    perplexity = 1 / perplexity
    perplexity = perplexity ** (1 / len(big.unigramtable))
    print(f"Perplexity of unigram: {perplexity}")

#####################################################################################

def generate_random(uni):
    for i in range(0, 5):
        print(f"{uni.wordMatrix[random.randrange(0, len(uni.wordMatrix))]}", end=" ")
        for j in range(0, 10):
            max = [0, 0, 0, 0, 0]
            indexes = [0, 0, 0, 0, 0]
            for k in range(0, len(uni.wordMatrix)):
                if uni.countMatrix[k] >= max[0]:
                    max[0] = uni.countMatrix[k]
                    indexes[0] = k
                elif uni.countMatrix[k] >= max[1]:
                    max[1] = uni.countMatrix[k]
                    indexes[1] = k
                elif uni.countMatrix[k] >= max[2]:
                    max[2] = uni.countMatrix[k]
                    indexes[2] = k
                elif uni.countMatrix[k] >= max[3]:
                    max[3] = uni.countMatrix[k]
                    indexes[3] = k
                elif uni.countMatrix[k] >= max[4]:
                    max[4] = uni.countMatrix[k]
                    indexes[4] = k
            print(uni.wordMatrix[indexes[random.randrange(0, 4)]], end=" ")
        print("")