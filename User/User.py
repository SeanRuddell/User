class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_self, amount):
        self.account_balance -= amount
        other_self.account_balance += amount
        
sean = User("Sean", "seanruddell@yahoo.com")
guido = User("Guido", "guido@yahoo.com")
monty = User("Monty", "montymcgoo@yahoo.com")

sean.make_deposit(200)
sean.make_deposit(300)
sean.make_deposit(200)
sean.make_withdrawl(150)
sean.display_user_balance()
guido.make_deposit(100)
guido.make_deposit(500)
guido.make_withdrawl(50)
guido.make_withdrawl(100)
guido.display_user_balance()
monty.make_deposit(1000)
monty.make_withdrawl(150)
monty.make_withdrawl(200)
monty.make_withdrawl(100)
monty.display_user_balance()
sean.transfer_money(monty, 1)
sean.display_user_balance()
monty.display_user_balance()
