file_path = "test.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)  
        
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    
import json

file_path = "output.json"

try:
    with open(file_path, "r") as file:
        data = json.load(file)
        print(data)
        
except FileNotFoundError:   
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
import csv

file_path = "output.csv"

try:
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
            
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")