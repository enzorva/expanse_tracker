import sys
import csv
import pyfiglet
import time

class Expanse:
    def __init__(self, file_path):
        self.file_path = file_path

    def action_getter(self):
        if sys.argv[1] == "add":
            return self.add_expense()
        elif sys.argv[1] == "update":
            return self.update_expense()
        elif sys.argv[1] == "delete":
            return self.delete_expense()
        elif sys.argv[1] == "list":
            return self.list_expanses()
        elif sys.argv[1] == "summary":
            return self.summary_expanses()
        else:
            print("Invalid action. Please use 'add', 'update', 'delete', 'list', or 'summary'.")
            sys.exit(1)

    def add_expense(self):
        if len(sys.argv) != 4:
            print("Usage: python expanse_tracker.py add <category> <amount>")
            sys.exit(1)

        try:
            with open(self.file_path, 'r') as file:
                id = len(file.readlines()) - 1
        except FileNotFoundError:
            id = 1

        category = sys.argv[2]
        amount = sys.argv[3]
        date =  time.strftime("%Y-%m-%d")

        with open('expanse.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, date, category, amount])
            print(f"Expanse added successfully (ID: {id})")

    def update_expense(self):
        id = sys.argv[2]

        if len(sys.argv) != 5:
            print("Usage: python expanse_tracker.py update <id> <category> <amount>")
            sys.exit(1)
        elif id > len(sys.argv) or id <= 0:
            print("ID not found")
            sys.exit(1)

        category = sys.argv[3]
        amount = sys.argv[4]

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for i in range(2 ,len(rows)):
            if rows[i][0] == id:
                rows[i][2] = category
                rows[i][3] = amount
                break

        with open(self.file_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            print(f"Expanse updated successfully (ID: {id})")

    def delete_expense(self):
        id_to_delete = sys.argv[2]

        if len(sys.argv) != 3:
            print("Usage: python expanse_tracker.py delete <id>")
            sys.exit(1)
        elif id_to_delete > len(sys.argv) or id_to_delete <= 0:
            print("ID not found")
            sys.exit(1)

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for i in range(2, len(rows)):
            if rows[i][0] == id_to_delete:
                del rows[i]
                break

        for id, row in enumerate(rows[2:], start=1):
            row[0] = id

        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            print(f"Expanse deleted successfully (ID: {id_to_delete})")

    def list_expanses(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def summary_expanses(self):
        if len(sys.argv) == 2:

            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)

                total = 0
                for row in reader:
                    if len(row) >= 4 and row[1].startswith(time.strftime("%Y")):
                        total += float(row[3])
                print(f"Total expanse for: {total}")

        elif len(sys.argv) == 3:
            month = sys.argv[2].zfill(2)

            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)

                total = 0
                for row in reader:
                    if len(row) == 4 and row[1].startswith(f"{time.strftime("%Y")}-{month}"):
                        total += float(row[3])
        
                print(f"Total expanse for {time.strftime('%B', time.strptime(month, '%m'))}: {total}")

        else:
            print("Usage: python expanse_tracker.py summary <month>")
            sys.exit(1)

def main():
    f = pyfiglet.Figlet(font='small', width=80)
    print(f.renderText('Expanse Tracker'))

    file_path = 'expanse.csv'

    try:
        with open(file_path, 'r') as file:
            pass
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['ID','Date','Category','Amount'])

    expanse_manager = Expanse(file_path)
    expanse_manager.action_getter()

main()