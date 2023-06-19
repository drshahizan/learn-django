<a href="https://github.com/drshahizan/learn-django/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/learn-django" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/network/members"><img src="https://img.shields.io/github/forks/drshahizan/learn-django" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/learn-django" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/issues"><img src="https://img.shields.io/github/issues/drshahizan/learn-django" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/learn-django/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/learn-django?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2Flearn-django&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Forms in Django

Forms in Django are a powerful tool for handling user input and validating data. They allow you to create HTML forms with ease, and handle form submissions in a secure and flexible way. In Django, forms are defined using Python classes that inherit from the `django.forms.Form` or `django.forms.ModelForm` class, and provide fields and validation rules as attributes.

Here are the basic steps for creating a form in Django:

1. Create a new Python module for the form, or add it to an existing module. The module should import the `django.forms` module and define a new form class that inherits from `django.forms.Form` or `django.forms.ModelForm`. For example:

   ```python
   from django import forms
   from myapp.models import MyModel
   
   class MyForm(forms.Form):
       name = forms.CharField(max_length=100)
       email = forms.EmailField()
       message = forms.CharField(widget=forms.Textarea)
   ```

   In this example, we define a new form class called `MyForm` that has three fields: `name`, `email`, and `message`. The `name` field is a `CharField` with a maximum length of 100 characters, the `email` field is an `EmailField` that validates the input as an email address, and the `message` field is a `CharField` that uses a `Textarea` widget to allow multi-line input.

2. Create a view function that handles the form submission and renders the response. The view function should import the form class and instantiate it with the request data, validate the input data, and process the form if it is valid. For example:

   ```python
   from django.shortcuts import render
   from myapp.forms import MyForm
   
   def my_view(request):
       if request.method == 'POST':
           form = MyForm(request.POST)
           if form.is_valid():
               # Process the form data
               name = form.cleaned_data['name']
               email = form.cleaned_data['email']
               message = form.cleaned_data['message']
               # ...
               return render(request, 'success.html')
       else:
           form = MyForm()
       return render(request, 'my_template.html', {'form': form})
   ```

   In this example, we define a new view function called `my_view` that handles both GET and POST requests. When the form is submitted via POST, the view function instantiates the form with the request data and validates it using the `is_valid()` method. If the form is valid, the view function extracts the cleaned data from the form using the `cleaned_data` attribute, processes it, and renders a success template. If the form is invalid, the view function re-renders the form with the validation errors.

3. Create a template that displays the form and handles the form submission. The template should use the `{% csrf_token %}` template tag to include a CSRF token that protects against cross-site request forgery attacks, and render the form fields using the `{{ form.field }}` template syntax. For example:

   ```html
   <form method="post">
   {% csrf_token %}
   {{ form.name.label_tag }} {{ form.name }}<br>
   {{ form.email.label_tag }} {{ form.email }}<br>
   {{ form.message.label_tag }} {{ form.message }}<br>
   <input type="submit" value="Submit">
   </form>
   ```

   In this example, we define a new template that renders the form using the `{{ form.field }}` syntax. The `{{ form.field.label_tag }}` template tag generates a label for the form field, and the `{{ form.field }}` template variable renders the input widget for the form field. The `{% csrf_token %}` template tag includes a hidden input field that contains a CSRF token, which is used by Django to prevent cross-site request forgery attacks.

Overall, creating forms in Django involves defining a form class, instantiating it in a view function, and rendering it in a template. The form class provides validation and processing logic, while the view function handles form submission and rendering, and the template handles the HTML rendering of the form. Django's form system provides many powerful features, such as field validation, form rendering, and CSRF protection, which make it easy to create robust and secure forms for your web applications.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/learn-django/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

