# To-Do List Application

## Description
A simple To-Do List application that allows users to create, update, delete, and mark tasks as completed. Great for managing daily tasks effectively.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher

### Installation

1. Clone the repository:
bash
git clone https://github.com/yourusername/todo-list-app.git
cd todo-list-app

<b><h2>Create and activate a virtual environment:</h2></b>
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

<b><h2>Install the required packages:</h2></b>
pip install -r requirements.txt

<b><h2>Run migrations:</h2></b>
python manage.py migrate

<b><h2>Create a superuser:</h2></b>
python manage.py createsuperuser

<b><h2>Start the development server:</h2></b>
python manage.py runserver
Access the application:

Open your web browser and go to http://127.0.0.1:8000 to view the app.
Access the admin panel at http://127.0.0.1:8000/admin using your superuser credentials.
