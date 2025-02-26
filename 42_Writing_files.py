# Python writitng files(.txt, .json, .csv)

txt_data = "I like Pizaa"

file_path = "output.txt"    

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' has been created")
    
import json   
employee= {
    "name": "John",
    "age": 30,
    "department": "IT"  
}

file_path = "output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' has been created")
        
except FileExistsError:
    print(f"file '{file_path}' already exists")
    
    
import csv  

workers = [
    ["Name", "Age", "Department"],
    ["John", 30, "IT"],
    ["Jane", 25, "HR"],
    ["Jack", 22, "Finance"]
    ]

file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for worker in workers:
            writer.writerow(worker) 
        print(f"csv file '{file_path}' has been created")
        
except FileExistsError: 
    print(f"file '{file_path}' already exists")