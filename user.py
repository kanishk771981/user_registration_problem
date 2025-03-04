import re

def is_valid_first_name(name):
    """
    Validates if the first name starts with a capital letter and has a minimum of 3 characters.
    """
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    
    if re.match(pattern, name):
        print(f"{name} is a Valid First Name.")
    else:
        print(f"{name} is an Invalid First Name.")

#function for checking the last name
def is_valid_last_name(last_name):
    """Validates if the last name starts with a capital letter and has a minimum of 3 characters."""
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    
    if re.match(pattern, last_name):
        print(f"{last_name} is a Valid Last Name.")
    else:
        print(f"{last_name} is an Invalid Last Name.")

#function for checking correct enail address 
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

#function to check correct mobile number format
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


# user input for first namme
first_name = input("Enter your First Name: ")
is_valid_first_name(first_name)

#user input for last name 
last_name = input("Enter your Last Name: ")
is_valid_last_name(last_name)

#user input for email address
email = input("Enter an email address: ")
is_valid_email(email)

#user input for mobile number
mobile = input("Enter ypur mobile number:")
is_valid_mobile(mobile)







