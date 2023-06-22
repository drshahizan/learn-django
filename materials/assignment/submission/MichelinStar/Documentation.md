<h1>Social Network App </h1>

## Table of Content
- [Project Structure](#project-structure)
- [Design Choices](#design-choices)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [System Interface](#system-interface)

- [Quick Start](#quick-start)
- [Video Demo](#video-demo)


<h2>Project Structure</h2>

```bash
< PROJECT ROOT >
   |
   |-- first_project/                      # Implements app configuration
   |    |-- env                            # Inject Configuration via Environment
   |    |-- settings.py                    # Defines Global Settings
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |    |-- wsgi.py                        # Start the app in production
   |
   |-- hello/
   |    |                   
   |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |-- urls.py                   # Define user routes  
   |    |-- admin.py                  # The configuration for the Django admin interface for the app
   |    |
   |-- static/
   |    |-- assests                   # assets files
   |    |-- css                       # CSS files
   |    |-- fonts                     # fonts files
   |    |-- images                    # images files
   |    |-- js                        # js files 
   |    |-- settings                  # settings files
   |    |-- video                     # video files
   |    |
   |-- templates/                     # Templates used to render pages
   |         |-- index.html           # Templates used to index pages
   |         |-- profile.html         # Templates used to profile pages
   |         |-- search.html          # Templates used to search pages
   |         |-- setting.html         # Templates used to setting pages
   |         |-- signin.html          # Templates used to signin pages
   |         |-- signup.html          # Templates used to signup pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
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

<h4>User Login Page</h4>
<p align="center">
<img src="
" width="600" />
</p>

<h4>User Sign Up Page</h4>
<p align="center">
<img src="https://github.com/drshahizan/learn-django/assets/120615951/0f221929-5f74-4ec4-b31a-f3fef8a7008a" width="600" />
</p>

<h4>Set Up after Sign Up</h4>
<p align="center">
<img src="https://github.com/drshahizan/learn-django/assets/120615951/4bb39ced-368f-408b-8d5c-8ac79cdb5f15" width="600" />
</p>

<h4>User Home Page</h4>
<p align="center">
<img src="https://github.com/drshahizan/learn-django/assets/120615951/1524b508-859d-4132-84fa-f334785dd1a0" width="600" />
</p>

<h4>Upload Photo</h4>
<p align="center">
<img src="https://github.com/drshahizan/learn-django/assets/120615951/f48ed4f3-9841-4b77-a7f1-295aa3c3aa10" width="600" />
</p>

<h4>Search Result </h4>
<p align="center">
<img src="https://github.com/drshahizan/learn-django/assets/120615951/8b26c404-42d1-4458-a301-9ce2def2157d" width="600" />
</p>

<h4>View Other Users</h4>
<p align="center">
<img src="https://github.com/drshahizan/learn-django/assets/120615951/852b4f2e-1249-4296-8dfe-8d34ebb00808" width="600" />
</p>

<h2>Quick Start</h2>
<ul>
<li><a href="https://github.com/drshahizan/learn-django/blob/main/materials/django/topic/1-setting.md">How to run the project</a></li>

<li><a href="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/MichelinStar/QuickStart.md">How to run the project (if downloaded python and django)</a></li>
</ul>

<h2>Video Demo</h2>
<a href="https://www.youtube.com/watch?v=Linar24QyzY">Youtube Demo Link</a>

