n=int(input("Enter a number: "))

for i in range(0,n):
    k=0
    while(k!=n-i):
        print(end=" ")
        k=k+1
    for j in range(0,i+1):
        print("*",end="")
    print("\n")