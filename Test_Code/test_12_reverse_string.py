import importlib
module = importlib.import_module("Code.12_reverse_string")
def test_case_1():
 assert module.reverse_string('hello') == "olleh"
def test_case_2():
 assert module.reverse_string('Python') == "nohtyP"
def test_case_3():
 assert module.reverse_string('') == ""
if __name__ == "__main__":
 test_case_1()
 test_case_2()
 test_case_3()
 print("All test cases passed.")