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
            registered TIMESTAMP DEFAULT NOW(),
            isAdmin BOOL DEFAULT FALSE
        );
        CREATE TABLE IF NOT EXISTS meetups(
            meetupId serial PRIMARY KEY NOT NULL,
            userId INTEGER NOT NULL,
            FOREIGN KEY(userId) REFERENCES users(userId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            createdOn TIMESTAMP DEFAULT NOW(),
            location varchar NOT NULL,
            images varchar [],
            topic varchar NOT NULL,
            happeningOn DATETIME NOT NULL,
            tags varchar []
        );
        CREATE TABLE IF NOT EXISTS questions(
            questionId serial PRIMARY KEY NOT NULL,
            createdOn TIMESTAMP DEFAULT NOW(),
            createdBy INTEGER NOT NULL,
            meetup INTEGER NOT NULL,
            FOREIGN KEY(createdBy) REFERENCES users(userId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY(meetup)REFERENCES meetups(meetupId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            title varchar NOT NULL,
            body varchar NOT NULL,
            votes integer DEFAULT 0,
            voters integer []
        );
        CREATE TABLE IF NOT EXISTS rsvps(
            rsvpId serial PRIMARY KEY NOT NULL,
            meetup INTEGER NOT NULL,
            FOREIGN KEY (meetup) REFERENCES meetups(meetupId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            user integer REFERENCES users(userId),
            response varchar (5)
        );
        CREATE TABLE IF NOT EXISTS comments(
            commentId serial PRIMARY KEY NOT NULL,
            question INTEGER NOT NULL,
            title varchar NOT NULL,
            body varchar NOT NULL,
            FOREIGN KEY (question) REFERENCES questions(questionId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (title) REFERENCES questions(title)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (body) REFERENCES questions(body)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            comment varchar NOT NULL
        );""")

        cls.connect.commit()

    @classmethod
    def drop_tables(cls):
        """Method to delete tables"""
        query = """DROP TABLE IF EXISTS users, meetups, questions, rsvps,\
        comments CASCADE;"""
        cls.cursor.execute(query)
        cls.connect.commit()

    @classmethod
    def database_admin(cls):
        """method to create database admin"""
        firstname = "Nelson"
        lastname = "Mandela"
        othername = "lohilala"
        email = "mandelanelson@email.com"
        phoneNumber = "0711333666"
        username = "tata"
        password = "andela"
        salt = password + username
        hashed = hashlib.md5(str.encode(salt)).hexdigest()
        isAdmin = True
        query = """SELECT * FROM users WHERE username = %s""".format(username)
        cls.cursor.execute(query)
        admin = cls.cursor.fetchone()
        if not admin:
            query = """INSERT INTO users (firstname, lastname, othername,\
            email, phoneNumber, username, hashed, isAdmin) VALUES(firstname,\
            lastname, othername, email, phoneNumber, username, hashed,\
            isAdmin)"""
            cls.cursor.execute(query)
            cls.connect.commit()
        else:
            cls.connect.close()
