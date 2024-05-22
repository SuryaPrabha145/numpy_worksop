#write a program to find if the given number is prime no or not
 n = int(input("Enter number: ")); print("Prime" if (n%2 != 0 and n%n == 0) or n == 2 else "Not Prime")
