import importlib
module = importlib.import_module("Code.20_word_frequency")
def test_case_1():
 assert module.word_frequency('cat dog cat') == {'cat': 2, 'dog': 1}
def test_case_2():
 assert module.word_frequency('Hello, hello!') == {'hello': 2}
def test_case_3():
 assert module.word_frequency('') == {}
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")