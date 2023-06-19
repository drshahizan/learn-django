<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Django Object-Relational Mapping
Django ORM (Object-Relational Mapping) is a tool that provides a high-level, Pythonic interface for working with relational databases. The ORM allows developers to interact with the database using Python code instead of SQL statements. 

There are several methods available in the Django ORM for retrieving data from the database. Here are some of the commonly used methods:

### 1. `get()`
This method retrieves a single record from the database that matches the specified condition. For example, `MyModel.objects.get(id=1)` would retrieve the record from the `MyModel` table where the `id` column equals 1.

### 2. `all()`
This method retrieves all records from the specified table. For example, `MyModel.objects.all()` would retrieve all records from the `MyModel` table.

### 3. `filter()`
This method retrieves all records from the specified table that match the specified condition. For example, `MyModel.objects.filter(name='John')` would retrieve all records from the `MyModel` table where the `name` column equals 'John'.

Here is an example of how these methods can be used to retrieve data from a database:

```python
from myapp.models import MyModel

# Retrieve a single record from the database
record = MyModel.objects.get(id=1)

# Retrieve all records from the database
records = MyModel.objects.all()

# Retrieve all records from the database that match a specific condition
filtered_records = MyModel.objects.filter(name='John')
```

In addition to these methods, there are other methods available in the Django ORM for more complex queries, such as `exclude()`, `order_by()`, `annotate()`, and `aggregate()`. The Django ORM also supports raw SQL queries if needed.

Overall, the Django ORM provides a simple and convenient way to work with relational databases in Python, allowing developers to write database queries in a more Pythonic and readable way.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

