
# import math

# print("Hello World")
# print(8+4)
# this is singe line comment

''' this is multiline commnent 
'''
'''
print(math.gcd(3,6))
print(math.factorial(5))
'''
'''
 age=5

if(age>13):
    print("Welcome")
else:
    print("Hey Kid")

print("Hi")
'''

# a=10
# b="Ashu"
# c=3

# print(a+c)
# print(a-c)
# print(a*c)
# print(a/c)

# 1. variable should start an Underscore Or with letter.
# 2. variable cannot start with number.
# 3. It can only contain alpha numeric (A-Z,a-z,0-9) characters.
# 4. variables names are case senstive. 

# print(type(a))
# print(type(b))

# e=int("51") 
# print(type(e))
# print(e+8)

# name="Ashu is good boy"
# name='Ashu'
# name='''Ashu
# is a good boy'''

# name="Ashu, samar"
# print(name[2])
# print(name[2:4]) This is called slicing
# print(name)
# print(name.strip()) remove spaces
# print(len(name))
# print(name.lower())
# print(name.upper())
# var=name.replace("As","n")
# print(var)
# print(name.replace(", ", "\n"))

# str1="My Name is "
# str2="Dashminder"
# print(str1+str2)

'''
name1="Ashu"
name2="Samar"

print("This is {1} and He is good boy named {0}".format(name1,name2))
print(f"This is {name2} and he is good named {name1}")

'''
# 1. Exponentiation operator **
# 2. Floor division operator //
# 3. Modulo operator %

'''
a=5
b=2
c=a**b
print(c)
print(a//b)
print(a%b)
'''

# Collections in Python
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

'''
 1. List
ls=[19,3,5,8,11,15,25]
# print(ls)
# print(ls[2])
# print(ls[2:4])
ls[2]=48
print(ls)
# ls.append(100)
# ls.insert(4,21)
# ls.remove(19)
# ls.pop() last element remove
# del ls[3]
# ls.clear() empty list
print(ls)
'''

# Tuple
'''
a=("Ashu", "Samar")
# var=type(a)
# print(var)
print(a)
# a[0]="Samy" cannot change
a=list(a)
a[0]="Sunny"
print(a)
'''

# Set
'''
s1={4,3,7,3,3,9,9,9,7,7,4,4,4}
print(s1)
# print(type(s1))
# s1.add(85)
# s1.update([7,8,8,10,10,2,2,2,2,2,2])
# print(len(s1))
# s1.remove(66)
# s1.discard(66)
# s1.clear()
print(s1)
'''
'''
# Dictionary
dict1={"Name":"Ashu",
        "Class":"8th",
        "Country":"India"
}
print(dict1)
dict1["Country"]="US"
# dict1.pop("Class")
# print(dict1["Country"])
# dict1.update({"Hours":8})
print(dict1)

'''
'''
age=int(input("Enter Age: "))
# print(type(age))

if(age>18):
    print("you can drive a car")
elif(age==18):
    print("you are an awesome teen")
else:
    print("you cannot drive")
'''

# Loops

# for i in range(0,10):
#     print(i)

# for i in reversed(range(5+1)):
#     print(i, end= " ")

# for i in range(5,0,-1):
#     print(i, end= " ")

'''
print("\n")    
li=[45, 10, "Hello"]
for i in li:
    print(i)
'''
'''
i=5
while(i>0):
    print(i)
    i=i-1
'''
# Functions

# def greet():
#     print("Good Morning Sir")

# greet()

# def Sum(a,b):
#     print(a+b)

# Sum(6,7)
'''
def even_odd(n):

    if(n%2==0):
        return True
    else:
        return False

N=int(input("Enter a Number: "))

if(even_odd(N)):
    print(N,"is Even")
else:
    print(N,"is Odd")

'''
'''
class Employee:

    def get_data(self,gname,gsalary):
        self.name=gname
        self.salary=gsalary

    def show_data(self):
        print("Name:",self.name,"\nSalary:",self.salary)


e1=Employee()
e1.get_data("John Smith",45000.00)
e1.show_data()
'''

class Employee:

    def __init__(self,gname,gsalary):
        self.name=gname
        self.salary=gsalary


e1=Employee("John Smith",45000.00)
print(e1.name,"\n",e1.salary)



