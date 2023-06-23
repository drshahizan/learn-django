<h1>Online Education Platform</h1>

## Table of Content
- [Project Structure](#project-structure)
- [Design Choices](#design-choices)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [System Interface](#system-interface)
    - [General](#general)
    - [Admin](#admin)
    - [Instructor](#instructor)
    - [Student](#student)

<h2>Project Structure</h2>

```
gadgeteen
├── courses
│   ├── admin.py
│   ├── apps.py
│   ├── fields.py
│   ├── fixtures
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── static
│   ├── templates
│   ├── templatetags
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── educa
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   └── images
├── requirements.txt
├── staticfiles
│   ├── admin
│   ├── assets
│   ├── css
│   ├── debug_toolbar
│   ├── fontawesomefree
│   └── redisboard
└── students
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── __init__.py
    ├── migrations
    ├── models.py
    ├── __pycache__
    ├── templates
    ├── tests.py
    ├── urls.py
    └── views.py
```

<h2>Design Choices</h2>

- Django Framework: The project is developed using the Django web framework due to its robustness, scalability, and built-in features for handling web applications. Django follows the Model-View-Controller (MVC) architectural pattern, which promotes code organization and separation of concerns.

- Database: The project utilizes a relational database management system (RDBMS) called SQLite which is Django's default database, to store and manage data.

- User Authentication: Django's built-in authentication system is used to handle user registration, login, and session management.

- User Roles and Permissions: The project implements role-based access control (RBAC) to differentiate between different types of users, such as students, instructors, and administrators.

<h2>Assumptions</h2>

- The project assumes there are three types of users: admin, instructor and student in the system.

- The project assumes that course content, including courses, modules, and resources, will be provided by instructors or administrators. Students can then access the course content.

- 

<h2>Limitations</h2>

- The online educational platform's scalability may be limited by the hardware resources and hosting environment.

- 

<h2>System Interface</h2>

<h3>General</h3>

1. Landing Page

The landing page shows a list of subjects and courses. User need to register or login to access the content.
![Screenshot from 2023-06-23 14-00-22](https://github.com/drshahizan/learn-django/assets/69034742/db61f8b8-ee65-42bf-9471-e9e0d5464131)

3. Student Sign up

![Screenshot from 2023-06-23 14-03-24](https://github.com/drshahizan/learn-django/assets/69034742/a3584ee9-9ee8-42c9-978c-fc42d755a901)

3. Login Page

![Screenshot from 2023-06-22 01-04-58](https://github.com/drshahizan/learn-django/assets/69034742/84dc0d5e-bd0f-4d71-82b6-dfac9dba53e7)

<h3>Admin</h3>

1. Manage User

![Screenshot from 2023-06-22 01-07-57](https://github.com/drshahizan/learn-django/assets/69034742/3471c696-7596-47aa-9ea4-255c99a55ee9)

2. Add User

![Screenshot from 2023-06-22 01-08-15](https://github.com/drshahizan/learn-django/assets/69034742/1f26597c-e81f-4c51-bf3a-3843293a026f)

3. Manage Course

![Screenshot from 2023-06-23 14-12-14](https://github.com/drshahizan/learn-django/assets/69034742/71f59334-a6c0-4e70-a372-8db46991a77e)

4. Add Course

![Screenshot from 2023-06-22 01-14-17](https://github.com/drshahizan/learn-django/assets/69034742/df038b4d-196a-4c05-82e1-2e0bf2abc2ec)

5. Course Summary

![Screenshot from 2023-06-22 01-25-15](https://github.com/drshahizan/learn-django/assets/69034742/3cf9c239-b5f1-4eb8-b140-9d28a589a945)

6. Manage Subject

![Screenshot from 2023-06-23 14-16-33](https://github.com/drshahizan/learn-django/assets/69034742/0a9b0817-ab89-43b4-94a3-ff218c8e1bf8)

8. Add Subject

![Screenshot from 2023-06-23 14-16-39](https://github.com/drshahizan/learn-django/assets/69034742/c827e68a-288b-4241-937e-44cf137ff4c5)

<h3>Instructor</h3>

1. Manage Course

![Screenshot from 2023-06-22 01-26-46](https://github.com/drshahizan/learn-django/assets/69034742/d7988d9d-d4e4-4395-92b1-e10e8381ffaf)

2. Edit Course

![Screenshot from 2023-06-22 01-33-54](https://github.com/drshahizan/learn-django/assets/69034742/4bd51f1d-5aaa-484f-b739-a63c489a3ec4)

3. Delete Course

![Screenshot from 2023-06-23 14-21-07](https://github.com/drshahizan/learn-django/assets/69034742/c527f38d-4b14-47a9-87a2-c13b36482c95)

4. Edit Course Module

![Screenshot from 2023-06-22 01-34-20](https://github.com/drshahizan/learn-django/assets/69034742/e6fae04b-c01d-4734-973e-e07c0722d7de)

5. Manage Content

Instructor can create several types of new content including text, image, video and file content. Then, instructor can edit or delete existing content.
![Screenshot from 2023-06-22 01-37-49](https://github.com/drshahizan/learn-django/assets/69034742/26501fdc-6e1b-4236-b6ba-cd9c90c3fd08)


<h3>Student</h3>

1. My Course

The system shows the list of courses that the student is enrolled. Student can view the content by clicking 'Access contents'.
![Screenshot from 2023-06-22 01-33-28](https://github.com/drshahizan/learn-django/assets/69034742/da0cc1c9-5cac-470f-98f3-5f63b966eb4c)

2. Access Course

After student click 'Access contents', the system display the module and its contents. Student can switch module by clicking on the link in the modules list.
![Screenshot from 2023-06-22 01-38-09](https://github.com/drshahizan/learn-django/assets/69034742/e394aee8-e147-4627-bead-8d38795eb3f4)



