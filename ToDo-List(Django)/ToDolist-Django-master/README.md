# Django To-Do List Application

A full-featured web-based To-Do List application built with Django that allows users to create accounts, manage their personal tasks, mark tasks as complete, and delete tasks. The application features user authentication, a clean Bootstrap-based UI, and a secure user-specific task management system.

## Features

- **User Authentication**
  - User registration with email and password
  - Secure login/logout functionality
  - Password validation (minimum 8 characters)
  - Username uniqueness validation

- **Task Management**
  - Create new tasks
  - View all personal tasks
  - Mark tasks as completed
  - Delete tasks
  - Task status tracking (In Progress / Completed)

- **User Interface**
  - Modern, responsive Bootstrap 5 design
  - Clean and intuitive interface
  - User-friendly forms and navigation

- **Security**
  - Login-required protection for task management
  - User-specific task isolation (users can only see their own tasks)
  - CSRF protection
  - Secure password handling

## Technologies Used

- **Backend**: Django 5.2
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Python**: 3.x

## Project Structure

```
ToDolist-Django-master/
│
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── Procfile                  # Deployment configuration
├── .gitignore               # Git ignore rules
│
├── todoproj/                # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── todoapp/                 # Main application directory
│   ├── __init__.py
│   ├── models.py            # Database models (Todo model)
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── admin.py             # Admin configuration
│   ├── apps.py
│   ├── tests.py
│   │
│   ├── migrations/          # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   └── templates/           # HTML templates
│       └── todoapp/
│           ├── login.html
│           ├── register.html
│           └── todo.html
│
└── static/                  # Static files directory (for collectstatic)
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Navigate to the Project

```bash
cd ToDo-List(Django)/ToDolist-Django-master
```

### Step 2: Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install Django directly:
```bash
pip install Django==5.2
```

## How to Run the Project

### Step 1: Run Database Migrations

Create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Create a Superuser (Optional)

Create an admin account to access Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin username, email, and password.

### Step 3: Collect Static Files

Collect static files (CSS, JS, images) for the admin panel:

```bash
python manage.py collectstatic
```

When prompted, type `yes` to confirm.

### Step 4: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/` or `http://localhost:8000/`

### Step 5: Access the Application

- **Home/Login Page**: `http://127.0.0.1:8000/`
- **Register Page**: `http://127.0.0.1:8000/register/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/` (requires superuser)

## Usage Instructions

### For New Users

1. **Register an Account**
   - Navigate to the register page
   - Enter a unique username
   - Provide a valid email address
   - Create a password (minimum 8 characters)
   - Click "Register"

2. **Login**
   - Use your username and password to log in
   - You'll be redirected to your personal to-do list

### Managing Tasks

1. **Add a Task**
   - Enter your task in the input field
   - Click "Add Task" button

2. **Mark Task as Completed**
   - Click the "Finished" button next to any task
   - The status will change from "In progress" to "Completed"

3. **Delete a Task**
   - Click the "Delete" button next to any task
   - The task will be permanently removed

4. **Logout**
   - Click the "Logout" button to securely log out

## Database Model

The application uses a simple Todo model:

- **user**: Foreign key to Django's User model
- **todo_name**: CharField (max 1000 characters) - the task description
- **status**: BooleanField (default: False) - completion status

## URL Patterns

- `/` - Home page (login required) - displays user's to-do list
- `/register/` - User registration page
- `/login/` - User login page
- `/logout/` - Logout functionality
- `/delete-task/<task_name>/` - Delete a specific task
- `/update/<task_name>/` - Mark a task as completed
- `/admin/` - Django admin panel

## Configuration

### Settings

The main settings are in `todoproj/settings.py`:

- **DEBUG**: Set to `False` (production mode)
- **ALLOWED_HOSTS**: Configured for specific domains
- **STATIC_ROOT**: Set to `static/` directory
- **Database**: SQLite3 (default Django database)

### Changing Settings for Development

If you want to run in development mode, edit `todoproj/settings.py`:

```python
DEBUG = True
ALLOWED_HOSTS = ['*']  # Allow all hosts (development only)
```

## Troubleshooting

### Common Issues

1. **Migration Errors**
   ```bash
   python manage.py migrate --run-syncdb
   ```

2. **Static Files Not Loading**
   ```bash
   python manage.py collectstatic --noinput
   ```

3. **Port Already in Use**
   ```bash
   python manage.py runserver 8001  # Use different port
   ```

4. **Module Not Found Errors**
   - Ensure virtual environment is activated
   - Reinstall requirements: `pip install -r requirements.txt`

## Production Deployment

For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up a production database (PostgreSQL recommended)
4. Configure static file serving
5. Use a production WSGI server (Gunicorn, uWSGI)
6. Set up environment variables for `SECRET_KEY`

The `Procfile` is configured for Heroku deployment with Gunicorn.

## License

This project is open source and available for educational purposes.

## Author

Django To-Do List Application

---

**Note**: This is a development version. For production use, ensure proper security configurations, use environment variables for sensitive data, and deploy with a production-grade database and web server.

