n = int(input("Enter nth number: "))
sum=0
for i in range(1,n+1):
    if(i>0):
        print(i)
        sum=sum+i
print("Sum of",n,"natural numbers is:",sum)