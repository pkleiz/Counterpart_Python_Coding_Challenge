# Counterpart EQ Near: Earthquake Monitoring Software

> Counterpart EQ Near is a software system for monitoring earthquakes. It utilizes the public API of the USGS Earthquake Catalog to gather information about earthquakes occurring worldwide. Additionally, it enables users to monitor earthquakes in a specific city and view information about the closest earthquake to that city.

## Documentation
https://github.com/pkleiz/Counterpart_Python_Coding_Challenge/

## Introduction
This API uses Django and Django REST Framework (DRF) to provide a set of endpoints to access the data.

## Setup
You can set up the project by following the steps below:

1 Clone the repository.

2 Navigate to the project's root directory.

3 Create a .env file with the following environment variables (you can see a example in the rootdirectory/env_example.md):

```
DEBUG= True or False (if you want to see the details on browser)
DJANGO_SETTINGS_MODULE= configuration.settings.base (Point to the configuration made for production or development)
SECRET_KEY= 'dkfj3kfk' (It's a unique and secret string of characters that is used to provide cryptographic, can choose any characters)
BASE_POINT= 'http://127.0.0.1:8000/apis/' (basepoint for calls, can changed if it's choosed a default port)
USER= 'user' (user to authenticate the api, will be created)
PASS= 'password' (password to authenticate the api, will be created)
```

4. Create a virtual enviroment using python3 -m venv venv and start it. (optional)

5. In the root of the project, install the requirements.py with:
```
pip install -r requirements.py
```

6. Create migrations and migrate the database with:
```
python manage.py makemigrations cities logs usgs_earthquakes or django mm cities logs usgs_earthquakes
```
Following of:
```
python manage.py migrate or django m
```

7. Create a superuser for access the API data and django admin page with:
```
python manage.py createsuperuser or django csu
```

8. Fill the .env with USER and PASSWORD:
> This method of authentication is basic, but the system is ready for token authentication, it's easy to change in the rest_framework_settings.py. After, it's necessary generate a token on django admin panel.

6. Start the server with:
```
python manage.py runserver or django r
```

The application will be available at http://localhost:8000/. But the Api is avaliable on  http://localhost:8000/apis

## Endpoints:

The following models are supported by Counterpart EQ Near:

### Cities:
The City model stores information about a city, including its name, latitude, and longitude. You can insert manually the city, latitude and longitude or you only insert the city and the system will find for you the lat and long for the location!

#### The supported parameters for this endpoint are:

name (optional): a string of city of address(unstable, can returns a not expected latitude and longitude).

latitude (optional): a float that represents a latitude (required if longitude is filled).

longitude (optional): the end date of the search, in the format YYYY-MM-DD (required if latitude is filled).

#### Get all cities: Get
http://127.0.0.1:8000/apis/cities

#### Insert a new city: Post
parameter name or name, latitude and longitude.

#### Delete a city: Delete
delete based on id of city.


### Earthquakes:
The Earthquake model stores information about an earthquake, including its magnitude, location, title, latitude, longitude, and date.

#### The supported parameters for this endpoint are:

min_magnitude (optional): the minimum magnitude of the earthquake to be returned (default: 5.1).

start_date (optional): the start date of the search, in the format YYYY-MM-DD (required if end_date is filled).

end_date (optional): the end date of the search, in the format YYYY-MM-DD (required if start_date is filled).

#### Get all earthquakes searched in the system before: Get

http://127.0.0.1:8000/apis/earthquakes

#### Get earthquakes between 2 dates: Get

use start_date and end_date

> Everytime a search with start_date and end_date are made, the result is saved and can be consulted without connection with external api.

### Nearest_earthquake:

The Nearest_earthquake model is used to store the results of a search for earthquakes near and earthquakes between 2 dates. It contains information about the searched city, the start and end dates of the search, the closest earthquake found, and the distance from the earthquake to the city.

#### The supported parameters for this endpoint are:

city (optional): the name of the city to be searched (need to registred first on cities).

start_date (optional): the start date of the search, in the format YYYY-MM-DD (required if end_date is filled).

end_date (optional): the end date of the search, in the format YYYY-MM-DD (required if start_date is filled).

min_magnitude (optional): the minimum magnitude of the earthquake to be considered (default: 5.1).

#### Get all searchs made in the system before: Get

http://127.0.0.1:8000/apis/nearest-earthquake

#### Get the closest earthquake based in a city: Get
Use city, start_date and end_date

### Logs
Was created for storage any error in the system. Can be consulted on Database or Django Admin

## Frontend
The frontend of the project was made thinking in simplify the view of data, for this reason, all data is showed in a single page!

## Introduction
Made using some technologies, like jquery, html, fontawesome, javascript, css and more!

## Usability
The most important functionalities are avaliable there, but it's not possible to delete any register directly.
