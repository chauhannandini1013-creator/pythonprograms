import importlib
module = importlib.import_module("Code.16_remove_duplicates")
def test_case_1():
 assert module.remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
def test_case_2():
 assert module.remove_duplicates(['a', 'a', 'b']) == ['a', 'b']
def test_case_3():
 assert module.remove_duplicates([]) == []
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")