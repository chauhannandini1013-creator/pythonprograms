def primes_in_range(start, end):
 return [number for number in range(start, end + 1) if number >= 2 and all(number % d != 0 for d in range(2, int(number ** 0.5) + 1))]
if __name__ == "_main_":
 start, end = map(int, input("Enter start and end: ").split())
 print (primes_in_range(start, end))