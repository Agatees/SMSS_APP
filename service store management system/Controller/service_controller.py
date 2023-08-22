# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

from Model.service import Service
from Model.user import User
from View.view import get_user_choice
from View.service_view import ServiceViewer
from View.user_view import UserViewer
from Controller.user_controller import UserController
from fetch_property import fetch_property


class ServiceController:
    # Customer part

    # 1. User-defined funtion to get device name
    @staticmethod
    def get_device_name():
        flag = True
        device_name = ""
        prompt = "Please select the device category to which the device for servicing belongs\n\t\t1.Laptop\t\t\t\t\t\t2.Phone\n\t\t3.Earphones or Headphones\t\t4.Television\n\t\t5.Gaming consoles\t\t\t\t6.Personal Computers(Desktop pc)\n\t\t7.Smart watches\t\t\t\t\t8.Other\nSelect the device category\n"
        valid_choice = [1, 2, 3, 4, 5, 6, 7, 8]
        while flag:
            userchoices = get_user_choice(prompt, valid_choice)
            if userchoices == 1:
                device_name = 'Laptop'
                flag = False
            elif userchoices == 2:
                device_name = 'Phone'
                flag = False
            elif userchoices == 3:
                device_name = 'Earphones'
                flag = False
            elif userchoices == 4:
                device_name = 'Television'
                flag = False
            elif userchoices == 5:
                device_name = 'Console'
                flag = False
            elif userchoices == 6:
                device_name = 'Computers'
                flag = False
            elif userchoices == 7:
                device_name = 'Smart watch'
                flag = False
            elif userchoices == 8:
                device_name = ServiceViewer.get_device_name()
                print(len(device_name))
                if 0 < len(device_name) < 50:
                    print(1)
                    if Service.validate_name(1, device_name):
                        flag = False
                    else:
                        flag = True
                else:
                    flag = True
        return device_name

    # 2. User-defined funtion to get model name
    @staticmethod
    def get_model_name():
        model = None
        flag = True
        while flag:
            model = ServiceViewer.get_model_name()
            if 0 < len(model) < 40:
                if Service.validate_name(2, model):
                    flag = False
                else:
                    flag = True
            else:
                flag = True
        return model

    # 3. User-defined funtion to get updated values if any
    @staticmethod
    def get_updated_values():
        device_name = None
        model_name = None
        defect_description = None
        usage = None
        prompt = "Which details do you need to update?\n\t\t1.Device name\n\t\t2.Model name\n\t\t3.Defect\t\t4.Usage\n"
        valid_choice = [1, 2, 3, 4]
        user_choice = get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            device_name = ServiceController.get_device_name()
        elif user_choice == 2:
            model_name = ServiceController.get_model_name()
        elif user_choice == 3:
            defect_description = ServiceViewer.get_defect_details()
        elif user_choice == 4:
            usage = ServiceViewer.get_device_usage()
        return device_name, model_name, defect_description, usage

    # 4. User-defined funtion to Rise a service request
    @classmethod
    def service_request_controller(cls, user_id):
        ServiceViewer.service_decoration(1)
        device_name = ServiceController.get_device_name()
        model_name = ServiceController.get_model_name()
        service_id = Service.generate_service_id(device_name, model_name)
        defect_description = ServiceViewer.get_defect_details()
        usage = ServiceViewer.get_device_usage()
        status = ServiceViewer.get_confirmation(user_id, service_id, device_name, model_name, defect_description, usage)
        if not status:
            values = ServiceController.get_updated_values()
            device_name = values[0]
            model_name = values[1]
            defect_description = values[2]
            usage = values[3]
        Service.rise_service_request(user_id, device_name, model_name, defect_description, usage)
        ServiceViewer.service_decoration(2)
        result = User.fetch_user_detail(3, user_id)
        UserViewer.display_user_address(result[1:7])
        prompt = "\nAre you available in this address with the defective device\n\t1.Yes\t\t2.No\n"
        valid_choices = [1, 2]
        user_choice = get_user_choice(prompt, valid_choices)
        if user_choice == 2:
            print("Please update the address as soon as possible in the yours details")
            UserController.update_user_information(user_id)

    # 5. User-defined funtion to update a payment status
    @staticmethod
    def auto_update_payment_status(service_id):
        values = (fetch_property('payment', 'PAYMENT_STATUS2'), service_id)
        Service.auto_update_status(values)

    # Employee part
    # 6. User-defined funtion to view the pending requests
    @staticmethod
    def view_pending_service_requests():
        result = Service.fetch_service_request(1, None)
        ServiceViewer.display_service_request(1, result, service_id=None)

    # 7. User-defined funtion to assign a service request
    @staticmethod
    def assign_service_request(name):
        ServiceController.view_pending_service_requests()
        service_id = ServiceViewer.get_service_id(1)
        if Service.validate_service_id(service_id):
            result = Service.fetch_service_request(2, service_id)
            ServiceViewer.display_service_request(2, result, service_id)
            if ServiceController.get_employee_confirmation(1):
                Service.update_service_request(1, [service_id, name])
                ServiceViewer.display_assign_service_request_result(1, service_id)
            else:
                ServiceViewer.display_assign_service_request_result(2, service_id)
        else:
            ServiceViewer.display_assign_service_request_result(3, service_id)

    # 8. User-defined funtion to view the employee's pending requests
    @staticmethod
    def view_employee_service_request(name):
        result = Service.fetch_service_request(3, name)
        ServiceViewer.display_service_request(1, result, service_id=None)

    # 9. User-defined funtion to update the service status
    @staticmethod
    def update_service_status(name):
        ServiceController.view_employee_service_request(name)
        service_id = ServiceViewer.get_service_id(2)
        if Service.validate_service_id(service_id):
            service_status = ServiceViewer.update_service_status()
            data = (service_id, service_status)
            if ServiceController.get_employee_confirmation(2):
                Service.update_service_request(2, data)
                ServiceViewer.display_update_service_status_result(1, service_id)
            else:
                ServiceViewer.display_update_service_status_result(2, service_id)
        else:
            ServiceViewer.display_update_service_status_result(3, service_id)

    # 10. User-defined funtion to update the service cost
    @staticmethod
    def update_service_cost(name):
        ServiceController.view_employee_service_request(name)
        service_id = ServiceViewer.get_service_id(2)
        if Service.validate_service_id(service_id):
            cost = ServiceViewer.get_service_cost()
            data = (service_id, cost)
            if ServiceController.get_employee_confirmation(2):
                Service.update_service_request(3, data)
                ServiceViewer.display_update_service_cost_result(1, service_id)
                return service_id
            else:
                ServiceViewer.display_update_service_cost_result(2, service_id)
        else:
            ServiceViewer.display_update_service_cost_result(3, service_id)
        return None

    # 11. User-defined funtion to get the employee's confirmation
    @staticmethod
    def get_employee_confirmation(case):
        prompt = None
        if case == 1:
            prompt = "Are you sure that you can handle this service request\n\t\t1.Yes\t\t2.No\n"
        elif case == 2:
            prompt = "Are you sure about updating the details\n\t\t1.Yes\t\t2.No\n"
        user_choices = get_user_choice(prompt, valid_choices=[1, 2])
        if user_choices == 1:
            return True
        else:
            return False

# CLASSES   : 01, ServiceController
# FUNCTIONS : 11
