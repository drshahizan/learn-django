<h1> Student Information System </h1>

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

