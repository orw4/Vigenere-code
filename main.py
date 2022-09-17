# Visenere code
# 17/9/2022

# changes letter l using num shifts
def shift(l, num):
    if l in letters:
        i = letters.index(l)
        i = (i + num) % len(letters)
        l = letters[i]
    return(l)

# encryptes using caesar code
def encrCaesar(text, num):
    encrypted = ""
    for i in text:
        encrypted += shift(i,num)
    return(encrypted)

# decryptes caesar code
def decrCaesar(text):
    num = findShift(findFrequency(text))
    return encrCaesar(text, -num)

# returns a list of letters frequency in the text
def findFrequency(text):
    textFrequency = []
    for i in letters:
        textFrequency.append(text.count(i) * 100 / len(text))
    return(textFrequency)

# shifts the list of letter frequencies by num and finds the errors in the list
def shiftError(textFrequency,num):
    error = textFrequency.copy()
    for i in range(len(textFrequency)):
        error[(i - num) % len(textFrequency)] = abs(textFrequency[i] - frequency[(i - num) % len(textFrequency)])
    return error

# finds the right shift
def findShift(textFrequency):
    shift = 0
    error = 100000
    for i in range(len(frequency)):
        newError = sum(shiftError(textFrequency,i))
        if newError < error:
            shift = i
            error = newError
    return shift

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
frequency = [8.2,1.5,2.8,4.3,13,2.2,2,6.1,7,0.15,0.77,4,2.4,6.7,7.5,1.9,0.095,6,6.3,9.1,2.8,0.98,2.4,0.15,2,0.074]
