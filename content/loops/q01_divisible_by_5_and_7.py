n=int(input("Enter the number: "))
for n in range (1000,3001):
    if (n%7==0) and (n%5==0):
        print(n, end=",")
    else:
        continue
