# Sicunet Access Control Log API

This is a simple Django REST API that simulates an access control logging system.

---

## Features

* Django + Django REST Framework (DRF)
* SQLite database (default)
* CRUD APIs
* Django Signals for create/delete events
* Use `subprocess` for Listing every Log
* Simple Unit tests using `APITestCase`
* Simple Homepage


---

## Tech Stack

* Python 3.13.7
* Django 6.0.1
* Django REST Framework
* SQLite3
* Simple UI (HTML+ CSS + Boostrap)

---

## Project Structure

```
sicunet_project/
│
├── access_control/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── apps.py
│
├── sicunet_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── event_list.txt      
├── db.sqlite3
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd sicunet_project
```

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv env

# Windows
env\Scripts\activate

# macOS / Linux
source env/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install django djangorestframework
```

---

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Start Development Server

```bash
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

## 🔌 API Endpoints

| Method | Endpoint          | Description                |
| ------ | ----------------- | -------------------------- |
| POST   | `/api/logs/`      | Create a new access log    |
| GET    | `/api/logs/`      | List all access logs       |
| GET    | `/api/logs/<id>/` | Retrieve single access log |
| PUT    | `/api/logs/<id>/` | Update an access log       |
| DELETE | `/api/logs/<id>/` | Delete an access log       |

---

## 🧪 Running Tests

Unit tests are written using DRF's `APITestCase`.

```bash
python manage.py test
```

Expected output:

```
Ran 3 tests in 0.246s
OK
```

---

## 📝 System Event Logging

* Uses Django signals (`post_save`, `post_delete`)
* Logs are written via `subprocess` to:

```
event_list.txt
```

### Example Log Output

```
[2026-01-06 22:07:52] - CREATE : Acess Log Created for CARD 213902047. status: GRANTED     
[2026-01-06 22:22:34] - DELETE: Access log (ID: 6) for card 213902049 was deleted.

```

---

## 🌿 Git Workflow

* Work done on `mhn` branch

---

## 📌 Notes

* This project uses Django's development server
* SQLite is used for simplicity
* Basic Template UI
---

## 👤 Author

**Md. Mehedi Hassan Nayeem**
--Backend / Django Developer
---
<a href = "https://dev-webnestle.pantheonsite.io/">Portfolio <a>

✅ This project was built as a  task for  <a href="https://sicunet.com/">**Sicunet**<a>.
