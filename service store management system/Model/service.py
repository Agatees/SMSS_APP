# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

import re
import math
from Model.connect_db import db_manager
from Model.model import generate_sha256_hash, get_timestamp
from fetch_property import fetch_property


class Service:

    # Customer part

    # 1. User-defined funtion to generate service-Id
    @staticmethod
    def generate_service_id(name, model_name):
        timestamp = get_timestamp(2)
        input_string = f"{name}_{model_name}_{timestamp}"
        hash_object = generate_sha256_hash(input_string)
        unique_hash = hash_object[:10]
        service_id = 'SER' + unique_hash[:7]
        return service_id

    # 2. User-defined funtion to validate model name
    @staticmethod
    def validate_name(case, name):
        pattern1 = fetch_property('service', 'NAME_PATTERN1')
        pattern2 = fetch_property('service', 'NAME_PATTERN2')
        if case == 1:
            rule = re.compile(pattern1)
        else:
            rule = re.compile(pattern2)
        result = re.match(rule, name)
        if result is not None:
            return True
        else:
            return False

    # 3. User-defined funtion to push the service request details into the database
    @classmethod
    def rise_service_request(cls, user_id, device_name, model_name, defect, usage):
        time = get_timestamp(2)
        repair_status = fetch_property('service', 'REPAIR_STATUS1')
        payment_status = fetch_property('payment', 'PAYMENT_STATUS1')
        service_id = Service.generate_service_id(device_name, model_name)
        date = get_timestamp(3)
        #  pushing into database
        #  table service_requests column names
        #  customer_id, service_id, device_type, model, defect, usaage, repair_status, time, price, payment_status
        data = (user_id, service_id, device_name, model_name, defect, usage, repair_status, time, 0, payment_status)
        query = fetch_property('insert', 'INSERT_SERVICE_REQUESTS')
        db_manager.query_execute(1, query, data)
        #  pushing into database
        #  table services column names
        # service_id, serviced_by, servie_date, service_status, price, payment_status, time
        data = (service_id, None, date, repair_status, 0, payment_status, time)
        query = fetch_property('insert', 'INSERT_SERVICES')
        db_manager.query_execute(1, query, data)

    # Employee part

    # 4. User-defined funtion to validate service-Id
    @staticmethod
    def validate_service_id(service_id):
        query = fetch_property('validate', 'CHECK_SERVICE_ID')
        result = db_manager.query_execute(3, query, (service_id,))
        return result is not None

    # 5. User-defined funtion to fetch service request details
    @staticmethod
    def fetch_service_request(case, data):
        if case == 1:
            query = fetch_property('service_query', 'FETCH1')
            result = db_manager.query_execute(4, query, values=None)
            return result
        if case == 2:
            query = fetch_property('service_query', 'FETCH2')
            result = db_manager.query_execute(4, query, values=(data,))
            return result
        if case == 3:
            query = fetch_property('service_query', 'FETCH3')
            repair_status = fetch_property('service', 'REPAIR_STATUS3')
            result = db_manager.query_execute(4, query, values=(data, repair_status))
            return result

    # 6. User-defined funtion to calculate percentage
    @staticmethod
    def calculate_percentage(s_cost):
        return math.ceil(s_cost * 0.20)

    # 7. User-defined funtion to update the service request details
    @classmethod
    def update_service_request(cls, case, data):
        service_id = data[0]
        # Updates service agent
        if case == 1:
            name = data[1]
            query = fetch_property('service_query', 'UPDATE_SERVICED_BY')
            values = (name, service_id)
            db_manager.query_execute(2, query, values)

        # Updates service_status
        elif case == 2:
            service_status = data[1]
            query = fetch_property('service_query', 'UPDATE_SERVICE_STATUS')
            values = (service_status, service_id)
            db_manager.query_execute(2, query, values)
            query = fetch_property('service_query', 'UPDATE_REPAIR_STATUS')
            db_manager.query_execute(2, query, values)

        # Updates service_cost
        else:
            repair_cost = data[1]
            query = fetch_property('service_query', 'UPDATE_SERVICE_COST')
            values = (repair_cost, service_id)
            db_manager.query_execute(2, query, values)
            query = fetch_property('service_query', 'UPDATE_REPAIR_COST')
            service_cost = repair_cost + Service.calculate_percentage(repair_cost)
            values = (service_cost, service_id)
            db_manager.query_execute(2, query, values)

    # 8. User-defined funtion to update status
    @staticmethod
    def auto_update_status(values):
        query = fetch_property('service_query', 'UPDATE_PAYMENT_STATUS1')
        db_manager.query_execute(2, query, values)
        query = fetch_property('service_query', 'UPDATE_PAYMENT_STATUS2')
        db_manager.query_execute(2, query, values)

# CLASSES   : 01, Service
# FUNCTIONS : 08
