from argparse import ArgumentParser
import json
from datetime import datetime
import os

# Part 2 : Try SQL injestion
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

def save_db(database, path) -> None:
    with open(path, "w") as f:
        json.dump(database, f, indent = 2, ensure_ascii = True)

def add(database,description,amount, category = None) -> None:

    # while True: 
    #     print("""Please Choose a category:
    #         1. Food 
    #         2. Transport
    #         3. Self Care
    #         4. Travel
    #         5. ETC
    #         """)
        
    #     choice = input("Enter a number corresponding to the category: ")

    #     categories = {
    #         "1" : "Food", 
    #         "2" : "Transport",
    #         "3" : "Self Care",
    #         "4" : "Travel",
    #         "5" : "ETC"
    #     }

    #     if choice in categories:
    #         category = categories[choice]
    #         break
    #     else:
    #         print("Please choose a valid choice")

        dt = datetime.now()
        uniqueid = str(int(max("0", *database.keys())) + 1)
        today = dt.date()
        database[uniqueid] = {
            "ID": uniqueid,
            "Date": today.isoformat(), # converts date to string, without it json cannot store the date
            "Description": description,
            "Category": category,
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
def update(database,id,*args):
    description = None
    amount = None

    if len(args) == 1:
        try: 
            amount = float(args[0])
        except ValueError:
            description = args[0]
    elif len(args) == 2:
        description = args[0]
        amount = args[1]

    if amount is not None:
        database[id]['Amount'] = amount
        print(f"Amount of expense {id} has changed to {amount}")
    if description is not None:
        database[id]['Description'] = description
        print(f"Description of expense {id} has changed to {description}")
    if amount is None and description is None:
        print(f"Nothing has changed for expense {id}")
    viewlist({id: database[id]})

def viewsummary(database, month = None):
    # total = sum(float(data['Amount']) for data in database.values())
    total = 0
    for data in database.values():
        entry_date = datetime.strptime(data['Date'], "%Y-%m-%d").date()
        if month is None or entry_date.month == int(month):
            total += float(data['Amount'])
    print(f"Total expenses: {total}")


def viewlist(database) -> None:
    print(f"{'ID':<5} {'Date':<15} {'Description':<40} {'Amount':<10}")
    print("-" * 75)
    for id, properties in database.items():
        print(f"{id:<5} {properties['Date']:<15} {properties['Description']:<40} {properties['Amount']:<10}")
        # can import textwrap to wrap long ass texts

def main() -> None:
    parser = ArgumentParser(description = "expense tracker")
    subparsers = parser.add_subparsers(dest = 'command', required = True)
    
    add_parser = subparsers.add_parser("add", help = "Add an amount n description")
    add_parser.add_argument('description', help = 'Description of item')
    add_parser.add_argument('amount', help = 'Amt spent')
    add_parser.set_defaults(func = add)

    del_parser = subparsers.add_parser("delete")
    del_parser.add_argument("id")
    del_parser.set_defaults(func = delete)

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id")
    # nargs = number of arguments; 3 -> 3, ? -> optional single value, * -> flexible no. of values, put into list, + -> at least 1 value
    update_parser.add_argument("fields", nargs = "+" )
    # change is regardless of whether amount of description, this is settled in update function
    update_parser.set_defaults(func = update)

    view_parser = subparsers.add_parser("view")
    view_parser.set_defaults(func = viewlist)

    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", required = False, help = " Filtered by Month ")
    summary_parser.set_defaults(func = viewsummary)

    date_changer = subparsers.add_parser("change")
    date_changer.add_argument("id")
    date_changer.add_argument("date",type = lambda s: datetime.strptime(s, "%Y-%m-%d").date())
    date_changer.set_defaults(func = lambda db, id, date: (db[id].update({"Date": str(date)}),
                              print(f"Date of {id} changed to {date}")))

    reset_paser = subparsers.add_parser("reset")
    # clear removes all elements from a dictionary
    reset_paser.set_defaults(func = lambda db: db.clear())

    args = parser.parse_args()
    database_path = os.path.expanduser("~/money.json")
    database = load_db(database_path)

    args_dict = vars(args).copy()
    func = args_dict.pop("func")
    args_dict.pop("command", None)

    if func == update: 
        func(database, args.id, *args.fields)
    else:
        func(database,**args_dict)
    save_db(database, database_path)

if __name__ == "__main__":
    main()








