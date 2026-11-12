def sum_of_digits(number):
 return sum(int(digit) for digit in str(abs(number)))
if __name__ == "_main_":
 number = int(input("Enter a number: "))
 print("Sum of digits:", sum_of_digits(number))