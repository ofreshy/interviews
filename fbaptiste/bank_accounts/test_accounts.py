
from fbaptiste.bank_accounts import models


people_factory = models.PeopleFactory()
bank_account_factory = models.BankAccountFactory()
transaction_factory = models.TransactionFactory()

o_sharabi = people_factory.new(first_name="offer", last_name="sharabi")
ba = bank_account_factory.open(person=o_sharabi, overdraft=100, time_zone=models.ist)

print(ba)
print()

t = transaction_factory.deposit(ba, 100)
print(t)
print()
t = transaction_factory.apply_interest(ba, 0.5)
print(t)
print()
t = transaction_factory.withdraw(ba, 101)
print(t)
print()
t = transaction_factory.withdraw(ba, 200)
print(t)
