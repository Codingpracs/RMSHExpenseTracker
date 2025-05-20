from argparse import ArgumentParser
import json

def load_db(path):
    try:
        with open(path) as f:
            database = json.load(f)
    # file doesn't exist -> create empty database or file exist but empty 
    except (FileNotFoundError, json.JSONDecodeError):
        database = {}
    except Exception as e:
        database = {}

    return database

def save_db(database, path):
    with open(path, "w") as f:
        json.dump(database, f, indent = 2, ensure_ascii = False)

def add(description,amount):
    pass

def delete(id):
    pass

def update(id, ):
    pass

def viewsummary():
    pass

def viewexpense():
    pass

def main():
    pass