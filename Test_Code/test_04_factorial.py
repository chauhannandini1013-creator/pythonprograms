import importlib
module = importlib.import_module("Code.04_factorial")
def test_case_1():
 assert module.factorial(5) == 120
def test_case_2():
 assert module.factorial(0) == 1
def test_case_3():
 assert module.factorial(1) == 1
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")