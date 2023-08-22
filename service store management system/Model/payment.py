# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :
import re
from fetch_property import fetch_property
from Model.model import get_timestamp
from Model.connect_db import db_manager


class Payment:

    # 1. User-defined function to fetch total
    @staticmethod
    def calculate_total(user_id):
        query = fetch_property('payment_query', 'FETCH_TOTAL')
        result = db_manager.query_execute(3, query, (user_id,))
        return result[0]

    # 2. User-defined function to validate card number
    @staticmethod
    def is_luhn_valid(card_number):
        card_number = str(card_number).replace(" ", "")  # Remove any spaces
        if not card_number.isdigit():
            return False  # The card number must contain only digits
        digits = [int(digit) for digit in card_number]
        # Double every second digit from the right
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        # Sum all the digits, including the doubled ones
        checksum = sum(digits)
        # Check if the checksum is divisible by 10
        return checksum % 10 == 0

    # 3. User-defined function to validate month in expiry date
    @staticmethod
    def validate_month(valid_month):
        current_month = get_timestamp(5)
        if 1 <= valid_month < 13 and valid_month >= current_month:
            return False
        else:
            return True

    # 4. User-defined function to validate year in expiry date
    @staticmethod
    def validate_year(valid_year):
        current_year = get_timestamp(6)
        if valid_year >= current_year:
            return False
        else:
            return True

    # 5. User-defined function to validate CCV
    @staticmethod
    def validate_ccv(ccv):
        ccv_pattern = fetch_property('payment', 'CCV_PATTERN')
        rule = re.compile(ccv_pattern)
        if re.search(rule, ccv):
            return False
        else:
            return True

    # 6. User-defined function to validate PIN
    @staticmethod
    def validate_pin(pin):
        pin_pattern = fetch_property('payment', 'PIN_PATTERN')
        rule = re.compile(pin_pattern)
        if re.search(rule, str(pin)):
            return False
        else:
            return True

    # 7. User-defined function to validate Bank Name
    @staticmethod
    def validate_bank_name(bank_name):
        query = fetch_property('payment', 'CHECK_BANK')
        result = db_manager.query_execute(3, query, (bank_name,))
        return result is None

    # 8. User-defined function to validate Username
    @staticmethod
    def validate_bank_username(username):
        username_pattern = fetch_property('user', 'USERNAME_PATTERN')
        rule = re.compile(username_pattern)
        if re.search(rule, username):
            return False
        else:
            return True

    # 9. User-defined function to validate Password
    @staticmethod
    def validate_bank_password(password):
        password_pattern = fetch_property('user', 'PASSWORD_PATTERN')
        rule = re.compile(password_pattern)
        if re.search(rule, password):
            return False
        else:
            return True

    # 10. User-defined function to validate UPI ID
    @staticmethod
    def validate_upi_id(upi_id):
        upi_id_pattern = fetch_property('payment', 'UPI_ID_PATTERN')
        rule = re.compile(upi_id_pattern)
        if re.search(rule, upi_id):
            return False
        else:
            return True

    # 11. User-defined function to update payment status
    @staticmethod
    def update_payment_status(customer_id):
        query = fetch_property('payment_query', 'FETCH_SERVICE_ID')
        result = db_manager.query_execute(4, query, (customer_id,))
        for row in result:
            list1 = row
            query = fetch_property('payment_query', 'UPDATE_PAYMENT_STATUS1')
            values = (fetch_property('payment', 'PAYMENT_STATUS3'), customer_id, list1[0])
            db_manager.query_execute(4, query, values)
            query = fetch_property('payment_query', 'UPDATE_PAYMENT_STATUS2')
            db_manager.query_execute(2, query, (fetch_property('payment', 'PAYMENT_STATUS3'), list1[0],))


class Bill:
    # 12. User-defined function to fetch bill
    @staticmethod
    def fetch_bill_details(user_id):
        query = fetch_property('payment_query', 'FETCH_BILL')
        result = db_manager.query_execute(4, query, (user_id,))
        return result

# CLASSES   : 2, Payment, Bill
# FUNCTIONS : 12
