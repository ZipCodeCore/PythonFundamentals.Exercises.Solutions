# Part 10

## Accompanying resources
* Slide deck: https://zipcoder.github.io/reveal-slides.data-engineering/zcw_content/python/fundamentals-part10.html

## Exercise 1

Create a program called *small_town_teller.py*

Declare a **Person** class with the following attributes:
* person id
* first name
* last name

Declare an **Account** class with the following attributes:
* account number
* account type
* account owner

Declare a **Bank** class able to support the following operations:
* Adding a customer to the bank
* Adding an account to the bank
* Removing an account from the bank
* Depositing money into an account
* Withdrawing money from an account
* Balance inquiry for a particular account

From an interactive terminal, you should be able to import these classes an interact with the objects and methods defined above.

```python
from small_town_teller import Person, Account, Bank

account = Account(2, "savings", 1)
Bank.add_account_to_bank(account)
Bank.deposit(1, 200)
Bank.balance_inquiry(1)
# 200

```

## Exercise 2 

Create a program called *persistent_small_town_teller.py*

This application should extend exercise one so that all of the customers and accounts persist between restarts.
