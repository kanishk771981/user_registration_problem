import re
import logging

# Configure logging
logging.basicConfig(
    filename="validation.log",  # Ensure this path is writable
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def is_valid_first_name(name):
    """
    Validates if the first name:
    - Starts with a capital letter
    - Has a minimum of 3 characters
    
    """
   
    pattern = r'^[A-Z][a-zA-Z]{2,}$'

    if re.match(pattern, name):
        logging.info(f"Valid First Name: {name}")
        print(f"{name} is a Valid First Name.")
    else:
        logging.error(f"Invalid First Name: {name}")
        print(f"{name} is an Invalid First Name.")

def is_valid_last_name(last_name):
    """Validates if the last name starts with a capital letter and has a minimum of 3 characters."""
    pattern = r'^[A-Z][a-zA-Z]{2,}$'

    if re.match(pattern, last_name):
        logging.info(f"Valid Last Name: {last_name}")
        print(f"{last_name} is a Valid Last Name.")
    else:
        logging.error(f"Invalid Last Name: {last_name}")
        print(f"{last_name} is an Invalid Last Name.")

def is_valid_email(email):
    """Validates the email format as per defined structure."""
    pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$'

    if re.match(pattern, email):
        logging.info(f"Valid Email: {email}")
        print(f"{email} is a Valid Email Address.")
    else:
        logging.error(f"Invalid Email: {email}")
        print(f"{email} is an Invalid Email Address.")

def is_valid_mobile(mobile):
    """Validates the mobile number format (Country code + 10-digit number)."""
    pattern = r'^[0-9]{2} [0-9]{10}$'

    if re.match(pattern, mobile):
        logging.info(f"Valid Mobile Number: {mobile}")
        print(f"{mobile} is a Valid Mobile Number.")
    else:
        logging.error(f"Invalid Mobile Number: {mobile}")
        print(f"{mobile} is an Invalid Mobile Number.")

def is_valid_password(password):
    """
    - Minimum 8 characters.
    - At least 1 uppercase letter.
    - At least 1 numeric digit.
    - Exactly 1 special character.
    """
    pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'  # Ensures at least 8 chars, 1 uppercase, and 1 digit
    special_chars = re.findall(r'[^\w\s]', password)  # Finds special characters

    if re.match(pattern, password) and len(special_chars) == 1:
        logging.info(f"Valid Password: {password}")
        print(f"{password} is a Valid Password.")
    else:
        logging.error(f"Invalid Password: {password}")
        print(f"{password} is an Invalid Password. It must have at least 8 characters, 1 uppercase letter, 1 numeric digit, and exactly 1 special character.")

# User Inputs
first_name = input("Enter your First Name: ")
is_valid_first_name(first_name)

last_name = input("Enter your Last Name: ")
is_valid_last_name(last_name)

email = input("Enter an Email Address: ")
is_valid_email(email)

mobile = input("Enter your Mobile Number: ")
is_valid_mobile(mobile)

password = input("Enter your Password: ")
is_valid_password(password)








