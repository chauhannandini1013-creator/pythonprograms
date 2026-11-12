import importlib
module = importlib.import_module("Code.05_fibonacci_series")
def test_case_1():
 assert module.fibonacci_series(6) == [0, 1, 1, 2, 3, 5]
def test_case_2():
 assert module.fibonacci_series(1) == [0]
def test_case_3():
 assert module.fibonacci_series(0) == []
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")
