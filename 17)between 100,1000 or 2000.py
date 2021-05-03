number=int(input("Enter a number:"))

if number<100:
    print(f"{number} is lesser than 100")

elif number>=100 and number<1000 :
    print(f"{number} is between 100 and 1000")

elif number>=1000 and number<2000:
    print(f"{number} is between 1000 and 2000")

else:
    print(f"{number} is greater than 2000")