def count_vowels_consonants(text):
 vowels = sum(1 for char in text.lower() if char in "aeiou")
 consonants = sum(1 for char in text.lower() if char.isalpha() and char not in "aeiou")
 return vowels, consonants
if __name__ == "__main__":
 text = input("Enter text: ")
 vowels, consonants = count_vowels_consonants(text)
 print("Vowels:", vowels)
 print("Consonants:", consonants)
 