# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

from tabulate import tabulate


class PaymentViewer:

    # 1. User-defined function to display the payment headers
    @staticmethod
    def payment_headers(case):
        if case == 1:
            text = "-> Payment <-"
            print("_" * 105, "\n", text.center(105))
            print("_" * 105, "\n")
        elif case == 2:
            text = "-> Net Banking <-"
            print(text.center(105), "\n")
        elif case == 3:
            text = "-> Card Transaction <-"
            print(text.center(105), "\n")
        else:
            text = "-> Upi payment <-"
            print(text.center(105), "\n")

    # 2. User-defined function to display the total
    @staticmethod
    def print_total(total):
        print("Your making a payment of Rs:", total)

    # 3. User-defined function to get card details
    @staticmethod
    def get_card_details(case):
        if case == 1:
            while True:
                print("Enter your card number:\n")
                try:
                    value = int(input())
                except (ValueError, KeyboardInterrupt):
                    print("Invalid entry, try entering Integers")
                else:
                    return value

        elif case == 2:
            while True:
                try:
                    print("Enter your card's expiry month")
                    valid_month = int(input())
                except (ValueError, KeyboardInterrupt):
                    print("Invalid entry!")
                else:
                    return valid_month

        elif case == 3:
            while True:
                try:
                    print("Enter your card's expiry year")
                    valid_year = int(input())
                except (ValueError, KeyboardInterrupt):
                    print("Invalid entry!")
                else:
                    return valid_year

        elif case == 4:
            while True:
                try:
                    print("Enter your card's ccv")
                    ccv = int(input())
                except (ValueError, TypeError, KeyboardInterrupt):
                    print("Invalid entry!")
                else:
                    return str(ccv)

        else:
            while True:
                print("Enter your Transaction pin")
                try:
                    pin = int(input())
                except (KeyboardInterrupt, ValueError):
                    print("Invalid entry!")
                else:
                    return pin

    # 4. User-defined function to display the validation result for the card details
    @staticmethod
    def display_validated_card_details(case):
        if case == 1:
            print("You have entered an invalid card number, please try entering valid a card number")
        elif case == 2:
            print("You have entered an invalid expiry date, please try entering valid a expiry date")
        elif case == 3:
            print("You have entered an invalid ccv, please try entering valid a ccv")

    # 5. User-defined function to display the transaction result
    @staticmethod
    def display_transaction_result(status):
        if status:
            print("The transaction has been completed successfully and will be updated in the dashboard later")
        else:
            print("The transaction has failed as you have entered an in valid pin!")

    # 6. User-defined function to get bank details
    @staticmethod
    def get_bank_details(case):
        if case == 1:
            print("Enter your Bank name")
            return input()
        elif case == 2:
            print("Enter username for your internet banking: ")
            return input()
        elif case == 3:
            print("Enter password for your internet banking: ")
            return input()
        else:
            while True:
                print("Enter your Transaction pin")
                try:
                    pin = int(input())
                except (KeyboardInterrupt, ValueError):
                    print("Invalid entry!")
                else:
                    return pin

    # 7. User-defined function to display the validation result for the bank details
    @staticmethod
    def display_validated_online_bank_details(case):
        if case == 1:
            print("You have entered an Invalid Bank Name!, please try entering valid a Bank Name")
        elif case == 2:
            print("You have entered an invalid online banking username, please try entering \nvalid a online banking username")
        elif case == 3:
            print("You have entered an invalid online banking password, please try entering \nvalid a online banking password")

    # 8. User-defined function to get upi details
    @staticmethod
    def get_upi_id_details(case):
        if case == 1:
            print("Enter your UPI-ID :")
            return input()
        else:
            while True:
                print("Enter your Transaction pin")
                try:
                    pin = int(input())
                except (KeyboardInterrupt, ValueError):
                    print("Invalid entry!")
                else:
                    return pin

    # 9. User-defined function to display the validation result for the upi details
    @staticmethod
    def display_validated_upi_id_details():
        print("You have entered an Invalid UPI Id!, please try entering valid a UPI Id")

    # 10. User-defined function to payment eligibility
    @staticmethod
    def display_payment_eligibility():
        print("Sorry!, there are no service requests which are in pending status currently")


class BillViewer:
    # 11. User-defined function to display the bill result
    @staticmethod
    def display_billing_details(result):
        if result is not None:
            header = ["service id", "Model name", "Defect description", "Repair status", "Price"]
            print(tabulate(result, headers=header, tablefmt="grid"))

    # 12. User-defined function to display the pending bills header
    @staticmethod
    def display_pending_bills_header():
        text = "-> Pending bills <-"
        print(text.center(105))

# CLASSES   : 02, PaymentViewer, BillViewer
# FUNCTIONS : 12
