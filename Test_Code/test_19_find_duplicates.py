import sys, os
sys.path.append(os.getcwd())
import importlib
module = importlib.import_module("Code.19_find_duplicates")
def test_case_1():
 assert module.find_duplicates([1, 2, 2, 3, 1]) == [2, 1]
def test_case_2():
 assert module.find_duplicates([1, 2, 3]) == []
def test_case_3():
 assert module.find_duplicates([5, 5, 5]) == [5]
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")