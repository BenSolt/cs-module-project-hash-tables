ciphertext = open("./applications/book_cipher/book.txt", "r")
code = open("./applications/book_cipher/code.txt", "r")


plain_text = open("./applications/book_cipher/textfile.txt", "r")
code2 = open("./applications/book_cipher/codelotr.txt", "r")


import string

line_count = 0
word_count = 0
book = []
cipher_text = ""


for line in plain_text: # ciphertext2 = textfile.txt

    words = line.split()
    textline_index = line.split()[0]
    textword_index = line.split()[2]

    book.append(words)

        # index_10 = word.split()[5] + ":" + word.split()[9]

    # print("\033[1;34mEntire length of text line:\033[0m", words) # <-- entire length of line
    # print("\033[1;35mLine Index:\033[0m", textline_index) # <-- first index, 0
    # print("\033[1;32mWord Index:\033[0m", textword_index)


for line in code2: # code 2 = code2.txt
    
    linecode = line.split()[0] + ":" + line.split()[1]
    
    # print("line:word",linecode) 
    
    code_num = line.split()
    line_index = int(line.split()[0]) - 1
    word_index = int(line.split()[1]) - 1
    code_word = book[line_index][word_index]

    #cipher_text += (" " + code_word)
    
    if word_count == 0:
        
        cipher_text += (code_word)
    else: 
        cipher_text += (" " + code_word)

    word_count += 1



    # print("\033[1;34mEntire length of text line:\033[0m", code_num)
    # print("\033[1;35mLine Index:\033[0m", line_index)
    # print("\033[1;32mWord Index:\033[0m", word_index)

    # print("\033[1;34mEntire length of text line:\033[0m", words) # <-- entire length of line
    # print("\033[1;35mCode word:\033[0m", code_word) # <-- first index, 0

print("\n" + cipher_text)

 
code2.close()
plain_text.close()
