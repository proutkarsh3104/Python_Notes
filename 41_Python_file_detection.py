# Python file detection

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"the location {file_path} exists")
    
    if os.path.isfile(file_path):
        print(f"{file_path} is a file")
    elif os.path.isdir(file_path):
        print(f"{file_path} is a directory")
    
else:
    print(f"the location {file_path} does not exist")

