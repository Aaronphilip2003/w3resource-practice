# string=input("Enter a string:")
#
# copies=int(input("Enter how many copies of the string do you want:"))
#
# print(string*copies)

# Im trying to make it using a funnction

def copies(str,n):
    result=""

    for i in range(n):
        result=result+str

    return result

print(copies("Aaron",5))

