# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

import re
from fetch_property import fetch_property
from Model.connect_db import db_manager
from Model.model import get_timestamp, generate_sha256_hash


class User:
    # 1. User-defined function to check user roles
    @staticmethod
    def check_user_role(user_id):
        case = user_id[0:3]
        if case == 'CUS':
            role = 'CUSTOMER'
        elif case == 'ADM':
            role = 'ADMIN'
        else:
            role = 'EMPLOYEE'
        return role

    @staticmethod
    # 2.User-defined function to generate Customer_id
    def generate_user_id(case, username="", phone=""):
        user_id = ''
        username = re.sub(r"\s+", " ", username)
        username = username.upper()
        if case == 1:
            user_id = "CUS" + username[:2] + phone[:5]
        elif case == 2:
            user_id = "EMP" + username[:2] + phone[:5]
        return user_id

    # 3.User-defined function to validate the user_ credentials
    @staticmethod
    def validate_sign_in_info(case, key1, __password):
        hash_value = generate_sha256_hash(__password)
        query = None
        if case == 1:
            query = fetch_property('validate', 'CHECK_CREDENTIALS1')
        elif case == 2:
            query = fetch_property('validate', 'CHECK_CREDENTIALS2')
        elif case == 3:
            query = fetch_property('validate', 'CHECK_CREDENTIALS3')
        result = db_manager.query_execute(3, query, (key1,))
        try:
            __customer_id = result[0]
            credentials = result[2]
        except TypeError:
            return False
        else:
            if credentials == hash_value:
                return True, __customer_id
            else:
                return False

    # 4.User-defined function to generate check existing user or not
    @staticmethod
    def check_existing_user(value="", case=0):
        result = ""
        values = (value,)
        if case == 1:
            query = fetch_property('validate', 'CHECK_USERNAME')
            result = db_manager.query_execute(3, query, values)
        elif case == 2:
            query = fetch_property('validate', 'CHECK_PHONE')
            result = db_manager.query_execute(3, query, values)
        elif case == 3:
            query = fetch_property('validate', 'CHECK_EMAIL')
            result = db_manager.query_execute(3, query, values)
        return result is not None

    # 5.User-defined function to validate username
    @staticmethod
    def username_validation(username):
        regex = fetch_property('user', 'USERNAME_PATTERN')
        rule = re.compile(regex)
        if re.search(rule, username):
            result = User.check_existing_user(username, 1)
            if result:
                return True
            else:
                return False
        else:
            return None

    # 6. User-defined function to validate password
    @staticmethod
    def password_validation(password):
        regex = fetch_property('user', 'PASSWORD_PATTERN')
        rule = re.compile(regex)
        if re.search(rule, password):
            return False
        else:
            return True

    # 7. User-defined function to validate mobile number
    @staticmethod
    def phone_no_validation(phone):
        if 6000000000 < phone < 10000000000:
            if User.check_existing_user(str(phone), 2):
                return True
            else:
                return False
        else:
            return True

    # 8. User-defined function to validate email-id
    @staticmethod
    def email_id_validation(email_id):
        email_id_pattern = fetch_property('user', 'EMAIL_ID_PATTERN')
        rule = re.compile(email_id_pattern)
        if re.search(rule, email_id):
            if User.check_existing_user(email_id, 3):
                return True
            else:
                return False
        else:
            return None

    # 9. User-defined function to create user
    @classmethod
    def create_user(cls, username, password, phone, email_id):
        customer_id = User.generate_user_id(1, username, str(phone))
        date1 = get_timestamp(3)
        password = generate_sha256_hash(password)
        query = fetch_property('insert', 'INSERT_USER_CREDENTIALS')
        values = (customer_id, username, password, str(phone), email_id, date1)
        db_manager.query_execute(1, query, values)
        timestamp = get_timestamp(2)
        query = fetch_property('insert', 'INSERT_USER_DATA')
        values = (customer_id, username, None, None, None, email_id, str(phone), None, timestamp)
        db_manager.query_execute(1, query, values)
        query = fetch_property('insert', 'INSERT_ADDRESS')
        values = (customer_id, None, None, None, None, None, None, timestamp)
        db_manager.query_execute(1, query, values)

    # 10. User-defined function to fetch user-details
    @staticmethod
    def fetch_user_detail(case, user_id):
        if case == 1:
            name = ''
            query = fetch_property('user_query', 'FETCH_NAME')
            values = (user_id,)
            result = db_manager.query_execute(3, query, values)
            try:
                name = result[2] + " " + result[3]
            except TypeError:
                name = result[1]
            finally:
                return name
        if case == 2:
            values = (user_id, user_id)
            query = fetch_property('user_query', 'FETCH_USER_DATA')
            result = db_manager.query_execute(3, query, values)
            return result
        if case == 3:
            values = (user_id,)
            query = fetch_property('user_query', 'FETCH_ADDRESS')
            result = db_manager.query_execute(3, query, values)
            return result

    # 11. User-defined function to update user-details
    @classmethod
    def update_user_data(cls, case, value, __user_id):
        if case == 1:
            query = fetch_property('user_query', 'UPDATE_FIRST_NAME')
            timestamp = get_timestamp(2)
            values = (value, timestamp, __user_id)
            db_manager.query_execute(2, query, values)
        elif case == 2:
            query = fetch_property('user_query', 'UPDATE_LAST_NAME')
            timestamp = get_timestamp(2)
            values = (value, timestamp, __user_id)
            db_manager.query_execute(2, query, values)
        elif case == 3:
            print("Enter the Your Date of Birth (YYYY-MM-DD):")
            __DOB = input()
            query = fetch_property('user_query', 'UPDATE_DOB')
            timestamp = get_timestamp(2)
            values = (__DOB, timestamp, __user_id)
            db_manager.query_execute(2, query, values)
        elif case == 4:
            query = fetch_property('user_query', 'UPDATE_ADDRESS')
            timestamp = get_timestamp(2)
            values = (value[0], value[1], value[2], value[3], value[4], value[5], timestamp, __user_id)
            db_manager.query_execute(2, query, values)
        elif case == 5:
            query = fetch_property('user_query', 'UPDATE_USER_DATA')
            timestamp = get_timestamp(2)
            values = (value[0], value[1], value[2], timestamp, __user_id)
            db_manager.query_execute(2, query, values)
            query = fetch_property('user_query', 'UPDATE_ADDRESS')
            timestamp = get_timestamp(2)
            values = (value[3], value[4], value[5], value[6], value[7], value[8], timestamp, __user_id)
            db_manager.query_execute(2, query, values)

    # 12. User-defined function to fetch notification
    @staticmethod
    def fetch_notification(user_id):
        query = fetch_property('user_query', 'FETCH_NOTIFICATION')
        result = db_manager.query_execute(4, query, (user_id,))
        return result is not None

    # 13. User-defined function to fetch last service details
    @staticmethod
    def fetch_last_service_details(user_id):
        query = fetch_property('service_query', 'FETCH_LAST_SERVICE_DETAILS')
        result = db_manager.query_execute(3, query, (user_id,))
        return result


class Admin(User):

    # 14. User-defined function to generate password with username and year from Date of birth
    @staticmethod
    def auto_generate_password(name, dob):
        year, month, day = map(int, dob.split('-'))
        password = name + "@" + str(year)
        return password

    # 15. User-defined function to validate user Date of birth
    @staticmethod
    def validate_dob(case, dob):
        dob_pattern = fetch_property('user', 'DOB_PATTERN')
        current_year = get_timestamp(6)
        if case == 1:
            if re.match(dob_pattern, dob):
                year, month, day = map(int, dob.split('-'))
                if current_year - year >= 21 and 0 < month < 13:
                    return False
            return True
        else:
            if re.match(dob_pattern, dob):
                year, month, day = map(int, dob.split('-'))
                if current_year - year >= 15 and 0 < month < 13:
                    return False
            return True

    # 16. Overriding  the create user User-defined function to create employee
    @classmethod
    def create_user(cls, username, dob, phone, email_id):
        __employee_id = Admin.generate_user_id(2, username, str(phone))
        date1 = get_timestamp(3)
        __password = Admin.auto_generate_password(username, dob)
        __password = generate_sha256_hash(__password)
        query = fetch_property('insert', 'INSERT_USER_CREDENTIALS')
        values = (__employee_id, username, __password, str(phone), email_id, date1)
        db_manager.query_execute(1, query, values)
        timestamp = get_timestamp(2)
        query = fetch_property('insert', 'INSERT_USER_DATA')
        values = (__employee_id, username, None, None, dob, email_id, str(phone), None, timestamp)
        db_manager.query_execute(1, query, values)
        query = fetch_property('insert', 'INSERT_ADDRESS')
        values = (__employee_id, None, None, None, None, None, None, timestamp)
        db_manager.query_execute(1, query, values)

    # 17. User-defined function to fetch Employee list
    @classmethod
    def fetch_employees(cls):
        query = ""
        result = db_manager.query_execute(4, query, values=None)
        return result

    # 18. User-defined function to remove Employee
    @classmethod
    def remove_employee(cls, user_id):
        values = (user_id,)
        query = fetch_property('admin_query', 'DELETE_EMPLOYEE_FROM_USER_CREDENTIALS')
        db_manager.query_execute(2, query, values)
        query = fetch_property('admin_query', 'DELETE_EMPLOYEE_FROM_USER_DATA')
        db_manager.query_execute(2, query, values)
        query = fetch_property('admin_query', 'DELETE_EMPLOYEE_FROM_USER_ADDRESS')
        db_manager.query_execute(2, query, values)
        query = fetch_property('admin_query', 'CHECK_EMPLOYEE')
        result = db_manager.query_execute(3, query, values)
        return result


class Employee(User):

    # 19. Overriding  the update user date User-defined function to fetch employee's details
    @staticmethod
    def fetch_user_detail(case, user_id):
        query = "select username, customer_id, phone, email_id, dob from user_data where customer_id = %s"
        result = db_manager.query_execute(3, query, (user_id,))
        return result

    # 20. Overriding  the update user date User-defined function to update employee's details
    @classmethod
    def update_user_data(cls, case, value, user_id):
        result = None
        if case == 1:
            query = fetch_property('user_query', 'UPDATE_USERNAME_IN_USER_CREDENTIALS')
            db_manager.query_execute(3, query, (value, user_id))
            query = fetch_property('user_query', 'UPDATE_USERNAME_IN_USER_DATA')
            db_manager.query_execute(3, query, (value, user_id))
        elif case == 2:
            query = fetch_property('user_query', 'UPDATE_PHONE')
            db_manager.query_execute(2, query, (value, user_id))
        elif case == 3:
            query = fetch_property('user_query', 'UPDATE_EMAIL')
            db_manager.query_execute(2, query, (value, user_id))
        elif case == 4:
            query = fetch_property('user_query', 'UPDATE_DOB')
            db_manager.query_execute(2, query, (value, user_id))

        return result


# CLASSES   : 3, USER, ADMIN, EMPLOYEE
# FUNCTIONS : 20
