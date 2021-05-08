input_string = input('Enter elements of a list separated by space:')
user_list = input_string.split()
count=0
# print('list: ', user_list)

for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
    # print(user_list[i])
    if user_list[i]==4:
        count=count+1

print("The number of '4' in the list is:", count)