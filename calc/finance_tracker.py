class FinanceTracker:
    def __init__(self):
        self.income = []
        self.expenses = []

    def add_income(self, amount, description):
        self.income.append({"amount": amount, "description": description})
        print(f"Income of {amount} added!")

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})
        print(f"Expense of {amount} added!")

    def view_income(self):
        print("Income:")
        for i, income in enumerate(self.income, 1):
            print(f"{i}. {income['description']}: {income['amount']}")

    def view_expenses(self):
        print("Expenses:")
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i}. {expense['description']}: {expense['amount']}")

    def calculate_balance(self):
        total_income = sum(item["amount"] for item in self.income)
        total_expenses = sum(item["amount"] for item in self.expenses)
        balance = total_income - total_expenses
        return balance

    def view_summary(self):
        total_income = sum(item["amount"] for item in self.income)
        total_expenses = sum(item["amount"] for item in self.expenses)
        print("Summary:")
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Balance: {self.calculate_balance()}")


def main():
    tracker = FinanceTracker()
    while True:
        print("\n1. Add income")
        print("2. Add expense")
        print("3. View income")
        print("4. View expenses")
        print("5. View summary")
        print("6. Quit")

        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            tracker.add_income(amount, description)
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.add_expense(amount, description)
        elif choice == "3":
            tracker.view_income()
        elif choice == "4":
            tracker.view_expenses()
        elif choice == "5":
            tracker.view_summary()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
