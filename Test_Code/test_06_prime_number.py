import sys, os
sys.path.append(os.getcwd())
import importlib
module = importlib.import_module("Code.06_prime_number")
def test_case_1():
 assert module.is_prime(17) == True
def test_case_2():
 assert module.is_prime(1) == False
def test_case_3():
 assert module.is_prime(2) == True
def test_case_4():
 assert module.is_prime(18) == False
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 test_case_4()
 print("All test cases passed.")