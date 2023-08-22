# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

# Application-Database connectivity
import mysql.connector
from fetch_property import fetch_property

db_host = fetch_property('database', 'HOST')
db_user = fetch_property('database', 'USER')
db_password = fetch_property('database', 'PASSWORD')
db_database = fetch_property('database', 'DATABASE')


class Database:
    # 1. Initializing the connection using a parametrized constructor
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.global_cursor = self.connection.cursor()

    # 2. User-defined function to perform various query operations
    def query_execute(self, case, query, values):
        result = None
        self.global_cursor.execute(query, values)
        if case in (1, 2):
            self.connection.commit()
        elif case == 3:
            result = self.global_cursor.fetchone()
        elif case == 4:
            result = self.global_cursor.fetchall()
        elif case == 5:
            result = self.global_cursor.fetchone()
        return result

    # 3. User-defined function to close the cursor and the connections
    def close_db_connection(self):
        self.global_cursor.close()
        self.connection.close()


db_manager = Database(db_host, db_user, db_password, db_database)


class Databasemanager:

    # 4. User-defined function to create table user_credentials
    @staticmethod
    def initialize_table1():
        query = fetch_property('create_tables', 'CREATE_TABLE_USER_CREDENTIALS')
        db_manager.query_execute(5, query, values=None)
        data = ('ADMAd44674', 'Admin', 'e86f78a8a3caf0b60d8e74e5942aa6d86dc150cd3c03338aef25b7d2d7e3acc7', '4467404000',
                'admin-india@aspiresys.com', '2023-07-02')
        query = fetch_property('insert', 'INSERT_USER_CREDENTIALS')
        db_manager.query_execute(1, query, data)

    # 5. User-defined function to create table user_data
    @staticmethod
    def initialize_table2():
        query = fetch_property('create_tables', 'CREATE_TABLE_USER_DATA')
        db_manager.query_execute(5, query, values=None)
        data = ('ADMAd44674', 'Admin', None, None, None, 'admin-india@aspiresys.com', '4467404000', None, '2023-07-02')
        query = fetch_property('insert', 'INSERT_USER_DATA')
        db_manager.query_execute(1, query, data)

    # 6. User-defined function to create table user_address
    @staticmethod
    def initialize_table3():
        query = fetch_property('create_tables', 'CREATE_TABLE_USER_ADDRESS')
        db_manager.query_execute(5, query, values=None)
        query = fetch_property('insert', 'INSERT_ADDRESS')
        data = ('ADMAd44674', None, None, None, None, None, None, '2023-07-02')
        db_manager.query_execute(1, query, data)

    # 7. User-defined function to create table Service_requests
    @staticmethod
    def initialize_table4():
        query = fetch_property('create_tables', 'CREATE_TABLE_SERVICE_REQUESTS')
        db_manager.query_execute(5, query, values=None)

    # 8. User-defined function to create table services
    @staticmethod
    def initialize_table5():
        query = fetch_property('create_tables', 'CREATE_TABLE_SERVICES')
        db_manager.query_execute(5, query, values=None)

    # 9. User-defined function to create table bank and inserts some bank names
    @staticmethod
    def initialize_table6():
        query = fetch_property('create_tables', 'CREATE_TABLE_BANK')
        db_manager.query_execute(5, query, values=None)
        query = fetch_property('insert', 'INSERT_BANK')
        data = [
            (1, 'State Bank Of India'), (2, 'Punjab National Bank'), (3, 'Indian Bank'),
            (4, 'Bank Of India'), (5, 'UCO Bank'), (6, 'Union Bank Of India'),
            (7, 'Central Bank Of India'), (8, 'Bank Of Baroda'), (9, 'Bank Of Maharashtra'),
            (10, 'Canara Bank'), (11, 'Punjab And Sind Bank'), (12, 'Indian Overseas Bank'),
            (13, 'ICICI Bank'), (14, 'HDFC Bank'), (15, 'Axis Bank'),
            (16, 'IDBI Bank'), (17, 'Dhanlaxmi Bank'), (18, 'Kotak Mahindra Bank'),
            (19, 'Federal Bank')
        ]
        db_manager.global_cursor.executemany(query, data)
        db_manager.connection.commit()

    # 10. User-defined function to check whether all the necessary tables are in the DB and if not create it
    @staticmethod
    def check_db():
        # Check for table user_credentials
        query = fetch_property('show_tables', 'TABLE_CREDENTIALS')
        result = db_manager.query_execute(4, query, values=None)
        if not result:
            Databasemanager.initialize_table1()

        # Check for table user_data
        query = fetch_property('show_tables', 'TABLE_USERDATA')
        result = db_manager.query_execute(3, query, values=None)
        if not result:
            Databasemanager.initialize_table2()

        # Check for table address
        query = fetch_property('show_tables', 'TABLE_ADDRESS')
        result = db_manager.query_execute(3, query, values=None)
        if not result:
            Databasemanager.initialize_table3()

        # Check for table service
        query = fetch_property('show_tables', 'TABLE_SERVICE')
        result = db_manager.query_execute(3, query, values=None)
        # print(result)
        if not result:
            Databasemanager.initialize_table5()

        query = fetch_property('show_tables', 'TABLE_SERVICE_REQUEST')
        result = db_manager.query_execute(3, query, values=None)
        # print(result)
        if not result:
            Databasemanager.initialize_table4()

        # Check for table bank
        query = fetch_property('show_tables', 'TABLE_BANK')
        result = db_manager.query_execute(3, query, values=None)
        if not result:
            Databasemanager.initialize_table6()


Databasemanager.check_db()

# CLASSES   : 2, Database, DatabaseManager
# FUNCTIONS : 10
