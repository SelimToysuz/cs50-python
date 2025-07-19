from twttr import shorten

def test_banned():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("David Malan") == "Dvd Mln"

def test_irrelevant():
    assert shorten("") == ""
    assert shorten("123!") == "123!"
