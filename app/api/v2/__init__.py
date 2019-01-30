from flask import Blueprint
from flask_restful import Api, Resource
from app.api.v2.views.user_views import (Users, UserLogin, Promote,
                                         ResetPassword, UserLogout)
from app.api.v2.views.meetup_views import AllMeetups, Upcoming, OneMeetup
from app.api.v2.views.meetup_views import AdminMeetups
from app.api.v2.views.question_views import AllQuestions, Upvote, Downvote
from app.api.v2.views.question_views import MeetupQuestions, UserQuestions
from app.api.v2.views.comment_views import AllComments, QuestionComments
from app.api.v2.views.rsvp_views import Rsvps

version2 = Blueprint('v2', __name__, url_prefix='/api/v2')

api = Api(version2, catch_all_404s=True)

api.add_resource(Users, '/auth/signup', strict_slashes=False)
api.add_resource(UserLogin, '/auth/login', strict_slashes=False)
api.add_resource(UserLogout, '/auth/logout', strict_slashes=False)
api.add_resource(Promote, '/auth/promote/<int:userId>', strict_slashes=False)
api.add_resource(ResetPassword, '/auth/reset_password', strict_slashes=False)
api.add_resource(AllMeetups, '/meetups', strict_slashes=False)
api.add_resource(Upcoming, '/meetups/upcoming/', strict_slashes=False)
api.add_resource(OneMeetup, '/meetups/<int:meetupId>', strict_slashes=False)
api.add_resource(AdminMeetups, '/meetups/admin', strict_slashes=False)
api.add_resource(Rsvps, '/meetups/<int:meetupId>/rsvps', strict_slashes=False)
api.add_resource(AllQuestions, '/questions', strict_slashes=False)
api.add_resource(UserQuestions, '/questions/user', strict_slashes=False)
api.add_resource(Upvote, '/questions/<int:questionId>/upvote',
                 strict_slashes=False)
api.add_resource(Downvote, '/questions/<int:questionId>/downvote',
                 strict_slashes=False)
api.add_resource(AllComments, '/comments/', strict_slashes=False)
api.add_resource(QuestionComments, '/comments/<int:questionId>',
                 strict_slashes=False)
api.add_resource(MeetupQuestions, '/questions/<int:meetupId>',
                 strict_slashes=False)
