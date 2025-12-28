from functions.get_file_content import get_file_content

file = get_file_content("calculator", "lorem.txt")
print(len(file))
print(file[10000:])

try:
    print(get_file_content("calculator", "main.py"))
except Exception as e:
    print(e)

try:
    print(get_file_content("calculator", "pkg/calculator.py"))
except Exception as e:
    print(e)

try:
    print(get_file_content("calculator", "/bin/cat"))
except Exception as e:
    print(e)

try:
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
except Exception as e:
    print(e)
