#!/usr/bin/env python
import os


# pytest: disable=too-few-public-methods
class Config:
    DEBUG = True
    DEVELOPMENT = True
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_PORT = os.environ.get("DB_PORT", 3306)
    DB_DATABASE = os.getenv("POSTGRES_DATABASE")
    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
