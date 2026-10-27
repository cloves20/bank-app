
from main import deposit, withdraw


def test_successful_deposit():
    assert deposit(1600, 400, []) == 2000


def test_negative_deposit():
    assert deposit(1600, -400, []) == 1600


def test_zero_deposit():
    assert deposit(1600, 0, []) == 1600


def test_successful_withdrawal():
    assert withdraw(1600, 400, []) == 1200


def test_insufficient_funds():
    assert withdraw(1600, 2000, []) == 1600


def test_negative_withdrawal():
    assert withdraw(1600, -400, []) == 1600


def test_zero_withdrawal():
    assert withdraw(1600, 0, []) == 1600

