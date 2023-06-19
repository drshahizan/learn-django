<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Views and Templates

In Django, views and templates are two core components of the Model-View-Template (MVT) architecture, which is similar to the Model-View-Controller (MVC) pattern used in other web frameworks.

## Views

Views are Python functions that handle HTTP requests and return HTTP responses. Views are responsible for fetching data from the database, processing it, and returning it to the user in a format suitable for rendering by the template. Views can perform various operations, such as querying the database, rendering HTML templates, and returning JSON or other data formats.

Here is an example of a simple view that returns a list of blog posts:

```python
from django.shortcuts import render
from myapp.models import BlogPost

def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
```

This view queries the `BlogPost` model to fetch a list of all posts, and then renders a template called `post_list.html`, passing the list of posts as a context variable.

## Templates

Templates are HTML files that define the structure and layout of your web pages. Templates can include variables, loops, conditionals, and other control structures that allow you to dynamically generate content based on data provided by the view. Templates can also include static files such as CSS, JavaScript, and images.

Here is an example of a simple template that displays a list of blog posts:

```html
{% extends "base.html" %}

{% block content %}
  <h1>Blog Posts</h1>
  <ul>
  {% for post in posts %}
    <li><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></li>
  {% endfor %}
  </ul>
{% endblock %}
```

This template extends a base template called `base.html`, and defines a block called `content` where the list of blog posts will be displayed. The template uses a for loop to iterate over the list of posts passed from the view, and generates a list item for each post, with a link to the post's detail page.

In summary, views and templates are two essential components of a Django web application. Views handle requests and return responses, while templates define the structure and layout of web pages. Together, views and templates provide a powerful and flexible way to generate dynamic content for your users.
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

