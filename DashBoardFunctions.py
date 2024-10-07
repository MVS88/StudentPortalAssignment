from ast import Param
import MainFunctions as mf
import HelpingMaterial as hm
import Dashboard as db


def grade_calculator():

    z = hm.Student["Marks"]
    total_Marks = 100

    if z <= 30:
       print("\nYour Grade is F")
    elif 30 < z <= 50:
        print("\nYour Grade is E")
    elif 50 < z <= 60:
        print("\nYour Grade is D")
    elif 60 < z <= 70:
        print("\nYour Grade is C")
    elif 70 < z <= 80:
        print("\nYour grade is B")
    elif 80 < z <= 90:
        print("\nYour grade is A")

    average = z / total_Marks * 100
    print(f"Your percentage is {average}\n")

def get_personal_info():

   name = hm.Student["Name"]
   age =  hm.Student["Age"]
   username =  hm.Student["Personal_Info"]["Username"]
   email = hm.Student["Personal_Info"]["email"]
   password =  hm.Student["Personal_Info"]["Password"]

   print(f'\n***********PERSONAL INFORMATION***********\n' 
         f"Name : {name}\n"
         f"Age : {age}\n"
         f"Username : {username}\n"
         f"Email : {email}\n"
         f"Password : {password}\n")


def update_personal_info():
    hm.Student["Name"] = input("Enter your Full Name : ")
    hm.Student["Age"] = int(input("Enter your Age : "))
    hm.Student["Personal_Info"]["email"] = input("Enter Your Email Address: ")
    hm.Student["Personal_Info"]["Password"] = mf.check_strength()
    hm.Student["Personal_Info"]["Username"] = mf.create_username(hm.Student["Personal_Info"]["email"])

    print("Your personal info is updated")

def customize_welcome_message():
    current = hm.Student["Welcome_Message"]

    print(f"Current Welcome Message : {current}\n")
    edit = input("Do you want to update your welcome message (y/n)\n").lower()

    if edit == 'y':
        hm.Student["Welcome_Message"] = input("Enter new welcome message : ")
    elif edit == 'n':
        db.dashboard_functionality()


def pakistani_cities_quiz():

    score = 0

    print("Welcome to the Pakistani Cities Quiz!\n")


    print("1. What is the capital city of Pakistan?")
    print("a) Lahore\nb) Islamabad\nc) Karachi\nd) Peshawar")
    answer1 = input("Enter your answer (a/b/c/d): ").lower()
    if answer1 == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Islamabad.\n")


    print("2. Which city is known as the 'City of Lights'?")
    print("a) Lahore\nb) Islamabad\nc) Karachi\nd) Quetta")
    answer2 = input("Enter your answer (a/b/c/d): ").lower()
    if answer2 == "c":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Karachi.\n")


    print("3. Which city is famous for the Badshahi Mosque?")
    print("a) Lahore\nb) Islamabad\nc) Multan\nd) Faisalabad")
    answer3 = input("Enter your answer (a/b/c/d): ").lower()
    if answer3 == "a":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Lahore.\n")


    print("4. Which city is known as the 'City of Saints'?")
    print("a) Multan\nb) Lahore\nc) Islamabad\nd) Rawalpindi")
    answer4 = input("Enter your answer (a/b/c/d): ").lower()
    if answer4 == "a":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Multan.\n")

    print("5. Which city is home to the famous 'Mohenjo-daro' ruins?")
    print("a) Sukkur\nb) Lahore\nc) Karachi\nd) Larkana")
    answer5 = input("Enter your answer (a/b/c/d): ").lower()
    if answer5 == "d":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Larkana.\n")

    print(f"Quiz Completed! Your score: {score}/5")

    hm.Student["Quiz_History"].append(score)

    if score == 5:
        print("Excellent! You know your Pakistani cities very well!")
    elif score >= 3:
        print("Good job! You have decent knowledge of Pakistani cities.")
    else:
        print("You can improve. Keep learning about Pakistan's beautiful cities!")


def show_quiz_history():
    print("\n--- Quiz History ---")
    if len(hm.Student["Quiz_History"]) == 0:
        print("No quizzes taken yet.")
    else:
        attempt = 1  # To track the attempt number
        for score in hm.Student["Quiz_History"]:
            print(f"Attempt {attempt}: Score = {score}/5")
            attempt += 1