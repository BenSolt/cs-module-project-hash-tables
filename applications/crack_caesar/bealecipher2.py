
import string

with open("./applications/crack_caesar/bealecipher2.txt") as code:
    code = code.read()

    #print(code)

with open("./applications/crack_caesar/declaration.txt") as declar:
    declar = declar.read()

#     print("\n",declar) #  <-- prints out entire Declaration Independence

    # numwords = len(declar)
    # print("\nNumber of words in Declaration Independence:", numwords)


# with open("./applications/crack_caesar/dectest.txt") as declar2:
#     declar2 = declar2.read()

#     print("\n",declar2) #  <-- prints out entire Declaration Independence


def declaration(s):
    word_counter = 0
      
    #word = " ".join(s.split()).lower().split(" ")  
    word = " ".join(s.split()).lower().split(" ")  

    for numwords2 in word:
        word_counter += 1
        print(f"{word_counter}", numwords2)
        #word = word.strip('":;,.-+=/|[]}{()*^&')
        

if __name__ == "__main__":
    print(declaration(f"{declar}"))
