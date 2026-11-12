import sys, os
sys.path.append(os.getcwd())
import importlib
module = importlib.import_module("Code.09_palindrome_number")
def test_case_1():
 assert module.is_palindrome_number(121) == True
def test_case_2():
 assert module.is_palindrome_number(123) == False
def test_case_3():
 assert module.is_palindrome_number(-121) == False
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")