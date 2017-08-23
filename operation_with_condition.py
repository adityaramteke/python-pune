# Demo of loop with condition at the bottom
choice = 0
a, b = 6, 3
while choice !=5:
    print("Menu")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1: print("Sum =", (a+b))
    if choice == 2: print("Difference =", (a-b))
    if choice == 3: print("Product =", (a*b))
    if choice == 4: print("Quotient=", (a/b))
    if choice == 5: break;
print("End of Program ")

