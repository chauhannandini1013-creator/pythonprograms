def reverse_number(number):
 sign = -1 if number < 0 else 1
 reversed_value = int(str(abs(number))[::-1])
 return sign * reversed_value
if __name__ == "_main_":
 number = int(input("Enter a number: "))
 print("Reversed:", reverse_number(number))