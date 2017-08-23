# Program for finding vowel or not
vowels = 'aeiou'
# Infinite Loop
while True:
    v = input("Enter a letter: ")
    if v in vowels:
        print(v, "is a vowel ")
        break
    print("This is not a vowel, Enter another letter")
print("End of program")

