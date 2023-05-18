<h1>Food Delivery System</h1>

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
   |--db.sqlite3                   
   |
   |-- manage.py                   
   |
   |-- ************************************************************************
 ```
<h2>Design Choices</h2>

This is a web application called food delivery system for MakanMakan company. This application developed using Django framework and SQLite. The main purpose of this application is to allow customer browse menu, place order and deliver the food to their doorstep. When designing a food delivery system, there are several key design choices that we consider. 
* User interface and experience - We designed interfaces that are user-friendly which makes it clear and easy for customers to browse menu. It has a search bar where user can insert keyword and the results will appear. This function save so much time compared to scroll the menu until the last page.
* Restaurant management - We create a dashboard where restaurant are able to view incoming orders and status of current order where it has been delivered or not. This dashboard allow restaurant to keep track of their orders and minimize risk of making mistakes due to many orders made at the same time.
* Payment and pricing - There will be 2 types of payment which are online and cash on delivery. We have implemented a safe payment gateway which user can just click pay and it will redirect to the payment. On the other hand,if they prefer to pay by cash they can opt to cash on delivery method. Options are given to customers so they can choose which payment method suits them.

<h2>Assumptions</h2>

Assumptions in system development refer to the beliefs or expectations made by project stakeholders regarding various aspects of the system being developed. These assumptions are based on limited information, incomplete understanding, or simplifications made to facilitate the development process. 
1. The system is made customized for MakanMakan restaurant only, no other restaurant participating on the same web application.
2. The system are open to public and has only one user: Admin. Customers do not need to sign up, only fill in form to order.
3. The system assumes that all customers understood the flow of placing online order.

<h2>Limitations</h2>

Limitations in system development refer to the constraints or restrictions that can impact the design, development, implementation, or operation of a system. 
1. Customers cannot track their order as there is no status of order other than it is succesfully delivered.
2. Customers need to fill in their details each time they want to place an order as the system do not store customer details.
3. Only one online payment gateway available.
4. The application has not been tested with many incoming orders at the same time, so it is not recommended for large-scale business.
5. Technical limitations such network bandwith and storage can impact the application performance.


<h2>System Interface</h2>

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
