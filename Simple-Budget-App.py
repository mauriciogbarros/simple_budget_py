class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        output = ""
        n_star = (30 - len(self.name)) // 2
        output += '*' * n_star
        output += self.name
        output += '*' * n_star
        output += '\n'
        for transaction in self.ledger:
            if len(transaction['description']) >= 23:
                output += transaction['description'][:23]
                output += f" {transaction['amount']:.2f}"
            else:
                output += transaction['description']
                output += f"{transaction['amount']:>{30 - len(transaction['description'])}.2f}"
            output += '\n'
        output += f'Total: {self.get_balance()}'
        return output

    def deposit(self, amount, description = ""):
        if not isinstance(amount, float):
            float(amount)
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True        
    
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

def create_spend_chart(categories):
    spenditures = []
    total_spent = 0
    height = 0
    for category in categories:
        spent = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                spent += transaction['amount']
        spenditures.append(spent)
        total_spent += spent
        if len(category.name) > height:
            height = len(category.name)

    percentages = []
    for s in spenditures:
        percentages.append(int((s / total_spent) * 100))
    chart = 'Percentage spent by category\n'
    for line in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]:
        if line == 100:
            chart += f'{line}|'
        if line < 100 and line > 0:
            chart += f' {line}|'
        if line == 0:
            chart += f'  {line}|'
        for p in percentages:
            if p >= line:
                chart += ' o '
            else:
                chart += '   '
        chart += ' \n'
    chart += '    '
    chart += '-' * (3 * len(spenditures) + 1)
    chart += '\n'
    line = 0
    while line < height:
        chart += '    '
        for category in categories:
            if line < len(category.name):
                chart += f' {category.name[line]} '
            else:
                chart += '   '
        line += 1
        # chart += '*\n'
        if line < height:
            chart += ' \n'
        else:
            chart += ' ' 

    return chart

def main():
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)
    print(clothing)
    auto = Category('Auto')
    categories = [food, clothing, auto]
    print(create_spend_chart(categories))

if __name__ == '__main__':
    main()
