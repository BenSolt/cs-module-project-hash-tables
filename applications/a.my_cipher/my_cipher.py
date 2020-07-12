with open("./applications/a.my_cipher/code.txt") as small_code:
    small_code = small_code.read()
# print(small_code)

with open("./applications/a.my_cipher/text.txt") as declaration:
    declaration = declaration.read()

book = declaration.split()
#print(book)

with open("./applications/a.my_cipher/text_bible_verse.txt") as declaration:
    declaration = declaration.read()


#=========SMALL CODE ================================
code_array_small = small_code.split()
plain_text2 = ""

for i in code_array_small:
    #print(i)
    #w= book[int(115)
    word = book[int(i) - 1]
    letter = word[0]

    plain_text2 += letter
    
print("\n" + plain_text2)

# I have buried treasure