# Visenere code
# 17/9/2022

def shift(l, num):
    if l in letters:
        i = letters.index(l)
        i = (i + num) % len(letters)
        l = letters[i]
    return(l)

def encrCaesar(message, num):
    encrypted = ""
    for i in message:
        encrypted += shift(i,num)
    return(encrypted)

def decrCaesar(message,num):
    

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#print(encrCaesar("hello!",1))
