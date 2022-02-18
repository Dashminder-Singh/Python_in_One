# print("Hello World")

# for i in range(10):
#     print(i,end=" ")

'''
num=int(input("Enter a number: "))
highest=0
while(num!=0):
    r=num%10
    if(r>highest):
        highest=r
    
    num=num/10

print("Highest Number is ",int(highest))

'''
'''
N=int(input("Enter a number: "))

for i in range(0,10):
    print(N,"X",i+1,"=",N*(i+1))
'''
'''
N=int(input("Enter a number: "))

for i in range(N,0,-1):
    print(2*i)
'''
from tokenize import Double


fact=1
N=int(input("Enter a number: "))

for i in range(N,0,-1):
    fact=fact*i

print(N,"!=",fact)