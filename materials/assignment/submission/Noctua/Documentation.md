<h1 align="center">Django Job Portal</h1>
      
## Table of Content
- [Project Structure](#project-structure)
- [Design Choices](#design-choices)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [Steps](#steps)
   - [Employer](#employer)
   - [Admin](#admin)
   - [Applicants](#applicants)

## Project Structure

```bash
< PROJECT ROOT >
   |
   |-- account/                              
   |    |-- admin.py                   
   |    |-- apps.py                        
   |    |-- forms.py                       
   |	|-- managers.py
   |    |-- models.py
   |    |-- urls.py
   |    |-- views.py
   |	
   |-- job/
   |    |-- asgi.py
   |    |-- settings.py
   |    |-- urls.py
   |    |-- wsgi.py
   |
   |-- jobapp/
   |    |-- admin.py                   
   |    |-- apps.py                        
   |    |-- forms.py                       
   |	|-- managers.py
   |    |-- models.py
   |    |-- urls.py
   |    |-- views.py             
   |    |
   |-- static/
   |    |-- <bs4, css, JS, images>         
   |    |
   |-- templates/                     
   |         |-- account/                 
   |         |    |-- employee-edit-profile.html      
   |         |    |-- employee-registration.html     
   |         |    |-- employer-registration.html     
   |         |    |-- login.html               
   |         |
   |         |-- jobapp/                   
   |         |    |-- all-applicants.html  
   |         |    |-- applicant-details.html             
   |         |    |-- dashboard.html    
   |         |    |-- employee-edit-profile.html
   |         |    |-- index.html
   |         |    |-- job-edit.html
   |         |    |-- job-list.html   
   |         |    |-- job-single.html
   |         |    |-- paginator.html
   |         |    |-- post-job.html
   |         |    |-- result.html
   |         |    |-- search.html     
   |         |
   |         |-- base.html                
   |         |-- footer.html            
   |         |-- head.html         
   |         |-- header.html
   |         |-- messages.html
   |         |-- scripts.html
   |
   |-- requirements.txt                     
   |                               
   |-- manage.py                            
   |
   |-- ************************************************************************
```
## Design Choices
The system is a job portal that allows employees to search for available jobs, apply for said jobs, while employers on the other hand, posts an opening.
The job portal system provides a platform for employees to efficiently search and apply for available job openings, while employers can conveniently post their job vacancies. The system facilitates efficient job search and application processes for employees while providing employers with a streamlined approach to managing job postings and applications.

The system encompasses essential data models such as Category, Job, Applicant, and BookmarkJob, enabling seamless Create, Read, Update, and Delete (CRUD) operations. It leverages a variety of tools and technologies, including Python as the primary programming language, Django as the robust web framework, HTML for creating the fundamental structure of the system, and CSS for visually enhancing its appearance.

## Assumptions
<ul>
   <li>The system assumes there are only three types of employement status which are full-time, part-time, and internship.</li>
   <li>It assumes that there will only be two types of users which are employer, employee and admin.</li>
   <li>Employer will add job vacancies, admin approve the job to be displayed, and employee can view and apply for the job.</li>
</ul>

## Limitations
<ul>
   <li>The system may not be suitable to support large number of users as it could have limitations in terms of scalability.</li>
   <li>It may not fulfill specific requirements of every company as some might have different approach in hiring employees.</li>
   <li>The system may not have the flexibility in terms of customization in order to completely adapt to a specific needs of a particular company.</li>
</ul>

## Steps
### Employer
Employer can add job vacancies. Each job vacancy added must be publish by admin before employee can view and or applicants apply the job.

1. Employer must firstly sign up and sign in as employer. Below is the landing page for employer after signing in.

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-dashboard-2020-05-08-17_01_07.png)

2. Employer can post a job by filling in job and company details.

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-job-create-2020-05-08-17_00_46.png)

3. Employer can view all jobs that they posted in Dashboard.

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-dashboard-2020-05-08-17_01_07.png)

4. Employer view applicants. 

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-dashboard-employer-job-54-applicants-2020-05-08-17_01_34.png)

### Admin
Admin will publish job listed by employer so that applicants can view and apply. 

1. Admin sign up at the command prompt by running the code below.
``` ruby
python manage.py createsuperuser
```

2. Details needed in cmd to create an admin are email and password.

3. Admin login and access django admin page.

![Settings Window](https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Noctua/image/adminjobs.png)

4. Admin publish job.

![Settings Window](https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/Noctua/image/adminjobs.png)

### Applicants
Employee/applicants can see the list of jobs offer and apply.

1. Job published can be view by both employee and employer.

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-jobs-2020-05-08-17_40_01.png)

2. Employee can see the job description and apply from here.

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-job-79-2020-05-08-16_59_55.png)


<div align="center">
    <h3>========Thank You=========</h3>
</div>

