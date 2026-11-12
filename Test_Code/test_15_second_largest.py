import importlib
module = importlib.import_module("Code.15_second_largest")
def test_case_1():
 assert module.second_largest([10, 5, 8, 20]) == 10
def test_case_2():
 assert module.second_largest([4, 4, 2]) == 2
def test_case_3():
 assert module.second_largest([-1, -5, -3]) == -3
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")