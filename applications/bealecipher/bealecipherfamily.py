
#import string

#FAMILY/RELATIVES

# Declaration Virginia
with open("./applications/crack_caesar/declaration_virginia.txt") as declaration_virgina:
    declaration_virgina = declaration_virgina.read()
#print(declaration_virgina)

# Declaration of Independence
with open("./applications/crack_caesar/declaration.txt") as declaration:
    declaration = declaration.read()
# print(declaration)

# Family Cipher Code
with open("./applications/crack_caesar/bealecipherfamily.txt") as family_code:
    family_code = family_code.read()

# LARGEST NUMBER: 975

declar_virginia = declaration_virgina.split()
declaration= declaration.split()
code_array = family_code.split()
plain_text = ""
counter = 0

for i in code_array:
    
    word = declaration[int(i) - 1]
    letter = word[0] #<-- first letter of word
  

    plain_text += letter

#====DECODED CIPHER========
#print("\n" + plain_text)



#NUMBER TIMES NUMBERS APPEAR

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
    print(cipher(f"{family_code}"))