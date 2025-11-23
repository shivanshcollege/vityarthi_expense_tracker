import storage
import menu

FILENAME = "expenses.txt"

def main():
    open(FILENAME,"a").close()
    expenses, next_id = storage.load_expenses(FILENAME) #loading existing data
    expenses, next_id = menu.run(expense_list=expenses, next_id=next_id) #running the main menu

    storage.save_expenses(FILENAME, expenses)
    print("Your data is saved. Goodbye!")

if __name__ == "__main__":
    main()
