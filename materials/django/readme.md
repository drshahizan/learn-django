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

<img src="./images/2-app.png" width="400" />

Overall, these components work together to define the functionality and user interface of the App1 web application. By organizing the application logic into separate apps, Django allows developers to build complex applications with a modular and maintainable codebase.

## Example: Create website using Django.
Creating a website like Facebook.com using Django would be a complex and challenging task that would require a team of experienced developers and a significant amount of time and resources. However, here's a brief overview of the key steps involved in building some of Facebook.com's core features using Django:

### 1. Users:
- Pages: To allow users to create pages on the website, the developer would need to define a "Page" model in Django's ORM (Object-Relational Mapping) system. This model would store information about the page, such as its name, description, and category. The developer would also need to create views and templates to allow users to create, edit, and view pages on the site.
- Photos: To allow users to upload and view photos, the developer would need to create a "Photo" model in Django's ORM system. This model would store information about the photo, such as its title, caption, and image file. The developer would also need to create views and templates to allow users to upload and view photos on the site.
- Friends: To allow users to connect with each other and become friends on the site, the developer would need to create a "Friendship" model in Django's ORM system. This model would store information about the friendship, such as the two users involved and the date the friendship was formed. The developer would also need to create views and templates to allow users to send friend requests, accept friend requests, and view their list of friends.

### 2. Feed:
- Likes: To allow users to like posts and photos in their feed, the developer would need to create a "Like" model in Django's ORM system. This model would store information about the like, such as the user who liked the post, the post they liked, and the date the like was made. The developer would also need to create views and templates to allow users to like and unlike posts and photos.
- Comments: To allow users to comment on posts and photos in their feed, the developer would need to create a "Comment" model in Django's ORM system. This model would store information about the comment, such as the user who made the comment, the post or photo they commented on, and the text of the comment. The developer would also need to create views and templates to allow users to create and view comments on posts and photos.

### 3. Groups:
- Members: To allow users to create and join groups on the site, the developer would need to create a "Group" model in Django's ORM system. This model would store information about the group, such as its name, description, and category. The developer would also need to create views and templates to allow users to create, edit, and view groups on the site, as well as a "Membership" model to track which users are members of each group.
- Messages: To allow users to send messages to each other within groups, the developer would need to create a "Message" model in Django's ORM system. This model would store information about the message, such as the user who sent the message, the group the message was sent to, and the text of the message. The developer would also need to create views and templates to allow users to send and view messages within groups.

<img src="./images/3-fb.png" width="400" />

Overall, building a website like Facebook.com using Django would require a combination of technical skills, design expertise, and project management experience. It would also require a deep understanding of the site's core features and functionality, as well as the ability to adapt to changing user needs and trends.

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
