<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Models in Django	

In Django, a model is a Python class that represents a database table and its associated fields. Models define the structure of a database and provide an API for accessing the data stored within it. When you define a model in Django, you can specify the fields that it contains, as well as any relationships it has with other models.

To create models that represent your data in Django, you define Python classes that inherit from the django.db.models.Model class. Each attribute of the class represents a field in the database table, and you can specify the data type and other attributes of the field using the various field classes provided by Django.

Here's an example of a simple model in Django:

```python
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
```

In this example, we define a model called `BlogPost` with three fields: `title`, `content`, and `pub_date`. The `title` field is a `CharField` that can hold up to 200 characters, the `content` field is a `TextField` that can hold an arbitrary amount of text, and the `pub_date` field is a `DateTimeField` that will automatically be set to the current date and time when a new `BlogPost` object is created.

Models can also have relationships with other models. For example, you could define a `Comment` model that has a foreign key relationship with the `BlogPost` model:

```python
class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
```

In this example, we define a `Comment` model with three fields: `blog_post`, which is a foreign key to a `BlogPost` object, `author`, which is a `CharField` that can hold up to 100 characters, and `content`, which is a `TextField` that can hold an arbitrary amount of text.

Models in Django provide a powerful and flexible way to define the structure of a database and interact with the data stored within it. They also provide an abstraction layer that allows you to work with data in a way that is independent of the underlying database engine.

## Database
Django is a high-level Python web framework that supports various relational database management systems (RDBMS) as its back-end database. Here are some of the most popular databases that are suitable for use with Django:

| Database | Description |
| --- | --- |
| PostgreSQL | An open-source object-relational database system that provides powerful features such as transactional integrity, concurrency control, and extensibility. It is known for its scalability, reliability, and performance, and is a popular choice for large-scale applications. |
| MySQL | Another open-source RDBMS that is widely used and supported. MySQL is known for its ease of use, flexibility, and reliability, and is suitable for a wide range of applications, from small-scale to enterprise-level. |
| SQLite | A lightweight, serverless database engine that stores data in a single file. SQLite is a popular choice for small-scale applications and development environments due to its simplicity and ease of use. |
| Oracle | A commercial RDBMS that is widely used in enterprise-level applications. Oracle provides a robust and scalable platform for managing large amounts of data and supporting complex business logic. |
| Microsoft SQL Server | Another commercial RDBMS that is widely used in enterprise-level applications. SQL Server provides a robust and scalable platform for managing large amounts of data and supporting complex business logic, and integrates well with other Microsoft technologies. |

When selecting a database for your Django project, it is important to consider factors such as performance, scalability, ease of use, and support. You should also consider any specific requirements of your application, such as data volume and transactional requirements, to ensure that the selected database can meet your needs.

## MongoDB
It is possible to use MongoDB with Django using a third-party package called "Django MongoDB Engine". This package provides a MongoDB-based database backend for Django, allowing you to use MongoDB as the primary data store for your Django application.

However, it is important to note that Django was originally designed to work with relational databases and its ORM (Object-Relational Mapping) is optimized for this type of database. MongoDB is a document-oriented NoSQL database, which means that its data model is different from that of a traditional relational database.

While it is possible to use MongoDB with Django, it may require more configuration and customization than using a relational database. Additionally, some of the features that come with Django's ORM may not be fully supported when using MongoDB, such as complex query generation and transactions.

If you have experience with MongoDB and prefer its data model over that of a traditional relational database, and if the features and performance of Django MongoDB Engine meet your requirements, then using MongoDB with Django can be a suitable option. However, if you are new to both Django and MongoDB, it may be easier to start with a traditional relational database that is natively supported by Django.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

