string=input("Enter a string:")

first=""
second=""

n=int(input("Enter the number of copies:"))

for i in range(len(string)):
    first=string[0]
    second=string[1]

print(first*n)
print(second*n)