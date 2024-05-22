#write a program to find the sum of digits of a given number'
def sums(n):
    return sum(int(digit) for digit in str(n))

num = int(input("Enter a number: "))
print("Sum of digits is:", sums(num))
