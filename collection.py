# List
# ls=[10,20,30,4,8,11]
# print(ls)

'''
ls=[]
n=int(input("Enter size: "))

for i in range(0,n):
    k=int(input())
    ls.append(k)

for i in range(0,n):
    print(ls[i],end=" ")

'''
'''
print("\n")
ls.append(25)
print(ls)
ls.insert(2,45)
print(ls)

'''
# Tuple

from turtle import clear


tu=(10,2,4,9,23,67)

# print(t[2:4]) slicing

# t[2]=34 Not allowed
tu=list(tu)
tu[2]=34
print(tu) # Convert to List

tu=tuple(tu)
print(tu) #Convert to Tuple

'''
t=(12,34)
print(t*3)

'''


