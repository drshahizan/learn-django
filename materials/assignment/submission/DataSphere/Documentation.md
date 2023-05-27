<h1>Blogging Platform</h1>

## Table of Content
- [Project Structure](#project-structure)
- [Design Choices](#design-choices)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [System Interface](#system-interface)

<h2>Project Structure</h2>

```
< PROJECT ROOT >
   |
   |-- blog/                                  # Django app for blog functionality
   |    |-- __pycache__/                      # Compiled Python files (bytecode)
   |    |    |-- __init__.cpython-311.pyc
   |    |    |-- admin.cpython-311.pyc
   |    |    |-- apps.cpython-311.pyc
   |    |    |-- models.cpython-311.pyc
   |    |    |-- urls.cpython-311.pyc
   |    |    |-- views.cpython-311.pyc
   |    |
   |    |-- migrations/                       # Database migration files
   |    |    |-- __pycache__/                  # Compiled Python files (bytecode)
   |    |    |
   |    |    |-- 0001_initial.py               # Initial database migration file
   |    |    |-- __init__.py                    # Migration package initializer
   |    |
   |    |-- static/blog/                       # Static files for the blog app (CSS, JavaScript, etc.)
   |    |    |-- main.css
   |    |
   |    |-- templates/blog/                    # HTML templates for the blog app
   |    |    |-- about.html                     # About page template
   |    |    |-- base.html                      # Base template (common elements for other templates)
   |    |    |-- home.html                      # Home page template
   |    |    |-- post_confirm_delete.html        # Post deletion confirmation template
   |    |    |-- post_detail.html                # Post detail template
   |    |    |-- post_form.html                  # Post creation/edit form template
   |    |
   |    |-- __init__.py                         # Blog app package initializer
   |    |-- admin.py                            # Admin site configuration for the blog app
   |    |-- apps.py                             # App configuration for the blog app
   |    |-- models.py                           # Models (database schema) for the blog app
   |    |-- tests.py                            # Unit tests for the blog app
   |    |-- urls.py                             # URL routing configuration for the blog app
   |    |-- views.py                            # View functions (request handlers) for the blog app
   |    
   |-- blogproj/                               # Django project configuration
   |    |-- __pycache__/                       # Compiled Python files (bytecode)
   |    |    |-- __init__.cpython-311.pyc
   |    |    |-- settings.cpython-311.pyc
   |    |    |-- urls.cpython-311.pyc
   |    |    |-- wsgi.cpython-311.pyc
   |    |
   |    |-- __init__.py                         # Project package initializer
   |    |-- asgi.py                             # ASGI configuration for the project
   |    |-- settings.py                         # Project settings (database, static files, etc.)
   |    |-- urls.py                             # Root URL routing configuration for the project
   |    |-- wsgi.py                             # WSGI configuration for the project
   |    
   |-- media/                                  # Media files uploaded by users
   |    |-- profile_pics/                      # User profile picture directory
   |    |-- default.jpg                         # Default profile picture
   |    
   |-- users/                                  # Django app for user management
   |    |-- __pycache__/                       # Compiled Python files (bytecode)
   |    |    |-- __init__.cpython-311.pyc
   |    |    |-- admin.cpython-311.pyc
   |    |    |-- apps.cpython-311.pyc
   |    |    |-- forms.cpython-311.pyc
   |    |    |-- models.cpython-311.pyc
   |    |    |-- signals.cpython-311.pyc
   |    |    |-- views.cpython-311.pyc
   |    |
   |    |-- migrations/                       # Database migration files
   |    |    |-- __pycache__/                  # Compiled Python files (bytecode)
   |    |    |
   |    |    |-- 0001_initial.py               # Initial database migration file
   |    |    |-- __init__.py                    # Migration package initializer
   |    |
   |    |-- static/blog/                       # Static files for the users app (CSS, JavaScript, etc.)
   |    |    |-- main.css
   |    |
   |    |-- templates/users/                   # HTML templates for the users app
   |    |    |-- login.html                     # User login template
   |    |    |-- logout.html                    # User logout template
   |    |    |-- profile.html                   # User profile template
   |    |    |-- profile_update.html            # User profile update form template
   |    |    |-- register.html                  # User registration template
   |    |
   |    |-- __init__.py                         # Users app package initializer
   |    |-- admin.py                            # Admin site configuration for the users app
   |    |-- apps.py                             # App configuration for the users app
   |    |-- forms.py                            # Forms (input validation) for the users app
   |    |-- models.py                           # Models (database schema) for the users app
   |    |-- signals.py                          # Signal handlers for the users app
   |    |-- tests.py                            # Unit tests for the users app
   |    |-- views.py                            # View functions (request handlers) for the users app
   |    
   |-- db.sqlite3                             # SQLite database file
   |                               
   |-- manage.py                              # Django's command-line utility for administrative tasks
   |
   |-- ************************************************************************
  ```

<h2>Design Choices</h2>

Our team was tasked with creating a blogging platform using Django. Users should be able to manage their own postings, make and publish blog entries, and leave comments on other people's writings on the platform. The most popular content and overall blog activity could be shown on the admin dashboard. Django was selected as the project's framework because it is an established framework that is ideal for creating online applications. Data for the project will be kept in a SQLite database. For tiny applications, SQLite is the ideal database because it is compact and simple to use. The application's primary data models are Profile and BlogModel. When building user profiles and blog entries, these models can conduct Create, Read, Update, and Delete (CRUD) activities. The project's user interface will be styled using the Bootstrap CSS framework. A responsive and mobile-friendly user interface can be easily made using the well-liked and documented Bootstrap framework.


Below are the tools and languages that are used in developing this system:

    Python: Main programming language
    Django: Web framework
    HTML: Creating the base structure
    CSS: Styling the system
    JavaScript: Adding interactivity and dynamic features



<h2>Assumptions</h2>
A few common assumptions that are implemented while developing the blogging system:
<ul>

   <li>The platform assumes that it is governed only by the Administrator (Admin user). </li>

   <li>The platform assumes that everyone that visits the blogging platform can make and publish blog entries, as well as comment on other’s posts </li>

   <li>The platform assumes that the general public are well aware of the procedures in creating and managing their blog posts</li>
</ul>

<h2>Limitations</h2>
A few limitations that are faced while developing the blogging system are:
<ul>

   <li> Designing a user-friendly and visually appealing interface was a bit challenging. Balancing functionality with simplicity, creating intuitive navigation, and           optimizing the user experience across different devices and screen sizes can present difficulties..</li>

   <li>Limited time for the development of blogging system </li>

   <li>Development was a little bit limited by technical constraints which impacted the performance and scalability of the blogging system..</li>
</ul>

<h2>Additional Features</h2>
There are several other features that might be added to the project in addition to the core ones of the Django blogging platform. These characteristics could include:
<ul>
<li>The capability of labeling blog content using categories and tags.</li>
<li>The capability of comment moderation.</li>
<li>The capacity to follow blog entries.</li>
<li>Being able to monitor blog traffic.</li>
</ul>
The Django blogging platform would become a more potent and adaptable tool for users with the addition of these new functionalities.





<h2>System Interface</h2>
