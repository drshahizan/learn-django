<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# CRUD (Create, Read, Update, Delete)
In Django, CRUD (Create, Read, Update, Delete) operations are performed using functions that are defined in views.py. These functions correspond to HTTP methods: GET, POST, PUT, and DELETE.

<p align="center">
<img src="../images/10-crud.png" width="300" />
</p>

### 1. Create
To create a new record in the database, a view function is created that handles the HTTP POST method. The function creates a new instance of the model and saves it to the database.

```python
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})
```

> In this example, the function `create_book` handles the creation of a new book. It checks whether the HTTP method is POST and validates the form. If the form is valid, it saves the data to the database and redirects the user to the book list page.

### 2. Read
To retrieve data from the database, a view function is created that handles the HTTP GET method. The function queries the database using the model and returns the data to the user in a format that is specified in the view.

```python
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
```

> In this example, the function `book_list` retrieves all books from the database using the all() method of the Book model. It passes the retrieved data to the book_list.html template to be rendered.

### 3. Update
To update an existing record in the database, a view function is created that handles the HTTP PUT method. The function retrieves the record from the database, updates the fields, and saves the changes back to the database.

```python
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'update_book.html', {'form': form})
```

> In this example, the function `update_book` retrieves the book with the specified primary key from the database and populates the form with the book data. If the form is valid, it updates the book data in the database and redirects the user to the book list page.

### 4. Delete
To delete a record from the database, a view function is created that handles the HTTP DELETE method. The function retrieves the record from the database and deletes it.

```python
from django.shortcuts import render, redirect
from .models import Book

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')
```

> In this example, the function `delete_book` retrieves the book with the specified primary key from the database and deletes it. It then redirects the user to the book list page.

In Django, these CRUD operations can be performed using built-in functions and classes such as CreateView, DetailView, UpdateView, and DeleteView. These classes provide pre-defined templates and methods to simplify the implementation of CRUD functionality.

Overall, CRUD operations are essential in any web application, and Django provides a straightforward way to implement them using functions and classes. This makes it easier for developers to build complex web applications that allow users to perform CRUD operations on data in the database.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

