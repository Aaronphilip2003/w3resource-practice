number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
number3=int(input("Enter the third number:"))

if number1==number2 and number1==number3:
    sum=(number1+number2+number3)*3

else:
    sum=number1+number2+number3

print(sum)