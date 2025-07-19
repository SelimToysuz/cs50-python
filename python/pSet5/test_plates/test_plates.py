from plates import is_valid

def test_is_valid():
    assert is_valid("55555") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("ALIBABANINCIFTLIGI") == False
    assert is_valid("CS5A0") == False
    assert is_valid("CS,50") == False
