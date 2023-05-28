<h1>E-commerce platform</h1>

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

The application is a simple e-commerce website that allows users to browse products, add them to a cart, and checkout by creating an order. The design of the application is straightforward and built on top of the Django framework.

The main data models used in the application are Category, Product, Order, and OrderItem. Category and Product are used to organize the products in the database, while Order and OrderItem are used to manage the checkout process.

The application is designed to be easy to use and navigate, with a simple, responsive interface that allows users to quickly find what they are looking for. The UI is built with HTML templates, CSS, and JavaScript.

<h2>Assumptions</h2>

- The system assumes that all products are priced the same regardless of quantity or any other factors, as there is no option to set different prices for different quantities or offer discounts or promotions.
- The system assumes there is only one seller in the system. 
- The system assumes that all products are available for purchase at all times, and there is no option to indicate if a product is out of stock or temporarily unavailable.

<h2>Limitations</h2>

- The implementation may not be optimized for large-scale applications, as it has not been tested with very large datasets.
- The implementation may have security vulnerabilities, such as SQL injection attacks, if not used and configured properly.
- The implementation assumes that the database schema is already created and will not handle schema changes automatically. Manual intervention may be required to handle schema changes.
- The implementation may have performance issues if the database is not properly indexed.
- The implementation does not integrate with payment gateway.

<h2>System Interface</h2>
<h4>Public Access</h4>
  
1. Home Page

When users access the website, they will be directed to the home page to view the products. However, to make a purchase, they must log in first.   
  <img width="947" alt="image" src="https://user-images.githubusercontent.com/120556342/236977320-a2140acc-7515-4e6a-baca-54fa74d4fc81.png">

2. Search a Product
  
To find a specific product, users can simply type in their desired item in the search bar. 
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236977386-f8b6ac2e-e909-417c-905b-44701b796e1b.png">

3. User Registration

New users can register on the site by simply clicking the register link.  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236977434-442209bf-dcfe-4216-9ce9-0109f1262922.png">

4. Sign In

Once registered, the user will be prompted to proceed to the login page. 
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236977483-8bd44d87-0745-41e7-94eb-2aaf57ee8d1a.png">
 
<h4>Customers</h4>
  
1. Product

Customers who have signed in can easily find and view the products they desire.
  - Read
  
  <img width="945" alt="image" src="https://user-images.githubusercontent.com/120556342/236979630-5139d7af-1def-4662-937d-ebd4a22f6674.png">

  - Search
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236979689-b3b6e767-5d29-4916-b384-94be1e183b09.png">
  
2. Add Products in Cart

To make a purchase, the customer can add the desired item to their cart. If they need to make any changes, they have the option to remove or update items in the cart.
  - Create
  
  <img width="947" alt="image" src="https://user-images.githubusercontent.com/120556342/236979824-840bf3ed-c8aa-4032-a119-ef900ca23e27.png">

  - Read/Update/Delete
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236979869-279d4f59-9654-4689-b989-7df91a9414d9.png">

3. Order

To complete the order, customers need to provide their shipping and billing details.
  - Create
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236979957-134e72b6-6388-41b2-9423-a97235ecc709.png">

  - Read
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236980163-cacf530a-70ed-472d-9a1f-fcdfdbc6443e.png">
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236980217-4f8aa29c-ee19-4ea9-814d-38737470e21f.png">

<h4>Admin</h4>

1. Dashboard

When logging in as an administrator, the interface will appear differently. The dashboard will display the overall products, categories, orders, and total sales for the admin to view.
  <img width="946" alt="image" src="https://user-images.githubusercontent.com/120556342/236977845-15533c81-62e1-49b8-9b85-8996e346464d.png">

2. Category

The administrator can create, modify, remove, view, and search product categories that have been made.
  - Create
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236977962-0bbe1558-90b5-4772-a0e8-2d640ea25f81.png">
  
  - Read
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236977910-abd43419-baf5-4b12-907c-bfa4aa69e1f0.png">

  - Update
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236978002-1204ed33-0bb2-4c39-9f36-fb33ba2ae57d.png">
  
  - Delete
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236978039-f7e7ae06-2beb-4b00-a5f6-77574a23e491.png">

  - Search
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236978165-2233ca93-f2c0-434c-b831-f0c1c242d523.png">

2. Products

The administrator can perform various tasks such as creating, viewing, updating, deleting, and searching for new or previously listed products to sell in the store.
  - Create
  
  <img width="943" alt="image" src="https://user-images.githubusercontent.com/120556342/236984525-266c3c1d-cf27-4916-994a-0ee1a4fcaec6.png">


  - View
  
  <img width="947" alt="image" src="https://user-images.githubusercontent.com/120556342/236978395-f8c9910d-5b46-4618-8aaf-0d865cf6a389.png">
  <img width="945" alt="image" src="https://user-images.githubusercontent.com/120556342/236978489-889ee112-e1c2-4b22-add6-42c80708a37b.png">

  - Update 
  
  <img width="948" alt="image" src="https://user-images.githubusercontent.com/120556342/236978554-55faa3f2-07fe-478d-acdd-7ac011eca29e.png">

  - Delete
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236978590-dda2b3fc-66c7-45d0-9ffb-1c7197e0812e.png">

  - Search
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236978815-65239cfc-47f7-43fe-a213-95aaa6c19f77.png">

3. Orders

The Orders section will show all created orders. The administrators have the ability to view and modify the status of the order, indicating whether it has been shipped or delivered.
  - Read
  <img width="947" alt="image" src="https://user-images.githubusercontent.com/120556342/236978877-9434f1bd-4b76-420f-859f-60b8f6d454fa.png">

  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236979112-dc0f7710-a831-4378-9c1f-a9bacc325ecd.png">
  
  - Update
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236979263-630a7b7a-0d22-48b6-bd99-2d1f691cf8a8.png">

  - Search
  
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/120556342/236979321-7ac6f9ca-9266-4b09-bcd8-a0b26c990e7e.png">

<h2>Quick Start</h2>

[How to Run the Project](https://github.com/drshahizan/learn-django/edit/main/materials/assignment/submission/Regex/shop/README.md)
