
import json

FILE_NAME = "students.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}

def save_data(student):
    with open(FILE_NAME, "w") as file:
        json.dump(student, file, indent=4)