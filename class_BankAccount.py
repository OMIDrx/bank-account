class BankAccount:
    def __init__ (self,name,balance = 0):
        self.name = name
        self.balance = balance

    def deposit (self,amount):
        if amount > 0:
            self.balance += amount
            print(f'you add {amount}$ in your wallet')
        else:
            print(f'your {amount} is not valid..!')
    
    def withdraw (self,amount):
        if amount > self.balance:
            print(f'you dont have enoghe money')
        elif amount <= 0 :
            print(f'your number is under zero...ERROR!')
        else:
            self.balance -= amount
            print(f'{amount} It was deducted from your account.\n you have {self.balance}$ left')

    def show_balance(self):
        print(f'MR/MISS {self.name} you have {self.balance}$ \nin your wallet')

q = input('enter you name:')
w = int(input('enter your balance:'))
while w <= 0:
    w = int(input('try again...enter your balance:'))

x = BankAccount(q, w)
x.show_balance()
x.deposit(500)
x.withdraw(300)
x.withdraw(2000)
x.show_balance()
