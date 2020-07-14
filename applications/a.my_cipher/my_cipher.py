with open("./applications/a.my_cipher/code.txt") as small_code:
    small_code = small_code.read()
# print(small_code)

#text d
with open("./applications/a.my_cipher/text_declaration.txt") as declaration:
    declaration = declaration.read()

book = declaration.split()
#print(book)


#=======text bibl====================================
with open("./applications/a.my_cipher/text_bible_verse.txt") as text2:
    text2 = text2.read()

book2 = text2.split()


with open("./applications/a.my_cipher/code2.txt") as code2:
    code2 = code2.read()
print("\n" "CODE GENERAL")
print(code2)


#=========CODE GENERAL ================================
code_array2 = code2.split()
plain_text2 = ""
counter = 0
for i in code_array2:

    word = book2[int(i) - 1]
    letter = word[0]
    plain_text2 += letter
    counter += 1

#ANSWER
print(plain_text2)


#i-have-buried-treasure-nearby--code1-tells-the-location

#=======================================
# GIVEN CLUE - explains that the location is in code 2

# the treasure that you seek 
# will be yours to keep 
# if you solve the code/cipher


#I have deposited in the county of Montgomery,PA
# about 2 miles from New Life Dresher Church, a treasure
# buried under ground.

# The document labeled Location, describes the exact 
# location of the treasure.


#===================================

counter = 0
for i in book2:
    counter += 1
    print(counter, i)
