# Prompt to the user to enter a password
prompt = input("Tell me your password: ")

# Find the first letter of the password
first_letter = prompt[0]

# Convert to uppercase
first_letter = first_letter.upper()

# Show the first letter
print(f'The first letter you entered was: {first_letter}')