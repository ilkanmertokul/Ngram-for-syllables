
#This piece of code is from
#https://github.com/batuhangun/Syllable-Turkish-Words/blob/master/spell_out.py

#modified to get syllables individually, and some other things that is explained in the report..

consonant = ["b", "c", "d", "g", "ğ", "j", "l", "m", "n", "r", "v", "y", "z", "ç", "f", "h", "k", "p", "s", "ş", "t"]
vowel = ["a", "ı", "o", "u", "e", "i", "ö", "ü", "â"]
other = ["<", ">", ",", "=", "/", "'", ".", ";", "-","\"", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def parser(word):
    word = word.lower()
    spell = list(word)
    vowel_count = sum([1 for i in spell if i in vowel])
    other_count = sum([1 for i in spell if i in other])
    lenght = len(word)

    if lenght == 1 or lenght == 2:
        return word

    if (lenght == 4 or lenght == 3) and vowel_count == 1:
        return word

    if other_count > 1:
        return word
    if other_count ==1:
        i=0
        for char in word:
            if char in other:
                break
            i += 1
        if lenght == 1:
            return word
        return parser(word[0:i]) + " " + word[i] + " " + parser(word[i+1:])

    if word[0] in consonant:
        if word[1] in consonant:
            if word[4] in consonant:
                return word[:4] + " " + parser(word[4:])
            else:
                return word[:3] + " " + parser(word[3:])
        else:
            if word[2] in consonant and word[3] in consonant and not word[4] in consonant:
                return word[:3] + " " + parser(word[3:])
            elif word[2] in consonant and word[3] in consonant and word[4] in consonant:
                return word[:4] + " " + parser(word[4:])
            else:
                return word[:2] + " " + parser(word[2:])
    else:
        if word[1] in vowel:
            return word[0] + " " + parser(word[1:])
        else:
            if word[2] in vowel:
                return word[:1] + " " + parser(word[1:])
            else:
                return word[:2] + " " + parser(word[2:])