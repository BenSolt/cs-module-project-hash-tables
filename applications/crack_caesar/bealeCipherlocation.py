from collections import Counter

#LOCATION LOCATION

with open("./applications/crack_caesar/bealecipherlocation.txt") as beale:    
    beale = beale.read()



# nums = [71,194,38,1701,89,76,11,83,1629,48,94,63,132,16,111,95,84,341,

# numbers = Counter(nums)

# code = numbers.most_common() 
# print(code)


def cipher2(s):
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
    print(cipher2(""))
    print(cipher2(f"{beale}"))



