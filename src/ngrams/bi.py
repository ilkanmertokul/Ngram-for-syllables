#Take %95 and %5 text.

#calculate for both:
# 1 - parse them up
# 2 - tokenize
# 3 - count them
# 4 - clear low frequency
# 5 - prepare ngram with chain rule.

#####################################################################################
import random
from nltk import ngrams


class bigram:
    def __init__(self):
        self.wordMatrix = []
        self.countMatrix = []
        self.bitable = []
        self.ug = []
        self.total = 0

#####################################################################################

def bigram_runner(text, smalltext):
    print("You started bigram!")

    print("\nTracing big data: %95")
    big = get_bigram_class(text)

    print("\n\nTracing big data: %5")
    small = get_bigram_class(smalltext)

    #--
    print("\nCalculating bigrams")
    calculate_bigram_table(big)
    calculate_bigram_table(small)

    #--
    print("\nCalculating perplexity with the help of smaller data (%5)")
    calculate_perplexity(big,small)

    #--
    print("\nGenerating random sentences:")
    generate_random(big)

#####################################################################################

def get_bigram_class(text):
    u = bigram()
    u.ug = list(ngrams(text, 2))
    print(len(u.ug))
    print(len(u.wordMatrix))
    # get ALL
    for token in u.ug:
        u.total += 1
        i = 0
        found = 0
        for word in u.wordMatrix:
            if token[0] == word:
                u.countMatrix[i] += 1
                found = 1
                break
            i += 1
        if found == 0:
            u.wordMatrix.append(token[0])
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

def calculate_bigram_table(bigram):

    for i in range(0,len(bigram.wordMatrix)):
        e = []
        for j in range(0,len(bigram.wordMatrix)):
            e.append(0)
        bigram.bitable.append(e)
#
    for i in range(0,len(bigram.wordMatrix)):
        for j in range(0,len(bigram.wordMatrix)):
            for k in range(0,len(bigram.ug)):
                if bigram.wordMatrix[i] == bigram.ug[k][0] and bigram.wordMatrix[j] == bigram.ug[k][1]:
                    print(f"found i.{i} j.{j} k.{k}-> {bigram.wordMatrix[i]} == {bigram.ug[k][0]} and {bigram.wordMatrix[j]} == {bigram.ug[k][1]}")
                    bigram.bitable[i][j] += 1

#####################################################################################

def calculate_perplexity(big,small):
    perplexity = 1
    for i in range(0, len(big.bitable)):
        found = False
        index = 0
        for j in range(0,len(small.bitable)):
            if(small.bitable[j] == big.bitable[i]):
                found = True
                index = j
        if found:
            perplexity += big.bitable[index]
        else:
            perplexity += big.total/len(big.bitable)

    perplexity = 1 / perplexity
    perplexity = perplexity ** (1 / len(big.bitable))
    print(f"Perplexity of bigram: {perplexity}")

#####################################################################################

def generate_random(bi):
    for i in range(0, 5):
        rand = random.randrange(0, len(bi.wordMatrix))
        print(f"{bi.wordMatrix[rand]}", end=" ")
        for j in range(0, 10):
            max = [0, 0, 0, 0, 0]
            indexes = [0,0,0,0,0]
            for k in range(0, len(bi.wordMatrix)):
                if bi.bitable[rand][k] > max[0]:
                    max[0] = bi.bitable[rand][k]
                    indexes[0] = k
                elif bi.bitable[rand][k] > max[1]:
                    max[1] = bi.bitable[rand][k]
                    indexes[1] = k
                elif bi.bitable[rand][k] > max[2]:
                    max[2] = bi.bitable[rand][k]
                    indexes[2] = k
                elif bi.bitable[rand][k] > max[3]:
                    max[3] = bi.bitable[rand][k]
                    indexes[3] = k
                elif bi.bitable[rand][k] > max[4]:
                    max[4] = bi.bitable[rand][k]
                    indexes[4] = k

            print(bi.wordMatrix[indexes[random.randrange(0, 4)]], end=" ")
        print("")