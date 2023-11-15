import unittest
from fbaptiste.bank_accounts import models


class TestPerson(unittest.TestCase):
    def test_middle_name_when_not_empty(self):
        p = models.Person(id_="", first_name="Andrew", middle_name="Charlie", last_name="Hall")
        expected_name = "Andrew Charlie Hall"

        self.assertEqual(expected_name, p.full_name())

    def test_middle_name_when_empty(self):
        p = models.Person(id_="", first_name="Andrew", last_name="Hall", middle_name="")
        expected_name = "Andrew Hall"

        self.assertEqual(expected_name, p.full_name())

    def test_capitalizing(self):
        p = models.Person(id_="", first_name="andrew", middle_name="charlie", last_name="hall")
        expected_name = "Andrew Charlie Hall"

        self.assertEqual(expected_name, p.full_name())


def new_bank_account(overdraft=0):
    return models.BankAccount(
        id_="test",
        person=models.Person(id_="", first_name="a", middle_name="c", last_name="b"),
        time_zone=models.ist,
        _overdraft=overdraft,
    )


class TestBankAccount(unittest.TestCase):

    def test_new_bank_account_is_0_balance(self):
        b = new_bank_account()
        self.assertEqual(0.0, b.balance)

    def test_new_bank_account_with_overdraft_set(self):
        b = new_bank_account(overdraft=100)
        self.assertEqual(100.0, b.overdraft)

    def test_bank_account_update_after_deposit(self):
        b = new_bank_account()
        b.deposit(models.Deposit(value=100))
        self.assertEqual(100.0, b.balance)

    def test_bank_account_update_after_withdraw(self):
        b = new_bank_account()
        b.deposit(models.Deposit(value=100))
        b.withdraw(models.Withdraw(value=50))
        self.assertEqual(50.0, b.balance)

    def test_bank_account_update_after_withdraw_with_overdraft(self):
        b = new_bank_account(overdraft=50)
        b.deposit(models.Deposit(value=100))
        b.withdraw(models.Withdraw(value=120))
        self.assertEqual(-20.0, b.balance)

    def test_bank_account_update_after_withdraw_without_overdraft(self):
        b = new_bank_account()
        b.deposit(models.Deposit(value=100))
        with self.assertRaises(ValueError):
            b.withdraw(models.Withdraw(value=150))

    def test_bank_account_update_after_withdraw_when_exceeds_overdraft(self):
        b = new_bank_account(overdraft=20)
        b.deposit(models.Deposit(value=100))
        with self.assertRaises(ValueError):
            b.withdraw(models.Withdraw(value=150))


class TestTransactions(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()


# people_factory = models.PeopleFactory()
# bank_account_factory = models.BankAccountFactory()
# transaction_factory = models.TransactionFactory()
#
# o_sharabi = people_factory.new(first_name="offer", last_name="sharabi")
# ba = bank_account_factory.open(person=o_sharabi, overdraft=100, time_zone=models.ist)
#
# print(ba)
# print()
#
# t = transaction_factory.deposit(ba, 100)
# print(t)
# print()
# t = transaction_factory.apply_interest(ba, 0.5)
# print(t)
# print()
# t = transaction_factory.withdraw(ba, 101)
# print(t)
# print()
# t = transaction_factory.withdraw(ba, 200)
# print(t)
