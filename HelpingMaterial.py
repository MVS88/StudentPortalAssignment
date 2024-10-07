#initalizing the variable that sir used in the data structure.

std_id = 0
name = ""
age = 0
welcome_message = "Welcome to the Student Portal"
marks = 0
grade = ""
email = ""
username = ""
password = ""


#Data structure format that sir gave.

Student = {
    "Id" : std_id, "Name" : name, "Age" : age, "Welcome_Message" : welcome_message, "Marks" : marks, "Grade" : grade,
    "Personal_Info" : {
        "email" : email, "Username" : username, "Password" : password,
    },
    "Quiz_History" : []
}

#Main Menu

menu = ("\n*********************Student Portal*********************\n"
        "\nPress 1 to register Yourself\n"
        "Press 2 to login into Student Portal\n"
        "Press 3 to Access Student Portal Dashboard\n"
        "Press 4 to Logout Your Account\n"
        "Press 5 to Exit Student Portal\n"
        "\n********************************************************\n")

#DashBoard Menu provided by the Sir.

dashboard_Menu = ("\n********WELCOME TO DASHBOARD********\n"
                  "\nPress 1 to calculate your grade\n"
                  "Press 2 to view your Personal Information\n"
                  "Press 3 to edit your Personal information\n"
                  "Press 4 to customize your Welcome Message\n"
                  "Press 5 to start quiz\n"
                  "Press 6 to see quiz History\n"
                  "Press 7 to go back to main menu"
                  "\n************************************\n")


username = email.split('@')[0]
