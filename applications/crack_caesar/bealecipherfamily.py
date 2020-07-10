
#import string

#FAMILY/RELATIVES

with open("./applications/crack_caesar/bealecipherfamily.txt") as family:
    family = family.read()


def cipher(s):
    if len(s) < 1:
        return {}
    else:
        word_counter = {}

    s = " ".join(s.split()).lower().split(" ")
    
    for word in s:
        
        word = word.strip(',[,]')
           
        if word_counter.get(f"{word}"):
            word_counter[word] += 1
           
        else: 
            word_counter[word] = 1
        
    words = list(word_counter.items())

    words.sort(key=(lambda e: (-e[-1], e[0])))
    for word, a in words:
        word = word + " " * (35-len(word)) + "#" * a
        print(word)

if __name__ == "__main__":
    print(cipher(""))
    print(cipher(f"{family}"))