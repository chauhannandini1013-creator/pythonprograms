import sys, os
sys.path.append(os.getcwd())
import importlib
module = importlib.import_module("Code.02_largest_of_three")
def test_case_1():
 assert module.largest_of_three(10, 25, 7) == 25
def test_case_2():
 assert module.largest_of_three(-1, -5, -3) == -1
def test_case_3():
 assert module.largest_of_three(4, 4, 2) == 4
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")