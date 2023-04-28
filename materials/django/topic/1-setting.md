<a href="https://github.com/drshahizan/python-web/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/python-web" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/python-web/network/members"><img src="https://img.shields.io/github/forks/drshahizan/python-web" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/python-web/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/python-web" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/python-web/issues"><img src="https://img.shields.io/github/issues/drshahizan/python-web" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/python-web/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/python-web?color=2b9348"></a>
![](https://visitor-badge.glitch.me/badge?page_id=drshahizan/python-web)

Don't forget to hit the :star: if you like this repo.

# Setting up a Django Project

Step-by-step guide to setting up a Django project on your computer:

### 1. Install Python
Django is a Python web framework, so you'll need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/.

### 2. Install Django: 
Once you have Python installed, you can install Django using pip, the Python package manager. Open a terminal or command prompt and run the following command:

   ```python
   pip install django
   ```

   This will install the latest version of Django.

### 3. Create a virtual environment
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

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/python-web/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

![](https://visitor-badge.glitch.me/badge?page_id=drshahizan)
