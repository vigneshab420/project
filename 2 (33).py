# 24. Remove Hyphens - PrepInsta
def remove_hyphens(text):
    return text.replace("-", "")

# Test the function
phone = "123-456-7890"
print(f"Original: {phone}")
print(f"Without hyphens: {remove_hyphens(phone)}")