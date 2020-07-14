from collections import Counter

#LOCATION LOCATION

#Declaation Independence
with open("./applications/crack_caesar/declaration.txt") as declaration:    
    declaration = declaration.read()
    
    book1 = declaration.split()

# Declaration multiply by 2
with open("./applications/crack_caesar/declar_times3.txt") as declaration:    
    declaration = declaration.read()
    
    book2 = declaration.split()


with open("./applications/crack_caesar/bealecipherlocation.txt") as codelocation:    
    codelocation = codelocation.read()
    #print(codelocation)
    

# BIGGEST NUMBER: 2906

code_array = codelocation.split()
plain_text1 = ""
counter = 0
num1 = "1701"
num2 = "1629"


for i in code_array:

    word = book2[int(i) - 1]
    #word = book1[int(i) - 1]
    letter = word[0]
    plain_text1 += letter
    counter += 1
print("LOCATION")
print(plain_text1)

    
#     if num1 == i: # 1701
#         i = "0"
#         #print(f"\033[1;34mNUMBER:\033[0m {i}")
#     if num2 == i:
#         i = "0"
#         print(f"\033[1;34mNUMBER:\033[0m {i}")
#     else:
#         print('NUM:',i)
        
        



#NUMBER OF WORDS
# for i in book1:
#     #print(i)
#     counter += 1
#     print(counter, i)



# def cipher2(s):
#     if len(s) < 1:
#         return {}
#     else:
#         word_counter = {}

#     s = " ".join(s.split()).lower().split(" ")
    
#     for word in s:
        
#         word = word.strip(',[,]')
           
#         if word_counter.get(f"{word}"):
#             word_counter[word] += 1
           
#         else: 
#             word_counter[word] = 1
        
#     words = list(word_counter.items())

#     words.sort(key=(lambda e: (-e[-1], e[0])))
#     for word, a in words:
#         word = word + " " * (35-len(word)) + "#" * a
#         print(word)

# if __name__ == "__main__":
#     print(cipher2(""))
#     print(cipher2(f"{codelocation}"))




