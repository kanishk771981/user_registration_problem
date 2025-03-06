import re

def is_valid_first_name(name):
    """
    Validates if the first name:
    - Starts with a capital letter
    - Has a minimum of 3 characters
    - Contains exactly 1 special character
    """
    pattern = r'^[A-Z][a-zA-Z]{1,}[^\w\s][a-zA-Z]*$'  # Ensures one special character at any position

    special_char_pattern = r'[^\w\s]'  # Finds special characters (excluding letters and digits)
    special_chars = re.findall(special_char_pattern, name)

    if re.match(pattern, name) and len(special_chars) == 1:
        print(f"{name} is a Valid First Name.")
    else:
        print(f"{name} is an Invalid First Name. It must start with a capital letter, have at least 3 characters, and contain exactly 1 special character.")

# Function for checking the last name
def is_valid_last_name(last_name):
    """Validates if the last name starts with a capital letter and has a minimum of 3 characters."""
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    
    if re.match(pattern, last_name):
        print(f"{last_name} is a Valid Last Name.")
    else:
        print(f"{last_name} is an Invalid Last Name.")

# Function for checking correct email address
def is_valid_email(email):
    """
    - Three mandatory parts: local part (abc), domain name (bl), and main domain (co).
    - Two optional parts: subdomain (xyz) and country code (in).
    - Precise positions for '@' and '.'.
    """
    pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$'
    
    if re.match(pattern, email):
        print(f"{email} is a Valid Email Address.")
    else:
        print(f"{email} is an Invalid Email Address.")

# Function to check correct mobile number format
def is_valid_mobile(mobile):
    """
    - Starts with a 2-digit country code.
    - Followed by a space.
    - Followed by a 10-digit number.
    """
    pattern = r'^[0-9]{2} [0-9]{10}$'
    
    if re.match(pattern, mobile):
        print(f"{mobile} is a Valid Mobile Number.")
    else:
        print(f"{mobile} is an Invalid Mobile Number.")

# Function for checking password rules
def is_valid_password(password):
    """
    - Minimum 8 characters.
    - At least 1 uppercase letter.
    - At least 1 numeric digit.
    - Exactly 1 special character.
    """
    pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'  # Ensures at least 8 chars, 1 uppercase, and 1 digit
    special_char_pattern = r'[^\w\s]'  # Finds special characters

    special_chars = re.findall(special_char_pattern, password)

    if re.match(pattern, password) and len(special_chars) == 1:
        print(f"{password} is a Valid Password.")
    else:
        print(f"{password} is an Invalid Password. It must have at least 8 characters, 1 uppercase letter, 1 numeric digit, and exactly 1 special character.")

# User input for first name
first_name = input("Enter your First Name: ")
is_valid_first_name(first_name)

# User input for last name
last_name = input("Enter your Last Name: ")
is_valid_last_name(last_name)

# User input for email address
email = input("Enter an email address: ")
is_valid_email(email)

# User input for mobile number
mobile = input("Enter your mobile number: ")
is_valid_mobile(mobile)

# User input for password
password = input("Enter your password: ")
is_valid_password(password)






