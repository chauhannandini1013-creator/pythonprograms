def is_palindrome_number(number):
 return number >= 0 and str(number) == str(number)[::-1]
if __name__ == "_main_":
 number = int(input("Enter a number: "))
 print("Palindrome" if is_palindrome_number(number) else "Not Palindrome")