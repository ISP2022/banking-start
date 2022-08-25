"""Unit tests of the Bank Account class."""
import unittest
from bank_account import BankAccount
from money import Money


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        """Create test fixtures for use in tests."""
        # account with 0 minimum balance
        self.account = BankAccount("Account with No Min Balance")

    def test_deposit_cash(self):
        """Test deposit correctly adds to balance."""
        # a new account should have 0 balance
        self.assertEqual(0.0, self.account.balance)
        sum = 0
        for amount in [0.1, 1, 1000]:
            sum += amount
            self.account.deposit(Money(amount))
            self.assertEqual(sum, self.account.balance)
    
    def test_withdraw(self):
        """You can withdraw anything up to the balance from account."""
        self.account.deposit(Money(1000))
        # withdraw a tiny value
        wd = self.account.withdraw(1.0)   # argument to withdraw is a number
        self.assertEqual(1.0, wd.value) 
        self.assertEqual(999.0, self.account.balance)
        # withdraw more
        wd = self.account.withdraw(900.0)
        self.assertEqual(900.0, wd.value) 
        self.assertEqual(100, self.account.balance)  # TODO fix this

     @unittest.skip("Not done yet.")
     def test_withdraw_invalid_amount(self):
        """You cannot withdraw more than the balance of account."""
        self.fail("Write this test. withdraw should raise a ValueError.")
