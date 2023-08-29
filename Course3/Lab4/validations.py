#!/usr/bin/env python3
import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    condition1 = len(username) >= minlen
    # Usernames can only use letters, numbers, dots, and underscores
    condition2 = re.match('^[a-z0-9._]+$', username) is not None
    # Usernames can't begin with a number
    condition3 = not username[0].isnumeric()

    return condition1 and condition2 and condition3

# Test cases
print(validate_user("username", 1))           # True
print(validate_user("user.name123", 2))      # False
print(validate_user("123username", 3))       # True
print(validate_user("user_name", 1))         # False
