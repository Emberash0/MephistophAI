from functions.run_python_file import run_python_file

try:
    print(run_python_file("calculator", "main.py"))
except Exception as e:
    print(e)

try:
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
except Exception as e:
    print(e)

try:
    print(run_python_file("calculator", "tests.py"))
except Exception as e:
    print(e)

try:
    print(run_python_file("calculator", "../main.py"))
except Exception as e:
    print(e)

try:
    print(run_python_file("calculator", "nonexistent.py"))
except Exception as e:
    print(e)

try:
    print(run_python_file("calculator", "lorem.txt"))
except Exception as e:
    print(e)
