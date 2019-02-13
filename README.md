[![Build Status](https://travis-ci.com/matthenge/Questioner-api-v2.svg?branch=develop)](https://travis-ci.com/matthenge/Questioner-api-v2)
[![Maintainability](https://api.codeclimate.com/v1/badges/2dbeec0ab08c5b929906/maintainability)](https://codeclimate.com/github/matthenge/Questioner-api-v2/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/matthenge/Questioner-api-v2/badge.svg?branch=develop)](https://coveralls.io/github/matthenge/Questioner-api-v2?branch=develop)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

# Questioner

Questioner is a platform where users crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

## Getting started
These instructions will get you a copy of the project running on your local machine for development and testing puposes.


## Prerequisites

	.Python 3.6

	.Postman

	.Git


## Installing

    .Clone this repository from [here](https://github.com/matthenge/Questioner-api-v2.git)

    .Ensure Python 3.6 is installed
	
    .To test the API locally, set up a virtual environment in the root folder 
    - virtualenv env
	
    .Activate the virtual environment through; ` source env/bin/activate ` via the terminal
	
    .Run the ` export FLASK_APP=run.py ` command via the terminal
	
    .Install dependencies through ` pip install -r requirements.txt `
	
    .Run tests through ` pytest `
	
    .Test the endpoints using Postman throught the button below.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d382f317baaca2db855d)

    .Alternativerly the hosted app can be tested through the button below
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://questioner-v2.herokuapp.com/api/v2/) 


| **Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| `POST` | ` /api/v2/auth/signup ` | Signup new User |
| `POST` | ` /api/v2/auth/login ` | Login a User |
| `POST` | ` /api/v2/auth/logout ` | Logout a User |
| `PUT` | ` /api/v2/auth/promote/<int:userId> ` | Promote a User |
| `PUT` | ` /api/v2/auth/reset_password/<token> ` | Pasword Reset |
| `POST` | ` /api/v2/auth/reset_password ` | Request Password Reset |
| `POST` | ` /api/v2/meetups ` | Create new Meetup |
| `POST` | ` /api/v2/questions ` | Post new Question |
| `POST` | ` /api/v2/comments/ ` | Post new Comment |
| `POST` | ` /api/v2/meetups/<meetupId>/rsvps ` | Create an RSVP |
| `GET` | ` /api/v2/meetups/<meetupId> ` | Fetch a Specific Meetup |
| `GET` | ` /api/v2/meetups ` | Fetch all Meetups |
| `GET` | ` /api/v2/meetups/admin ` | Fetch all Meetups by Admin |
| `GET` | ` /api/v2/questions ` | Fetch all Questions |
| `GET` | ` /api/v2/questions/user ` | Fetch all Questions by User |
| `GET` | ` /api/v2/meetups/upcoming/ ` | Fetch all upcoming Meetups |
| `GET` | ` /api/v2/meetups/<meetupId>/rsvps ` | Fetch all Meetup RSVPs |
| `GET` | ` /api/v2//questions/<int:meetupId> ` | Fetch all Meetup questions |
| `GET` | ` /api/v2/comments/<int:questionId> ` | Fetch all question comments |
| `PATCH` | ` /api/v2/questions/<questionId>/upvote ` | Upvote a specific Question | 
| `PATCH` | ` /api/v2/questions/<questionId>/downvote ` | Downvote a specific Question |
| `DELETE` | ` /api/v2/meetups/<meetupId> ` | Delete a Specific Meetup |

## Built with

    .Python 3
    
    .Flask-Restful
    
    .Flask
    
    
## Author

James Maruhi
