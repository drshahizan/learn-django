<h1>Car Booking System</h1>

## Table of Content
- [Project Structure](#project-structure)
- [Design Choices](#design-choices)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [System Interface](#system-interface)
   - [Customers](#customers)
   - [Public Access](#public-access)
   - [Admin](#admin)

<h2>Project Structure</h2>

```bash
< PROJECT ROOT >  ///still in progress...do not change
   |
   |-- booking/                               # Implements app configuration
   |    |-- __pycache__/
   |    |    
   |    |-- migrations/
   |    |    |-- __init__.py
   |    |    |-- 0001_initial.py
   |    |
   |    |-- __init__.py                    # Defines Global Settings
   |    |-- admin.py                        # Start the app in production
   |    |-- apps.py                        # Define URLs served by all apps/nodes
   |    |-- models.py
   |    |-- models.py
   |    |-- tests.py
   |    |-- urls.py
   |    |-- views.py
   |
   |-- cms/
   |    |
   |    |-- __pycache__/                          # A simple app that serve HTML files
   |    |        
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component of admin
   |         |    |-- navigation2.html     # Top menu component of customer
   |         |    |-- navigation3.html     # Top menu component of landing page
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |    |-- base2.html            # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<h2>Design Choices</h2>



<h2>Assumptions</h2>



<h2>Limitations</h2>



<h2>System Interface</h2>
<h4>Public Access</h4>
  

