"""Configuration Module"""
import os


class Config(object):
    """Main configuration class"""
    DEBUG = False
    TESTING = False


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
