<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Setting up a Django Project
Setting up a Django project involves installing Python and Django, creating a virtual environment, creating a new Django project using the django-admin command, configuring the database in the settings.py file, and starting the development server using the python manage.py runserver command. Once the server is running, you can build your web application by creating new apps and adding views, templates, and models. It's a good practice to create a virtual environment for your Django projects to keep them isolated from your system-wide Python installation.

## Setting up a Django project on your computer

### 1. [Install Python](1-1-python.md)
Django is a Python web framework, so you'll need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/. 

### 2. [Install Django](1-2-django.md)
Once you have Python installed, you can install Django using pip, the Python package manager. Open a terminal or command prompt and run the following command:

   ```python
   pip install django
   ```

   This will install the latest version of Django.

### 3. [Create a virtual environment](1-3-ve.md)
It's a good practice to create a virtual environment for your Django projects. A virtual environment is a self-contained environment that allows you to install packages without affecting your system-wide Python installation. To create a virtual environment, run the following command in your terminal:

   ```python
   python -m venv myenv
   ```

   Replace "myenv" with the name you want to give to your virtual environment.

### 4. Activate the virtual environment: 
Once you've created the virtual environment, you need to activate it. To activate the virtual environment on Windows, run the following command:

   ```python
   myenv\Scripts\activate
   ```

   On macOS or Linux, run the following command:

   ```
   source myenv/bin/activate
   ```

### 5. Create a new Django project
With the virtual environment activated, you can create a new Django project using the following command:

   ```python
   django-admin startproject myproject
   ```

   Replace "myproject" with the name you want to give to your project.

### 6. Configure the database
By default, Django uses SQLite as its database backend. If you want to use a different database, you need to modify the settings.py file in your project folder. Look for the DATABASES setting and update it with your database details.

### 7. Run the development server
With the database configured, you can start the development server using the following command:

   ```python
   python manage.py runserver
   ```

   This will start the server on http://127.0.0.1:8000/. You can open this URL in your web browser to see the default Django welcome page.

That's it! You've now set up a Django project on your computer. You can start building your web application by creating new apps and adding views, templates, and models.

## Django in Visual Studio Code
To use Django in Visual Studio Code, you need to follow these steps:

1. Install Python: Before you can use Django, you need to install Python on your machine. You can download and install Python from the official website.

2. Create a virtual environment: It is recommended to create a virtual environment for your Django project. A virtual environment is a way to isolate your project’s dependencies from other projects on your machine. To create a virtual environment, open the terminal in Visual Studio Code and run the following command:

   ```
   python -m venv env
   ```

   This command will create a new virtual environment named `env` in your project directory.

3. Activate the virtual environment: To activate the virtual environment, run the following command in the terminal:

   - On Windows: `.\env\Scripts\activate`
   - On macOS or Linux: `source env/bin/activate`

   Once activated, you should see the name of the virtual environment in the terminal prompt.

4. Install Django: To install Django, run the following command in the terminal:

   ```
   pip install django
   ```

5. Create a Django project: To create a new Django project, run the following command in the terminal:

   ```
   django-admin startproject project_name
   ```

   This will create a new Django project in a directory named `project_name`.

6. Run the development server: To run the development server, navigate to the project directory and run the following command in the terminal:

   ```
   python manage.py runserver
   ```

   This will start the development server on `http://localhost:8000`.

7. Create an app: To create a new app in your Django project, run the following command in the terminal:

   ```
   python manage.py startapp app_name
   ```

   This will create a new app in a directory named `app_name`.

8. Configure the database: Django uses a database to store data. You need to configure the database settings in the `settings.py` file.

9. Create models: Models are Python classes that represent the data in the database. You can create models in the `models.py` file in your app directory.

10. Create views: Views are Python functions that handle requests and generate responses. You can create views in the `views.py` file in your app directory.

11. Create templates: Templates are HTML files that define the structure and layout of your web pages. You can create templates in a directory named `templates` in your app directory.

12. Connect URLs to views: You need to create URL patterns in the `urls.py` file in your app directory to connect URLs to views.

By following these steps, you can create a basic Django web application in Visual Studio Code.

## Django extension for Visual Studio Code

The Django extension for Visual Studio Code is a plugin that provides a set of useful tools and features for Django developers working with Visual Studio Code. The extension includes features like IntelliSense for Django templates, syntax highlighting for Django template tags, snippets for common Django code patterns, and support for running Django manage.py commands from within the editor. 

Other features of the Django extension include Django project creation, code navigation, and debugging support. The extension also supports various Django versions, including the latest version, and can be configured to work with different Python environments.

With the Django extension for Visual Studio Code, developers can write Django code more efficiently, debug their applications with ease, and improve their overall productivity.

To install the Django extension for Visual Studio Code, follow these steps:

1. Open Visual Studio Code and click on the Extensions icon in the sidebar.
2. Search for "Django" in the Extensions Marketplace and click on the Django extension by Microsoft.
3. Click on the Install button to install the extension.

Once the Django extension is installed, you can use it to develop Django applications in Visual Studio Code. Here are some of the features you can use:

1. IntelliSense for Django templates: The Django extension provides code completion and suggestions for Django template tags and filters.

2. Syntax highlighting for Django template tags: The extension highlights Django template tags and filters in different colors for better readability.

3. Snippets for common Django code patterns: The extension includes snippets for common Django code patterns, such as creating a new Django app or defining a view.

4. Django project creation: You can use the extension to create a new Django project with a single command.

5. Code navigation: The extension allows you to quickly navigate between views, models, and templates in your Django project.

6. Debugging support: The extension provides debugging support for Django applications, allowing you to set breakpoints, step through code, and inspect variables.

To use the Django extension, open a Django project in Visual Studio Code and start coding. You should see IntelliSense suggestions for Django tags and filters, as well as syntax highlighting for Django templates. You can also use the extension to create new Django apps, navigate between different parts of your project, and debug your code.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

