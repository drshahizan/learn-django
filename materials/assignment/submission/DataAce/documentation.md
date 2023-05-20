<h1>Food Delivery System</h1>

In today's fast-paced world, we understand the importance of convenience and saving time. That's why our Food Delivery System is designed to streamline the entire food ordering process, eliminating the hassle of long phone calls and waiting in lines. With just a few clicks or taps, customers can explore a wide selection of restaurants, browse through menus, customize their orders, and securely complete their transactions – all from the comfort of their own homes or while on the go. We believe that ordering food should be a seamless and enjoyable experience, and our application is tailored to meet those expectations. Whether it's a quick lunch, a family dinner, or a special occasion, our Food Delivery System is here to make every meal a hassle-free delight.

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
 
**2. Sign Up**

Sign Up is section is closed and admin can only add new admin through admin's site.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/sign-up.png">

**3. Login**
 
 Admin can access two different login pages.
 
 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Admin%20Login.png">
 
 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Sign%20In.png">

**4. Forget Password**

Admin can reset their password in the Forget Password page by providing their email address.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Forget%20Password.png">

**5. Admin Site**

Admin can see the recent changes that they have committed and also edit the sub-categories for each categories by pressing the Add and Change button.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Admin%20Site.png">
 
 **6. Change Password**
 
 Admin can change the password by providing the old password and the new password.
 
 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Change%20Password.png">
 
  **7. Email address**
  
Admin can see and edit the email address of user, the type of user of the email address including if the user is a primary user and if the user is a verified user. Admin can also add email address by completing the form. By selecting certain email address, admin can also delete it in the Action.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Email%20Page.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Email%20Form.png">
  
 **8. Groups**
  
Admin can see and edit the groups in the system and can also add groups by completing the form. By selecting certain groups, admin can also delete it in the Action.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Groups%20page.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Groups%20Form.png">
  
 **9. Users**
  
Admin can see and edit the usernames and the staff status. Admin can also add users by completing the form. By selecting certain users, admin can also delete it in the Action.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Users%20page.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/User%20Form.png">
  
   **10. Category**
  
Admin can see and add including edit the types of food categories in the system. By selecting certain categories, admin can also delete it in the Action.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Category%20Page.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Category%20Form.png">
  
  **11. Menu Items**
  
 Admin can see and add including edit the food menus in the system. By selecting certain categories, admin can also delete it in the Action.

 <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Menu%20Admin%20Page.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Menu%20Form.png">
  
  **12. Order Models**
  
  Admin can see and add including edit the customers' orders in the system. By selecting certain categories, admin can also delete it in the Action.
  
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Order%20Page.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Order%20Form.png">
  
  **13. Sites**
  
Admin can see and add including edit the sites in the system. By selecting certain categories, admin can also delete it in the Action. In addition, admin can also search for certain sites for easier access.

<img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Site%20Page.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Site%20Form.png">
  
  **14. Social Accounts**
  
  Admin can see and add including edit the social accounts in the system. By selecting certain categories, admin can also delete it in the Action.
  
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Social%20Acc%20Page.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Social%20Acc%20Form.png">
  
   **15. Social Application Tokens**
   
   Admin can see and add including edit the social application tokens in the system. By selecting certain categories, admin can also delete it in the Action.
   
   <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Social%20Token%20Page.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Social%20Token%20Form.png">
   
   **16. Social Applications**
   
   Admin can see and add including edit the social applications in the system. By selecting certain categories, admin can also delete it in the Action.
  
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Social%20App%20Page.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Social%20App%20Form.png">
  
  **17. Customer Information**
  
  Admin can see the customer information for certain orders and check if the order has been paid and shipped. If the order has not been marked shipped, the admin can click on the 'Mark as Shipped' button.
  
   <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Cust%20Info.png">
 
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Shipped.png">
  
  **18. Logout**
  
  Admin can logout and be redirected to the page below.
  
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Logout.png">
  
### Customer

**1. About Us**
  
  Customers can see the details about the system in About Us.
  
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/About%20Us.png">
  
  **2. Menu**
  
  Customers can see the photos, food names and also the description of the menus available in MakanMakan restaurant. In addition, customers can also search certain keywords to ease their findings.
  
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Menu%20Page.png">
  
   <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Search.png">
  
  **3. Order**
  
  Customers can check the menus that they want and fill in their information in the form. Customers need to confirm and place their order. Once confirmed, orders will be submitted and paid by using Paypal.
  
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Order%20Now%20page.png">
  
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Order%20Page%20Form.png">
  
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Order%20Submit.png">
  
  <img width="1020" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/DataAce/photos/Order%20Confirmation.png">
