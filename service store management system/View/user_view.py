# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

from View.animator import Animator
from View.view import get_user_choice
from tabulate import tabulate


class UserViewer:
    __username: str = ''
    __password: str = ''
    __email_id: str = ''
    __phone: int = 0

    # 1. User-defined function to display sign-up header
    @staticmethod
    def sign_up_header():
        text = "-> Sign-up <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105, "\n")

    # 2. User-defined function to get user details
    @classmethod
    def get_user_details(cls, case):
        if case == 1:
            __username = input("Enter the Username:\n")
            return __username
        if case == 2:
            __password = input("Enter the password:\n")
            return __password
        if case == 3:
            __phone = UserViewer.get_phone_no()
            return __phone
        if case == 4:
            __email_id = input("Enter the email:\n")
            return __email_id
        if case == 5:
            __dob = input("Enter the the year from the employee's date of birth(YYYY-mm-dd):\n")
            return __dob

    # 3. User-defined function to get phone number
    @classmethod
    def get_phone_no(cls):
        while True:
            try:
                phone = int(input("Enter your Mobile number:\n"))
            except(ValueError, TypeError, KeyboardInterrupt):
                print("Invalid entry !\nPlease try to enter a valid Mobile number\n")
            else:
                return phone

    # 4. User-defined function to display sign-in header
    @staticmethod
    def sign_in_header():
        text = "-> Sign-in <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105, "\n")

    # 5. User-defined function to get user credentials
    @staticmethod
    def get_user_credentials(case):
        if case == 1:
            print("Enter your username:")
            __value = input()
        if case == 2:
            print("Enter your email-Id:")
            __value = input()
        else:
            print("Enter your user-Id:")
            __value = input()
        print("Enter your password:")
        __password = input()
        return __value, __password

    # 6. User-defined function to display sign in result
    @staticmethod
    def show_login_result(is_valid):
        prompt = ("\n\t\t\t\t\tError!, invalid credentials\nWant retry to signing-in ? or "
                  "exit the"
                  "application.\n\t 1.Sign-in\t2.Exit\n")
        valid_choice = [1, 2]
        if is_valid:
            Animator.loading_animation(5, word=None)
            text = "logged-in successfully!"
            print(text.center(105))
        else:
            user_choice = get_user_choice(prompt, valid_choice)
            if user_choice == 1:
                return None
            elif user_choice == 2:
                quit()

    # 7. User-defined function to display validation result
    @staticmethod
    def display_validation_result(case):
        if case == 1:
            print("Invalid Username!\nPlease try to enter a valid username!\n")
        if case == 2:
            print("Invalid password!\nPlease try  to enter a valid password\n")
        if case == 3:
            print("Invalid entry !\nPlease try to enter a valid Mobile number\n")
        if case == 3.2:
            print(
                "This phone number is already link with another account\n\t Try to enter another number...")
        if case == 4:
            print("Invalid Email Id!\nPlease try to enter a valid email")
        if case == 5:
            print("Invalid Date Of Birth!\nPlease try to enter a valid Date Of Birth!\n")

    # 8. User-defined function to display user creation result
    @staticmethod
    def display_user_creation_result():
        Animator.loading_animation(1, 'upload data')
        print("\n"),
        text = ("-" * 25, ">Successfully registered as the User<", "-" * 25)
        print(text.count(105))

    # 9. User-defined function to display user details header
    @staticmethod
    def display_user_detail_header():
        text = "-> Details <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105, "\n")

    # 10. User-defined function to display user details
    @staticmethod
    def display_user_details(result):
        print("Customer ID:", result[0], "\t\t\t", "Username:", result[1])
        print("First Name:", result[2], "\t\t\t", "Last Name:", result[3])
        print("Date of Birth:", result[4], "\t\t  ", "Email ID:", result[5])
        print("Mobile Number:", result[6])

    # 11. User-defined function to display user's address
    @staticmethod
    def display_user_address(user_address):
        for i in range(len(user_address)):
            if i < 1:
                print("Address:", user_address[i], ",")
            elif i < len(user_address) - 1:
                print("\t\t", user_address[i], ",")
            else:
                print("\t\t", user_address[i], ".")

    # 12. User-defined function to display the update header
    @staticmethod
    def updation_header():
        text = "-> Updation <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105, "\n")

    # 13. User-defined function to display last service request details
    @staticmethod
    def display_last_service_request_details(result):
        text = "-> Service history <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105, "\n")
        # customer_id, service_id, device_type, model, defect, usaage, repair_status, time, price, payment_status
        if result is None:
            text = "Sorry!, there no service requests initiated by you"
            print(text.center(105))
        else:
            print("\tService_id\t\t\t:", result[0], "\n\tDevice type\t\t\t:", result[1], "\n\tModel name\t\t\t:",
                  result[2], "\n\tDefect Description  :", result[3], "\n\tUsage\t\t\t\t:", result[4],
                  "\n\tRepair status\t\t:", result[5], "\n\tService time\t\t:", result[8], "\n\tPrice\t\t\t\t:",
                  result[6], "\n\tPayment status\t\t:", result[7])

    # 14. User-defined function to update the user details
    @staticmethod
    def update_user_data(case):
        values = None
        if case == 1:
            print("Enter the your First name:")
            __first_name = input()
            return __first_name
        elif case == 2:
            print("Enter the your Last name:")
            __last_name = input()
            return __last_name
        elif case == 3:
            print("Enter the Your Date of Birth (YYYY-MM-DD):")
            __DOB = input()
            values = __DOB
        elif case == 4:
            print("Enter the Your address:")
            print("Door no:")
            door_no = input()
            print("Street name:")
            street = input()
            print("City:")
            city = input()
            print("State:")
            state = input()
            print("Pin code/ Postal code:")
            zip_code = input()
            print("Country:")
            country = input()
            values = [door_no, street, city, state, country, zip_code]
        elif case == 5:
            print("Enter the your First name:")
            __first_name = input()
            print("Enter the your Last name:")
            __last_name = input()
            print("Enter the Your Date of Birth (YYYY-MM-DD):")
            __DOB = input()
            print("Enter the Your address:")
            print("Door no:")
            door_no = input()
            print("Street name:")
            street = input()
            print("City:")
            city = input()
            print("State:")
            state = input()
            print("Pin code/ Postal code:")
            zip_code = input()
            print("Country:")
            country = input()
            values = [__first_name, __last_name, __DOB, door_no, street, city, state, country, zip_code]
        return values

    # 15. User-defined function to display dob result
    @staticmethod
    def display_dob_result():
        print('Invalid date of birth')

    # 16. User-defined function to display update result
    @staticmethod
    def updation_footer():
        print("\n", "-" * 25, ">Successfully updated the User Information<", "-" * 25, "\n")

    # 17. User-defined function to notification header
    @staticmethod
    def notification_header():
        text = "-> Notifications <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105, "\n")

    # 18. User-defined function to trigger notification
    @staticmethod
    def trigger_notification(total):
        i = 1
        prompt = str(i) + ".You have a pending bill amount of : Rs " + str(total) + "\n"
        if total is not None:
            UserViewer.notification_header()
            print(prompt.center(105))
        #     i = i + 1
        # if len(result):
        #     text = str(i) + ".The service request rose by you has been completed it service\n"
        #     print(text.center(105))
        else:
            text = "You have no notification"
            print(text.center(105))
            i = 0
        if i:
            print("please navigate to make your payments to pay the remaining bill\n\n")


class AdminViewer:

    # 19. User-defined function to display employee creator header
    @staticmethod
    def employee_creator_header(case):
        if case == 1:
            text = "-> Employee creator <-"
            print("_" * 105, "\n", text.center(105))
            print("_" * 105, "\n")
        else:
            Animator.loading_animation(1, word='Uploading data')
            print("\n")
            text = "-" * 34 + "-> Successfully created an employee <-" + "-" * 34
            print(text.center(105))

    # 20. User-defined function to display employees list
    @staticmethod
    def view_employees(result, case):
        text = "-> Employees list <-"
        if case == 1:
            print("_" * 105, "\n", text.center(105))
            print("_" * 105, "\n")
        else:
            print(text.center(105))
        if len(result):
            header = ["Employee_id", "Username"]
            print(tabulate(result, headers=header, tablefmt="grid"))
        else:
            text = 'There are no employees currently'
            print(text.center(105))

    # 21. User-defined function to remove the employee
    @staticmethod
    def remove_employee():
        text = "-> Remove employee <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105, "\n")
        print("Enter the employee_id:\n")
        __employee_id = input()
        return __employee_id

    # 22. User-defined function to display remove employee result
    @staticmethod
    def remove_employee_result(result):
        if result is None:
            text = "-> Successfully removed the employee <-"
            print(text.center(105))
        else:
            text = "-> Failed to remove the employee <-"
            print(text.center(105))


class EmployeeViewer(UserViewer):

    # 23. Overriding the User-defined function display user details to display the employee's details
    @staticmethod
    def display_user_details(result):
        print("Customer ID\t  :", result[1], "\nUsername\t  :", result[0])
        print("Date of Birth :", result[4], "\nEmail ID\t  :", result[3])
        print("Mobile Number :", result[2])

    # 25. Overriding the User-defined function update user data to update the employee's details
    @staticmethod
    def update_user_data(case):
        value = None
        if case == 1:
            prompt = "Enter the username\n"
            value = input(prompt)
        elif case == 2:
            value = UserViewer.get_phone_no()
        elif case == 3:
            prompt = "Enter the email Id\n"
            value = input(prompt)
        elif case == 4:
            prompt = "Enter the Date of birth\n"
            value = input(prompt)
        elif case == 5:
            pass
        elif case == 6:
            pass
        return value

# CLASSES   : 03, UserViewer, AdminViewer, EmployeeViewer
# FUNCTIONS : 24
