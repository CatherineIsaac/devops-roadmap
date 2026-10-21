from password_checker import is_strong_password

def test_short_password_fails():
    assert not is_strong_password("abc1")

def test_long_password_with_digit_and_symbol_passes():
    assert is_strong_password("correcthorse9battery!")

def test_password_without_symbol_fails():
    assert not is_strong_password("correcthorse9battery")
