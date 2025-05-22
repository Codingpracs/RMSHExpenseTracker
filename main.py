from argparse import ArgumentParser
import json
from datetime import datetime

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

def add(database,description,amount) -> None:
    uniqueid = str(int(max("0", *database.keys())) + 1)
    dt = datetime.now()
    today = dt.date()

    database[uniqueid] = {
        "ID": uniqueid,
        "Date": today,
        "Description": description,
        "Amount": amount
    }

    viewlist({uniqueid: database[uniqueid]})

def delete(database, id) -> None:
    viewlist({id:database[id]})
    print(f"You are deleting database{id}. Press 1 to proceed, and 2 to return")
    while True:
        choice = int(input())
        if choice == 1:
            del database[id]
            print(f"database{id} deleted")
            break
        if choice == 2:
            print("Deletion Cancelled")
            break
        else: 
            print("Invalid Choice. Please choose an option.")
    


# args means can determine what the argument represents depending on the input count/ type
def update(id,*args):
    pass

def viewsummary(database):
    amt_log = []
    total = sum(int(data['amount']) for data in database.values())
    # for id, data in database.items():
    #     amt_log.append(int(data['amount']))
    # total = sum(amt_log)
    print(f"Total expenses: {total}")

# def listexpense(database, default = all) -> None:
#     viewlist({id: database[id]})
    

def viewlist(database) -> None:
    print(f"{'ID':<5} {'Status': <15} {'Description': <30} {'createdAt': <20} {'updatedAt':<20}")
    print("-" * 95)
    for id,properties in database.items():
        print(f"{id:<5} {properties['Date']:<15} {properties['Description']:<30} {properties['Amount']:<20}")

def main():
    pass