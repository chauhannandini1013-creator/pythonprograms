def find_duplicates(numbers):
 seen = set()
 duplicates = []
 for number in numbers:
  if number in seen and number not in duplicates:
    duplicates.append(number)
 seen.add(number)
 return duplicates
if __name__ == "_main_":
 numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
 print("Duplicates:", find_duplicates(numbers))