import sys, os
sys.path.append(os.getcwd())
import importlib
module = importlib.import_module("Code.11_count_vowels")
def test_case_1():
 assert module.count_vowels_consonants('Hello') == (2, 3)
def test_case_2():
 assert module.count_vowels_consonants('AEIOU') == (5, 0)
def test_case_3():
 assert module.count_vowels_consonants('123!') == (0, 0)
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")