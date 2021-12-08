
import sqlite3
from sqlite3.dbapi2 import Connection #importing sqlite3 to get my database 






#
CREATE_APPLICANT_TABLE = "CREATE TABLE IF NOT EXISTS applicants (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, phone_number INTEGER, level INTEGER, age_range INTEGER, interested_jobs TEXT, availability TEXT, location_miles INTEGER);"
INSERT_APPLICANT = "INSERT INTO applicants (first_name, last_name, phone_number, level, age_range, interested_jobs, availability, location_miles) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"


#queries to find an applicant by name 
GET_ALL_APPLICANTS = "SELECT * FROM applicants;"
GET_APPLICANTS_BY_FIRST_NAME = "SELECT * FROM applicants WHERE first_name = ?;"
GET_BEST_APPLICANT_FOR_JOB = """
SELECT * FROM applicants
WHERE interested_jobs = ?
ORDER BY level DESC
LIMIT 5;"""
GET_APPLICANT_TO_EDIT = ""


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
def get_applicants_by_first_name(connection, name):
    with connection:
        return connection.execute(GET_APPLICANTS_BY_FIRST_NAME, (name,)).fetchall()


#function for finding the best applicant for the job
def get_best_applicant_for_job(connection, interested_job):
    with connection:
        return connection.execute(GET_BEST_APPLICANT_FOR_JOB, (interested_job,)).fetchone()

def update_applicants():
    Conn = sqlite3.connect('applicants.db')
    c = Conn.cursor()

    c.execute("""UPDATE applicants SET
        first_name = :first,
        last_name = :last,
        phone_number = :number,
        interested_jobs = :jobs,
        availability = :availability,
        location_miles = :miles

        WHERE oid = :oid""",)


def update_applicant():
    for row in get_all_applicants():
            thisrow = "  --> "
            for item in row:
                thisrow += str(item) + "  "
            print (thisrow)
update_name = input("Enter the name of the applicant to edit: ")
print('''
        1 = edit name
        2 = edit hire status
        3 = edit location
        4 = edit availability
        5 = edit Jobs
        6 = edit expirationdate''')

feature = input("Enter which feature of the data do you want to edit: ")
update_value = input ("Editing "+feature+ ": enter the new info: ")


if(feature == "1"):
    sql = "UPDATE applicant name = ? where id =  ?"
elif (feature == "2"):
       sql = "UPDATE applicant hire status = ? where id =  ?" 
elif (feature == "3"):
       sql = "UPDATE applicant location  = ? where id =  ?"
elif (feature == "4"):
       sql = "UPDATE applicant availability  = ? where id =  ?"
elif (feature == "5"):
       sql = "UPDATE applicant interested jobs  = ? where id =  ?"
elif (feature == "6"):
       sql = "UPDATE applicant set expirationdate = ? where id =  ?"  


