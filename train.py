import sys


# read all of the input lines in our tagged corpus
lines = sys.stdin.readlines()

# variable to store the counts for individual tags
tag_count = {}
# variable to store counts of tags given words
words = {}
# variable to store the counts of individual surface forms/words
words_of_word = {}
total = 0
for line in lines:
    # skip lines that don't have a tab in 
    if '\t' not in line:
        continue
        
    # split the line into a list of cells in the row
    row = line.split('\t')

    # get the tag from the 4th column and put it in a variable
    tag = row[3]
    if tag == '_':
        continue
    # if we haven't seen the tag before then initialise the count to 0
    if tag not in tag_count:
        tag_count[tag] = 0
    tag_count[tag] = tag_count[tag] + 1
    # get the surface form from the 2nd column
    word = row[1]
    if word == '_':
        continue
    # if we haven't seen the word before then initialise the word counter to 0
    if word not in words_of_word: 
        words_of_word[word] = 0
    words_of_word[word] = words_of_word[word] + 1
    # if we haven't seen the word before then initialise it to an empty dict
    if word not in words:
        words[word] = {}
    # if we haven't seen the tag GIVEN the word before, initialise it to 0
    if tag not in words[word]:
        words[word][tag] = 0
    words[word][tag] = words[word][tag] + 1
    total = total + 1
    #print(tag_count[tag], tag, row)
print()
# {'ADJ': 2, 'NOUN': 5, 'NUM': 2, '_': 80, 'PROPN': 3}                                                       

for tag in tag_count:
    freq = tag_count[tag]/total
    print(tag, tag_count[tag], freq)

# for each of the words in the matrix
for word in words:
    # for each of the tag
    for tag in words[word]:
        freq = words[word][tag]/words_of_word[word]
        print('%.2f\t%d\t%s\t%s' % (freq, words[word][tag], tag, word))
