<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Assignment

The goal of this assignment is to create a web application using the Django framework, which is a popular Python web framework that follows the Model-View-Controller (MVC) architecture. The web application should have the following features:

1. CRUD functionality: This refers to the ability to create, read, update, and delete records in the database. For example, if you were building a web application for a bookstore, you would need to create records for books, read records to display them on a page, update records when a book's details change, and delete records when a book is no longer available.

2. Searching: The web application should allow users to search for records in the database. For example, users could search for a book by title, author, or genre.

3. Dashboard for admin reporting: The web application should have a dashboard that allows administrators to view reports and statistics about the data in the database. For example, an administrator of a bookstore web application might want to see how many books have been sold in a certain period, which books are the most popular, or how many customers have made purchases.


## Project Requirements

1. Create a Django project from scratch or use an existing one.

2. Create at least one Django app to handle the CRUD functionality.

3. Use Python, Bootstrap, JavaScript, and CSS to style the application and provide a modern user interface.

4. Create a model for your data. This model should include fields for the data you want to store.

5. Create a view for each of the CRUD operations and searching.

6. Use templates to render the views and display the data.

7. Create forms to handle the input of data.

8. Implement validation to ensure that the data entered is correct.

9. Implement user authentication and authorization to ensure that only authorized users can perform CRUD operations and view the admin dashboard.

10. Create a dashboard for admin reporting that displays relevant statistics and data visualizations.

## Project Steps

1. Create a new Django project using the `django-admin startproject` command.

2. Create a new Django app using the `python manage.py startapp` command.

3. Define your model in the app's `models.py` file. You can use Django's built-in fields or create custom fields. 

4. Create a view to handle the creation of new data. In this view, create a form using Django's built-in forms or create custom forms.

5. Create a view to handle the retrieval of data. This view should display a list of all the data entries in the database.

6. Create a view to handle the updating of data. In this view, create a form to allow users to update an existing data entry.

7. Create a view to handle the deletion of data. This view should prompt the user to confirm the deletion before deleting the data.

8. Create a view to handle searching of data. This view should allow users to search for specific data entries based on specific criteria.

9. Create templates for each view using HTML, CSS, and Django's templating language. Use Bootstrap and custom CSS and JavaScript to style the templates and provide a modern user interface.

10. Implement validation for your forms to ensure that the data entered is correct. You can use Django's built-in validators or create custom validators.

11. Implement user authentication and authorization using Django's built-in authentication system or a third-party library like Django-Allauth.

12. Create a dashboard for admin reporting using Django's built-in admin site or a third-party library like [Django-Adminlte](https://github.com/app-generator/django-adminlte). This dashboard should display relevant statistics and data visualizations based on the data in the database.

## Codebase structure
A suggested Django codebase structure that includes folders for documentation and images:

```
project_name/
│
├── app_name/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│   
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│   
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── item_list.html
│   ├── item_detail.html
│   ├── item_form.html
│   ├── item_confirm_delete.html
│   └── dashboard.html
│   
├── media/
│   └── item_images/
│
├── documentation/
│   ├── requirements.txt
│   ├── deployment.md
│   └── usage.md
│   
├── project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│   
├── manage.py
└── README.md
```

Here's a brief explanation of each folder and file:

- `app_name`: This folder contains the Django app. It includes files such as `models.py`, `views.py`, and `urls.py`.
- `static`: This folder contains static files such as CSS, JavaScript, and images.
- `templates`: This folder contains the HTML templates for the web application.
- `media`: This folder contains uploaded media files such as images.
- `documentation`: This folder contains documentation for the project, such as requirements and deployment instructions.
- `project_name`: This folder contains the project settings, such as `settings.py` and `urls.py`.
- `manage.py`: This file is used to run various commands for the project, such as starting the development server.
- `README.md`: This file contains information about the project, such as how to set it up and use it.

> Note: You can add more folders and files as per your requirement. Also, this is just a suggested structure and you can modify it as per your needs.

## Submission Requirements

1. Submit the source code of your project along with any necessary configuration files. A fully functional Django web application that meets the above requirements.

2. A document that explains the project structure, the design choices made, and how to run the application.

3. Include a README file that provides instructions on how to run the project and any dependencies.

3. Provide screenshots or a video demo of your project in action, showcasing each of the CRUD operations, searching, and the admin dashboard.

4. Clearly document any assumptions or limitations in your implementation.

5. Source code of the application, committed to a GitHub repository.

## Conclusion

By completing this assignment, you will have gained a practical understanding of how to create a web application using Django that implements CRUD functionality, searching, and a dashboard for admin reporting. This will help you in developing more complex web applications in the future. Good luck!

## Others
- Collaborate effectively with your group members to complete the task.
- Ensure to send the report in **mark down** format and **source code**.
- Please submit the assignments in the [**submission**](./submission/) folder. It would be best if you create a folder using your group name.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

