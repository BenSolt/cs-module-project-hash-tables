ciphertext = open("./applications/book_cipher/book.txt", "r")
code = open("./applications/book_cipher/code.txt", "r")


ciphertext2 = open("./applications/book_cipher/textfile.txt", "r")
code2 = open("./applications/book_cipher/code2.txt", "r")


import string

#Open the cipher text and find the appropriate line

# for line in code:
    
#     linecode = line.split()[0] + ":" + line.split()[1]
#     wordcode = line.split()[2]

#     for line in ciphertext:
#         if linecode in line:
#             print(line.split()[int(wordcode)])
        
# code.close()
# ciphertext.close()

letter_count = 0
word_count = 0

for line in code2: # code 2 = code2.txt
    
    linecode = line.split()[0] + ":" + line.split()[1]
    wordcode = line.split()[1] 

    print("line:word",linecode)  
    # print('word:', wordcode)  
    

    for line in ciphertext2: # ciphertext2 = textfile.txt
        letter_count += 1

        
        # print("int:",line.split()[int(wordcode)])
        #print(line.split()[int(linecode)])

        # if letter_count == 6:
        #     print(f"LINE {letter_count}: " +"WORD 10:", line.split()[9]) #9
        # elif letter_count == 8:
        #     print(f"LINE {letter_count}: " + "WORD 2:", line.split()[1])    
        # elif letter_count == 3:
        #     print(f"LINE {letter_count}: " + "WORD 4:", line.split()[3])     
        # elif letter_count == 4:
        #     print(f"LINE {letter_count}: " + "WORD 4:", line.split()[3])  
          
        # CODE TEXT
        #6:10 8:2 4:4 3:4

        # DECODED
        #find the Dark Men    

        # print(f"line {letter_count}:",line.split()[0] +" " + line.split()[1])

        if linecode in line:
            
            print(line.split()[int(wordcode)])
            
            # print(line.split()) #<-- prints each word in ' '
            # print([int(wordcode)]) # <-- prints the index
        
code2.close()
ciphertext2.close()


    # if linecode in line:
        #     letter_count += 1
        #     if line in freq:
        #         freq[line] += 1
        #     else:
        #         freq[line] = 1
