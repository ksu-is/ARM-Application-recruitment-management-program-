import database 

MENU_PROMPT = """
 Please choose from the following options:

 1) add a new applicant.
 2) view all applicants.
 3) Find applicant by name
 4) Find applicants best for job.
 5) Quit

 Your selection:"""

def menu():
    connection = database.connect()
    database.create_tables(connection)
    print("Welcome to ARMS! Your Application Recruitment Management System!")


    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            first_name = input("Enter applicant  first name: ")
            last_name = input("Enter applicant last name: ")
            phone_number = int(input("Enter applicant phone number: "))
            level = int(input("Enter applicant assessment level (1-5): "))
            age_range = int(input("Enter in the applicant age-range: "))
            interested_jobs = input("Enter in applicant interested jobs: ")
            availability = input("Enter applicant availability: ")
            location_miles = int(input("Enter location in miles: "))

            database.add_applicant(connection, first_name, last_name, phone_number, level, age_range, interested_jobs, availability, location_miles)

        elif user_input == "2":
            applicants = database.get_all_applicants(connection)
            for applicant in applicants:
                print(applicant)
        elif user_input =="3":
            pass
        elif user_input =="4":
            pass
        else:
            print("Invalid input, please enter a valid option!")

menu()

