from seasons import seasons
import pytest

def test_main():
    assert seasons("2024-08-08") == "One thousand, four hundred forty minutes"
    assert seasons("2024-08-07") == "Two thousand, eight hundred eighty minutes"
