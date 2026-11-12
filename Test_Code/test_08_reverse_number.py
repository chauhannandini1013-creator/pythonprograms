import sys, os
sys.path.append(os.getcwd())
import importlib
module = importlib.import_module("Code.08_reverse_number")
def test_case_1():
 assert module.reverse_number(12345) == 54321
def test_case_2():
 assert module.reverse_number(1200) == 21
def test_case_3():
 assert module.reverse_number(-456) == -654
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")