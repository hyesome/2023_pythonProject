def printCorrectWords(correct, word, alphabet):
    dap = list(correct) # ['_','_','_','_','_','_','_','_']
    for i in range(len(word)):
        if word[i] == alphabet:
            dap[i] = alphabet
    dap = ''.join(dap)
    return dap

word = "testtest"
correct = "_"*len(word)

while True:
    alphabet = input("input >>>>")
    correct = printCorrectWords(correct, word, alphabet)
    print(correct)