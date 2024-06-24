# Library Management System

"""
This Python program simulates a basic library management system with functionalities
for students, faculty, and administrators. It includes user authentication and
registration processes for different user roles (student, faculty, administrator).

Files Used:
- Student.txt: Stores usernames and passwords of students.
- Faculty.txt: Stores usernames and passwords of faculty members.
- Admin.txt: Stores usernames and passwords of administrators.

Functions:
1. signUp_student(): Allows students to sign up with a username and password.
2. login_student(): Allows students to log in with their credentials.
3. signUp_faculty(): Allows faculty members to sign up with a username and password.
4. login_faculty(): Allows faculty members to log in with their credentials.
5. signUp_admin(): Allows administrators to sign up with a username and password.
6. login_admin(): Allows administrators to log in with their credentials.
7. Main Menu:
   - Provides options for students, faculty, and administrators to perform login, sign up,
     or specific administrative tasks such as adding new users (students or faculty).

Usage:
- Run the program and choose your role (student, faculty, administrator) to access
  corresponding functionalities.
- Students and faculty can log in using their credentials after signing up.
- Administrators have additional options to add new students or faculty members.

Notes:
- Usernames and passwords are stored in plain text in separate files (Student.txt,
  Faculty.txt, Admin.txt). Consider enhancing security measures for storing passwords
  in a real-world application.
