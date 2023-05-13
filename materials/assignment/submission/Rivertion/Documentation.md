<h1 align="center"> Student Information System </h1>

## Table of Contents
- [Codebase Structure](#codebase-structure)
- [Design Choices](#design-choices)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [Screenshots](#screenshots)

<h2>Codebase Structure</h2>
    
```bash
.
└── <StudentInformationSystem>/                                                 # Root directory of the project
    ├── main_app/                                                               # Main application directory
    │   ├── _pycache_                                                           # Python cache directory
    │   │ 
    │   ├── migrations/                                                         # Database migration files
    │   │   ├── _pycache_                                                       # Python cache directory for migrations
    │   │   ├── __init__.py                                                     # Initialization file for migrations
    │   │   └── 0001_initial.py                                                 # Initial migration file
    │   │ 
    │   ├── static/                                                             # Static files directory
    │   │   ├── dist/                                                           # Distribution directory
    │   │   │   └── <css img js>                                                # CSS, image, and JavaScript files
    │   │   ├── plugins/                                                        # Plugins directory
    │   │   │   └── <Bootstrap and Javascripts plugins>                         # Bootstrap and JavaScript plugins
    │   │   └── 01 PROJECT INFO.txt                                             # Information file about the project
    │   │ 
    │   ├── templates/ <.html>                                                  # HTML templates directory
    │   │   ├── hod_template                                                    # Head of Department (HOD) templates
    │   │   ├── main_app                                                        # Main application templates
    │   │   ├── registartion                                                    # Registration templates
    │   │   ├── staff_template                                                  # Staff templates
    │   │   └── student_template                                                # Student templates
    │   │ 
    │   ├── __init__.py                                                         # Initialization file for the main app
    │   ├── 01 PROJECT INFO.txt                                                 # Information file about the main app
    │   ├── admin.py                                                            # Django admin configuration file
    │   ├── apps.py                                                             # Django application configuration file
    │   ├── EditResultView.py                                                   # View file for editing results
    │   ├── EmailBackend.py                                                     # Email backend file
    │   ├── forms.py                                                            # Form definition file
    │   ├── hod_views.py                                                        # Views for Head of Department (HOD)
    │   ├── middleware.py                                                       # Middleware configuration file
    │   ├── models.py                                                           # Database models file
    │   ├── staff_views.py                                                      # Views for staff members
    │   ├── student_views.py                                                    # Views for students
    │   ├── test.py                                                             # Test file
    │   ├── urls.py                                                             # URL configurations
    │   └── views.py                                                            # Views file
    │
    ├── media/                                                                  # Directory for saved uploaded images
    │
    ├── student_information_system/                                             # Student Information System directory
    │   ├── _pycachce_                                                          # Python cache directory
    │   ├── __init__.py                                                         # Initialization file
    │   ├── 01 PROJECT INFO.txt                                                 # Information file about the project
    │   ├── asgi.py                                                             # ASGI configuration file
    │   ├── settings.py                                                         # Django settings file
    │   ├── urls.py                                                             # URL configurations
    │   └── wsgi.py                                                             # WSGI configuration file
    │
    ├── 01 PROJECT INFO.txt                                                     # Information file about the project
    ├── db.sqlite3                                                              # SQLite database file
    ├── LICENSE                                                                 # License file
    ├── manage.py                                                               # Django management file
    ├── Procfile                                                                # File for specifying Heroku process types
    └── requirements.txt                                                        # File listing required libraries and dependencies
```
    
<h2>Design Choices</h2>

This system application is about a Student Information System which aims to facilitate the management and administration tasks in a college or educational institution. It includes features such as student enrollment, course management, faculty administration, attendance tracking, exam management, and generating reports.

In this system, there are four main models which act as Python classes that represent database tables. These models then can perform Create, Read, Update, Delete (CRUD) operations and implement various functionalities. Below are the models:
<ul>
  <li> Course: Educational program that students can enroll in </li>
  <li> Subject: Specific topic or class within a course </li>
  <li> Session: Academic period </li>
  <li> Student: Individual who is enrolled in the college </li>
  <li> Staff: Individual who gives lecture to the students </li>
</ul>

Below are the tools and languages that are used in developing this system:
<ul>
  <li>Python: Main programming language</li>
  <li>Django: Web framework</li>
  <li>HTML: Creating the base structure</li>
  <li>CSS: Styling the system</li>
  <li>JavaScript: Adding interactivity and dynamic features</li>
</ul>

<h2>Assumptions</h2>

When developing a college management system, there can be several common assumptions that might apply. Below are the assumptions found:
<ul>
  <li>The system assumes a standard college or educational institution setup with typical administrative and academic processes.</li>
  <li>It assumes that the college management system will be used by authorized staff members, students, and faculty members who have appropriate credentials.</li>
  <li>It assumes that the necessary hardware and infrastructure, such as servers, databases, and internet connectivity, are available for the system to operate effectively.</li>
  <li>It assumes that the system will support a specific number of users, courses, subjects, and other entities based on the anticipated requirements.</li>
</ul>

<h2>Limitations</h2>

There are also limitations and drawbacks that may be present when designing the system. Below are the limitations:
<ul>
  <li>The system might have limitations in terms of scalability, performance, and handling a large volume of data or concurrent users.</li>
  <li>It may not address all the specific needs and requirements of every college or educational institution, as different institutions may have unique processes and workflows.</li>
  <li>The system might not include advanced features or specialized functionalities that could be required by specific colleges.</li>
  <li>It may have limitations in terms of customization, requiring additional development effort to adapt it to the specific needs of a particular institution.</li>
</ul>

<h2>Screenshots</h2>

- Login
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/Login.png">

- Dashboard
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/Dashboard_1.png">
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/Dashboard_2.png">

- Update Profile
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/update_profile.png">

- Student Page
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/Student_page.png">

- Add Course
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/add_course.png">

- Manage Course
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/manage_course.png">

- Add Session
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/add_session.png">

- Manage Session
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/manage_session.png">

- Add Staff
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/add_staff.png">

- Manage Staff
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/manage_staff.png">

- Add Student
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/add_student1.png">
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/add_student2.png">

- Manage Student
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/manage_student.png">

- Add Subject
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/add_subject.png">

- Manage Subject
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/manage_subject.png">

- Notify Staff
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/notify_staff.png">

- Notify Student
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/notify_student.png">

- View Notification
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/view_notification.png">

- View Attendance
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/view_attendance.png">

- View Attendance Student
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/view_attendanceStudent.png">

- Apply Leave
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/Apply_Leave.png">

- Staff Leave
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/staff_leave.png">

- Student Leave
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/student_leave.png">

- Feedback Form
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/Feedback_Form.png">

- Staff Feedback
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/staff_feedback.png">

- Student Feedback
<img width="947" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Rivertion/Images/student_feedback.png">


