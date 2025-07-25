from working import convert
import pytest

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("17 AM to 17 PM")
    with pytest.raises(ValueError):
        convert("cat")
