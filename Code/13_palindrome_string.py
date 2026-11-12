def is_palindrome_string(text):
 cleaned = "".join(char.lower() for char in text if char.isalnum())
 return cleaned == cleaned[::-1]
if __name__ == "_main_":
 text = input("Enter a string: ")
 print("Palindrome" if is_palindrome_string(text) else "Not Palindrome")