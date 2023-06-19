<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# URL routing in Django

In Django, URL routing is the process of matching incoming HTTP requests with the appropriate view function to handle them. Here is a brief overview of how URL routing works in Django:

1. Create a new Django app or use an existing one. An app is a self-contained module that encapsulates related functionality, such as a blog, a forum, or a shopping cart.

2. Define a set of URL patterns for the app in the app's `urls.py` file. A URL pattern is a regular expression that matches a specific URL pattern and maps it to a corresponding view function. Here is an example of a URL pattern for a blog app:

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.index, name='index'),
       path('post/<int:pk>/', views.post_detail, name='post_detail'),
       path('category/<slug:slug>/', views.category_detail, name='category_detail'),
   ]
   ```

   In this example, we define three URL patterns using the `path` function from Django's `urls` module. The first pattern matches the root URL (i.e., the empty string) and maps it to the `index` view function. The second pattern matches URLs of the form `/post/<id>/`, where `<id>` is an integer, and maps them to the `post_detail` view function, passing the integer as a keyword argument called `pk`. The third pattern matches URLs of the form `/category/<slug>/`, where `<slug>` is a string consisting of letters, digits, hyphens, and underscores, and maps them to the `category_detail` view function, passing the string as a keyword argument called `slug`.

3. Define the view functions for the URL patterns in the app's `views.py` file. A view function is a Python function that takes a request object as input and returns an HTTP response object. Here is an example of a view function for the blog app:

   ```python
   from django.shortcuts import render, get_object_or_404
   from .models import Post, Category
   
   def index(request):
       posts = Post.objects.all()
       return render(request, 'blog/index.html', {'posts': posts})
   
   def post_detail(request, pk):
       post = get_object_or_404(Post, pk=pk)
       return render(request, 'blog/post_detail.html', {'post': post})
   
   def category_detail(request, slug):
       category = get_object_or_404(Category, slug=slug)
       posts = Post.objects.filter(category=category)
       return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})
   ```

   In this example, we define three view functions that correspond to the three URL patterns defined earlier. The `index` view function retrieves all the blog posts from the database using the `Post.objects.all()` method, and passes them as a context variable called `posts` to the `index.html` template. The `post_detail` view function retrieves a specific blog post from the database using the `get_object_or_404` function, which raises a 404 error if the post is not found, and passes it as a context variable called `post` to the `post_detail.html` template. The `category_detail` view function retrieves a specific category from the database using the `get_object_or_404` function, retrieves all the blog posts in that category using the `Post.objects.filter()` method, and passes them as context variables called `category` and `posts` to the `category_detail.html` template.

4. Create the HTML templates for the views in the app's `templates` directory. A template is a text file that contains HTML markup and optional placeholders for dynamic content, called template tags and filters. Here is an example of a template for the `index` view function:

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   <h1>Latest Posts</h1>
   {% for post in posts %}
   <div class="post">
       <h2><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h2>
       <p>{{ post.summary }}</p>
       <p class="meta">{{ post.pub_date|date:"F j, Y" }} | Category: {{ post.category }}</p>
   </div>
   {% endfor %}
   {% endblock %}
   ```

   In this example, we define a template that extends a base template called `base.html` (which contains the common layout for all pages in the app), and overrides a content block called `content` with a list of blog posts. The `{% for %}` template tag loops over the `posts` context variable passed by the `index` view function and generates a list of post titles, summaries, and publication dates using template tags and filters, such as `{% url %}` and `{{ post.pub_date|date:"F j, Y" }}`.

5. Test the app by running the Django development server and visiting the URLs defined in the URL patterns. The development server is started by running the `python manage.py runserver` command from the app's root directory. The server listens on port 8000 by default, and serves the app's pages dynamically by routing incoming requests to the appropriate view functions and rendering them using the corresponding templates.

That's a brief overview of how to create views that handle requests and generate HTML using templates in Django, and how to route URLs to the appropriate views. The Django framework provides many other features and tools for building web applications, such as authentication, forms, middleware, and static files handling, which can be customized and extended to suit your needs.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

