#write a program to find the factorial of a nummber
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
 number = int(input("Enter a number to calculate its factorial: "))
print("Factorial of", number, "is", factorial(number))
