# Sum of all elements in list
eg_list = input("Enter a list: ") # Read the List from the keyboard
list1 = map(int, eg_list.split()) # Convert the items in it to integer
sum1 = 0 # initialize sum to 0
for i in list1: sum1 +=i
print("The sum of all items in list", eg_list, "is ", sum1)


    
