def sum_of_n(n):
    if(n==1):
        return n
    return sum_of_n(n-1)+n


N=int(input("Enter a number: "))
res=sum_of_n(N)
print(res)