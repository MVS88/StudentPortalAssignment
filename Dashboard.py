import HelpingMaterial as hm
import DashBoardFunctions as df


def dashboard_functionality():
    print(hm.dashboard_Menu)

    while True:
        choice = int(input("Enter your choice : "))
        if choice == 1:
            df.grade_calculator()

        elif choice == 2:
            df.get_personal_info()

        elif choice == 3:
            df.update_personal_info()

        elif choice == 4:
            df.customize_welcome_message()

        elif choice == 5:
            df.pakistani_cities_quiz()

        elif choice == 6:
            df.show_quiz_history()

        elif choice == 7:
            import Main as m
            m.main()
