# Django-based ToDo Application
![image](https://github.com/user-attachments/assets/bf9e0b84-8e01-45b9-a747-6013e5b684e8)


## Setup

<h4>1. Clone the repository</h4>

```sh
$ git clone https://github.com/Middlewarer/ToDoAppdjango.git
$ cd folder
```

<h4>2. Create a virtual environment to install dependencies in and activate it:</h4>

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

<h4>3. Install the dependencies:</h4>

```sh
(env)$ pip install -r requirements.txt
```

<h4>Make and Apply the migrations</h4>

```
python manage.py makemigrations
python manage.py migrate
```

<h4>Configure the default keys in settings.py or in .env created file.<h4>

<hr/>

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/tasks/`.

