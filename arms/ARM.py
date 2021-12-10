#This is a simple aplication recruitment management program.
#importing Sql to use my database
import os
#importing sqlite3
import sqlite3
from sqlite3 import Error 
import datetime
import os
from sqlite3.dbapi2 import Connection

 
path_root = os.path.dirname(os.path.abspath(__file__))
database_file_path = str(path_root)+"/applicants.db"
database_file_path = "applicants.db" #connecting Database 
def create_connection(db_file):
    try:
        Connection = sqlite3.connect(db_file)
        return Connection
    except Error as e:
        print(e)
        return None
   


def insert_data(connection, first_name, last_name, phone_number, level, age_range, interested_jobs, availability, location_miles):
    first_name = input("Enter the name of the item: ")
    last_name = input("Enter the national drug code of the item: ")
    phone_number = input ("Enter the item inventory location: ")
    level = input("Enter number of doses left: ")
    age_range = input("Enter arrival date: ")
    interested_jobs = input("Enter expiration date: ")
    availability = input("Enter expiration date: ")
    location_miles = input("Enter expiration date: ")
    changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    try:      
        sqlresult = conn.execute("INSERT INTO applicants (first_name,last_name, phone_number, level, age_range, interested_jobs, availability, location_miles,changemade)\
            values("+"'"+ str(first_name) +"'" + ",'"+ str(last_name) +"', '"+ str(phone_number) +"','"+ str(age_range) +"','"+ str(location_miles) +"','"+ str (availability)+"','"+str(level)+"','"+ str (interested_jobs)+"','"+str(changemade)+"')")
        result = conn.commit() #this actually runs the SQL and inserts the data into the database
        if result == None:
            print("*** Data saved to database. ***")
    except Error as e:
        print ("*** Insert error: ",e)
        pass
                                 
def view_data(): 
    try:
        cursor = conn.execute ("SELECT id,name, ndc,location,availability,arrivaldate,expirationdate,changemade FROM applicants" )
        alldata = []
        alldata.append(["ID","Name","NDC","Location","Availability","Arrival Date","Expiration Date","Last Update"])
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
    update_ID = input("Enter the ID of the data record to edit: ")
    print('''
        1 = edit name
        2 = edit ndc
        3 = edit location
        4 = edit availability
        5 = edit arrivaldate
        6 = edit expirationdate''')

    feature = input("Enter which feature of the data do you want to edit: ")
    update_value = input ("Editing "+feature+ ": enter the new value: ")

    if(feature == "1"):
        sql = "UPDATE vaccines set name = ? where id =  ?"
    elif (feature == "2"):
       sql = "UPDATE vaccines set ndc = ? where id =  ?" 
    elif (feature == "3"):
       sql = "UPDATE vaccines set location  = ? where id =  ?"
    elif (feature == "4"):
       sql = "UPDATE vaccines set availability  = ? where id =  ?"
    elif (feature == "5"):
       sql = "UPDATE vaccines set arrivaldate  = ? where id =  ?"
    elif (feature == "6"):
       sql = "UPDATE vaccines set expirationdate = ? where id =  ?"  
        
    try:
        #if we call the connection execute method it invisibly creates a cursor for us
        conn.execute(sql, (update_value,update_ID))
        #update the change made date log
        sql = "UPDATE vaccines set changemade = ? where id =  ?"
        changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
        conn.execute(sql, (changemade,update_ID))
        conn.commit() 
        
    except Error as e:
        print(e)
        pass

def delete_data():
    id_  =  input("Enter the ID for the data record to delete:")
    cursor = conn.cursor() #This sets a spot in the database connection (cursor) for targeted retrieval
    cursor.execute("select first_name from applicants where ID = "+id_) #create an object referencing the data
    delete_item = cursor.fetchall() # get the data
    confirm = input("Are you sure you want to delete " + id_ + " " + str(delete_item[0]) + "? (Enter 'y' to confirm.)")
    if confirm.lower() == "y":
        try:
            delete_sql = "DELETE FROM applicants WHERE id = ?"
            conn.execute(delete_sql,id_)
            result = conn.commit() #capture the result of the commit and use it to check the result
            if result == None:
                print (id_ + " " + str(delete_item[0]) + " deleted.")
            else:
                print ("Deletion failed during SQL execution.")
        except Error as e:
            print (e)
            pass
    else:
        print("Deletion aborted.")

conn = create_connection(database_file_path)
now = datetime.datetime.now()

if conn:
    print ("Connected to database: ",conn)  
else:
    print("Error connecting to database.")

while True:
    print("Welcome to the Vaccine Management System!")
    print("1 to view the data")
    print("2 to insert a new data record")
    print("3 to update a data record")
    print("4 to delete a data record")
    print("X to exit")
    name = input ("Choose an operation to perform: ")
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
        break
  
    
    
    
    
    
   