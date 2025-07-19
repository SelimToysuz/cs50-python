from bank import value

def test_value():
    assert value("Hello...") == 0
    assert value("hello!") == 0
    assert value("hey!") == 20
    assert value("Hi") == 20
    assert value("") == 100
    assert value("selam") == 100

