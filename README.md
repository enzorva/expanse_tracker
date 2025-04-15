# Expanse Tracker

Expanse Tracker is a command-line tool for managing and tracking your expenses. It allows you to add, update, delete, list, and summarize expenses stored in a CSV file.

## Features
- **Add Expenses**: Add a new expense with a category and amount.
- **Update Expenses**: Update an existing expense by its ID.
- **Delete Expenses**: Delete an expense by its ID.
- **List Expenses**: Display all recorded expenses.
- **Summarize Expenses**: Calculate the total expenses for a specific month or the entire year.

## Requirements
- Python 3.x

## Installation
1. Clone this repository or download the files.
2. Ensure Python 3.x is installed on your system.

## Usage
Run the script using the command line. The following actions are supported:

### Add an Expense
```bash
python expanse_tracker.py add <category> <amount>
```
- `<category>`: The category of the expense (e.g., Food, Transport).
- `<amount>`: The amount of the expense (e.g., 20.5).

### Update an Expense
```bash
python expanse_tracker.py update <id> <category> <amount>
```
- `<id>`: The ID of the expense to update.
- `<category>`: The new category.
- `<amount>`: The new amount.

### Delete an Expense
```bash
python expanse_tracker.py delete <id>
```
- `<id>`: The ID of the expense to delete.

### List All Expenses
```bash
python expanse_tracker.py list
```

### Summarize Expenses
#### For the Entire Year
```bash
python expanse_tracker.py summary
```
#### For a Specific Month
```bash
python expanse_tracker.py summary <month>
```
- `<month>`: The numeric month (e.g., 4 for April).

## File Structure
- `expanse_tracker.py`: The main script for managing expenses.
- `expanse.csv`: The CSV file where expenses are stored.

## Example
### Adding an Expense
```bash
python expanse_tracker.py add Food 20.5
```
### Listing Expenses
```bash
python expanse_tracker.py list
```
### Summarizing Expenses for April
```bash
python expanse_tracker.py summary 4
```

## Notes
- The `expanse.csv` file is automatically created if it does not exist.
- Ensure the file is not open in another program while running the script.

## Project URL
[Expense Tracker Project](https://roadmap.sh/projects/expense-tracker)

## License
This project is licensed under the MIT License.