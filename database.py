import sqlite3 #importing sqlite3 to get my database 

#
CREATE_APPLICANT_TABLE = "CREATE TABLE IF NOT EXISTS applicants (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, phone_number INTEGER, level INTEGER, age_range INTEGER, interested_jobs TEXT, availibility TEXT, location_miles INTEGER);"
INSERT_APPLICANT = "INSERT INTO applicants (first_name, last_name, phone_number, level, age_range, interested_jobs, availability, location_miles) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"


#queries to find an applicant by name 
GET_ALL_APPLICANTS = "SELECT * FROM applicants;"
GET_APPLICANTS_BY_NAME = "SELECT * FRROM applicants WHERE name = ?;"
GET_BEST_APPLICANT_FOR_JOB = """
SELECT * FROM applicants
WHERE interested_jobs = ?
ORDER BY level DESC
LIMIT 1;"""


def connect():
    return sqlite3.connect("applicants.db")
#Creating my table 
def create_tables(connection):
    with connection: 
        connection.execute(CREATE_APPLICANT_TABLE)

#creating queries 
def add_applicant(connection, first_name, last_name, phone_number, level, age_range, interested_jobs, availability, location_miles):
    with connection:
        connection.execute(INSERT_APPLICANT, (first_name, last_name, phone_number, level, age_range, interested_jobs, availability, location_miles)) 

#Writeing function for the GET All queries
def get_all_applicants(connection):
    with connection:
        return connection.execute(GET_ALL_APPLICANTS).fetchall()



# Writeing function for get applicant by name 
def get_applicants_by_name(connection, name):
    with connection:
        return connection.execute(GET_APPLICANTS_BY_NAME, (name,)).fetchall()


#function for finding the best applicant for the job
def get_best_applicant_for_job(connection, interested_job):
    with connection:
        return connection.execute(GET_BEST_APPLICANT_FOR_JOB, (interested_job,)).fetchone()