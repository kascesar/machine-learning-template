"""
This module provides a `DataBase` class to simplify connecting to a database
using SQLAlchemy.  The class manages engine creation and provides an easy
interface to obtain a connection.

Classes:
    DataBase: Creates and manages the connection to the database using SQLAlchemy.
"""

from sqlalchemy import create_engine
from .tables import *


class DataBase:
    """
    Creates a connection to the database using SQLAlchemy.

    :param uri: The database URI to connect to.
    :type uri: str
    :param **kwrgs: Optional arguments to customize the connection behavior.
    :type **kwrgs: dict
    """

    def __init__(self, uri, **kwrgs):
        """
        Initializes the DataBase class with the database URI and other optional arguments.

        :param uri: The database URI.
        :type uri: str
        :param **kwrgs: Additional optional arguments.
        :type **kwrgs: dict
        """
        self.uri = uri
        self.engine = self._engine()

    def _engine(self):
        """
        Creates and returns a database engine using the provided URI.

        :return: A SQLAlchemy database engine.
        :rtype: sqlalchemy.engine.Engine
        """
        engine = create_engine(self.uri)
        return engine

    def __call__(self):
        """
        Opens a connection to the database.

        :return: An active connection to the database.
        :rtype: sqlalchemy.engine.Connection
        """
        con = self.engine.connect()
        return con
