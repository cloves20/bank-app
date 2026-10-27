# Bank Management System

A simple command line banking application built with Python. This project demonstrates fundamental programming concepts,
input validation, automated testing, and persistent data storage.

## Features

* Deposit money into an account
* Withdraw money with balance checks
* View the current account balance
* View transaction history
* Save account information between sessions
* Handle invalid menu selections and amounts
* Automated tests using pytest

## Technologies Used

* Python
* JSON for data storage
* pytest for automated testing

## Requirements

* Python 3.10 or later
* pytest

## Installation

1. Clone or download this repository.
2. Open the project folder.
3. Install pytest:

   
   python -m pip install pytest
   

## Running the Application

Run the following command from the project directory:


python main.py


## Running the Tests

Run:


python -m pytest -v


## Data Storage

Account information and transaction history are stored locally in `bank_data.json`.

If the file does not exist, the application starts with a default balance of 1600.

## Limitations

This project is intended for learning purposes. It is not a real banking system and does not implement user authentication, secure financial storage, or multiple accounts.

## Future Improvements

* Support decimal currency amounts
* Add account creation and multiple accounts
* Improve error handling and data validation
* Add more automated tests
* Introduce a database such as SQLite
