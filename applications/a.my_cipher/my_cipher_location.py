with open("./applications/a.my_cipher/text_bible_verse.txt") as text2:
    text2 = text2.read()
book1 = text2.split()

with open("./applications/a.my_cipher/codelocation.txt") as codelocation:
    codelocation = codelocation.read()
print("\n" "LOCATION")
print(codelocation)

#CODE VERSE
code_array = codelocation.split()
plain_text1 = ""
counter = 0
for i in code_array:

    word = book1[int(i) - 1]
    letter = word[0]
    plain_text1 += letter
    counter += 1
  
print(plain_text1)



for i in book1:
    counter += 1
    print(counter, i)


#two miles north west of New Life Dresher Church.
# It is located in Mondauk Manor Park,
# north east of the damn, just inside the tree line. Below
# the marked X
#====================================================
with open("./applications/a.my_cipher/text_declaration.txt") as text_declar:
    text_declar = text_declar.read()
book2 = text_declar.split()

with open("./applications/a.my_cipher/codelocation2.txt") as codelocation2:
    codelocation2 = codelocation2.read()
print("\n" "LOCATION")
#print(codelocation2)


code_array = codelocation2.split()
plain_text2 = ""
counter = 0
for i in code_array:

    word = book2[int(i) - 1]
    letter = word[0]
    plain_text2 += letter
    counter += 1
  
#print(plain_text2)

#assign each word a number

counter = 0
for i in book2:
    counter += 1
    #print(counter, i)

#CODE DECLARATION
# the treasure is buried 
# 32 308 201 -126 3 53 7 24 35 236 110 33 -126 2 35 -126 77 94 59 67 188 208

# about two miles north west of New
# 36 9 12 313 14 -126 16 40 46 -126 58 2 155 7 62 -126 10 5 53 26 20
# 338 7 38 32 -126 31 11 126 44 33 40 

# Life Dresher Church. 
# 126- L100 67 11 33 126- D250 53 49 35 6 188 110 126- 91 73 248 246 192 73

#It is located in Mondauk Manor Park,
#126 2 14 126 155 158 122 102 69 49 15 126 8 153 126 115 43 10 15 25 236 126 115 302
#126 119 45 53
# north east of the damn, just inside the tree line. Below
# the marked X

