#This is a simple aplication recruitment management program.
#importing Sql to use my database
import sqlite3 
from sqlite3 import Error
import datetime
import os
path_root = os.path.dirname(os.path.abspath(__file__)) #grab the file system path to the current script file
database_file_path = str(path_root)+"/Job_applications.db"
database_file_path = "Job_applications.db"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        return None

print('ARM')
class Applicant:
    def __init__(self):
        self._agerange = ''
        self._status = ''
        self._location = 0
        self._jobs = ''
        self._level= 0
        self._availability= '' 
# add an applicant 
    def addApplicant(self):
        try:
            self._agerange = input('Enter age range: ')
            self._status = input('Enter applicant level: ')
            self._location = int(input('Enter applicant location: '))
            self._jobs = input('Enter applicant interested jobs: ')
            self._level = int(input('Enter applicant status: '))
            self._availability = input('Enter applicant new availability')
            return True
        except ValueError:
                print('please enter applicant information in whole numbers for location and level')
                return False










inventory = Applicant()
while True:

    print('#1 Add Applicant to Store List')
    print('#2 Delete Applicant from Store List')
    print('#3 View Current Applicants in Store List')
    print('#4 Update Applicant in Store List')
    print('#5 View Hired Applicants in Store List')
    print('#6 View Applicants not Interviewed')
    print('#7 Quit')
    userInput=input('Please choose from one of the above options: ') 