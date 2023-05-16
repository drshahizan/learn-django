<h1>Car Maintenance Booking System</h1>

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
< PROJECT ROOT >
   |
   |-- booking/                               
   |    |-- __pycache__/
   |    |    
   |    |-- migrations/
   |    |    |-- __pycache__/
   |    |    |
   |    |    |-- __init__.py
   |    |    |-- 0001_initial.py
   |    | 
   |    |-- __init__.py                    
   |    |-- admin.py                         # display models in the Django admin panel                        
   |    |-- apps.py                          # allows Django to load them automatically when INSTALLED_APPS contains the path to an application module rather than the path to a configuration class.
   |    |-- models.py                        # structure of stored data
   |    |-- tests.py                         # simulate requests, insert test data, inspect your application's output
   |    |-- urls.py                          # request in Django first comes to urls.py and then goes to views.py.
   |    |-- views.py                         # takes http requests and returns http response, like HTML documents.
   |
   |-- cms/
   |    |-- __pycache__/                         
   |    |-- __init__.py
   |    |-- asgi.py
   |    |-- settings.py
   |    |-- urls.py
   |    |-- wsgi.py          
   |     
   |-- members/   
   |    |-- __pycache__/
   |    |
   |    |-- migrations/
   |    |
   |    |-- templates/
   |    |    |-- authenticate/
   |    |         |-- login.html
   |    |         |-- register_user.html
   |    |
   |    |-- __init__.py
   |    |-- admin.py                         
   |    |-- apps.py                          
   |    |-- forms.py                         # keep code easily maintainable
   |    |-- models.py                        
   |    |-- tests.py                         
   |    |-- urls.py                          
   |    |-- views.py                         
   |
   |-- db.sqlite3                            # database file that will keep all of the data that will be generating    
   |-- manage.py                             # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<h2>Design Choices</h2>


<h2>Assumptions</h2>

<h2>Limitations</h2>


<h2>How to Run Application</h2>



<h2>Video Demo</h2>



<h2>System Interface</h2>
<h4>Public Access</h4>
  

