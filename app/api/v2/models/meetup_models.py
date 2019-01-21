"""Module for meetup operations"""
import datetime
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
        table = "meetups"
        columns = ", ".join(meetup.keys())
        values = "', '".join(map(str, meetup.values()))
        details = {
            "location": "location",
            "images": "images",
            "topic": "topic",
            "happeningOn": "happeningOn",
            "tags": "tags"
        }
        data = ",".join(map(str, details.values()))
        newMeetup = BaseModels.save_data(self, table, columns, values, data)

        return newMeetup

    def get_all(self):
        """Method to retrieve all meetups"""
        table = "meetups"
        columns = "meetupId, topic, location, tags"
        meetups = BaseModels.fetch_all_items(self, columns, table)
        return meetups

    def get_upcoming(self):
        """Method to retrieve only upcoming meetups"""
        table = "meetups"
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        columns = "meetupId, topic, location, tags"
        column = "happeningOn"
        meetups = BaseModels.fetch_future(self, columns, table, column,
                                          current_time)
        return meetups
