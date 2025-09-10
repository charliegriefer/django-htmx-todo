# Tasks To-Do App

A simple to-do list web application built with Django and HTMX.

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/tasks.git
cd tasks
```

### 2. Set up virtual environment and install dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Apply migrations and run the dev server
```bash
python manage.py migrate
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🛠 Design Notes & Trade-offs

- **Single-page dynamic behavior** was achieved with **HTMX**, avoiding a full JavaScript frontend framework.
- Minimal **form validation** is done server-side, no custom JS.
- The project is **not split into components/services** beyond basic views, models, and templates — intentional for simplicity.
- No user authentication — all tasks are global. In a real project, this would be user-scoped.
- Only **basic tests** are included, mostly to demonstrate that tests are written, not full coverage.

These choices were made to focus on core functionality within a short time window.

---

## ⚖️ HTMX: Pros & Cons

### ✅ Pros

- **Super lightweight** — HTMX adds minimal JS but provides interactivity.
- Keeps frontend and backend in **tight sync** with no API layer.
- Perfect for **progressive enhancement** or **server-rendered apps**.
- Great developer experience for small to mid-sized features.

### ❌ Cons

- **Limited ecosystem** compared to React/Vue/Svelte.
- Complex UI state management is harder (e.g., modals, undo stacks).
- HTML over-the-wire can get verbose or hard to debug at scale.
- May feel limiting for large SPAs.

### In this project

HTMX was an ideal fit — it added instant interactivity (add, complete, delete tasks) without writing any JavaScript. Its simplicity and server-driven nature kept the stack focused and fast.

---

## ✅ Tests

To run the tests:

```bash
python manage.py test
```

---

## 📁 Project Structure

```
tasks/
├── manage.py
├── todo/
│   └── tasks/
│       ├── models.py
│       ├── views.py
│       ├── services.py
│       ├── forms.py
│       ├── urls.py
│       ├── templates/
│       │   └── tasks/
│       │       ├── task_list.html
│       │       ├── _task_form.html
│       │       ├── _task_row.html
│       │       ├── _task_edit_row.html
│       │       └── _messages.html
│       ├── static/
│       │   └── tasks/
│       │       └── css/
│       │           └── style.css
│       └── tests.py
└── requirements.txt
```

---

## 📌 Notes

- All HTML forms include `{% csrf_token %}` to satisfy CSRF protection requirements.
- HTMX interactions work seamlessly due to use of `hx-*` attributes and server-rendered partials.
