<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Static files
In Django, static files are used to serve files that do not change during the lifetime of a web application. Examples of static files include stylesheets, JavaScript files, and images. These files are served directly from the web server, without being processed by Django.

<p align="center">
<img src="../images/11-static.png" width="150" />
</p>

To serve static files in Django, you need to create a `static` directory in your application. Inside this directory, you can create subdirectories to organize your static files, such as `styles` for CSS files, `js` for JavaScript files, and `images` for image files.

Here is an example directory structure for static files in a Django project:

```
myproject/
|-- myproject/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- myapp/
|   |-- templates/
|   |-- static/
|       |-- styles/
|           |-- main.css
|           |-- profile.css
|       |-- js/
|           |-- script.js
|           |-- profile.js
|       |-- images/
|           |-- logo.png
|-- manage.py
```

To use static files in your templates, you need to add the `{% load static %}` template tag at the top of your template. You can then reference your static files using the `{% static %}` template tag, like this:

```html
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'styles/main.css' %}">
<script src="{% static 'js/script.js' %}"></script>
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

In addition to serving static files during development, you also need to configure your web server to serve static files in production. Django provides a `collectstatic` management command that collects all static files from your project and copies them to a single directory that can be served by your web server.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

