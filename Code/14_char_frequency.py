def character_frequency(text):
 frequency = {}
 for char in text:
  frequency[char] = frequency.get(char, 0) + 1
 return frequency
if __name__ == "_main_":
 text = input("Enter text: ")
 print(character_frequency(text))  