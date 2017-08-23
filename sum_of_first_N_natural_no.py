# Program to find the sum of first N natural numbers
N = int(input("Enter the limit: "))
sum = 0
i = 1
while(i <= N):
    sum = sum+i;
    i = i+1
print("sum of first", N, "natural numbers is ", sum)

