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
database_file_path = "Job_applicants.csv"
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
        #call the connection execute method to creates a cursor
        conn.execute(sql, (update_value,update_name))
        #update the change made date log
        sql = "UPDATE applicant changemade = ? where id =  ?"
        changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
        conn.execute(sql, (changemade,update_name))
        conn.commit() 

except Error as e:
        print(e)
        pass

# Now I want to delete applicants that are either not hired or no longer interested. 
def delete_data():
    ID  =  input("Enter the ID for the applicant to delete:") # can only enter ID to reduce mistaken deletions
    cursor = conn.cursor() # want to target the ID in the database
    cursor.execute("select name from Job_applicants where ID = "+ID) 
    delete_item = cursor.fetchall() # get the data targeted
    confirm = input("Are you sure you want to delete " + ID + " " + str(delete_item[0]) + "? (Enter 'y' to confirm.)")
    if confirm.lower() == "y":
        try:
            delete_sql = "DELETE FROM applicants WHERE id = ?"
            conn.execute(delete_sql,ID)
            result = conn.commit() # check if it worked 
            if result == None:
                print (ID + " " + str(delete_item[0]) + " deleted.")
            else:
                print ("Sorry, deletion failed for unknown reasons.")
        except Error as e:
            print (e)
            pass
conn = create_connection(database_file_path)
if conn:
    print ("Connected to database: ",conn)  
else:
    print("Error connecting to database.")

while True:
    print("Welcome to Application Recruitment Management System!")
    print("1 to view applicants")
    print("2 to insert a new applicant")
    print("3 to update a applicant application status")
    print("4 to delete a applicantion")
    print("X to exit")
    name = input ("Enter one of the above options to proceed: ")
    if (name =="1"):
        for row in view_data():
            thisrow = "  --> "
            for item in row:
                thisrow += str(item) + "  "
            print (thisrow)
    elif(name == "2"):
        insert_data()
    elif(name == "3"):
        update_data()
    elif(name == "4"):
        delete_data()
    elif(name == "X"):
        conn.close()
        #exit the loop
        print('Goodbye')
        break