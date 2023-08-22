# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

from View.view import get_user_choice
from View.animator import Animator
from fetch_property import fetch_property
from tabulate import tabulate


class ServiceViewer:

    # 1. User-defined function to get device name
    @staticmethod
    def get_device_name():
        return input("Enter the device name\n")

    # 2. User-defined function to get model name
    @staticmethod
    def get_model_name():
        return input("Enter the Model name\n")

    # 3. User-defined function to get defect details
    @staticmethod
    def get_defect_details():
        defect = None
        flag = True
        while flag:
            defect = input("Explain the faults that encountered while using this device:\n")
            if 10 <= len(defect) <= 200:
                flag = False
            else:
                print("Defect description should be between 10 and 200 characters.")
        return defect

    # 4. User-defined function to get device usage
    @staticmethod
    def get_device_usage():
        flag = True
        usage = ''
        prompt = "How do you use the device ?\n\t1.Minimal\t2.Nominal\t3.Extensive\n"
        valid_choices = [1, 2, 3]
        while flag:
            user_choice = get_user_choice(prompt, valid_choices)
            if user_choice == 1:
                usage = "Minimal"
                flag = False
            elif user_choice == 2:
                usage = "Nominal"
                flag = False
            elif user_choice == 3:
                usage = "Extensive"
                flag = False
            else:
                flag = True
        return usage

    # 5. User-defined function to get confirmation
    @staticmethod
    def get_confirmation(user_id, service_id, device_name, model_name, defect, usage):
        print("1.CustomerID:", user_id, "\n2.ServiceID:", service_id, "\n3.Device name:", device_name,
              "\n4.Model name:",
              model_name, "\n5.Defect:", defect, "\n6.Usage:", usage)
        prompt = "please ensure where all your request details are correct\n\t1.Yes\t2.No\n"
        valid_choice = [1, 2]
        user_choice = get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            return True
        else:
            return False

    # 7. User-defined function to get service initiation header
    @staticmethod
    def service_decoration(case):
        if case == 1:
            text = "-> Service initiation <-"
            print("_" * 105, "\n", text.center(105))
            print("_" * 105)
        else:
            Animator.loading_animation(1, 'Uploading data')
            print(
                "The service request has been raised.\nTechnicians will get to the address linked with your account and collect \nthe "
                "device within 1 or 2 working days,so please verify the address\n")

    # Employee part

    # 8. User-defined function to get service-Id
    @staticmethod
    def get_service_id(case):
        if case == 1:
            prompt = "Enter the service Id from the above listed to fetch their details\n"
        else:
            prompt = "Enter the service Id from the above listed to update their details\n"
        return input(prompt)

    # 9. User-defined function to display service request
    @staticmethod
    def display_service_request(case, result, service_id):
        if case == 1:
            text = "-> Service requests <-"
            print("_" * 105, "\n", text.center(105))
            print("_" * 105)
            if result:
                headers = ["Service ID", "Device", "Defect", "Service date"]
                print(tabulate(result, headers=headers, tablefmt="grid"))
                print("\n")
            else:
                text = 'There are no new services currently'
                print(text.center(105))
                return result
        else:
            text = "-> Service details <-"
            print("_" * 105, "\n", text.center(105))
            print("_" * 105)
            if not result:
                text = "There is no such new services with the entered Service_id: " + service_id
                print(text.center(105))
                return None
            else:
                for row in result:
                    list1 = row
                    # select service_id, device_type, model, defect, usaage, time from service_requests where  service_id = %s ;
                    print("Service_Id\t\t\t:", list1[0], "\nDevice_category \t:",
                          list1[1], " \nModel_Name\t\t\t:", list1[2], "\nDefect_description  :", list1[3],
                          " \nUsage\t\t\t\t:", list1[4], " \nTime\t\t\t\t:", list1[5])

    # 10. User-defined function to display the result for assign a service request
    @staticmethod
    def display_assign_service_request_result(case, service_id):
        if case == 1:
            text = "The " + service_id + " has been successfully assigned to you"
            print(text.center(105))
            Animator.loading_animation(1, 'Committing changes')
        elif case == 2:
            text = "You have canceled the process"
            print(text.center(105))
        else:
            text = "There is no such new service request with the entered Service_id: " + service_id
            print(text.center(105))

    # 11. User-defined function to update service status
    @staticmethod
    def update_service_status():
        prompt = "\nUpdate the Service status to \n\t1.In-progress\n\t2.Completed\n"
        valid_choice = [1, 2]
        user_choice = get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            status = fetch_property('service', 'REPAIR_STATUS2')
        else:
            status = fetch_property('service', 'REPAIR_STATUS3')
        return status

    # 12. User-defined function to display the update service status
    @staticmethod
    def display_update_service_status_result(case, service_id):
        if case == 1:
            text = "The Service status has been successfully updated for the service request Service Id: " + service_id
            print(text.center(105))
            Animator.loading_animation(1, 'Committing changes')
        elif case == 2:
            text = "You have canceled the process"
            print(text.center(105))
        else:
            text = "There is no such service request with the entered Service_id: " + service_id
            print(text.center(105))

    # 13. User-defined function to get service cost
    @staticmethod
    def get_service_cost():
        prompt = "Enter the price to update the service cost\n Rs "
        while True:
            try:
                service_cost = int(input(prompt))
            except (ValueError, TypeError, KeyboardInterrupt):
                print("Invalid entry !\nPlease try to enter a valid Mobile number\n")
            else:
                if service_cost >= 1000:
                    return service_cost
                else:
                    print("Invalid entry !\nMinimum service cost is 1000\n")

    # 14. User-defined function to display the update service cost result
    @staticmethod
    def display_update_service_cost_result(case, service_id):
        if case == 1:
            text = "The price has been successfully updated for the service request Service Id: " + service_id
            print(text.center(105))
            Animator.loading_animation(1, 'Committing changes')
        elif case == 2:
            text = "You have canceled the process"
            print(text.center(105))
        else:
            text = "There is no such service request with the entered Service_id: " + service_id
            print(text.center(105))

# CLASSES   : 01, ServiceViewer
# FUNCTIONS : 14
