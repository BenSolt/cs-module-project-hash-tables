#=========ENTIRE CODE========================
with open("./applications/crack_caesar/bealecipher2.txt") as total_code:
    total_code = total_code.read()
# print(total_code)

#===========SMALL CODE======================
with open("./applications/crack_caesar/bealecipher2small.txt") as small_code:
    small_code = small_code.read()
# print(small_code)

with open("./applications/crack_caesar/declaration.txt") as declaration:
    declaration = declaration.read()

# print(declaration)

book = declaration.split()
#print(book)

#ENTIRE CODE
code_array = total_code.split()
plain_text = ""


for i in code_array:
    #print(i)
    word = book[int(i) - 1]
    letter = word[0]

    plain_text += letter

#print("\n" + plain_text)


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
print(book[int(115) - 1])
print(book[int(73) - 1])








