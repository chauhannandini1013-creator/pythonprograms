import sys, os
sys.path.append(os.getcwd())
import importlib
module = importlib.import_module("Code.18_missing_number")
def test_case_1():
 assert module.find_missing_number([1, 2, 4, 5]) == 3
def test_case_2():
 assert module.find_missing_number([10, 12, 13]) == 11
def test_case_3():
 assert module.find_missing_number([1, 2, 3]) == []
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")