def is_strong_password(pw):
    return len(pw) >= 12 and any(c.isdigit() for c in pw) and any(not c.isalnum() for c in pw)
