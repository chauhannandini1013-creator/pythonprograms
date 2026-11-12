import sys, os
sys.path.append(os.getcwd())
import importlib
module = importlib.import_module("Code.01_even_odd")
def test_case_1():
 assert module.check_even_odd(10) == "Even"
def test_case_2():
 assert module.check_even_odd(7) == "Odd"
def test_case_3():
 assert module.check_even_odd(0) == "Even"
def test_case_4():
 assert module.check_even_odd(-4) == "Even"
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 test_case_4()
 print("All test cases passed.")