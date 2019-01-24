"""Module for rsvp operations"""
import json
from .base_models import BaseModels


class RsvpModels(BaseModels):
    """Class for rsvp CRUD operations"""

    def __init__(self, meetup, createdBy, response):
        """Initialize the rsvp models"""
        self.meetup = meetup
        self.createdBy = createdBy
        self.response = response

    def create_rsvp(self):
        """Method for creating rsvp"""
        rsvp_data = dict(
            meetup=self.meetup,
            createdBy=self.createdBy,
            response=self.response
        )
        data = {
            "response": "response"
        }
        table = "rsvps"
        columns = ", ".join(rsvp_data.keys())
        values = "', '".join(map(str, rsvp_data.values()))
        details = ",".join(map(str, data.values()))
        newRsvp = BaseModels.save_data(self, table, columns, values,
                                       details)
        newRsvp = json.dumps(newRsvp, default=str)

        return newRsvp

    def check_user(self, createdBy, meetupId):
        """Method to check user"""
        fields = "response"
        tbl = "rsvps"
        column = "createdBy"
        user = BaseModels.fetch_some_data(self, fields, tbl, column, createdBy,
                                          "meetup", meetupId)
        user = json.dumps(user, default=str)
        user = json.loads(user)
        return user
