import re
from collections import Counter

with open('text files/logfile.txt','r') as logfile:
    contents = logfile.read()
    timeStamp = re.findall(r'\[(.*?)\]',contents)
    Count = Counter(re.findall(r'\bERROR|WARNING|INFO|DEBUG\b',contents))
    
    print("Time Stamps:")
    for i in timeStamp:
        print(i )

    print("\nCount :")
    for key,value in Count.items():
        print(f"{key} : {value}" )

