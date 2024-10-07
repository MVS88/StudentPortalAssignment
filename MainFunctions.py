#this file contains the functionality for user login.
import HelpingMaterial as hm
from curses.ascii import isdigit, isupper

def login_user():

    username = input("Enter your Username : ")
    password = input("Enter your password : ")

    if username == hm.Student["Personal_Info"]["Username"] and password == hm.Student["Personal_Info"]["Password"]:
        print("Login Successful")
    else:
        print("Login Failed Kindly try again")



def check_strength():

    is_secure = False

    contains_letter = 0
    contains_digit = 0
    contains_upper = 0
    contains_special = 0

    while is_secure == False:

      password = input("Enter your password : ")

      z = len(password)

      special_Char = ['@','!','#','%','*','_']


      for x in password:
          if isdigit(x):
              contains_digit = 1

      for x in password:
          if isupper(x):
              contains_upper = 1

      for x in password:
         if x in special_Char:
             contains_special = 1


      if z < 8 :
          print("\nYou password must be 8 letters or above")
      else:
          contains_letter = 1

      if contains_digit != 1:
          print("Your password must contain a number")

      if contains_upper != 1:
          print("Your password must contain an upper case letter")

      if contains_special != 1:
         print("Your password must contain a special character")

      if contains_digit == 1 and contains_upper == 1 and contains_special == 1 and contains_letter == 1:
        is_secure = True
        print("\nYour Password is secure and saved")
        return password




def create_username(email):
    username = email.split('@')[0]
    return username




#User registration function using the same data structure sir provided.
def register_user():
    hm.Student["Id"] = hm.Student["Id"] + 1
    hm.Student["Name"] = input("Enter your Full Name : ")
    hm.Student["Age"] = int(input("Enter your Age : "))
    hm.Student["Marks"] = int(input("Enter your Marks Obtained : "))
    hm.Student["Personal_Info"]["email"] = input("Enter Your Email Address: ")
    hm.Student["Personal_Info"]["Password"] = check_strength()
    hm.Student["Personal_Info"]["Username"] = create_username(hm.Student["Personal_Info"]["email"])

    print("Your registration is successful")
    print("Your username is", hm.Student["Personal_Info"]["Username"])
    id = hm.Student["Id"]
    print(f"Your Student Id is {id}")