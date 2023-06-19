<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Admin interface in Django
Django provides a built-in admin interface that allows you to manage your application's data in a convenient and efficient way. The admin interface is automatically generated based on the models defined in your Django application, and it provides a variety of features, such as data management, user authentication, and permissions.

To use the admin interface in Django, you need to follow these steps:

1. Create a superuser: Before you can use the admin interface, you need to create a superuser account. You can create a superuser by running the following command in your terminal:

   ```
   python manage.py createsuperuser
   ```

   This command will prompt you to enter a username, email, and password for the superuser account.

2. Register models: To enable the admin interface for a model, you need to register it with the admin site. You can do this by creating an `admin.py` file in your application and registering the model using the `admin.site.register()` method. For example:

   ```python
   from django.contrib import admin
   from .models import Post

   admin.site.register(Post)
   ```

3. Access the admin interface: You can access the admin interface by navigating to `http://localhost:8000/admin` in your web browser and logging in with your superuser account. Once you are logged in, you can see a list of registered models and perform various actions such as adding, editing, and deleting data.

4. Manage your data: From the main admin page, you can click on a model to view and manage its data. You can add, edit, and delete objects using the provided forms and buttons. You can also search and filter objects based on their attributes.

The admin interface provides a variety of customization options, such as changing the layout, adding custom views, and defining permissions for users. You can also customize the forms used for adding and editing data, and provide custom validation and processing logic.

Overall, the admin interface in Django provides a convenient and powerful way to manage your application's data, and it can save you a lot of time and effort in developing custom management views and forms.
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

