[![Build Status](https://travis-ci.com/matthenge/Questioner-API.svg?branch=develop)](https://travis-ci.com/matthenge/Questioner-API)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/09bf041fca3841afad9685fadd90c67d)](https://www.codacy.com/app/matthenge/Questioner-API?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=matthenge/Questioner-API&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/matthenge/Questioner-API/badge.svg?branch=develop)](https://coveralls.io/github/matthenge/Questioner-API?branch=develop)
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

    .Clone this repository from [here](https://github.com/matthenge/Questioner-API.git)

    .Ensure Python 3.6 is installed
	
    .To test the API locally, set up a virtual environment in the root folder 
    - virtualenv env
	
    .Activate the virtual environment through; source env/bin/activate via the terminal
	
    .Run the export FLASK_APP=run.py command via the terminal
	
    .Install dependencies through pip install -r requirements.txt
	
    .Run tests through pytest
	
    .Test the endpoints using Postman throught the button below.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/395b1c540ee8c34c70b6)

    .Alternativerly the hosted app can be tested through the button below
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://questioner-v1.herokuapp.com/api/v1/meetups) 


| **Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| `POST` | ` /api/v2/auth/users ` | Signup new User |
| `POST` | ` /api/v2/meetups ` | Create new Meetup |
| `POST` | ` /api/v2/questions ` | Post new Question |
| `POST` | ` /api/v2/meetups/<meetupId>/rsvps ` | Create an RSVP |
| `GET` | ` /api/v2/meetups/<meetupId> ` | Fetch a Specific Meetup |
| `GET` | ` /api/v2/meetups ` | Fetch all Meetups |
| `GET` | ` /api/v2/meetups/upcoming/ ` | Fetch all upcoming Meetups |
| `PATCH` | ` /api/v2/questions/<questionId>/upvote ` | Upvote a specific Question | 
| `PATCH` | ` /api/v2/questions/<questionId>/downvote ` | Downvote a specific Question |
| `POST` | ` /api/v2/auth/login ` | Login a User |

## Built with

    .Python 3
    
    .Flask-Restful
    
    .Flask
    
    
## Author

James Maruhi
