# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

from Model.user import User, Admin, Employee
from View.user_view import UserViewer, AdminViewer, EmployeeViewer
from View.view import get_user_choice
from View.animator import Animator
from Controller.payment_controller import PaymentController


class UserController:

    # 1. User-defined function to get sign-in with
    @staticmethod
    def get_sign_with():
        prompt = "Your trying to sign-in with \n\t1.Username\t\t2.Email-id\t\t3.UserId\n"
        user_choice = get_user_choice(prompt, valid_choices=[1, 2, 3])
        return user_choice

    # 2. User-defined function to sign-in into the application with username
    @staticmethod
    def sign_in_core(case):
        __user_id = None
        flag = True
        while flag:
            values = UserViewer.get_user_credentials(case)
            status = User.validate_sign_in_info(case, values[0], values[1])
            if status:
                flag = not status[0]
                __user_id = status[1]
                UserViewer.show_login_result(status[0])
            else:
                UserViewer.show_login_result(status)
        return __user_id

    # 3. User-defined function to sign-in into the application
    @staticmethod
    def sign_in_controller():
        UserViewer.sign_in_header()
        case = UserController.get_sign_with()
        __user_id = UserController.sign_in_core(case)
        return __user_id

    # 4. User-defined function to sign-up into the application
    @classmethod
    def sign_up_controller(cls):
        flag = True
        UserViewer.sign_up_header()
        __username = ''
        while flag:
            __username = UserViewer.get_user_details(1)
            flag = User.username_validation(__username)
            if flag:
                prompt = "This username is already exist\n 1.Try to enter another username or 2.try log in with that username ?\n"
                valid_choice = [1, 2]
                user_choices = get_user_choice(prompt, valid_choice)
                if user_choices == 2:
                    return None
            elif flag is None:
                UserViewer.display_validation_result(1)
                flag = True

        flag = True
        __password = ''

        while flag:
            __password = UserViewer.get_user_details(2)
            flag = User.password_validation(__password)
            if flag:
                UserViewer.display_validation_result(2)

        flag = True
        __phone = 0

        while flag:
            __phone = UserViewer.get_user_details(3)
            flag = User.phone_no_validation(__phone)
            if flag:
                UserViewer.display_validation_result(3)
            elif flag is None:
                UserViewer.display_validation_result(3.2)
                flag = True

        flag = True
        __email_id = ''

        while flag:
            __email_id = UserViewer.get_user_details(4)
            flag = User.email_id_validation(__email_id)
            if flag:
                prompt = "This email Id is already linked with another account\n 1.Try to enter another email Id or 2.try log in with that email Id ?\n"
                valid_choice = [1, 2]
                user_choices = get_user_choice(prompt, valid_choice)
                if user_choices == 2:
                    return None
            elif flag is None:
                UserViewer.display_validation_result(4)
                flag = True
        User.create_user(__username, __password, __phone, __email_id)
        UserViewer.display_user_creation_result()

    # 5. User-defined function to show the user details
    @staticmethod
    def show_user_information(user_id):
        Animator.loading_animation(1, 'fetching data ')
        UserViewer.display_user_detail_header()
        result = User.fetch_user_detail(2, user_id)
        UserViewer.display_user_details(result)
        UserViewer.display_user_address(result[7:])

    # 6. User-defined function to get the date of birth
    @staticmethod
    def get_valid_dob():
        flag = True
        while flag:
            DOB = UserViewer.update_user_data(3)
            flag = Admin.validate_dob(2, DOB)
            if not flag:
                return DOB
            else:
                UserViewer.display_validation_result(5)

    # 7. User-defined function to update user information
    @staticmethod
    def update_user_information(user_id):
        flag = True
        UserViewer.updation_header()
        prompt = "Which details do you need to update \n\t1.First name,\n\t2.Last name,\n\t3.Date of Birth," \
                 "\n\t4.Phone number,\n\t5.Email Id,\n\t6.Address,\n\t7.Update all details,\n\t8.Back to dashboard\n"
        valid_choices = [1, 2, 3, 4, 5, 6, 7, 8]
        while flag:
            user_choice = get_user_choice(prompt, valid_choices)
            if user_choice == 1:
                values = UserViewer.update_user_data(1)
                User.update_user_data(1, values, user_id)
                Animator.loading_animation(1, 'committing changes')
                UserViewer.updation_footer()
            elif user_choice == 2:
                values = UserViewer.update_user_data(2)
                User.update_user_data(2, values, user_id)
                Animator.loading_animation(1, 'committing changes')
                UserViewer.updation_footer()
            elif user_choice == 3:
                values = UserController.get_valid_dob()
                User.update_user_data(3, values, user_id)
                Animator.loading_animation(1, 'committing changes')
                UserViewer.updation_footer()
            elif user_choice == 4:
                __phone = EmployeeController.update_phone()
                Employee.update_user_data(2, __phone, user_id)
            elif user_choice == 5:
                __email_id = EmployeeController.update_email_id()
                Employee.update_user_data(3, __email_id, user_id)
            elif user_choice == 6:
                values = UserViewer.update_user_data(4)
                User.update_user_data(4, values, user_id)
                Animator.loading_animation(1, 'committing changes')
                UserViewer.updation_footer()
            elif user_choice == 7:
                values = UserViewer.update_user_data(5)
                User.update_user_data(5, values, user_id)
                Animator.loading_animation(1, 'committing changes')
                UserViewer.updation_footer()
            elif user_choice == 8:
                break

    # 8. User-defined function to fetch last service request's details
    @staticmethod
    def fetch_last_service_request_details(user_id):
        Animator.loading_animation(1, 'fetching data ')
        result = User.fetch_last_service_details(user_id)
        UserViewer.display_last_service_request_details(result)

    # 9. User-defined function to check notification
    @staticmethod
    def check_notification(user_id):
        total = PaymentController.fetch_total(user_id)
        # result = User.fetch_notification(user_id)
        UserViewer.trigger_notification(total)


class AdminController(UserController):

    # 10. User-defined function to admin to create an employee
    @classmethod
    def sign_up_controller(cls):
        flag = True
        UserViewer.sign_up_header()
        __username = ''
        while flag:
            __username = UserViewer.get_user_details(1)
            flag = User.username_validation(__username)
            if flag:
                prompt = "This username is already exist do you want again to try to enter another username \n\t\t1.Yes\t2.No"
                valid_choice = [1, 2]
                user_choices = get_user_choice(prompt, valid_choice)
                if user_choices == 2:
                    return None
            elif flag is None:
                UserViewer.display_validation_result(1)
                flag = True

        flag = True
        __dob = ''

        while flag:
            __dob = UserViewer.get_user_details(5)
            flag = Admin.validate_dob(1, __dob)
            if flag:
                UserViewer.display_validation_result(5)

        flag = True
        __phone = 0

        while flag:
            __phone = UserViewer.get_user_details(3)
            flag = User.phone_no_validation(__phone)
            if flag:
                UserViewer.display_validation_result(3)
            elif flag is None:
                UserViewer.display_validation_result(3.2)
                flag = True

        flag = True
        __email_id = ''

        while flag:
            __email_id = UserViewer.get_user_details(4)
            flag = User.email_id_validation(__email_id)
            if flag:
                prompt = "This email Id is already linked with another account\n 1.Try to enter another email Id or 2.try log in with that email Id ?\n"
                valid_choice = [1, 2]
                user_choices = get_user_choice(prompt, valid_choice)
                if user_choices == 2:
                    return None
            elif flag is None:
                UserViewer.display_validation_result(4)
                flag = True
        Admin.create_user(__username, __dob, __phone, __email_id)
        UserViewer.display_user_creation_result()

    # 11. User-defined function to view employees list
    @staticmethod
    def view_employees():
        result = Admin.fetch_employees()
        AdminViewer.view_employees(result, 1)

    # 12. User-defined function to remove employee
    @classmethod
    def remove_employee(cls):
        result = Admin.fetch_employees()
        AdminViewer.view_employees(result, 2)
        user_id = AdminViewer.remove_employee()
        result = Admin.remove_employee(user_id)
        AdminViewer.remove_employee_result(result)


class EmployeeController(UserController):

    # 13. Overriding the show_user_information user-defined funtion to show employee's personal details
    @staticmethod
    def show_user_information(user_id):
        UserViewer.display_user_detail_header()
        result = Employee.fetch_user_detail(1, user_id)
        EmployeeViewer.display_user_details(result)

    # 14. Overriding the update_user_information user-defined funtion to update employee's personal details
    @classmethod
    def update_user_information(cls, user_id):
        flag = True
        UserViewer.updation_header()
        prompt = "Which details do you need to update \n\t1.Username,\n\t2.Phone\n\t3.Email Id\n\t4.Date of Birth," \
                 "\n\t5.Update all details\n\t6.Back to dashboard\n"
        valid_choices = [1, 2, 3, 4, 5, 6]
        while flag:
            user_choice = get_user_choice(prompt, valid_choices)
            if user_choice == 1:
                __username = EmployeeController.update_username()
                if __username:
                    Employee.update_user_data(1, __username, user_id)
            elif user_choice == 2:
                __phone = EmployeeController.update_phone()
                if __phone:
                    Employee.update_user_data(2, __phone, user_id)
            elif user_choice == 3:
                __email_id = EmployeeController.update_email_id()
                if __email_id:
                    Employee.update_user_data(3, __email_id, user_id)
            elif user_choice == 4:
                __dob = EmployeeController.update_dob()
                if __dob:
                    Employee.update_user_data(4, __dob, user_id)
            elif user_choice == 5:
                __username = EmployeeController.update_username()
                if __username:
                    Employee.update_user_data(1, __username, user_id)
                __phone = EmployeeController.update_phone()
                if __phone:
                    Employee.update_user_data(2, __phone, user_id)
                __email_id = EmployeeController.update_email_id()
                if __email_id:
                    Employee.update_user_data(3, __email_id, user_id)
                __dob = EmployeeController.update_dob()
                if __dob:
                    Employee.update_user_data(4, __dob, user_id)
            else:
                return

    # 15. User-defined funtion to update employee's username
    @staticmethod
    def update_username():
        while True:
            __username = EmployeeViewer.update_user_data(1)
            flag = User.username_validation(__username)
            if flag:
                prompt = "This username is already exist do you want again to try to enter another username \n\t\t1.Yes\t2.No\n"
                user_choices = get_user_choice(prompt, valid_choices=[1, 2])
                if user_choices == 2:
                    return None
            elif flag is None:
                UserViewer.display_validation_result(1)
                prompt = "Want to retry \n\t1.Yes\tor\t2.No\n"
                user_choices = get_user_choice(prompt, valid_choices=[1, 2])
                if user_choices == 2:
                    return None
            else:
                return __username

    # 16. User-defined funtion to update employee's phone number
    @staticmethod
    def update_phone():
        while True:
            __phone = EmployeeViewer.update_user_data(2)
            flag = User.phone_no_validation(__phone)
            if flag:
                prompt = "This phone number is already linked another account do you want\n\t1.Try again\t or \t2.Return to Updation dashboard\n"
                user_choices = get_user_choice(prompt, valid_choices=[1, 2])
                if user_choices == 2:
                    return None
            elif flag is None:
                UserViewer.display_validation_result(3)
                prompt = "Want to retry \n\t1.Yes\tor\t2.No\n"
                user_choices = get_user_choice(prompt, valid_choices=[1, 2])
                if user_choices == 2:
                    return None
            else:
                return __phone

    # 17. User-defined funtion to update employee's email
    @staticmethod
    def update_email_id():
        while True:
            __email_id = EmployeeViewer.update_user_data(3)
            flag = User.email_id_validation(__email_id)
            if flag:
                prompt = "This email Id is already linked another account do you want\n\t1.Retry entering another email Id\t or \t2.Return to Updation dashboard\n"
                user_choices = get_user_choice(prompt, valid_choices=[1, 2])
                if user_choices == 2:
                    return None
            elif flag is None:
                UserViewer.display_validation_result(4)
                prompt = "Want to retry \n\t1.Yes\tor\t2.No\n"
                user_choices = get_user_choice(prompt, valid_choices=[1, 2])
                if user_choices == 2:
                    return None
            else:
                return __email_id

    # 18. User-defined funtion to update employee's date of birth
    @staticmethod
    def update_dob():
        while True:
            __dob = EmployeeViewer.update_user_data(4)
            flag = Admin.validate_dob(1, __dob)
            if flag:
                UserViewer.display_validation_result(5)
                prompt = "Want to retry \n\t1.Yes\tor\t2.No\n"
                user_choices = get_user_choice(prompt, valid_choices=[1, 2])
                if user_choices == 2:
                    return None
            else:
                return __dob

# CLASSES   : 3, UserController, AdminController, EmployeeController
# FUNCTIONS : 18
