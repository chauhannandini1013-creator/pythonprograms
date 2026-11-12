def second_largest(numbers):
 unique_numbers = sorted(set(numbers), reverse=True)
 if len(unique_numbers) < 2:
  raise ValueError("At least two distinct numbers are required")
 return unique_numbers[1]
if __name__ == "__main__":
 numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
 print("Second largest:",second_largest(numbers))