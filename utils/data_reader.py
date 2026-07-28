# utils/data_reader.py
import csv
import os


def read_csv_data(filepath):
    # 1. Get the directory where data_reader.py is located (the 'utils' folder)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Go up one level to the project root folder
    project_root = os.path.dirname(current_dir)
    
    # 3. Join the root folder with 'data/users.csv'
    absolute_path = os.path.join(project_root, filepath)
    
    data = []
    # 4. Open using the absolute path
    with open(absolute_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append((row["username"], row["password"]))
            
    return data