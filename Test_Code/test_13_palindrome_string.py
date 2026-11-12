import importlib
module = importlib.import_module("Code.13_palindrome_string")
def test_case_1():
 assert module.is_palindrome_string('madam') == True
def test_case_2():
 assert module.is_palindrome_string('Hello') == False
def test_case_3():
 assert module.is_palindrome_string('A man, a plan, a canal: Panama') == True
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")