from collections import Counter
import re
with open('text files/text.txt','r') as text:
    data = text.read().lower()
    words = re.findall(r"\b[\w'-]+\b",data)
    wordfreq = Counter(words)
    w = wordfreq.most_common(1)
    print (f"most frequent word is '{w[0][0]}' appeared {w[0][1]} times")
    print("no of words",len(words))
    print("no of characters : ",len(re.sub(r"[^\w'-]","",data)))
    print("no of sentences:",data.count("."))
    wordlength = 0
    for word in words:
        wordlength += len(word)
    print("average word length : ",wordlength/len(words))

