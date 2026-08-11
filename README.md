<div align="center">
  <h1>✨ Django Blog Project ✨</h1>
  <p>A full-stack blog application built to master backend web development.</p>
  
  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
  [![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)]()
  [![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)]()
  [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)]()
  [![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)]()
</div>

---

## 🎯 About The Project

Welcome to my **Django Blog**! 🚀 I built this project from the ground up to solidify my knowledge of backend web development and the MVC (Model-View-Template) architecture. 

It is designed to be a fully functional blog system that demonstrates clean code practices, database management, and dynamic web page rendering.

### 💼 Technical Skills Showcased (ATS Friendly)
- **Backend Development:** Python, Django Web Framework.
- **Database Management:** Relational Databases, SQL, SQLite, Django ORM (Object-Relational Mapping).
- **Frontend Basics:** HTML5, CSS3, Template rendering.
- **Version Control & Security:** Git, GitHub, Environment variable management.

## ✨ Key Features

- 📝 **Dynamic Post Creation:** Users can create and read blog posts.
- 🗄️ **Database Integration:** Utilizes SQLite and the Django ORM for efficient data querying.
- 🎨 **Templating Engine:** Uses Django's built-in templating system to serve dynamic HTML.
- 🔐 **Secure Configuration:** Proper management of environment variables and sensitive keys.
- 🛠️ **Admin Panel:** Fully configured Django Admin interface for content management.

## 🚀 Getting Started

If you want to run this project locally, follow these simple steps!

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/spray-dev/django-blog.git
cd django-blog/blog_project
```

### 2️⃣ Set Up Your Virtual Environment
It's always best to keep dependencies isolated! 🛡️
```bash
python -m venv venv

# On Windows:
.\venv\Scripts\Activate.ps1

# On macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies & Setup Environment
```bash
pip install django

# Set up your development secret key
# Windows:
$env:DJANGO_SECRET_KEY = "your-dev-secret-key"
# macOS/Linux:
export DJANGO_SECRET_KEY="your-dev-secret-key"
```

### 4️⃣ Database & Migrations
Set up your SQLite database tables using the ORM:
```bash
python manage.py migrate
```

### 5️⃣ Run the Server
Launch the development server to see the app in action: 🌐
```bash
python manage.py runserver
```
Now, open your browser and visit: `http://127.0.0.1:8000/` 🎉

---

## 🌱 What I'm Learning Next
I am continuously improving my skills! Here is what I am diving into next:
- **Advanced SQL:** Writing complex queries and optimizing database performance.
- **PostgreSQL / MySQL:** Migrating from SQLite to a robust production database.
- **REST APIs:** Building endpoints with Django REST Framework (DRF).

---

<div align="center">
  <p>Created with 💻 and ☕ by <a href="https://github.com/spray-dev">Filipe Coelho</a></p>
</div>