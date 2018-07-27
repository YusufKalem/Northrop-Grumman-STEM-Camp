#Streams of Strings
#By Yusuf Kalem
import random
import os
os.system("color 0a")
wordlist = ['Hacker', 'Man']
wordlist.append(input("Enter a word"))
while True:
    num=random.randint(33,254)
    index = random.randint(0, len(wordlist)-1)
    print(chr(num)+ wordlist[index],end="")
    print(chr(num),end="")
