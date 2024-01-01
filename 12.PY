a=int(input("Enter the First Number"))
b=int(input("Enter the Second Number"))

userinput=input("Enter the sign,+,-,*,/,%,**")
print("Number 1 =",a,"Number 2 =",b)

if userinput == "+" :
    print("The sum is :",a+b)
elif userinput=="-":
    print("The subtraction  is :",a-b)
elif userinput=="*":
    print("The multiplication is :",a*b)
elif userinput=="/":
    print("The division is :",a/b)
elif userinput=="%":
    print("The modulus is :",a%b)
elif userinput=="**":
    print("The Exponent is :",a**b)
if a<b:
    print(b,"is greater than ",a)
elif a>b:
    print(a,"is greater than ",b)
elif a==b:
        print(a,"is equal to ",b)
elif a!=b:
         print(a,"is not equal to ",b)
if a<=b:
    print(b,"is greater than equal to",a)
elif a>=b:
    print(a,"is greater than equal to ",b)      

    