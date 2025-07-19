import fuel
import pytest

def test_convert():
    with pytest.raises(ValueError):
        fuel.convert("a/b")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("3/0")
    assert fuel.convert("3/5") == 60


def test_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(5) == "5%"
    assert fuel.gauge(99) == "F"
