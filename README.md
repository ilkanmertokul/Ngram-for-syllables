# Ngram-for-syllables

Developed a statistical language model of Turkish that will use N-grams of Turkish syllables.

Used Python language.

There are 3 data texts. 95.txt, 5.txt and 02.txt, you can use any of them you
want to run.
Program runs 5.txt and 02.txt as default, but they are really small datasets.
95.txt has 143599 syllables, and when the data is optimized, there will be 1099
unique syllables.
5.txt has 16682 syllables, and when the data is optimized, there will be 373
unique syllables.
02.txt has 4922 syllables, and when the data is optimized, there are 154 unique
syllables.

# UNIGRAM

This unigram calculations run on 95.txt and 5.txt first and these are the results.
The reason for unexpected perplexity must be a result of small dataset.
The data’s %95 and %5 are calculated seperately to calculate these.
![Ekran görüntüsü_20230102_161224](https://user-images.githubusercontent.com/61903795/210236070-fa0957bd-802f-4a63-aa5b-ce4da7292bb7.png)

# BIGRAM

These values calculated with the help of: zips law(efficient table), chain rule
(creating ) and Shannon’s Method(generating random sentences).

![Ekran görüntüsü_20230102_161229](https://user-images.githubusercontent.com/61903795/210236063-e3c1c64b-27df-4572-8388-ccad4932d7d8.png)

# Getting an efficient table

To get an efficient table, i ignored the syllables that is lesser frequency than 7.
This way, i can estimate their frequency with :
total_syllable / total_unique_syllable

Used Libraries / Github Codes:
To get syllables, i mainly used and modified:
https://github.com/batuhangun/Syllable-TurkishWords/blob/master/spell_out.py
This function is modified to give better output format.
To get ngrams, i used nltk library from python.
https://www.nltk.org/ to see documentation.
This library only used to get ngrams list, not ngram tables.
