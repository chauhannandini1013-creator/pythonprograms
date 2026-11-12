def find_missing_number(numbers):
 if not numbers:
  raise ValueError("List cannot be empty")
 expected = set(range(min(numbers), max(numbers) + 1))
 missing = sorted(expected - set(numbers))
 return missing[0] if len(missing) == 1 else missing
if __name__ == "_main_":
 numbers = list(map(int, input("Enter a sequence with one missing number: ").split()))
 print("Missing number:", find_missing_number(numbers))