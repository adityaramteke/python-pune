# Factorial of a nunber
a = int(input("Enter the number: ")) #Read number
fact = 1
for i in range (1, a+1):
    fact = fact*i
print("Factorial of ", a, "is ", fact)
