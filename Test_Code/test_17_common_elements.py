import importlib
module = importlib.import_module("Code.17_common_elements")
def test_case_1():
 assert module.common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
def test_case_2():
 assert module.common_elements(['a', 'b'], ['c']) == []
def test_case_3():
 assert module.common_elements([1, 1, 2], [1, 2]) == [1, 2]
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")
