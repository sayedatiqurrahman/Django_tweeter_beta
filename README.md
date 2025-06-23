
# 🐍 Django Professional Project Quick Setup (README Guide)

This is a quick and professional way to set up a Django project using virtual environment, static/media handling, template structure, and authentication handling.

---

## 🚀 Step-by-Step Setup

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

* Activation

  * for >> Linux/macOS/Git Bash Terminal (Windows)

    ```bash
    source .venv/bin/activate        
    ```

  * for >> Windows

  ```cmd
  .venv\Scripts\activate          
  ```

### 2. Install Django

```bash
pip install django
```

  ## 2.1 Install Existing Project Dependencies
  
  ```bash
  pip install -r requirements.txt
  ```


### 3. Save Requirements

```bash
pip freeze > requirements.txt
```

### 4. Create Django Project

```bash
django-admin startproject myproject .
```

### 4.1 enter inside your project

> myproject = your project name
```bash
cd myproject 
```


### 5. Create Your First App

```bash
python manage.py startapp website
```

### 6. Run Initial Migrations & Create Superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## 📁 Create Folders & Files (Cross-Platform)

### For macOS/Linux

```bash
mkdir static media templates templates/website templates/registration
cd templates/registration
> login.html
> logout.html
> register.html
> password_reset_form.html
> password_reset_done.html
> password_reset_confirm.html
> password_reset_complete.html
```

### For Windows

```cmd
mkdir static && mkdir media && mkdir templates && mkdir templates\website && mkdir templates\registration
cd templates\registration
copy NUL login.html
copy NUL logout.html
copy NUL register.html
copy NUL password_reset_form.html
copy NUL password_reset_done.html
copy NUL password_reset_confirm.html
copy NUL password_reset_complete.html
```

---

## 🗄 Folder Structure (Recommended)

```
project_root/
├── .venv/
├── myproject
│   ├── static/
│   ├── media/
│   ├── templates/
│   │   ├── layout.html             # Base layout
│   │   ├── website/               # App-level templates
│   │   │   └── index.html
│   │   └── registration/         # Auth-related templates
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── register.html
│   │       ├── password_reset_form.html
│   │       ├── password_reset_done.html
│   │       ├── password_reset_confirm.html
│   │       ├── password_reset_complete.html
│   ├── myproject/
│   ├── website/
│   ├── manage.py
└── requirements.txt
```

---

## ⚙️ settings.py Configuration

### Add Your App to INSTALLED\_APPS

In `myproject/settings.py`, add your new `website` app to the `INSTALLED_APPS` list.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',  # ➤ Add this line
]
```

### Static and Media Settings

```python
import os

# static file handling
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# media handling
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Auth Redirect Settings

```python
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/tweet/'
LOGOUT_REDIRECT_URL = '/tweet/'
```

### Templates Settings

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ➤ Highlight: Tell Django to look in the project-level 'templates' folder
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

## 📝 Creating a Base Layout & Using Template Inheritance

Template inheritance allows you to build a base "skeleton" template that contains all the common elements of your site and defines **blocks** that child templates can override.

### 1. Create Base Layout (`templates/layout.html`)

This is your main skeleton file.

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{% block title %}My Awesome Site{% endblock %}</title>
    <!-- Example of linking a static CSS file -->
    {# <link rel="stylesheet" href="{% static 'css/style.css' %}"> #}
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/admin/">Admin</a>
            <a href="/accounts/login/">Login</a>
            <a href="/accounts/logout/">Logout</a>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; 2024 My Project</p>
    </footer>
</body>
</html>
```

### 2. Create a Child Template (`templates/website/index.html`)

This template `extends` the base layout and fills in the blocks.

```html
{% extends "layout.html" %}

{% block title %}
Home Page - Welcome!
{% endblock %}

{% block content %}
<h1>Welcome to the Home Page!</h1>
<p>This content is from the <strong>index.html</strong> template, but the header and footer are from <strong>layout.html</strong>.</p>
{% endblock %}
```

### 3. Create Authentication Templates (`templates/registration/*.html`)

#### login.html

```html
{% extends "layout.html" %}
{% block title %}Login{% endblock %}
{% block content %}
<h2>Login</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Login</button>
</form>
{% endblock %}
```

#### logout.html

```html
{% extends "layout.html" %}
{% block title %}Logged Out{% endblock %}
{% block content %}
<p>You have been logged out.</p>
{% endblock %}
```

#### register.html

```html
{% extends "layout.html" %}
{% block title %}Register{% endblock %}
{% block content %}
<h2>Register</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Register</button>
</form>
{% endblock %}
```

#### password\_reset\_form.html

```html
{% extends "layout.html" %}
{% block title %}Password Reset{% endblock %}
{% block content %}
<h2>Reset your password</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Send Reset Email</button>
</form>
{% endblock %}
```

#### password\_reset\_done.html

```html
{% extends "layout.html" %}
{% block title %}Password Reset Sent{% endblock %}
{% block content %}
<p>An email has been sent with instructions to reset your password.</p>
{% endblock %}
```

#### password\_reset\_confirm.html

```html
{% extends "layout.html" %}
{% block title %}Confirm Password Reset{% endblock %}
{% block content %}
<h2>Enter new password</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Change Password</button>
</form>
{% endblock %}
```

#### password\_reset\_complete.html

```html
{% extends "layout.html" %}
{% block title %}Password Reset Complete{% endblock %}
{% block content %}
<p>Your password has been reset successfully. You can now <a href="{% url 'login' %}">log in</a>.</p>
{% endblock %}
```

---

## 🔌 Wiring Up the View and URL

### 1. Create a View (`website/views.py`)

```python
from django.shortcuts import render

def index(request):
    """A view to render the home page."""
    return render(request, 'website/index.html')
```

### 2. Create App-Level URLs (`website/urls.py`)

Create a **new file** inside your `website` app folder named `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
```

### 3. Include App URLs in Project (`myproject/urls.py`)

Finally, tell your main project's `urls.py` file to include the URLs from the `website` app, plus the auth URLs:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),  # Include your app's URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Auth URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧪 Run the Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

✅ You now have a professional Django setup with:

* Static and media handling
* Templates and template inheritance
* App structure
* Authentication system with login, logout, register, and password reset flows

---

If you want me to help you add example forms, views, or any other customization, just ask!
