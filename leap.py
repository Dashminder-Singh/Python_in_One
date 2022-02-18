year=int(input("Enter a year: "))

if((year%100==0 & year%400==0) | (year%4==0)):
    print("Leap Year")
else:
    print("Not Leap Year")