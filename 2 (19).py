# 31. Password Validator - PrepInsta
def validate_password(password):
    n = len(password)
    
    if n < 4:
        return "Invalid: Password must be at least 4 characters"
    
    if password[0].isdigit():
        return "Invalid: Password cannot start with a digit"
    
    has_digit = False
    has_upper = False
    
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
    
    if not has_digit or not has_upper:
        return "Invalid: Must contain at least one digit and one uppercase"
    
    return "Valid Password"

# Test
passwords = ["Pass123", "123Pass", "pass", "PASS", "Pass"]
for pwd in passwords:
    print(f"{pwd}: {validate_password(pwd)}")