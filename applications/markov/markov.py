import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

def markov(a):
    #dictionary
    cache = {}

    # makes the string a list, removing extra spaces
    a = " ".join(a.split()).split(" ")
    prev_word = ""
    # loop through the new list
    for word in a:
        # remove characters
        word = word.strip('()"}{')

        # if the word's in the cache
        if cache.get(f"{word}"):

            # add it to the previous words value
            cache[prev_word].append(word) 

        else: # if the word is not in the cache

            # enter current word into cache with empty list as value
            cache[word] = []

            # if the previous word has been set
            if len(prev_word) > 0:
                # add the current word to the previous words list
                cache[prev_word].append(word)
        prev_word = word
    keys = list(cache.keys())

    # sort list randomly
    random.shuffle(keys)

    # intialize sentence as a list of words 
    sentence = []

    # initialize word count
    word_count = 0

    # initialize new_word for next word
    new_word = ""
    for word in keys: 
        # if word_count is 0 and word[0].isupper():
        if word_count is 0 and word[0]:
            
            # add it to the sentence
            sentence.append(f"{word}")
            # word_count + 1
            word_count += 1
            # make a word in the cache list the new word
            new_word = random.choice(cache[word])
            #exit
            break
    # loop until the next word has no values(empty)
    while cache[new_word] != []:
            # pick a random word from the value                
            new_word = random.choice(cache[new_word])
            # add it to the sentence
            sentence.append(f"{new_word}")
            word_count += 1
            # if the last character in the added word is one of these..
            if new_word[-1] in list(["." ,"?" ,"!"]):
                return (" ".join(sentence), word_count)

# TODO: construct 5 random sentences
# Your code here

print(markov(words))
print(markov(words))
print(markov(words))
print(markov(words))
print(markov(words))
print(markov(words))