import re

def check_password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1  # Length requirement met
    if re.search(r'[A-Z]', password):
        score += 1  # Uppercase letter requirement met
    if re.search(r'[a-z]', password):
        score += 1  # Lowercase letter requirement met
    if re.search(r'[0-9]', password):
        score += 1  # Digit requirement met
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1  # Special character requirement met

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength

# Main program
if __name__ == "__main__":
    while True:
        user_password = input("Enter your password to check its strength (or type 'exit' to quit): ")
        if user_password.lower() == 'exit':
            print("Exiting the password checker.")
            break
        strength = check_password_strength(user_password)
        print(f"Password strength: {strength}")
