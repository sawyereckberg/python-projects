import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}"
        lines = [title]

        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            if len(amt) > 7:
                amt = amt[:7]
            lines.append(f"{desc:<23}{amt:>7}")

        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    spent_per_category = []
    for category in categories:
        spent = sum(
            -item["amount"] for item in category.ledger if item["amount"] < 0
        )
        spent_per_category.append(spent)

    total_spent = sum(spent_per_category)

    percentages = []
    for spent in spent_per_category:
        if total_spent == 0:
            pct = 0
        else:
            pct = math.floor((spent / total_spent) * 10) * 10
        percentages.append(pct)

    lines = ["Percentage spent by category"]

    for level in range(100, -1, -10):
        row = f"{level:>3}|"
        for pct in percentages:
            row += " o " if pct >= level else "   "
        row += " "
        lines.append(row)

    dash_line = "    " + "-" * (3 * len(categories) + 1)
    lines.append(dash_line)

    max_len = max((len(cat.name) for cat in categories), default=0)
    for i in range(max_len):
        row = "     "
        for cat in categories:
            ch = cat.name[i] if i < len(cat.name) else " "
            row += f"{ch}  "
        lines.append(row)

    return "\n".join(lines)