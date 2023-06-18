<h1>Social Network App </h1>

## Table of Content
- [Project Structure](#project-structure)
- [Design Choices](#design-choices)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [System Interface](#system-interface)
   - [Customers](#customers)
   - [Public Access](#public-access)
   - [Admin](#admin)
- [Quick Start](#quick-start)

<h2>Project Structure</h2>
```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define user routes  
   |    |    |-- forms.py                  # Define some forms (product, category, cart and order) 
   |    |    |-- admin.py                  # The configuration for the Django admin interface for the app
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
The application is a social network platform that enables users to upload their photos, follow other users and interact from one to another as they are able to like and comment on the photos of other users. The application is designed to provide a user-friendly and intuitive experience, featuring a straightforward and responsive interface that enables users to swiftly locate desired information.

The main data models in this application are User, Post and Comment. These data models are able to perform Create, Read, Update, Delete (CRUD) operations.


<h2>Assumption</h2>
<ul>
  <li>It assumes that there will be no same username in the system.</li>
  <li>It assumes that the new users will need to register first and system will be able to used by authorized staffs and user who have appropriate credentials.</li>
  <li>It assumes that in order for the system to operate correctly, some important infrastructure are needed such as servers, databases and  connectivity.</li>
  <li>It assumes that the system will allow users to upload photos as well as follow and view photos of other users.</li>
</ul>


<h2>Limitation</h2>
<ul>
   <li>The system could have limitation on handling large amount of user or large scale application.</li>
   <li>The system may not provide advance setting or special functions for users as there are only basic settings and features.</li>
   <li>The system will have limitation on  sharing or interacting with other application as there is no function to share to others.</li>
   <li>The system will not able to handle complicated uploaded file as users are only able to upload one picture at a time.</li>
   <li>The user of the system may not have enough of privacy as they system are not able to make privacy setting on users' account.</li>
</ul>


<h2>System Interface</h2>
<h2>Video Demo</h2>
<a href"https://www.youtube.com/watch?v=Linar24QyzY">Youtube Demo Link : </a>
https://www.youtube.com/watch?v=Linar24QyzY
