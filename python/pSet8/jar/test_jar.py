from jar import Jar
import pytest


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0

def test_str():
    jar2 = Jar()
    assert str(jar2) == ""
    jar2.deposit(1)
    assert str(jar2) == "🍪"
    jar2.deposit(11)
    assert str(jar2) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar3 = Jar()
    assert jar3.size == 0
    jar3.deposit(7)
    assert jar3.size == 7
    with pytest.raises(ValueError):
        jar3.deposit(7)


def test_withdraw():
    jar4 = Jar()
    jar4.deposit(12)
    assert jar4.size == 12
    jar4.withdraw(7)
    assert jar4.size == 5
    with pytest.raises(ValueError):
        jar4.withdraw(7)

