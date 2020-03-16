import unittest
import small_town_teller


class SmallTownTellerTest(unittest.TestCase):

    def setUp(self) -> None:
        self._customer = john = small_town_teller.Person(1, 'John', 'Smith')
        self._account = small_town_teller.Account(123, 'CHECKING', john)
        self._bank = small_town_teller.Bank()

    def test_person_initialization(self):
        expected_id = 1
        expected_first_name = 'John'
        expected_las_name = 'Smith'

        self.assertEqual(expected_id, self._customer.id)
        self.assertEqual(expected_first_name, self._customer.first_name)
        self.assertEqual(expected_las_name, self._customer.last_name)

    def test_account_initialization(self):
        expected_number = 123
        expected_type = 'CHECKING'
        expected_owner = 'id: 1. owner: John Smith'
        expected_balance = 0

        self.assertEqual(expected_number, self._account.number)
        self.assertEqual(expected_type, self._account.type)
        self.assertEqual(expected_owner, str(self._account.owner))
        self.assertEqual(expected_balance, self._account.balance)

    def test_bank_initialization(self):
        self.assertEqual(dict(), self._bank.accounts)
        self.assertEqual(dict(), self._bank.customers)

    def test_bank_add_customer(self):
        jane = small_town_teller.Person(2, 'Jane', 'Doe')
        self._bank.add_customer(jane)

        self.assertEqual(1, len(self._bank.customers))
        self.assertEqual(jane.id, self._bank.customers.get(2).id)
        self.assertEqual(jane.first_name, self._bank.customers.get(2).first_name)
        self.assertEqual(jane.last_name, self._bank.customers.get(2).last_name)

    def test_bank_add_customer_duplicate_id(self):
        jane = small_town_teller.Person(1, 'Jane', 'Doe')
        self._bank.add_customer(jane)

        with self.assertRaises(ValueError):
            self._bank.add_customer(self._customer)
