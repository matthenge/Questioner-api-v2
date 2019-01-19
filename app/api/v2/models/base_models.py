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
