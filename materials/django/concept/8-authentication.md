<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Authentication and authorization
Authentication and authorization are essential components of web applications that deal with user accounts and access control. Django provides built-in support for authentication and authorization, making it easy to add user authentication and authorization to your web application.

<p align="center">
<img src="../images/12-authentication.png" width="400" />
</p>

### 1. Authentication
Authentication refers to the process of verifying the identity of a user who is trying to access a web application. In Django, authentication is handled by the `django.contrib.auth` module, which provides a set of views and forms for user authentication. The `User` model is also provided by this module, which represents a user account in your application.

### 2. Authorization
Authorization refers to the process of determining what actions a user is allowed to perform in a web application. In Django, authorization is handled by the built-in permissions system, which allows you to define permissions for different types of users in your application. You can define permissions for specific models and actions, such as creating, reading, updating, and deleting records.

To use authentication and authorization in your Django application, you need to add the `django.contrib.auth` and `django.contrib.contenttypes` apps to your `INSTALLED_APPS` setting in `settings.py`. You can then create views and templates for user authentication, and use the `@login_required` decorator to require authentication for certain views.

Here is an example of using the `@login_required` decorator to require authentication for a view:

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    # Render the profile template
    return render(request, 'profile.html')
```

In addition to authentication and authorization, Django also provides support for other security features, such as password hashing, cross-site request forgery (CSRF) protection, and HTTPS encryption.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

