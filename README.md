# Bank Account (Python)

A simple Python class to simulate a bank account.

## Features
- Deposit money
- Withdraw money
- Show balance

## Example Usage

```python
from bank_account import BankAccount

name = input("Enter your name: ")
balance = int(input("Enter your balance: "))

while balance <= 0:
    balance = int(input("Try again, enter your balance: "))

account = BankAccount(name, balance)

account.show_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
account.show_balance()

MR/MISS Omid, your balance is 1000$.
You added 500$ to your wallet.
300$ deducted. Remaining balance: 1200$
You do not have enough money.
MR/MISS Omid, your balance is 1200$.

---

- Commit message:

