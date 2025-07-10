import re
with open('text files/emailinput.txt','r') as inFile:
    contents = inFile.read()
    emails = re.findall(r'\b\w+@\w+.com\b',contents)
    print(emails)

with open('text files/emailoutput.txt','w') as outfile:
    for email in emails:
        outfile.writelines(email+"\n")
