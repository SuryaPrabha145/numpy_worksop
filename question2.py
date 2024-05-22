# find if the given number is a palindrome or not?
def is_palindrome(number):
  
    num_str = str(number)
    
    
    reversed_num_str = num_str[::-1]
   
    if num_str == reversed_num_str:
        return True
    else:
        return False
  num = int(input("Enter a number: "))


if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


