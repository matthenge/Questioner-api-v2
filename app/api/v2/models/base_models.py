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
