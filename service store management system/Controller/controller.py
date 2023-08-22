# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

from View.view import get_user_choice
from View.dashboard_view import HomeViewer
from View.animator import Animator
from Model.model import get_timestamp
from Model.connect_db import db_manager
from Model.user import User
from Controller.user_controller import UserController, AdminController, EmployeeController
from Controller.service_controller import ServiceController
from Controller.payment_controller import PaymentController


class Home:
    # 1. User-defined function to start the application
    @staticmethod
    def greetings():
        user_id = None
        HomeViewer.greetings_header()
        prompt = "\nExisting User ?\n\t1.Yes\t2.No\n"
        valid_choice = [1, 2]
        user_choice = get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            user_id = UserController.sign_in_controller()
        elif user_choice == 2:
            prompt1 = "Want to register as a user or exit the application?\n\t1.Sign-up\t2.Exit\n"
            user_choice = get_user_choice(prompt1, valid_choice)
            if user_choice == 1:
                UserController.sign_up_controller()
                user_id = UserController.sign_in_controller()
            elif user_choice == 2:
                quit()
        Home.dashboard(user_id)

    # 2. User-defined function to check user's role
    @staticmethod
    def dashboard(user_id):
        date = get_timestamp(3)
        time = get_timestamp(4)
        name = User.fetch_user_detail(1, user_id)
        role = User.check_user_role(user_id)
        if role == 'ADMIN':
            Home.admin_side_dashboard(user_id, name, date, time)
        elif role == 'CUSTOMER':
            Home.customer_side_dashboard(user_id, name, date, time)
        else:
            Home.employee_side_dashboard(user_id, name, date, time)

    # 3. User-defined function to handle Employee's dashboard functionalities
    @staticmethod
    def employee_side_dashboard(user_id, name, date, time):
        HomeViewer.decoration(name, date, time)
        flag = True
        valid_choice = [1, 2, 3, 4, 5, 6, 7, 8]
        prompt = "\n1.View pending all service requests\n2.Assign a service request\n3.View service requests handled by me\n4.Update the service status\n5.Update the service cost\n6.View personal details\n7.Update personal details\n8.Sign out\n"
        user_choice = get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            ServiceController.view_pending_service_requests()
        elif user_choice == 2:
            ServiceController.assign_service_request(name)
        elif user_choice == 3:
            Animator.loading_animation(1, 'fetching service request details')
            ServiceController.view_employee_service_request(name)
        elif user_choice == 4:
            ServiceController.update_service_status(name)
        elif user_choice == 5:
            service_id = ServiceController.update_service_cost(name)
            ServiceController.auto_update_payment_status(service_id)
        elif user_choice == 6:
            EmployeeController.show_user_information(user_id)
        elif user_choice == 7:
            EmployeeController.update_user_information(user_id)
        elif user_choice == 8:
            flag = Home.sign_out(name)
        if flag:
            Home.employee_side_dashboard(user_id, name, date, time)

    # 4. User-defined function to handle admins dashboard functionalities
    @staticmethod
    def admin_side_dashboard(user_id, name, date, time):
        flag = True
        HomeViewer.decoration(name, date, time)
        valid_choice = [1, 2, 3, 4, 5]
        prompt = '\n1.Add employee\n2.View Employees\n3.Remove employee\n4.View stats(Under-development)\n5.Sign out\n'
        user_choice = get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            AdminController.sign_up_controller()
        elif user_choice == 2:
            AdminController.view_employees()
        elif user_choice == 3:
            AdminController.remove_employee()
        elif user_choice == 4:
            pass
        elif user_choice == 5:
            flag = Home.sign_out(name)
        if flag:
            Home.admin_side_dashboard(user_id, name, date, time)

    # 5. User-defined function to handle Customer's dashboard functionalities
    @staticmethod
    def customer_side_dashboard(user_id, name, date, time):
        flag = True
        HomeViewer.decoration(name, date, time)
        valid_choice = [1, 2, 3, 4, 5, 6, 7]
        prompt = "\n1.View your details,\n2.Update your details\n3.Service your device \n4.Your last Service details " \
                 "\n5.Make your payment\n6.Notifications\n7.Sign off\n"
        user_choice = get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            UserController.show_user_information(user_id)
        elif user_choice == 2:
            UserController.update_user_information(user_id)
        elif user_choice == 3:
            ServiceController.service_request_controller(user_id)
        elif user_choice == 4:
            UserController.fetch_last_service_request_details(user_id)
        elif user_choice == 5:
            PaymentController.payment_methods(user_id)
        elif user_choice == 6:
            UserController.check_notification(user_id)
        elif user_choice == 7:
            flag = Home.sign_out(name)
        if flag:
            Home.customer_side_dashboard(user_id, name, date, time)

    # 6. User-defined function to sign out of the application
    @classmethod
    def sign_out(cls, name):
        HomeViewer.sign_out_header()
        flag = True
        valid_choice = [1, 2]
        prompt = "\nExit Application or not ?\n 1.Yes\t2.No\n"
        while flag:
            user_choices = get_user_choice(prompt, valid_choice)
            if user_choices == 1:
                HomeViewer.sign_out(name)
                db_manager.close_db_connection()
                quit()
            elif user_choices == 2:
                flag = False
                return not flag

# CLASSES   : 01, Home
# FUNCTIONS : 06
