from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.get_balance()
Sara.get_balance()

Sara.deposit(500)

Dave.withdraw(5000)
Dave.withdraw(10)

Dave.transfer(500, Sara)

Jin = InterestRewardsAcc(1000, "Jin")
Jin.get_balance()
Jin.deposit(100)
Jin.transfer(1000, Dave)


Blaze = SavingsAcc(1000, "Blaze")

Blaze.get_balance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)
