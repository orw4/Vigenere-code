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

# encryptes using visenere code
def encrVisenere(text, nums):
    ind = 0
    encrypted = ""
    for i in text:
        encrypted += shift(i, nums[ind])
        #if i in letters:
        ind = (ind + 1) % len(nums)
    return (encrypted)

# splits the text to subtexts and decryptes each text independently using caesar
def splitDecr(text,length):
    splited = []
    for i in range(length):
        splited.append("")
    ind = 0
    for i in range(len(text)):
        splited[ind] += text[i]
        ind = (ind + 1) % length
    for i in range(length):
        splited[i] = decrCaesar(splited[i])
    return splited

# merges the decrypted subtext into 1 text
def mergeDecr(text, length):
    splited = splitDecr(text, length)
    decrypted = ""
    for i in range(len(splited[0])):
        for j in range(len(splited)):
            if i < len(splited[j]):
                decrypted += splited[j][i]
    return decrypted

def decrVisenere(text):
    error = 1000000
    length = 0
    for i in range(8):
        currText = mergeDecr(text, i + 1)
        currFreq = findFrequency(currText)
        currErr = sum(shiftError(currFreq,0))
        if currErr < error:
            length = i + 1
            error = currErr
            rightText = currText
    return rightText

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
frequency = [8.2,1.5,2.8,4.3,13,2.2,2,6.1,7,0.15,0.77,4,2.4,6.7,7.5,1.9,0.095,6,6.3,9.1,2.8,0.98,2.4,0.15,2,0.074]
