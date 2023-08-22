# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

from Model.payment import Payment, Bill
from View.payment_view import PaymentViewer, BillViewer
from View.view import get_user_choice
from View.animator import Animator


class PaymentController:

    # 1. User-defined funtion to cancel the transaction
    @staticmethod
    def cancel_transaction():
        prompt = "Do you want to \n\t\t1.Try again \t\t2.cancel the transaction\n"
        valid_choice = [1, 2]
        user_choice = get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            return True
        else:
            return None

    # 2. User-defined funtion to get online banking details
    @staticmethod
    def get_online_banking_details():
        flag = True
        while flag:
            bank_name = PaymentViewer.get_bank_details(1)
            flag = Payment.validate_bank_name(bank_name)
            if flag:
                PaymentViewer.display_validated_online_bank_details(1)
                flag = PaymentController.cancel_transaction()
            else:
                Animator.loading_animation(2, "Redirecting to your Banking server")

        if flag is not None:
            flag = True
        else:
            return False

        while flag:
            username = PaymentViewer.get_bank_details(2)
            flag = Payment.validate_bank_username(username)
            if flag:
                PaymentViewer.display_validated_online_bank_details(2)
                flag = PaymentController.cancel_transaction()

        if flag is not None:
            flag = True
        else:
            return False

        while flag:
            password = PaymentViewer.get_bank_details(3)
            flag = Payment.validate_bank_password(password)
            if flag:
                PaymentViewer.display_validated_online_bank_details(3)
                flag = PaymentController.cancel_transaction()

        if flag is not None:
            return True
        else:
            return False

    # 3. User-defined funtion to get card details
    @staticmethod
    def get_card_details():
        # gets and validates the card number
        flag = True
        while flag:
            card_number = PaymentViewer.get_card_details(1)
            flag = not Payment.is_luhn_valid(card_number)
            if flag:
                PaymentViewer.display_validated_card_details(1)
                flag = PaymentController.cancel_transaction()

        if flag is not None:
            flag = True
        else:
            return False

        while flag:
            valid_month = PaymentViewer.get_card_details(2)
            flag = Payment.validate_month(valid_month)
            if flag:
                PaymentViewer.display_validated_card_details(2)
                flag = PaymentController.cancel_transaction()

        if flag is not None:
            flag = True
        else:
            return False

        while flag:
            valid_year = PaymentViewer.get_card_details(3)
            flag = Payment.validate_year(valid_year)
            if flag:
                PaymentViewer.display_validated_card_details(2)
                flag = PaymentController.cancel_transaction()

        if flag is not None:
            flag = True
        else:
            return False

        while flag:
            ccv = PaymentViewer.get_card_details(4)
            flag = Payment.validate_ccv(ccv)
            if flag:
                PaymentViewer.display_validated_card_details(3)
                flag = PaymentController.cancel_transaction()
            else:
                Animator.loading_animation(2, 'Verifying your card details')

        if flag is not None:
            return True
        else:
            return False

    # 4. User-defined funtion to get upi id e details
    @staticmethod
    def get_upi_id_details():
        flag = True
        while flag:
            upi_id = PaymentViewer.get_upi_id_details(1)
            flag = Payment.validate_upi_id(upi_id)
            if flag:
                PaymentViewer.display_validated_upi_id_details()
                flag = PaymentController.cancel_transaction()

        if flag is not None:
            return True
        else:
            return False

    # 5. User-defined funtion to fetch total
    @staticmethod
    def fetch_total(user_id):
        return Payment.calculate_total(user_id)

    # 6. User-defined funtion to perform online banking
    @staticmethod
    def online_banking(total):
        PaymentViewer.payment_headers(2)
        status = PaymentController.get_online_banking_details()
        Animator.loading_animation(2, 'Verifying your credentials')
        if status:
            PaymentViewer.print_total(total)
            pin = PaymentViewer.get_bank_details(4)
            status = Payment.validate_pin(pin)
        PaymentViewer.display_transaction_result(status)
        return status

    # 7. User-defined funtion to perform card transaction
    @staticmethod
    def card_transaction(total):
        PaymentViewer.payment_headers(3)
        status = PaymentController.get_card_details()
        if status:
            PaymentViewer.print_total(total)
            pin = PaymentViewer.get_card_details(5)
            status = Payment.validate_pin(pin)
        PaymentViewer.display_transaction_result(status)
        return status

    # 8. User-defined funtion to perform upi payments
    @staticmethod
    def upi_id_payment(total):
        PaymentViewer.payment_headers(3)
        status = PaymentController.get_upi_id_details()
        Animator.loading_animation(2, 'Verifying your credentials')
        if status:
            PaymentViewer.print_total(total)
            pin = PaymentViewer.get_upi_id_details(2)
            status = Payment.validate_pin(pin)
        PaymentViewer.display_transaction_result(status)
        return status

    # 9. User-defined funtion to check payment eligibility
    @staticmethod
    def check_payment_eligibility(total):
        if total is None:
            PaymentViewer.display_payment_eligibility()
            total = False
        return total

    # 10. User-defined funtion to integrate all the payment methods
    @staticmethod
    def payment_methods(user_id):
        total = PaymentController.fetch_total(user_id)
        total = PaymentController.check_payment_eligibility(total)
        if total:
            PaymentViewer.payment_headers(1)
            BillController.bill_details(user_id)
            prompt = (
                "\nSelect a payment method to proceed\n\t1. Net Banking\n\t2. Credit / Debit card\n\t3. UPI Payment\n\t4. Back to Dashboard\nEnter your choice:\n")
            flag = True
            status = True
            valid_choice = [1, 2, 3, 4]
            while flag:
                user_choice = get_user_choice(prompt, valid_choice)
                if user_choice == 1:
                    status = PaymentController.online_banking(total)
                    PaymentController.update_payment_status(user_id, status)
                elif user_choice == 2:
                    status = PaymentController.card_transaction(total)
                    PaymentController.update_payment_status(user_id, status)
                elif user_choice == 3:
                    status = PaymentController.upi_id_payment(total)
                    PaymentController.update_payment_status(user_id, status)
                elif user_choice == 4:
                    status = True
                flag = not status
            return status

    # 11. User-defined funtion to perform update the payment status
    @staticmethod
    def update_payment_status(customer_id, status):
        if status:
            Payment.update_payment_status(customer_id)


class BillController:
    # 12. User-defined funtion to fetch and display the bill details
    @staticmethod
    def bill_details(user_id):
        result = Bill.fetch_bill_details(user_id)
        BillViewer.display_billing_details(result)
        total = PaymentController.fetch_total(user_id)
        PaymentViewer.print_total(total)

# CLASSES   : 02, PaymentController, BillController
# FUNCTIONS : 12
