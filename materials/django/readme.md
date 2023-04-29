<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![](https://visitor-badge.glitch.me/badge?page_id=drshahizan/learn-django)

Don't forget to hit the :star: if you like this repo.
# Django concept

Django is a web framework for building web applications in Python. It follows the Model-View-Controller (MVC) architectural pattern, where the Model represents the application's data and logic, the View is responsible for rendering the user interface, and the Controller handles user input and coordinates communication between the Model and View. 

## Django Project

In a Django project, the application logic is organized into individual apps. Each app typically consists of four main components: Models, Views, Templates, and URLs. Here's a brief overview of these components in the context of an example Django project called "App1":

<img src="./images/1-django-project.png" width="400" />

### 1. Models
Models define the data structure and relationships between database tables. In App1, the models might include classes such as "User" or "Post", which represent users and posts in the application. Models are defined in a file called "models.py" in the app directory.

### 2. Views
Views handle user requests and return HTTP responses. In App1, the views might include functions such as "list_posts" or "create_post", which display a list of posts or create a new post, respectively. Views are defined in a file called "views.py" in the app directory.

### 3. Templates
Templates define the HTML structure and layout of the application's user interface. In App1, the templates might include files such as "list_posts.html" or "create_post.html", which define the layout of the pages for listing posts or creating a new post, respectively. Templates are typically stored in a directory called "templates" within the app directory.

### 4. URLs
URLs map user requests to specific views. In App1, the URLs might include patterns such as "/posts/" or "/posts/create/", which map to the "list_posts" and "create_post" views, respectively. URLs are defined in a file called "urls.py" in the app directory.

Overall, these components work together to define the functionality and user interface of the App1 web application. By organizing the application logic into separate apps, Django allows developers to build complex applications with a modular and maintainable codebase.

## Key features
Django is a high-level, open-source web framework for Python that follows the Model-View-Controller (MVC) architectural pattern. It is designed to make web development faster, easier, and more secure by providing developers with a set of tools and features to build complex web applications.

### 1. Object-Relational Mapping (ORM)
Django provides an ORM that allows developers to interact with the database using Python objects instead of SQL statements. This makes it easier to work with databases and reduces the risk of SQL injection attacks.

### 2. Admin Interface
Django provides a built-in admin interface that allows developers to manage the data in the application without writing any code. It includes features such as CRUD operations, search, filtering, and sorting.

### 3. URL Routing
Django provides a URL routing system that allows developers to map URLs to views. This makes it easier to create SEO-friendly URLs and handle complex URL patterns.

### 4. Templating Engine
Django provides a built-in templating engine that allows developers to create dynamic web pages by separating the presentation logic from the business logic.

### 5. Security
Django provides built-in security features such as cross-site scripting (XSS) protection, cross-site request forgery (CSRF) protection, and password hashing.

### 6. Scalability
Django is designed to be scalable and can handle high traffic websites. It provides caching and session management features to improve performance.

### 7. Third-party Libraries
Django has a large and active community of developers who have created a wide range of third-party libraries and packages that extend its functionality.

Overall, Django is a powerful and flexible web framework that can be used to build a wide range of web applications, from simple websites to complex enterprise applications. Its ease of use, security features, and scalability make it a popular choice for web developers.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

![](https://visitor-badge.glitch.me/badge?page_id=drshahizan)
