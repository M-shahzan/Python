sentence = input("enter a sentence:")
wordList = sentence.split()
revSentence = ""
for i in wordList:
    revSentence += i[::-1]+" "
print(revSentence)