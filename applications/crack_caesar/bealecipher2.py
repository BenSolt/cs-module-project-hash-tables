
import string

with open("./applications/crack_caesar/bealecipher2.txt") as code:
    code = code.read()

    print(code)

with open("./applications/crack_caesar/declaration.txt") as declar:
    declar = declar.read()

with open("./applications/crack_caesar/declaration2.txt") as declar2:
    declar2 = declar2.read()    

#     print("\n",declar) #  <-- prints out entire Declaration Independence

    # numwords = len(declar)
    # print("\nNumber of words in Declaration Independence:", numwords)


# with open("./applications/crack_caesar/dectest.txt") as declar2:
#     declar2 = declar2.read()

#     print("\n",declar2) #  <-- prints out entire Declaration Independence



# def declarA(s):
#     word_counter = 0
    

#     s = " ".join(s.split()).lower().split(" ")  

#     for word in s:
#         word_counter += 1
#         word = word.strip('":;,.-+=/|[]}{()*^&')
#         print(f"{word_counter}", word)
        
        
# if __name__ == "__main__":
#     print(declarA(f"{declar}"))


# PART TWO

# def declarB(s):
#     word_counter = 0
#     #word_counter = code 

#     s = " ".join(s.split()).lower().split(" ")  

#     for word in s:
#         word_counter += 1
#         word = word.strip('":;,.-+=/|[]}{()*^&')
#         print(f"{word_counter}", word)
        
        
# if __name__ == "__main__":
#     print(declarB(f"{declar2}"))  




