import importlib
module = importlib.import_module("Code.10_sum_of_digits")
def test_case_1():
 assert module.sum_of_digits(1234) == 10
def test_case_2():
 assert module.sum_of_digits(0) == 0
def test_case_3():
 assert module.sum_of_digits(-56) == 11
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")