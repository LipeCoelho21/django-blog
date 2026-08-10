# Django Blog Project

A blog application built with Django while studying backend web development through Maximilian Schwarzmüller's Django course.

## About

This project is currently finished for the course stage. It was created to practice Django's project structure, URL routing, views, templates, models, the Django ORM, SQLite, and the Django admin interface.

## Technologies

- Python
- Django
- SQLite
- HTML and CSS
- Django Templates

## Concepts Practiced

- Model–Template–View (MTV) architecture
- URL configuration and views
- Database models and migrations
- Django ORM
- SQLite database management
- Admin interface
- Static files and template inheritance

## Run Locally

```bash
git clone https://github.com/LipeCoelho21/django-blog.git
cd django-blog
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

> This is a learning project. Setup details may change as the project evolves.