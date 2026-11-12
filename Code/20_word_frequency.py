def word_frequency(sentence):
 frequency = {}
 for word in sentence.lower().split():
  word = word.strip(".,!?;:")
 if word:
  frequency[word] = frequency.get(word, 0) + 1
 return frequency
if __name__ == "__main__":
 sentence = input("Enter a sentence: ")
 print(word_frequency(sentence))
