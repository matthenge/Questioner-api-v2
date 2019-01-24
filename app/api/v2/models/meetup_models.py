"""Module for meetup operations"""
import datetime
import json
from .base_models import BaseModels
from app.api.v2.utils.utilities import Helpers

helpers = Helpers()


class MeetupModels(BaseModels):
    """Class for meetup CRUD operations"""

    def __init__(self, userId, location, images, topic, happeningOn, tags):
        """Initialize the meetup models"""
        self.userId = userId
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.tags = tags

    def create_meetup(self):
        """method for creating meetups"""
        meetup = dict(
            userId=self.userId,
            location=self.location,
            images=self.images,
            topic=self.topic,
            happeningOn=self.happeningOn,
            tags=self.tags
        )
        meetData = {
            "topic": "topic",
            "location": "location",
            "happeningOn": "happeningOn",
            "tags": "tags"
        }
        table = "meetups"
        columns = ", ".join(meetup.keys())
        values = "', '".join(map(str, meetup.values()))
        details = ",".join(map(str, meetData.values()))
        newMeetup = BaseModels.save_data(self, table, columns, values, details)
        newMeetup = json.dumps(newMeetup, default=str)

        return newMeetup

    def get_all(self):
        """Method to retrieve all meetups"""
        table = "meetups"
        columns = "meetupId, topic, location, happeningOn, tags"
        meetups = BaseModels.fetch_all_items(self, columns, table)
        meetups = json.dumps(meetups, default=str)
        return meetups

    def get_upcoming(self):
        """Method to retrieve only upcoming meetups"""
        table = "meetups"
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        columns = "meetupId, topic, location, happeningOn, tags"
        column = "happeningOn"
        meetups = BaseModels.fetch_future(self, columns, table, column,
                                          current_time)
        meetups = json.dumps(meetups, default=str)
        return meetups

    def get_specific(self, meetupId):
        """Method to fetch a specific meetup"""
        table = "meetups"
        columns = "meetupId, topic, location, happeningOn, tags"
        column = "meetupId"
        search_item = meetupId
        meetup = BaseModels.fetch_specific(self, columns, table, column,
                                           search_item)
        meetup = json.dumps(meetup, default=str)
        return meetup

    def delete_specific(self, meetupId):
        """Delete meetup record"""
        table = "meetups"
        column = "meetupId"
        search_item = meetupId
        meetup = BaseModels.fetch_data(self, table, column, search_item)
        if not meetup:
            return False
        BaseModels.delete_item(self, table, column, search_item)

    def get_one(self, meetupId):
        """Method to fetch a one meetup"""
        table = "meetups"
        columns = "meetupId, topic"
        column = "meetupId"
        search_item = meetupId
        meetup = BaseModels.fetch_specific(self, columns, table, column,
                                           search_item)
        meetup = json.dumps(meetup, default=str)
        return meetup

    def repeat_meetup(self, location, happeningOn):
        """Method to verify a meetup is not posted twice"""
        columns = "meetupId, topic"
        table = "meetups"
        clm1 = "location"
        val1 = location
        clm2 = "happeningOn"
        val2 = happeningOn
        meetup = BaseModels.fetch_some_data(self, columns, table, clm1,
                                            val1, clm2, val2)
        meetup = json.dumps(meetup, default=str)
        return meetup
