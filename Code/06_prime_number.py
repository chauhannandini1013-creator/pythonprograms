def is_prime(number):
 if number < 2:
   return False
 for divisor in range(2, int(number ** 0.5) + 1):
  if number % divisor == 0:
   return False
 return True
if __name__ == "_main_":
 number = int(input("Enter a number: "))
 print("Prime" if is_prime(number) else "Not Prime")