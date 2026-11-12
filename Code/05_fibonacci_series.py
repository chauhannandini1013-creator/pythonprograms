def fibonacci_series(count):
 if count < 0:
  raise ValueError("Count cannot be negative")
 series = []
 a, b = 0, 1
 for _ in range(count):
  series.append(a)
 a, b = b, a + b
 return series
if __name__ == "_main_":
 count = int(input("How many terms? "))
 print(fibonacci_series(count))