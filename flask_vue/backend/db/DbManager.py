#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pony.orm import *
from .entitys.User import *

#from time import time
#import crypt, uuid

### GENERAL ###
db = Database()

def createDB(debugMode):
    try:
        #db.bind('sqlite', 'database_file.sqlite', create_db=True)
        db.bind(provider='mysql', host='localhost', user='root', passwd='1234', db='board_rol')
        db.generate_mapping(create_tables=True)
        sql_debug(True)
    except Exception as e:
        print("Error: [DbManager.createDB] ->"+str(e))



