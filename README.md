# EduPortal - Online School Admission Portal

## 📌 Project Overview
EduPortal is a web-based School Admission Portal developed using **Python (Django)**, **HTML**, **Tailwind CSS**, and **PostgreSQL**.  
The system digitalizes the traditional school admission process, making it faster, easier, and more efficient for students, parents, and administrators.

---

## 🎯 Objectives
- Digitalize school admission process
- Provide online application submission system
- Allow students to track application status
- Reduce manual paperwork
- Improve admission management efficiency

---

## 🚀 Features
- School listing with details
- Advanced school search (city/name)
- Online admission application form
- Application tracking system
- Admin panel for management

---

## 🛠️ Technologies Used

### Frontend:
- HTML
- Tailwind CSS

### Backend:
- Python
- Django Framework

### Database:
- PostgreSQL (Django ORM)

### Tools:
- VS Code / PyCharm
- Git & GitHub

---

## 📂 Project Modules
- School Management Module  
  (School details, facilities, images, documents, search, homepage display)

- Student Admission Module  
  (Student application form, validation, submission system)

- Application Management Module  
  (Application tracking, status update: Pending / Approved / Rejected)

- Newsletter Subscription Module  
  (Email subscription system)

- Admin Panel Module  
  (Django admin for managing schools, applications, and content)

---

## 🧩 System Architecture
- **Frontend:** HTML + Tailwind CSS (User Interface)
- **Backend:** Django (Business Logic)
- **Database:** PostgreSQL (Data Storage)

---

```md
## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/XploreWithRonak01/eduportal.git
cd eduportal

### 2. Create Virtual Environment – Python environment

python -m venv venv

---

### 3. Activate Virtual Environment – Virtual environment start

venv\Scripts\activate   # Windows
source venv/bin/activate   # Linux/Mac

---

### 4. Install Dependencies – Required packages install

pip install -r requirements.txt

---

### 5. Setup PostgreSQL database 

### 6. Create database: eduportal

### 7. Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eduportal',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 8. Run Migrations – Database tables create

python manage.py makemigrations
python manage.py migrate

---

### 9. Create Superuser – Admin login

python manage.py createsuperuser

---

### 10. Run Server – Project start

python manage.py runserver

---

### 11. Open Project – Browser 
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/

