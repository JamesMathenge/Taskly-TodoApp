# 📝 Taskly

Taskly is a simple and clean To-Do list web application built with **Django**. It allows users to create, view, and delete tasks with optional due dates. The app is designed for clarity, speed, and usability.

---

## 🚀 Features

- ✅ Add new tasks with a title, optional details, and due date
- 🗂 View a list of all tasks, ordered by creation date
- ⏰ Highlight overdue tasks
- ❌ Delete completed or unneeded tasks
- 📱 Responsive design using HTML & CSS (no JS dependency)
- 📅 Human-readable date formatting

---

## 🛠 Tech Stack

- **Backend:** Django 5.2.4 (Python 3.13)
- **Frontend:** HTML5, CSS3 (custom styling)
- **Database:** SQLite (default Django database)
- **Testing:** Django's built-in TestCase framework

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/taskly.git
cd taskly
```

### 2. Set up virtual environment
```bash
python -m venv myenv
.\myenv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```

Then open your browser and go to: `http://127.0.0.1:8000/`

---

## 🧪 Running Tests

To run the test suite:
```bash
python manage.py test
```

Tests include:
* ✅ Task creation
* ✅ Task list rendering
* ✅ Task deletion
* ✅ Task model behavior

---

## 📁 Project Structure

```
taskly/
│
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
├── todo_app/
│   ├── taskly/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── __init__.py
```

---

## 🧠 Future Improvements

* 🔐 User authentication (login/logout)
* 📝 Edit existing tasks
* 📊 Task filtering (by due date, completed, etc.)
* 📱 Mobile-first responsive design with Tailwind or Bootstrap

---

## 📜 License

This project is licensed under the MIT License. You're free to use, modify, and distribute it as needed.

---

## 👨‍💻 Author

Built with ❤️ by **James Mathenge**