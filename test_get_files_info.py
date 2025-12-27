from functions.get_files_info import get_files_info

print("Result for current directory:")
try:
    print(get_files_info("calculator", "."))
except Exception as e:
    print(e)

print("Result for 'pkg' directory:")
try:
    print(get_files_info("calculator", "pkg"))
except Exception as e:
    print(e)

print("Result for '/bin' directory:")
try:
    print(get_files_info("calculator", "/bin"))
except Exception as e:
    print(e)

print("Result for '../' directory:")    
try:
    print(get_files_info("calculator", "../"))
except Exception as e:
    print(e)