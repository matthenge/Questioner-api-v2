"""Database Configurations"""
import os
import psycopg2
import hashlib
from psycopg2.extras import RealDictCursor


class QuestionerDB():
    """Class with database connection"""

    @classmethod
    def dbconnection(cls, url):
        """Method to create the database connection"""
        cls.connect = psycopg2.connect(url)
        cls.cursor = cls.connect.cursor(cursor_factory=RealDictCursor)

    @classmethod
    def create_tables(cls):
        """Method to create tables"""
        cls.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            userId serial PRIMARY KEY NOT NULL,
            firstname varchar NOT NULL,
            lastname varchar NOT NULL,
            othername varchar,
            email varchar UNIQUE NOT NULL,
            phoneNumber varchar (15),
            username varchar UNIQUE NOT NULL,
            password varchar NOT NULL,
            registered TIMESTAMP DEFAULT current_timestamp,
            isAdmin BOOL DEFAULT FALSE
        );
        CREATE TABLE IF NOT EXISTS meetups(
            meetupId serial PRIMARY KEY NOT NULL,
            userId INTEGER NOT NULL,
            FOREIGN KEY(userId) REFERENCES users(userId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            createdOn TIMESTAMP DEFAULT current_timestamp,
            location varchar NOT NULL,
            images varchar [],
            topic varchar NOT NULL,
            happeningOn TIMESTAMP NOT NULL,
            tags varchar []
        );
        CREATE TABLE IF NOT EXISTS questions(
            questionId serial PRIMARY KEY NOT NULL,
            createdOn TIMESTAMP DEFAULT current_timestamp,
            createdBy INTEGER NOT NULL,
            meetup INTEGER NOT NULL,
            FOREIGN KEY(createdBy) REFERENCES users(userId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY(meetup)REFERENCES meetups(meetupId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            title varchar NOT NULL,
            body varchar NOT NULL,
            votes integer DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS rsvps(
            rsvpId serial PRIMARY KEY NOT NULL,
            meetup INTEGER NOT NULL,
            FOREIGN KEY (meetup) REFERENCES meetups(meetupId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            createdBy integer REFERENCES users(userId),
            response varchar (5)
        );
        CREATE TABLE IF NOT EXISTS comments(
            commentId serial PRIMARY KEY NOT NULL,
            userId INTEGER NOT NULL,
            question INTEGER NOT NULL,
            FOREIGN KEY(userId) REFERENCES users(userId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (question) REFERENCES questions(questionId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            comment varchar NOT NULL
        );
        CREATE TABLE IF NOT EXISTS voters(
            voteId serial PRIMARY KEY NOT NULL,
            questionId INTEGER NOT NULL,
            voterId INTEGER NOT NULL,
            FOREIGN KEY (questionId) REFERENCES questions(questionId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY(voterId) REFERENCES users(userId)\
            ON UPDATE CASCADE ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS blacklist(
            tokenId serial PRIMARY KEY NOT NULL,
            userId INTEGER NOT NULL,
            token varchar,
            loggedOutAt TIMESTAMP DEFAULT current_timestamp,
            FOREIGN KEY(userId) REFERENCES users(userId)\
            ON UPDATE CASCADE ON DELETE CASCADE
        );""")

        cls.connect.commit()
        QuestionerDB.database_admin()

    @classmethod
    def drop_tables(cls):
        """Method to delete tables"""
        query = """DROP TABLE IF EXISTS users, meetups, questions, rsvps,\
        comments, voters, blacklist CASCADE;"""
        cls.cursor.execute(query)
        cls.connect.commit()

    @classmethod
    def database_admin(cls):
        """method to create database admin"""
        passwrd = "andela"
        usernme = "Admin"
        salt = passwrd + usernme
        hashed = hashlib.md5(str.encode(salt)).hexdigest()
        isAdmin = True
        query = """SELECT * FROM users WHERE username = '{}'""".format(usernme)
        cls.cursor.execute(query)
        admin = cls.cursor.fetchone()
        if not admin:
            query = """INSERT INTO users (firstname, lastname, othername,\
            email, phoneNumber, username, password, isAdmin) VALUES('Nelson',\
            'lohilala', 'Mandela', 'mandelanelson@email.com', '0711333666',\
            'Admin', '{}', True)""".format(hashed)
            cls.cursor.execute(query)
            cls.connect.commit()

    @classmethod
    def save(cls, query):
        """Save data into tables"""
        cls.cursor.execute(query)
        cls.connect.commit()
        data = cls.cursor.fetchone()
        return data

    @classmethod
    def fetch_one(cls, query):
        """Method to fetch specific item"""
        cls.cursor.execute(query)
        return cls.cursor.fetchone()

    @classmethod
    def fetch_all(cls, query):
        """Method to fetch all items"""
        cls.cursor.execute(query)
        return cls.cursor.fetchall()

    @classmethod
    def remove_one(cls, query):
        """Method to delete record"""
        cls.cursor.execute(query)
        cls.connect.commit()
