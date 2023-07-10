<h1 align ='center'>Event Management System</h1>

## Table Content
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Design Choices](#design-choices)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [System Interface](#system-interface)
- [Conclusion](#conclusion)
- [Quick Start](#quick-start)

## Introduction
An Event Management System is a software solution created to make the process of planning, organizing, and carrying out events easier and more efficient. It offers event organizers various tools and functions to effectively handle tasks like attendee registration, event categorization and event wish list. The purpose of this system is to increase productivity enhance coordination and guarantee a seamless and successful event for the organizers and the participants.

Within this comprehensive report lies an elaborate analysis of our Django-based Event Management System. A wide range of topics will be covered including project structure, design choices, assumptions made during development process along with associated limitations, system interfaces and conclusions drawn from findings. Detailed explanations related to project structure and system components are discussed upfront. To establish a user-friendly as well as scalable experience, we delve into design choices such as implementing architectural patterns & following best practices. Providing clarity regarding capabilities on offer & areas that may benefit from future improvements, assumptions and limitations associated with this system are addressed. A special focus has been given to discussing its intuitive design and functionality within the system interface. The conclusion presents a summary - an evaluation of areas where the system performs well along with areas which may need further enhancements. Lastly, for convenience purposes, a quick start guide is also accompanied here in order to facilitate easy understanding of this system for event organizers. Through studying this report meticulously, event organizers will be equipped with thorough knowledge essential for making informed decisions while considering implementation of our Event Management System which offers remarkable solutions for streamlining their respective event management processes.

## Project Structure
```
django-event-management
├───.idea
│   ├───inspectionProfiles       
│   └───libraries
├───events
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───event_management
│   └───__pycache__
├───static
│   ├───css
│   ├───fonts
│   ├───img
│   ├───js
│   │   └───pages
│   └───plugins
│       ├───bootstrap
│       │   └───js
│       ├───chart.js
│       ├───fontawesome-free
│       │   ├───css
│       │   └───webfonts
│       ├───jquery
│       ├───jquery-mapael
│       │   └───maps
│       ├───jquery-mousewheel
│       ├───overlayScrollbars
│       │   ├───css
│       │   └───js
│       └───raphael
│           └───dev
│               └───test
│                   ├───svg
│                   └───vml
└───templates
    ├───base
    └───events
```
## Design Choices

This event management system is a versatile platform that enables users to browse, create, and join various events, such as concerts, workshops, seminars, and parties. The application is built on the robust Django framework and has a flexible and scalable design.

The main data models used in this application are Event, Ticket, Booking, and Review. Event and Ticket are used to store the details of the events and the tickets available for them, while Booking and Review are used to handle the reservation process and the feedback mechanism.

The application’s interface is designed to be engaging and interactive, appealing to users’ preferences. The UI is developed using HTML templates, CSS, Bootstrap, and jQuery and has a dynamic design that allows for easy filtering and sorting of the events.

## Assumptions
## Limitations
## System Interface
1. Dashboard

Admin can view the event category, number of user registrations and complete event on the dashboard. All the functions such as create, edit, delete can be accessed on the dashboard. 
 <img width="920" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/StaticIP/event/photo/1-dashboard.png">
 
2. Event Category

Admin can create new event category such as carnival by entering all the details shown in the figure below.
 <img width="920" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/StaticIP/event/photo/2-Create%20event%20category.png">
 
After successfully added a new event category, admin can view the event category list.
 <img width="920" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/StaticIP/event/photo/3-Event%20category.png">
 
3. Create new event

Admin can create new event under any event category. 
 <img width="920" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/StaticIP/event/photo/4-create%20event.png">
 
 <img width="920" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/StaticIP/event/photo/5-create%20event.png">
 
 <img width="920" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/StaticIP/event/photo/6-create%20event.png">
 
4. Event member

Another function is where the admin can add new event member for different event and the system will display the member list. 
 <img width="920" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/StaticIP/event/photo/8-add%20event%20member.png">
 
 <img width="920" alt="image" src="https://github.com/drshahizan/learn-django/blob/main/materials/assignment/submission/StaticIP/event/photo/9-join%20event%20list.png">
 
## Conclusion
## Quick Start
