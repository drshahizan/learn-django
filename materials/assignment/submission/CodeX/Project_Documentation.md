<h1>Car Maintenance Booking System</h1>

## Table of Content
- [Project Structure](#project-structure)
- [Design Choices](#design-choices)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [How to Run Application](#how-to-run-application)
- [Video Demo](#video-demo)
- [System Interface](#system-interface)

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
The Car Maintenance System is designed to assist customers in scheduling their car maintenance appointments conveniently via the company's website. It offers various features, including customer registration, a user-friendly booking form, and tools for tracking and managing bookings. Additionally, the system administrator has access to a comprehensive list of all bookings made by customers.

Within this system, there are four primary models implemented as Python classes, each representing a specific database table. These models facilitate Create, Read, Update, and Delete (CRUD) operations while incorporating various functionalities. The following are the models:

1. Customer Model: This model stores information related to customer details, such as their first name, last name, and registration details. It enables CRUD operations to manage customer data effectively.
2. Booking Model: The Booking Model is responsible for storing information regarding car maintenance bookings made by customers. It includes details like the customer's ID, type of maintenance to be made, preferred date and time for the maintenance, and any additional comments. CRUD operations can be performed on this model to manage booking records efficiently.
3. Admin Model: The Admin Model represents the system administrator. It contains data such as the administrator's username, password, and access privileges. This model allows CRUD operations to manage administrator accounts and their associated permissions. Admin could also view the list of bookings made by customers.
4. Service Model: The Service Model holds information about the various car maintenance services provided by the company. It includes details such as service names, descriptions, durations, and prices. CRUD operations on this model enable the addition, modification, and deletion of services offered by the company.

Below are the tools and languages that are used in developing this system:
1. Python
2. HTML
3. CSS
4. Bootstrap
5. Django
6. JavaScript


<h2>Assumptions</h2>

1. The system is designed as a web-based application, accessible through a web browser, allowing customers to make car maintenance bookings on the company's website. The system administrator can log in securely to access administrative functionalities.
2. User authentication and authorization mechanisms are implemented, requiring customers to register and log in to access booking features, while the system administrator has exclusive access to administrative tools. The Admin Model facilitates the management of administrator accounts and permissions.
3. The system incorporates features for tracking and managing bookings, allowing customers to view their booking details and providing the system administrator with access to a comprehensive list of all customer bookings. This facilitates efficient monitoring and organization of maintenance appointments.

<h2>Limitations</h2>

1. The system may face limitations in handling a growing number of customers and bookings, potentially resulting in performance issues and the need for additional resources.
2. The system's user experience may be hindered if it lacks intuitive and user-friendly design, leading to difficulties in navigation or understanding instructions.
3. While the system covers basic functionalities, it may lack advanced features such as automated reminders or comprehensive reporting capabilities.

<h2>How to Run Application</h2>

To access the system on your local host, please follow these steps after downloading the app folder:

1. Open the cms folder until the manage.py file is in view

<img height='200px' src='https://github.com/drshahizan/special-topic-data-engineering/assets/96984290/43f37a92-c7a1-4e67-9c74-04b498a862dd'/>

2. Type in `cmd` in the diirectory, then hit enter.

![2](https://github.com/drshahizan/learn-django/assets/96984290/18d6c8ff-1a57-4207-9cab-2c3068c7c89d)

3. A command prompt will appear. Execute the provided command within the command prompt.

```python
#copy paste into the command prompt
python manage.py runserver
```

4. This command will launch the website on your local host, allowing you to view and interact with it. Copy and paste the link provided by the cmd prompt

![3](https://github.com/drshahizan/learn-django/assets/96984290/37e1326a-f069-46d6-8ce4-507ece5ab12d)


<h2>Video Demo</h2>



<h2>System Interface</h2>


  

