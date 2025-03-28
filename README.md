# Counterpart EQ Near: Earthquake Monitoring Software

> Counterpart EQ Near is a software system for monitoring earthquakes. It utilizes the public API of the USGS Earthquake Catalog to gather information about earthquakes occurring worldwide. Additionally, it enables users to monitor earthquakes in a specific city and view information about the closest earthquake to that city.

## Documentation
https://github.com/pkleiz/Counterpart_Python_Coding_Challenge/

## Introduction
This API uses Django and Django REST Framework (DRF) to provide a set of endpoints to access the data.

## Setup
You can set up the project by following the steps below:

1. Clone the repository.

2. Navigate to the project's root directory.

3. Create a `.env` file with the following environment variables (you can see an example in `rootdirectory/env_example.md`):

```
DEBUG=True or False  # if you want to see the details in the browser
DJANGO_SETTINGS_MODULE=configuration.settings.base  # for production or development
SECRET_KEY='your_secret_key'  # unique and secret string for cryptographic use
BASE_POINT='http://127.0.0.1:8000/apis/'  # base URL for API calls
USER='user'  # API user to be created
PASS='password'  # API password to be created
```

4. (Optional) Create a virtual environment using:
```
python3 -m venv venv
```
Activate it with:
```
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

5. Install the dependencies:
```
pip install -r requirements.txt
```

6. Create migrations and migrate the database:
```
python manage.py makemigrations cities logs usgs_earthquakes
python manage.py migrate
```

7. Create a superuser:
```
python manage.py createsuperuser
```

8. Fill in the `.env` with USER and PASSWORD. This method uses basic authentication, but the system is ready for token-based authentication. You can configure this in `rest_framework_settings.py` and generate a token through the Django admin panel.

9. Start the server:
```
python manage.py runserver
```

The application will be available at http://localhost:8000/. The API is available at http://localhost:8000/apis

## Endpoints

The following models are supported by Counterpart EQ Near:

### Cities
Stores information about a city, including name, latitude, and longitude. You can manually insert latitude and longitude, or just the city name and the system will find coordinates for you.

**Supported parameters:**
- `name` (optional): string representing the city or address
- `latitude` (optional): float, required if `longitude` is provided
- `longitude` (optional): float, required if `latitude` is provided

**Endpoints:**
- Get all cities: `GET /apis/cities`
- Insert a new city: `POST /apis/cities` (use `name`, or `name`, `latitude`, `longitude`)
- Delete a city: `DELETE /apis/cities/{id}`

### Earthquakes
Stores information about earthquakes: magnitude, location, title, latitude, longitude, and date.

**Supported parameters:**
- `min_magnitude` (optional): minimum magnitude to return (default: 5.1)
- `start_date` (optional): format YYYY-MM-DD (required if `end_date` is used)
- `end_date` (optional): format YYYY-MM-DD (required if `start_date` is used)

**Endpoints:**
- Get all stored earthquakes: `GET /apis/earthquakes`
- Get earthquakes between two dates: `GET /apis/earthquakes?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`

> Searches with `start_date` and `end_date` are saved and can be retrieved later without external API calls.

### Nearest Earthquake
Stores the result of a search for the closest earthquake to a city.

**Supported parameters:**
- `city` (optional): name of the city (must be registered in `/cities` first)
- `start_date` (optional): required if `end_date` is used
- `end_date` (optional): required if `start_date` is used
- `min_magnitude` (optional): default is 5.1

**Endpoints:**
- Get all previous searches: `GET /apis/nearest-earthquake`
- Get the closest earthquake: `GET /apis/nearest-earthquake?city=X&start_date=Y&end_date=Z`

### Logs
Stores system errors. Can be viewed via the database or Django Admin.

## Frontend
The frontend was designed to simplify data viewing. All data is displayed on a single page.

### Technologies used
HTML, CSS, JavaScript, jQuery, FontAwesome.

### Usability
The main features are accessible via the UI, but deletion of entries is not currently supported through the frontend.
