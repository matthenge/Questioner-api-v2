"""Configuration Module"""
import os


class Config(object):
    """Main configuration class"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("EMAIL_USER")
    MAIL_PASSWORD = os.getenv("EMAIL_PASS")


class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True
    DB_URL = os.getenv("DB_URL")


class TestingConfig(Config):
    """Testing Configuration"""
    TESTING = True
    DEBUG = True
    DB_URL = os.getenv("TEST_DB_URL")


class ProductionConfig(Config):
    """Production Configuration"""
    DEBUG = False
    TESTING = False

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
