<h1 align="center">Blogging Platform</h1>

## Table of Content
- [Project Prerequisites](#project-prerequisites)
- [Setting Up A Django Project](#setting-up-a-django-project)

<h2>Project Prerequisites</h2>

1. Install Python.
2. Install Visual Studio Code

<h2>Setting up a Django Project</h2>

1. **Create a folder to contain your Django Project files.** 

2. **Install Django.**
```bash
pip install django
```

3. **Create a virtual environment.**  In your current working directory, this command creates a new virtual environment called ``environment``. 
```bash
python -m venv environment
```

4. **Activate the virtual environment.** When the process is finished, you must additionally activate the virtual environment:
```bash
environment\Scripts\activate
```

5. **Create a new Django project.**
```bash
django-admin startproject blogproject
```

6. **Run the development server** through the ‘blogproject’ folder.
```bash
python manage.py runserver
```

You’ll see the following output on the command line:
```bash
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

May 26, 2023 - 15:50:53
Django version 4.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```



