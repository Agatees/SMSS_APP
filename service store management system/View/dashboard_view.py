# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

class HomeViewer:
    # 1. User-defined function to welcome the user
    @staticmethod
    def greetings_header():
        text = '-> Welcome to the Application <-'
        print("_" * 105, "\n", text.center(105))
        print("_" * 105, "\n")

    # 2. User-defined function to decorated homepage header
    @staticmethod
    def decoration(name, date, time):
        text = "-> home <-"
        print("_" * 105, "\n", text.center(105))
        text = "-> Dashboard <-"
        print("_" * 105, "\n", text.center(105))
        print(name, "  signed in @", date, " " * 50, time)

    # 3. User-defined function to display the sign-out header
    @staticmethod
    def sign_out_header():
        text = "-> Sign-out <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105)

    # 4. User-defined function to display sign out page result
    @staticmethod
    def sign_out(name):
        text1 = "-> Signed out Successfully! <-"
        text = name + " thanks for using this application"
        print(text1.center(105))
        print(text.center(105))

    # 5. User-defined function to display notification header
    @staticmethod
    def notification_header():
        text = "-> Notifications <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105, "\n")

# CLASSES   : 01, HomeViewer
# FUNCTIONS : 05
