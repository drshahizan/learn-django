<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![](https://visitor-badge.glitch.me/badge?page_id=drshahizan/learn-django)

Don't forget to hit the :star: if you like this repo.

# Models in Django	

In Django, a model is a Python class that represents a database table and its associated fields. Models define the structure of a database and provide an API for accessing the data stored within it. When you define a model in Django, you can specify the fields that it contains, as well as any relationships it has with other models.

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
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

![](https://visitor-badge.glitch.me/badge?page_id=drshahizan)
