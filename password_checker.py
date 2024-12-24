import random
import string

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "@#$%^&*!"
    return ''.join(random.choice(characters) for _ in range(12))

# Suggest improvement
def suggest_improvement(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Increase length to at least 8 characters.")
    if not re.search("[A-Z]", password):
        suggestions.append("Add at least one uppercase letter.")
    if not re.search("[0-9]", password):
        suggestions.append("Include at least one number.")
    if not re.search("[@#$%^&*!]", password):
        suggestions.append("Include at least one special character.")
    return suggestions

# Example usage
password = input("Enter your password: ")
strength = password_strength(password)
print("Password Strength:", strength)
if strength != "Strong":
    print("Suggestions:", suggest_improvement(password))
    print("Generated Strong Password:", generate_strong_password())
