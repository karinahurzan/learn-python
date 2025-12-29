class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmmount, accName):
        self.balance = initialAmmount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.get_balance()

    def valiableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.valiableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete")
            self.get_balance()
        except BalanceException as e:
            print(f"\nWithdraw interrupted: {e}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.. 🚀")
            self.valiableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")


class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("\nDeposit complete.")
        self.get_balance()


class SavingsAcc(InterestRewardsAcc):
    def __init__(self, initialAmmount, accName):
        super().__init__(initialAmmount, accName)
        self.fee = 7

    def withdraw(self, amount):
        try:
            self.valiableTransaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWithdraw completed.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
