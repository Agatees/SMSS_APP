# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

# 1. User-defined function to get user choice
def get_user_choice(prompt, valid_choices):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in valid_choices:
                return user_input
            else:
                print("Invalid choice. Please try again.")
        except (ValueError, KeyboardInterrupt):
            print("Invalid input. Please enter an integer.")

# CLASSES   : 00
# FUNCTIONS : 01

