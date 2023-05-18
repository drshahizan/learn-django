<h1>Food Delivery System</h1>
```bash
#!/bin/bash

echo "Hello, World!"
```

## Table of Content
- [Project Structure](#project-structure)
- [Design Choices](#design-choices)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [System Interface](#system-interface)
   - [Homepage](#homepage)
   - [Admin](#admin)
   - [Customer](#customer)

<h2>Project Structure</h2>
```bash
< PROJECT ROOT >
   |
   |-- customer/                             
   |    |-- __pycache__                      
   |    |-- migrations/   
   |    |         |-- __pycache__
   |    |         |-- 0001_initial.py 
   |    |         |-- 0002_ordermodel_city_ordermodel_email_ordermodel_name_and_more.py
   |    |         |-- 0003_ordermodel_is_paid.py 
   |    |         |-- 0004_ordermodel_is_shipped.py
   |    |         |-- __init__.py 
   |    |-- templates/customer   
   |    |         |-- about.html   
   |    |         |-- base.html 
   |    |         |-- footer.html  
   |    |         |-- index.html  
   |    |         |-- menu.html
   |    |         |-- navigation.html 
   |    |         |-- order.html  
   |    |         |-- order_confirmation.html
   |    |         |-- order_pay_confirmation.html    
   |    |--__init__.py
   |    |--admin.py
   |    |--apps.py
   |    |--models.py
   |    |--tests.py
   |    |--views.py
   |-- deliver/
   |    |--__pycache__
   |    |-- home/                          
   |    |--__init__.py   
   |    |-- asgi.py                     
   |    |-- settings.py  
   |    |-- urls.py           
   |    |-- wsgi.py             
   |-- djangoenv/               
   |    |--Lib/site-packages                 
   |    |--Scripts                  
   |    |--pyvenv.cfg                 
   |    |
   |-- media/menu_images/
   |    |-- FP-Nasi-lemak-with-all-its-trimmings.jpg        
   |    |--aglio.jpg
   |    |--cheesecake.jpg
   |    |--chickendrummet.jpg
   |    |--fishchip.jpg
   |    |--friedrice.jpg
   |    |--icedcappo.jpg
   |    |--laksa.jpg
   |    |--lambshank.jpg
   |    |--lavacake.jpg
   |    |--spaghetti.jpg
   |    |--wonton.jpg
   |    |
   |-- restaurant/                     
   |    |-- __pycache__
   |    |-- templates/restaurant/                 
   |    |         |-- navigation.html     
   |    |         |-- base.html     
   |    |         |-- dashboard.html     
   |    |         |-- order-details.html         
   |    |--__init__.py        
   |    |--account_adapter.py        
   |    |-- admin.py                   
   |    |-- apps.py 
   |    |-- models.py            
   |    |-- tests.py           
   |    |--urls.py                
   |    |
   |--templates/
   |    |--account/
   |    |      |-- email/
   |    |      |-- messages/
   |    |      |-- snippets/
   |    |      |-- account_inactive.html
   |    |      |-- base.html
   |    |      |-- email.html
   |    |      |-- email_confirm.html
   |    |      |-- login.html
   |    |      |-- logout.html
   |    |      |-- password_change.html
   |    |      |-- password_reset.html
   |    |      |-- password_reset_done.html
   |    |      |-- password_reset_from_key.html
   |    |      |-- password_reset_from_key_done.html
   |    |      |-- password_set.html
   |    |      |-- signup.html
   |    |      |-- signup_closed.html
   |    |      |-- verification_sent.html
   |    |      |-- verified_email_required.html
   |    |--openid/  
   |    |      |-- base.html
   |    |      |-- login.html
   |    |--socialaccount/   
   |    |      |-- messages/
   |    |      |-- snippets/
   |    |      |-- base.html
   |    |      |-- authentication_error.html
   |    |      |-- connections.html
   |    |      |-- login_cancelled.html
   |    |      |-- signup.html
   |    |--tests
   |    |      |-- test_403_csrf.html
   |    |--base.html  
   |--db.sqlite3                   # Development modules - SQLite storage
   |
   |-- manage.py                   # Start the app - Django default start script
   |
   |-- ************************************************************************
```

### Homepage
Both admin and customers can access the homepage of the website for MakanMakan.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Homepage.png">
 
### Admin

**1. Dashboard**

Admin can see the total revenue and total orders for the current day. Admin can also monitor the orders that has not been paid and shipped including the customers information.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Dashboard.png">
 
**2. Login**
 
 Admin can access two different login pages.
 
 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Admin%20Login.png">
 
 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Sign%20In.png">

**3. Forget Password**

Admin can reset their password in the Forget Password page by providing their email address.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Forget%20Password.png">

**4. Admin Site**

Admin can see the recent changes that they have committed and also edit the sub-categories for each categories by pressing the Add and Change button.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Admin%20Site.png">
 
 **5. Change Password**
 
 Admin can change the password by providing the old password and the new password.
 
 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Change%20Password.png">

### Customer
