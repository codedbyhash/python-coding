n = int(input("Enter the number: "))

if n == 0:
    print(n,"is zero.")
elif (n > 0):
    print(n,"is positive.")
else:
    print(n,"is negative.")

for i in range(1, 11):
    print(n,"x",i,"=",n*i)

while n > 0:
    print(n)
    n -= 1 