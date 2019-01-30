"""Module for CRUD Operations to the Database"""
from app.database import QuestionerDB


class BaseModels(QuestionerDB):
    """Class for Model operations"""

    def save_data(self, table, columns, values, details):
        """Method to save data to table"""
        query = """INSERT INTO {}({}) VALUES ('{}') \
                RETURNING {};""".format(table, columns, values, details)
        return QuestionerDB.save(query)

    def fetch_data(self, table, column, search_item):
        """Method to return all fields of a specific item"""
        query = """SELECT * FROM {} WHERE {} = '{}'\
        """.format(table, column, search_item)
        return QuestionerDB.fetch_one(query)

    def fetch_specific(self, columns, table, column, search_item):
        """Method to return specific fields of a specific item"""
        query = """SELECT {} FROM {} WHERE {} = '{}'\
        """.format(columns, table, column, search_item)
        return QuestionerDB.fetch_one(query)

    def fetch_all_items(self, columns, table):
        """Method to fetch all data"""
        query = """SELECT {} FROM {}""".format(columns, table)
        return QuestionerDB.fetch_all(query)

    def fetch_future(self, columns, table, column, search_item):
        """Method to return specific fields of a future event"""
        query = """SELECT {} FROM {} WHERE {} > '{}'\
        """.format(columns, table, column, search_item)
        return QuestionerDB.fetch_all(query)

    def delete_item(self, table, column, search_item):
        """Method to delete meetup records"""
        query = """DELETE FROM {} WHERE {} = '{}'\
        """.format(table, column, search_item)
        return QuestionerDB.remove_one(query)

    def update_record(self, table, columns, column, search_item):
        """Method to update tables"""
        query = """UPDATE {} SET {} WHERE {} = '{}'\
        """.format(table, columns, column, search_item)
        return QuestionerDB.remove_one(query)

    def insert_data(self, table, columns, value1, value2, data):
        """Method to save data to table"""
        query = """INSERT INTO {}({}) VALUES ('{}','{}') RETURNING {};\
        """.format(table, columns, value1, value2, data)
        return QuestionerDB.remove_one(query)

    def fetch_some_data(self, columns, table, clm1, val1, clm2, val2):
        """Method to return data of two conditions"""
        query = """SELECT {} FROM {} WHERE {} = '{}'\
        AND {} = '{}'""".format(columns, table, clm1, val1, clm2, val2)
        return QuestionerDB.fetch_one(query)

    def fetch_all_by_one(self, columns, table, column, search_item):
        """Method to return specific fields of items"""
        query = """SELECT {} FROM {} WHERE {} = '{}'\
        """.format(columns, table, column, search_item)
        return QuestionerDB.fetch_all(query)
