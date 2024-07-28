
# Django Registration and Login Authentication


Django Registration and Login Authentication
This project demonstrates a basic user registration and login system using the Django framework. The system includes user authentication, password hashing, and displaying messages for successful registration and login errors. 

Any one who wants to get a login and register authentication they can apply the changes and use it. Use it on your webiste to store the data in an efficient way.


## Features

- User Registration
- User Login
- Password Hashing
- Success and Error Messages
- Responsive Design




## Requirements

- Python 3.x
- Django 3.x or higher
- SQLite (default database)
- Bootstrap (for styling, included via CDN)
## Project Structure

```bash
  myproject/
├── manage.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   └── register.html
│   └── static/
│       └── images/
│           └── IMAGE.jpg
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```




## Setup Instructions

- Clone the repository
```bash
git clone https://github.com/yourusername/django-authentication.git
cd django-authentication
```

- Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

- Install the required packages
```bash
pip install django
```

- Run database migrations
```bash
python manage.py migrate
```

- Create a superuser
```bash
python manage.py createsuperuser
```

- Run the development server
```bash
python manage.py runserver
```

- Access the application
Open your web browser and navigate to http://127.0.0.1:8000/


## Troubleshooting

- Database Errors: Ensure that you've run all migrations and created a superuser.

- Static Files: Make sure static files are properly configured and collected.

- Messages Not Displaying: Verify that the MessageMiddleware is enabled and that the message storage backend is correctly configured.
## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

