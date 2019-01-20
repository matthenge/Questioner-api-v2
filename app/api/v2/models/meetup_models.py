"""Module for meetup operations"""
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
