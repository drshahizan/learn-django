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

Within this system, there are four primary models implemented as Python classes, each representing a specific database table. These models facilitate Create, Read, Update, and Delete (CRUD) operations while incorporating various functionalities. 

The following are the models:

1. `Customer Model`: This model stores information related to customer details, such as their first name, last name, and registration details. It enables CRUD operations to manage customer data effectively.
2. `Booking Model`: The Booking Model is responsible for storing information regarding car maintenance bookings made by customers. It includes details like the customer's ID, type of maintenance to be made, preferred date and time for the maintenance, and any additional comments. CRUD operations can be performed on this model to manage booking records efficiently.
3. `Admin Model`: The Admin Model represents the system administrator. It contains data such as the administrator's username, password, and access privileges. This model allows CRUD operations to manage administrator accounts and their associated permissions. Admin could also view the list of bookings made by customers.
4. `Service Model`: The Service Model holds information about the various car maintenance services provided by the company. It includes details such as service names, descriptions, durations, and prices. CRUD operations on this model enable the addition, modification, and deletion of services offered by the company.

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

<h4>Public</h4>

<h4>Admin</h4>

1. Login Page.(Login as admin)
![Screenshot 2023-05-27 001040](https://github.com/drshahizan/learn-django/assets/92329710/fce12b5b-5711-493c-8365-1fa12b0d91ef)

2. Home Page of Admin.
![Screenshot 2023-05-27 001057](https://github.com/drshahizan/learn-django/assets/92329710/0aaea240-838f-4840-83c7-df577db61390)

3. Customer Booking List. (Admin View)
![Screenshot 2023-05-27 002204](https://github.com/drshahizan/learn-django/assets/92329710/83c1c6e9-da78-4d44-8449-e37e0b9e6811)
![Screenshot 2023-05-27 002226](https://github.com/drshahizan/learn-django/assets/92329710/76749816-de91-4100-ab82-18bceca81c22)

4. Edit Booking Status.
a. Admin approve customer booking.
![Screenshot 2023-05-27 002320](https://github.com/drshahizan/learn-django/assets/92329710/40d8ac05-bbcc-4c4e-94e9-80b13d6f3c7d)
b. Approved booking updated into approved booking list.
![Screenshot 2023-05-27 002343](https://github.com/drshahizan/learn-django/assets/92329710/6e629e3c-9420-4c90-8d47-34ffaa976680)
c. Message shows that appointment has been edited successfully.
![Screenshot 2023-05-27 002423](https://github.com/drshahizan/learn-django/assets/92329710/e9ceef35-def6-423d-8a1a-54ed5dcd740c)
d. Admin reject customer booking.
![Screenshot 2023-05-27 002511](https://github.com/drshahizan/learn-django/assets/92329710/ed430ef5-f68f-4c22-a66d-1e2e994bf5a6)
e. Rejected booking updated into rejected booking list.
![Screenshot 2023-05-27 002545](https://github.com/drshahizan/learn-django/assets/92329710/e1ec8829-0b7f-49d0-b2d8-79170a088b46)

5. Profile View (Admin)
![Screenshot 2023-05-27 002600](https://github.com/drshahizan/learn-django/assets/92329710/3a68ff07-9c2a-4a3b-a413-8861baf9488d)


<h4>Customer</h4>


  

