encrypted = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = input().split(" ")  # given first array
length = int(input())
i = 0

while i < length:
    line = input()
    encrypted.append(line)
    i += 1

dictionary = dict((el, []) for el in encrypted)

i = 0
result = []
while i < len(encrypted):
    for word in text:
        if len(encrypted[i]) == len(word):
            #print(encrypted[i], "text  ", word)
            flag = True
            if alphabet.index(encrypted[i][0]) >= alphabet.index(word[0]):
                rotN = alphabet.index(encrypted[i][0]) - alphabet.index(word[0])
            else:
                rotN = alphabet.index(word[0]) - alphabet.index(encrypted[i][0])
            k = 0
            for char in encrypted[i]:
                #print("here", alphabet.index(char) - alphabet.index(word[k]))
                if alphabet.index(char) >= alphabet.index(word[k]):
                    iter_var = alphabet.index(char) - alphabet.index(word[k])
                else:
                    iter_var = alphabet.index(word[k]) - alphabet.index(char)
                if iter_var != rotN:
                    flag = False
                    break
                k += 1
            if flag:
                #print("put word -----------", word)
                result.append(word)
                dictionary[encrypted[i]].append(rotN)
    i += 1
listToStr = '\n'.join([str(elem) for elem in result])
print(listToStr)


