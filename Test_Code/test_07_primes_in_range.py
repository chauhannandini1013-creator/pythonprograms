import sys, os
sys.path.append(os.getcwd())
import importlib
module = importlib.import_module("Code.07_primes_in_range")
def test_case_1():
 assert module.primes_in_range(1, 10) == [2, 3, 5, 7]
def test_case_2():
 assert module.primes_in_range(10, 15) == [11, 13]
def test_case_3():
 assert module.primes_in_range(4, 4) == []
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")