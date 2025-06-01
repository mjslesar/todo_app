# ToDoApp
ToDo API (Django REST Framework)

A simple RESTful ToDo list application built with Django and DRF. Includes user registration, JWT authentication, task management with CRUD operations, status filtering, pagination, and web interface.

 Features:

- JWT Authentication (access/refresh tokens)
- User registration
- Create / Read / Update / Delete tasks
- Filter tasks by status (New, In Progress, Completed)
- Pagination on task list
- Permissions: users see only their own tasks
- Unit tests for API endpoints
- Responsive web UI (basic styling)
- PostgreSQL support

    
Run with docker: 

1.Run the container from the directory "docker/" inside the project(required step)

Build and run containers:

    docker-compose up --build

2.Apply migrations & create superuser(optional):

    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser

3.Stop containers:

    docker-compose down

Run with command line:
1.Clone the repository:

    git clone https://github.com/mjslesar/todo_app.git
    
2.Create virtual environment and install dependencies:

    python -m venv .venv
    source .venv/bin/activate or .venv\Scripts\activate on Windows
    pip install -r requirements.txt

3.Configure PostgreSQL in settings.py:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

4.Run migrations and create superuser:

    python manage.py migrate
    python manage.py createsuperuser

5.Start the server:

    python manage.py runserver

6.Access the application:

    API: http://127.0.0.1:8000/api/
    Web interface: http://127.0.0.1:8000/

Running tests:

    python manage.py test

API Endpoints:
    
    POST /api/register/ – User registration
    POST /api/token/ – Obtain JWT token
    POST /api/token/refresh/ – Refresh JWT token
    GET /api/tasks/ – List user tasks (supports ?status= filter)
    POST /api/tasks/ – Create a new task
    GET /api/tasks/<id>/ – Retrieve a specific task
    PUT /api/tasks/<id>/ – Update a task
    DELETE /api/tasks/<id>/ – Delete a task

Technologies Used:

    Python 3.11+
    Django 5.2
    Django REST Framework
    djangorestframework-simplejwt
    PostgreSQL
    Docker & Docker Compose

