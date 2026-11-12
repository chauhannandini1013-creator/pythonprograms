import importlib
module = importlib.import_module("Code.03_pos_neg_zero")
def test_case_1():
 assert module.number_type(5) == "Positive"
def test_case_2():
 assert module.number_type(-3) == "Negative"
def test_case_3():
 assert module.number_type(0) == "Zero"
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")