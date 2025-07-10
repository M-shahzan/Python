n1= int(input("enter the length of list 1:"))
print("enter the elements:")
l1=[]
for i in range(n1):
    val = int(input())
    l1.append(val)

n2 = int(input("enter the length of list 2:"))
print("enter the elements:")
l2 = []
for i in range(n2):
    val = int(input())
    l2.append(val)    

lmerged = l1+l2
print(sorted(lmerged))