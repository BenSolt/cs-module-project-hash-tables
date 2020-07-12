import string 
   
# A list containing all characters 
all_letters= string.ascii_letters 

"""  
create a dictionary to store the substitution  
for the given alphabet in the plain text  
based on the key 
"""

plain_txt= "I am studying Data Encryption"
coded_txt = 'M eq wxyhCmrk Hexe IrgvCtxmsr'
cipher_txt=[] 

# ======= ENCODED TEXT = 'M eq wxyhCmrk Hexe IrgvCtxmsr'===================
# =========================================================================

dict1 = {} 
key = 4
   
for i in range(len(all_letters)): 
    dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)] 
  
for char in plain_txt: 
    if char in all_letters: 
        temp = dict1[char] 
        cipher_txt.append(temp) 
    else: 
        temp =char 
        cipher_txt.append(temp) 
          
cipher_txt= "".join(cipher_txt) 
print("\033[1;34mCipher Text is:\033[0m",cipher_txt) 


# ===== DECODED TEXT = "I am studying Data Encryption" ==============
# ===================================================================

dict2 = {} 
key2 = -4

for i in range(len(all_letters)): 
    dict2[all_letters[i]] = all_letters[(i+key2)%len(all_letters)] 

cipher_txt=[] 
for char in coded_txt: 
    if char in all_letters: 
        temp = dict2[char] 
        cipher_txt.append(temp) 
    else: 
        temp =char 
        cipher_txt.append(temp) 
          
cipher_txt= "".join(cipher_txt) 
print("\033[1;34mDecoded Text is:\033[0m",cipher_txt) 

# 3 ===============================================================
# ================================================================

# Genesis 1:1
plain_txt2 = 'I am studying Data Encryption'

dict3 = {} 
key3 = 3

for i in range(len(all_letters)): 
    dict3[all_letters[i]] = all_letters[(i+key3)%len(all_letters)] 

cipher_txt=[] 
for char in plain_txt2: 
    if char in all_letters: 
        temp = dict3[char] 
        cipher_txt.append(temp) 
    else: 
        temp =char 
        cipher_txt.append(temp) 
          
cipher_txt= "".join(cipher_txt) 
print("\033[1;34mTest:\033[0m",cipher_txt) 


#======== SPLIT SENTENCE===============================================
# =====================================================================

textfile = open("./applications/asub_cipher/subsitut.txt", "r")

dict4 = {} 
key4 = 3

for line in textfile: 

    print("\033[1;34mEntire length of line:\033[0m",line.split()) # <-- entire length of line
    print("\033[1;34mIndex 0:\033[0m",line.split()[0]) # <-- first index, 0

#     print(line.split()[int(wordcode)])

# =================================================================
# =================================================================

all_letters= string.ascii_letters 
cipher_txt = []
plain_txt2 = 'I am studying Data Encryption'
textfile2 = open("./applications/asub_cipher/subsitut.txt", "r")

for i in range(len(all_letters)): 
    dict4[all_letters[i]] = all_letters[(i+key4)%len(all_letters)] 

cipher_txt=[] 
#for char in plain_txt2: 
for char in textfile2: 
    if char in all_letters: 
        temp = dict4[char] 
        cipher_txt.append(temp) 
    else: 
        temp =char 
        cipher_txt.append(temp) 
          
cipher_txt= "".join(cipher_txt) 
print("\033[1;34mTest:\033[0m",cipher_txt) 