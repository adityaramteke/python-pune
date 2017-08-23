# Count the nuber of vowels
s = input("Enter a String:") #Read the String
count = 0
for i in s:
    if i in 'aeiouAEIOU':
        count += 1
print("The number of vowels in ", s, "is ", count)

