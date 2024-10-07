import HelpingMaterial as hm
import MainFunctions as mf
import DashBoardFunctions as df
import Dashboard

# My Main function that will perform all the functionalities

def main():
    while True:
        login_status = False
        main_Menu_choice = int(input("Enter your choice : "))

        if main_Menu_choice == 1:
            mf.register_user()
            print(hm.menu)

        elif main_Menu_choice == 2:
            mf.login_user()
            login_status = True
            print(hm.Student["Welcome_Message"])
            Dashboard.dashboard_functionality()

        elif main_Menu_choice == 3:
             if login_status == True:
                  Dashboard.dashboard_functionality()
             else:
                  print("You need to login first")

        elif main_Menu_choice == 4:
              print("You logged out of your account")
              login_status = False

        elif main_Menu_choice == 5:
           print("THANKS FOR USING STUDENT PORTAL")
           break


print(hm.menu)
main()