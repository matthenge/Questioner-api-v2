"""Module for CRUD Operations to the Database"""
from app.database import QuestionerDB


class BaseModels(QuestionerDB):
    """Class for Model operations"""

    def save_data(self, table, columns, values, data):
        """Method to save data to table"""
        query = """INSERT INTO {}({}) VALUES ('{}') \
                RETURNING {};""".format(table, columns, values, data)
        QuestionerDB.save(query)
        return data

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
