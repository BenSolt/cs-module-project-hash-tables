#=========ENTIRE CODE========================


with open("./applications/crack_caesar/declaration.txt") as declaration:
    declaration = declaration.read()
#print(declaration)


with open("./applications/crack_caesar/bealecipher2.txt") as decoded_code:
    decoded_code = decoded_code.read()
#print(decoded_code)


book1 = declaration.split()
#print(book)

# LARGEST NUMBER: 1005

#ENTIRE CODE
code_array = decoded_code.split()
plain_text = ""
counter = 0

for i in code_array:
    #print(i)
    word = book1[int(i) - 1]
    letter = word[0] #<-- first letter of word
    

    plain_text += letter

print("\n" + plain_text)



#DECODED CIPHER  
#print("\n" + plain_text)


# for i in book1:
#     counter += 1
#     print(counter, i)


#NUMBER OF NUMBERS in decoded message
# for i in code_array:
#     counter += 1
#     print(counter,i)


# #multiply by 2
# a = 762 <-- number of words in decoded cipher
# b = 2  
# print(a * b) 








# NUMBER OF TIMES NUMBERS APPEAR

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
#     print(cipher2(f"{decoded_code}"))

