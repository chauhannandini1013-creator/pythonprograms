import sys, os
sys.path.append(os.getcwd())
import importlib
module = importlib.import_module("Code.14_char_frequency")
def test_case_1():
 assert module.character_frequency('banana') == {'b': 1, 'a': 3, 'n': 2}
def test_case_2():
 assert module.character_frequency('') == {}
def test_case_3():
 assert module.character_frequency('a a') == {'a': 2, ' ': 1}
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")