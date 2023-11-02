
# Simple MySQL to JSON API

## Description

This Python script provides a lightweight API to fetch data from a MySQL database and return it as a JSON response. It's a practical workaround for situations where hosting services, like the ones provided by GoDaddy, impose limitations on hosting web applications. Instead of paying for expensive hosting packages to run web framework-based apps, this script offers a cost-effective solution by hosting it as a simple Python CGI application.

## Context

Our company faced restrictions from our hosting provider, GoDaddy, which limited our ability to host applications using frameworks. To circumvent this and avoid unnecessary costs, we developed this API, which can be hosted as a Python application and accessed via a DOM on our main webpage.

## Features

- **Simple Database Connection**: Uses `mysql.connector` to connect to a MySQL database and fetch data.
- **Datetime Conversion**: Converts all `datetime` objects to strings to ensure JSON serializability.
- **CORS Support**: Includes CORS headers to allow cross-origin access, enabling integration with frontend applications hosted on different domains.
- **WSGI Compatible**: Can be deployed as a WSGI application, making it compatible with many web servers.

## Required Libraries

To run this script, you'll need to install the following Python libraries:
- `mysql.connector`
- `cgi`
- `json`
- `datetime`

You can install these libraries using `pip`:

```bash
pip install mysql-connector-python
```

## Functions

### `get_db_connection()`
```python
def get_db_connection():
    # ... (connection details)
```
Establishes and returns a MySQL database connection.

### `get_jobs()`
```python
def get_jobs():
    # ... (fetch and process jobs)
```
Fetches and processes job records from the database, returning them as a list of dictionaries.

### `application(environ, start_response)`
```python
def application(environ, start_response):
    # ... (WSGI application entry point)
```
Serves as the WSGI application entry point, returning the job data as a JSON response.

## Deployment

The script can be deployed on a web server that supports CGI or WSGI. Ensure the database connection details are correctly set before deployment.

## Usage

The API can be accessed from any frontend application, fetching data with a simple HTTP request.

## Alternative to Limited Hosting Services

This script is an effective alternative for users who face limitations from hosting services like GoDaddy, which may charge extra for hosting applications using popular web frameworks.

## Contributing

Feel free to fork this project, make improvements, and submit pull requests.

## Postdata 
Godaddy is trash, dont use it c:.
