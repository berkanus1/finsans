import json
import os

DATA_FILE = "data.json"
transactions = []


def load():
    global transactions
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            transactions = json.load(f)
        print(f"Loaded {len(transactions)} transaction(s) from {DATA_FILE}.")


def save():
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=2)


def add(amount, category, note=""):
    kind = "income" if amount > 0 else "expense"
    transactions.append({"amount": amount, "category": category, "note": note, "type": kind})
    save()
    print(f"Added {kind}: {amount:+.2f} TL  [{category}]")


def balance():
    total = sum(t["amount"] for t in transactions)
    print(f"\nBalance: {total:+.2f} TL")
    return total


def summary():
    if not transactions:
        print("No transactions yet.")
        return
    print("\n--- Transactions ---")
    for t in transactions:
        print(f"  {t['type']:7s}  {t['amount']:+8.2f} TL  {t['category']}  {t['note']}")
    balance()


def menu():
    load()
    print("\n=== Finsans Budget Tracker ===")
    while True:
        print("\n1. Add income")
        print("2. Add expense")
        print("3. View summary")
        print("4. Quit")
        choice = input("\nChoose (1-4): ").strip()

        if choice == "1":
            try:
                amount = float(input("Amount (TL): "))
                category = input("Category: ").strip() or "other"
                note = input("Note (optional): ").strip()
                add(abs(amount), category, note)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            try:
                amount = float(input("Amount (TL): "))
                category = input("Category: ").strip() or "other"
                note = input("Note (optional): ").strip()
                add(-abs(amount), category, note)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "3":
            summary()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    menu()
