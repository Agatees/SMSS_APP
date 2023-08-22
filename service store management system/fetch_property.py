# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

import configparser

# Create a ConfigParser object
config = configparser.ConfigParser(interpolation=None)
# Read the property file
config.read("\service store management system\Model\property.properties")


# 1. User-defined function to fetch property from the property.properties
def fetch_property(section, key_name):
    value = config.get(section, key_name)
    return value

# CLASSES   : 00
# FUNCTIONS : 01
