#This is a simple aplication recruitment management program.
#importing Sql to use my database
import os
#importing sqlite3
import sqlite3
from sqlite3 import Error 
import datetime

now = datetime.datetime.now()
#connecting Database 
database_file_path = "Job_applicants.db"
def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file) 
        return connection
    except Error as e:
        print(e)
        return None

#creat a database or connect to one 
conn = sqlite3.connect('job_applicants.db')
#Create cursor
c = conn.cursor()

#date to be inserted 
def insert_data():
    name = input("Enter the name of the applicant: ")
    ID = input("Enter the applicant ID number: ") # number unique to the applicant 
    phone_number = input("Enter the applicant #") # appicant phone number
    location = input ("Enter the applicant location in miles: ") # This is how far the applicant is willing to travel for the job
    availability = input("Enter applicant availability: ") # The days the applicants are willing to work 
    level = input("Enter applicant level: ") #This is the level the applicant gets after taking the job assassment 
    Jobs = input("Enter applicant interested jobs: ") # positions applicant is interested in working in
    changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    try:      
        sqlresult = conn.execute("INSERT INTO job_applicants (first_name,last_name,ID, phone_number,location, availability, level, jobs,changemade)\
            values("+"'"+ str(name) +"'" + ",'"+ str(ID) +"', '"+ str(phone_number) +"', '"+ str(location) +"','"+ str (availability)+"','"+str(level)+"','"+ str (Jobs)+"','"+str(changemade)+"')")
        result = conn.commit() #this actually runs the SQL and inserts the data into the database
        if result == None:
            print("*** Data saved to database. ***")
    except Error as e:
        print ("*** Insert error: ",e)
        pass


def view_data():
    try:
        cursor = conn.execute ("SELECT first_name,last_name, ID,location,availability,level,jobs,changemade FROM Job_applicants" )
        alldata = []
        alldata.append(["First_Name","Last_Name","ID","Phone_Number","Location","Availability","Level","Jobs","Last Update"])
        for row in cursor:
            thisrow=[]
            for x in range(8):
                thisrow.append(row[x])
            alldata.append(thisrow)
        return alldata
    except Error as e:
        print (e)
        pass


def update_data():
    for row in view_data():
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


try:
        #if we call the connection execute method it invisibly creates a cursor for us
        conn.execute(sql, (update_value,update_name))
        #update the change made date log
        sql = "UPDATE vaccines set changemade = ? where id =  ?"
        changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
        conn.execute(sql, (changemade,update_name))
        conn.commit() 

except Error as e:
        print(e)
        pass
