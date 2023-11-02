
# Typical CRUD Application

## Description

This project is a typical Create, Read, Update, Delete (CRUD) application using Flask and a MySQL database. It provides a simple web interface to add, view, and manage records in a database table.

## Features

- **Data Entry Form**: A web form that allows users to submit new records to the database.
- **Data Table View**: A table that displays all the records from the database and refreshes upon new entry submissions.

## Project Structure

- `app.py`: The Flask application's main script, which contains the logic for database connection, routing, and CRUD operations.
- `Templates`:
- `index.html`: A Bootstrap-styled HTML template for displaying the data entry form and the data table.

## Setup

1. Install Python and Flask.
2. Install MySQL and ensure it is running.
3. Configure the database connection details in `app.py`.
4. Create the necessary table in your MySQL database (replacing `test_table` with your actual table name).

## Running the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser to view the application.

## Usage

- Fill out the form with the details of a new record and submit.
- View the updated list of records in the data table below the form.
