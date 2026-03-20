<<<<<<< HEAD
# 🎓 CampuSkill

CampuSkill is a web-based placement and student management platform designed to streamline the interaction between **students, recruiters, and administrators**. The system provides role-based access control (RBAC) and enables efficient job application, tracking, and management.

---

## 🚀 Features

* 🔐 Role-Based Access Control (RBAC)

  * Admin
  * Recruiter
  * Student

* 👨‍🎓 Student Module

  * Profile creation & management
  * View available job postings
  * Apply for jobs

* 🏢 Recruiter Module

  * Post job openings
  * Manage applications
  * View candidate profiles

* 🛠️ Admin Module

  * Manage users (students & recruiters)
  * Monitor job postings
  * Control platform access

* 📊 Job Management

  * Create, update, delete job listings
  * Track application status

---

## 🧑‍💻 Tech Stack

**Backend:**

* Python
* Django
* Django REST Framework

**Database:**

* PostgreSQL

**Frontend:**

* (Add your frontend tech here – React / HTML / CSS / JS)

---

## 📁 Project Structure

```
campuskill/
│── backend/
│   ├── applications/
│   ├── jobs/
│   ├── users/
│   ├── backend_core/
│   └── manage.py
│
│── campuSkill/ (if applicable)
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/aishwarya442/campuskill.git
cd campuskill
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Database (PostgreSQL)

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

### 7️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🔗 API Endpoints (Sample)

| Module       | Endpoint             |
| ------------ | -------------------- |
| Users        | `/api/users/`        |
| Jobs         | `/api/jobs/`         |
| Applications | `/api/applications/` |

---

## 🔐 RBAC Roles

| Role      | Permissions              |
| --------- | ------------------------ |
| Admin     | Full access              |
| Recruiter | Manage jobs & applicants |
| Student   | Apply for jobs           |

---

## 📌 Future Enhancements

* Resume upload feature
* Email notifications
* Interview scheduling
* Dashboard analytics

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is for educational purposes.

---

## 👩‍💻 Author

**Aishwarya Shetty**
GitHub: https://github.com/aishwarya442

---
=======
# campuskill
>>>>>>> main
