transactions = []


def add(amount, category, note=""):
    kind = "income" if amount > 0 else "expense"
    transactions.append({"amount": amount, "category": category, "note": note, "type": kind})
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


if __name__ == "__main__":
    add(5000, "salary", "May salary")
    add(-120, "food", "groceries")
    add(-45, "transport", "bus pass")
    add(500, "freelance", "design work")
    add(-200, "bills", "electricity")
    summary()
