def remove_duplicates(items):
 return list(dict.fromkeys(items))
if __name__ == "_main_":
 items = input("Enter items separated by spaces: ").split()
 print(remove_duplicates(items))