''' This is a VERY simple application recruitment management system using SQLite. 
    This demonstrates my very limited capabilities using SQLite. 
    
    '''
import sqlite3
#importing Error 
from sqlite3 import Error 
import datetime

import os
path_root = os.path.dirname(os.path.abspath(__file__)) #grabs the file system path to the current script file
database_file_path = str(path_root)+"/myinventory.db" #construct the path to the database file 

database_file_path = "myinventory.db"
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

def insert_data(): #user inputs needed here
    name = input("Enter the name of the applicant: ")
    phonenumber = input("Enter applicant phone number: ")
    level = input("Enter applicant assessment level: ")
    jobs = input("Enter applicant interested jobs: ")
    location = input ("Enter the location in miles: ")
    availability = input("Enter applicant availability: ")
    hirestatus = input("Enter applicant hire status: ")
    changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    try:      
        sqlresult = conn.execute("INSERT INTO applicants (name,phonenumber,level,jobs,location,availability,hirestatus,changemade)\
            values("+"'"+ str(name) +"'" + ",'"+ str(phonenumber) +"', '"+ str(level) +"', '"+ str(jobs) +"','"+ str (location)+"','"+str(availability)+"','"+ str (hirestatus)+"','"+str(changemade)+"')")
        result = conn.commit() #this actually runs the SQL and inserts the data into the database
        if result == None:
            print("New appliacant has been saved!")
    except Error as e:
        print ("*** Insert error: ",e)
        pass

def view_data(): #pulling all date within DB
    try:
        cursor = conn.execute ("SELECT id,name, phonenumber,level,jobs,location,availability,hirestatus,changemade FROM applicants" )
        alldata = []
        alldata.append(["ID","Name","Phonenumber","level","Jobs","Location","Availability","Hire Status","Last Update"])
        for row in cursor:
            thisrow=[]
            for x in range(8):
                thisrow.append(row[x])
            alldata.append(thisrow)
        return alldata
    except Error as e:
        print (e)
        pass

def update_data(): #update an applicant already in the DB
    for row in view_data():
            thisrow = " "
            for item in row:
                thisrow += str(item) + "  "
            print (thisrow)
    update_ID = input("Enter the ID of the applicant record to edit: ")
    print('''
        1) = edit name
        2) = edit phone number
        3) = edit jobs
        4) = edit location
        5) = edit availability
        6) = edit hire status''')

    feature = input("Enter which feature of the applicant do you want to edit: ")
    update_value = input ("Editing "+feature+ ": enter the new value: ")

    if(feature == "1"):
        sql = "UPDATE applicants set name = ? where id =  ?"
    elif (feature == "2"):
       sql = "UPDATE applicants set phone number = ? where id =  ?" 
    elif (feature == "3"):
       sql = "UPDATE applicants set jobs  = ? where id =  ?"
    elif (feature == "4"):
       sql = "UPDATE applicants set location  = ? where id =  ?"
    elif (feature == "5"):
       sql = "UPDATE applicants set availability  = ? where id =  ?"
    elif (feature == "6"):
       sql = "UPDATE applicants set hirestatus = ? where id =  ?"  
        
    try:
        #calling the connection execute method
        conn.execute(sql, (update_value,update_ID))
        #update the change made date log
        sql = "UPDATE applicants set changemade = ? where id =  ?"
        changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
        conn.execute(sql, (changemade,update_ID))
        conn.commit() #commiting changes to DB
        print("Applicant has been updated!") #letting managment know it has been done. 
    except Error as e:
        print(e)
        pass

def delete_data():
    id_  =  input("Enter the ID for the applicant record to delete:")
    cursor = conn.cursor() #This sets a spot in the database connection (cursor) for targeted retrieval
    cursor.execute("select name from applicants where ID = "+id_) #create an object referencing the data
    delete_item = cursor.fetchall() # get the data
    confirm = input("Are you sure you want to delete applicant with ID number " + id_ + " " + str(delete_item[0]) + "? (Enter 'y' to confirm.)")
    if confirm.lower() == "y":
        try:
            delete_sql = "DELETE FROM applicants WHERE id = ?" #showing where to delete from
            conn.execute(delete_sql,id_)
            result = conn.commit() #capture the result of the commit and use it to check the result
            if result == None:
                print (id_ + " " + str(delete_item[0]) + " has been deleted from store list.")
            else:
                print ("Deletion failed! Please try again later.")
        except Error as e:
            print (e)
            pass
    else:
        print("You have canceled the deletion.") #after you decided you no longer want to delete
    

conn = create_connection(database_file_path)
now = datetime.datetime.now()

if conn:
    print ("Connected to database: ",conn)  
else:
    print("Error connecting to database.")

while True: #opening print statements
    print("Welcome to the Applicantion Recruitment Management System!")
    print("1 to view all applicants in store list")
    print("2 to insert a new applicant record to store list")
    print("3 to update an applicant record in store list")
    print("4 to delete an applicant record in store list")
    print("5 to exit ARMS")
    name = input ("Choose an option to perform: ")
    if (name =="1"):
        for row in view_data():
            thisrow = " "
            for item in row:
                thisrow += str(item) + "  "
            print (thisrow)
    elif(name == "2"):
        insert_data()
        print("Applicant added to interview list")
    elif(name == "3"):
        update_data()
    elif(name == "4"):
        delete_data()
    elif(name == "5"): #logging out of ARMS
        print("Thank you for using ARMS! You are logged out!")
        conn.close()
        break
    else:
        print("Invalid input, please enter a valid option!") #adding an else if user inputs someting invalid