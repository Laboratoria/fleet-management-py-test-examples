#!/usr/bin/env python
import os

# https://flask.palletsprojects.com/en/2.3.x/config/
# pytest: disable=too-few-public-methods
class Config:
    DEBUG = True
    DEVELOPMENT = True
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_PORT = os.environ.get("DB_PORT", 3306)
    DB_DATABASE = os.getenv("POSTGRES_DATABASE")
    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

class TestConfig(Config):
    DB_HOST = os.getenv("POSTGRES_TEST_HOST")
    DB_PASSWORD = os.getenv("POSTGRES_TEST_PASSWORD")
