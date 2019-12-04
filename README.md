
# CRAFTY
Go2People assignment 
## Built with

CRAFTY was built with:

* [Django](https://www.djangoproject.com/)- Python-based free and open-source web framework

## Installation

### Packages
Install the required packages using pip:

```
pip install -r requirements.txt
```
### Database

For database and super-admin creation: 
```
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```
And then fill fixtures by running:
```
./manage.py loaddata */fixtures/*.json
```
### Collecting static files
Excute in terminal:
```
./manage.py collectstatic --noinput

```

### Running server:

To run server locally run in terminal :
`./manage.py runserver`

And open in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to check the plateforme

