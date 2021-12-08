import database 


MENU_PROMPT = """
 Please choose from the following options:

 1) add a new applicant.
 2) view all applicants.
 3) Find applicant by name
 4) Find applicants best for job.
 5) Update applicant 
 6) Quit

 Your selection:"""

def menu():
    connection = database.connect()
    database.create_tables(connection)
    print("Welcome to ARMS! Your Application Recruitment Management System!")


    while (user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            first_name = input("Enter applicant  first name: ")
            last_name = input("Enter applicant last name: ")
            phone_number = input("Enter applicant phone number: ")
            level = int(input("Enter applicant assessment level (1-5): "))
            age_range = int(input("Enter in the applicant age-range: "))
            interested_jobs = input("Enter in applicant interested jobs: ")
            availability = input("Enter applicant availability: ")
            location_miles = int(input("Enter location in miles: "))
            print("New appliacant has been saved!")

            database.add_applicant(connection, first_name, last_name, phone_number, level, age_range, interested_jobs, availability, location_miles)
             
        elif user_input == "2":
            applicants = database.get_all_applicants(connection)
            for applicant in applicants:
                print(applicant)
        elif user_input =="3":
            first_name = input("Enter applicant name to find: ")
            applicants = database.get_applicants_by_first_name(connection, first_name)
            for applicant in applicants: 
                print(applicant)
            else:
                print("Sorry, there is no applicant with that name!")    

        elif user_input =="4":
            interested_jobs = input("Enter the job your looking for")
            interested_jobs = database.get_best_applicant_for_job(connection, interested_jobs)
            print(f" The applicants interested in this job is: {interested_jobs[2]}")
        elif user_input =="5":
            update_applicants = input("Enter name of applicant you would like to update.")
            applicants= database.update_applicants(connection, update_applicants)
            print("update succesful")
        
        else:
            print("Invalid input, please enter a valid option!")

menu()

