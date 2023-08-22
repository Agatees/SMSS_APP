# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

import hashlib
from datetime import date, datetime


# 1. User-defined function to convert password into a hash value
def generate_sha256_hash(value):
    sha256_hash = hashlib.sha256(value.encode()).hexdigest()
    return sha256_hash


# 2. User-defined function to get timestamp
def get_timestamp(case=0):
    # gets the current timestamp
    value = datetime.now()
    timestamp = datetime.timestamp(value)
    # gets the current month
    current_month = value.month
    # gets the current year
    current_year = value.year
    # gets the current date
    value = date.today()
    # Format the datetime object as a string
    dt = datetime.fromtimestamp(timestamp)
    # Format the datetime object as a string
    formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
    current_time = datetime.now().time()
    time_string = current_time.strftime("%I:%M:%S %p")
    # function call for timestamp
    if case == 1:
        return timestamp
    # function call for date and time
    elif case == 2:
        return formatted_datetime
    # function call for date
    elif case == 3:
        return value
    # function call for time with local format
    elif case == 4:
        return time_string
    # function call for time with current month
    elif case == 5:
        return current_month
    # function call for time with current year
    elif case == 6:
        return current_year

# CLASSES   : 0
# FUNCTIONS : 2
