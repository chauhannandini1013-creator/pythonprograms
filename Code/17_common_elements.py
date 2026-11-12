def common_elements(first, second):
 second_set = set(second)
 return list(dict.fromkeys(item for item in first if item in second_set))
if __name__ == "_main_":
 first = input("Enter first list: ").split()
 second = input("Enter second list: ").split()
 print(common_elements(first, second))