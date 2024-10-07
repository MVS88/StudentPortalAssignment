
---

# Student Portal Application

## Overview

This is a simple student portal application built in Python. The application allows students to register, log in, and access a dashboard with various features. The project is modular, with different files handling various aspects of the application, making it easy to maintain and expand.

---

## File Structure

### 1. **HelpingMaterial.py**
   This file contains common resources or utilities that are used across the entire project. It may include:
   - Menus for the student portal
   - Helper functions for input validation
   - Messages or constants used across the app

   **Usage:**
   - This module is imported into other files like `Main.py` to display menus and use shared resources.

---

### 2. **Main.py**
   This is the entry point of the application. It handles the basic user interaction through a menu-driven interface and calls different functionalities based on user input.

   **Features:**
   - Display the main menu
   - Handle user inputs to register, log in, access the dashboard, log out, and exit the program
   - Import necessary modules like `Dashboard.py` and `Registration.py` to handle those specific functionalities

   **Usage:**
   - Run this file to start the application.

---

### 3. **MainFunctions.py**
   This file contains all the functions that are used by the `Main.py` file to manage the core functionalities of the student portal.

   **Functions Included:**
   - **register_user()**: Allows users to register by taking input such as name, age, marks, email, and password.
   - **login_user()**: Allows users to log in using their credentials.
   - **menu_display()**: Displays the main menu to users.
   
   **Usage:**
   - Functions in this file are invoked by `Main.py` to handle user registration, login, and other menu-based operations.

---

### 4. **Dashboard.py**
   This file manages the functionality related to the student dashboard, which the user can access after logging in. The dashboard offers additional features like viewing quiz history, updating details, etc.

   **Features:**
   - Access to student-related features once logged in
   - Links to various features like quizzes, viewing performance, and more
   
   **Usage:**
   - The dashboard is called from `Main.py` after a user successfully logs in.

---

### 5. **DashboardFunctions.py**
   This file contains all the functions used by `Dashboard.py`. It handles specific functionalities related to the student dashboard.

   **Functions Included:**
   - **dashboard_functionality()**: Main function to display dashboard options and allow the user to interact with the dashboard features.
   - **show_quiz_history()**: Function to display a student's quiz history.
   - **update_profile()**: Allows users to update their personal information.
   
   **Usage:**
   - `Dashboard.py` imports and calls functions from this file to execute the dashboard features.

---

## How to Run the Project

1. Make sure you have Python installed on your system.
2. Clone or download the project files.
3. Open a terminal or command prompt in the project directory.
4. Run the `Main.py` file using the command:
   ```bash
   python Main.py
   ```
5. Follow the on-screen instructions to navigate through the student portal.

---

## Features

- **User Registration:** Register yourself as a student with required details.
- **User Login:** Secure login with username and password.
- **Student Dashboard:** Once logged in, access the student dashboard to view your quiz history, update personal information, and more.
- **Quiz History:** View the history of your past quiz attempts and scores.

---

## Future Enhancements

- Add more features to the student dashboard like quiz-taking, personalized messages, and performance tracking.
- Improve security measures, such as password encryption.
- Add a database to store user information persistently.

---

## Contributing

If you would like to contribute to the project, feel free to submit a pull request or raise an issue for any bugs or feature suggestions.

---

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

