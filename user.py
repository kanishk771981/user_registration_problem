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


# user input for first namme
first_name = input("Enter your First Name: ")
is_valid_first_name(first_name)

#user imput for last name 
last_name = input("Enter your Last Name: ")
is_valid_last_name(last_name)



