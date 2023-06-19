<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# View function in Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is built on top of the Python programming language and follows the model-view-controller (MVC) architectural pattern.

In this particular example, the view function is called `profileView` and it takes a `request` object as its argument. The `request` object contains information about the current request, such as the user's browser, IP address, and any data they submitted in a form.

The first line of the view function imports the `render` function from the `django.shortcuts` module. The `render` function takes a request object, a template name, and a context dictionary as its arguments, and returns an HTTP response with the rendered template.

In the second line of the view function, the `getUser()` function is called to retrieve information about the current user. This function is not defined in the code snippet, but it is likely a custom function that retrieves user data from a database or other source.

Finally, the view function passes the `user` object to the `render` function as part of a context dictionary. This context dictionary allows variables to be passed from the view function to the template, where they can be displayed or manipulated as needed.

<p align="center">
<img src="../images/3-view.png" width="300" />
</p>

Overall, Django provides a powerful set of tools for building web applications, including a robust ORM (Object-Relational Mapping) system, a built-in admin interface, and a templating engine for creating dynamic HTML pages. The framework also emphasizes best practices such as DRY (Don't Repeat Yourself) coding and secure development practices.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

