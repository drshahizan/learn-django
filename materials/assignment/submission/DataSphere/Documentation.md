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


<h2>Assumptions</h2>
A few common assumptions that are implemented while developing the blogging system:

   <li>Assumptions are made about the features and capabilities required for content creation, editing, and management. This could involve assumptions about text             formatting   options, media uploading, categories, tags, and search functionalities.</li>

   <li>Assumptions are made about the desired user interactions and engagement on the platform. </li>

   <li>Assumptions are made about the user interface and user experience (UI/UX) design. This includes assumptions about the layout, navigation, and overall aesthetic         appeal of the platform.</li>


<h2>Limitations</h2>


<h2>System Interface</h2>
