# Flight Management System

The Flight Management System is designed to manage flight routes, schedules, airports, pilots, and their assignation to flights. It provides a command-line interface (CLI) to interact with a SQLite database, allowing users to manage various aspects of airline operations.

## Features

* View flight information, routes, schedules, and statuses.
* Manage airport records.
* View and manage pilot information and schedules.
* Add, update, or delete flight routes and schedules.
* Search for available pilots and flight details.
* Administrative actions like resetting or clearing the database.

## Project Structure

The project is divided into multiple Python modules for better organization:

### Main Script

* `main.py` – The entry point of the application, providing a CLI for users to interact with the system.

### Database Operations

* `database_setup.py`: Defines database structure, with functions for creating and dropping the tables and for inserting sample data. 
* `db_operations.py`: Handles all database interactions such as insert, update, delete, and search operations.
* `sql_queries.py`: Contains predefined SQL queries used throughout the project.

### Table Classes

* `airport.py`: Represents the Airport entity.
* `flight_route.py` – Manages flight routes between different airports.
* `flight_schedule.py` – Handles flight schedules, including departure time, date, and status.
* `pilot.py` – Represents pilot details.
* `pilot_schedule.py` – Manages pilots’ schedules and their assigned roles.

## Installation and Setup

### Prerequisites

* Python 3.x
* SQLite3
* Pandas (Python Package)

### Steps to Run the Application

1. Clone the repository

```sh
git clone https://github.com/afr40/Python-Lab-Sheet.git
cd Python-Lab-Sheet
```

2. Install dependencies.

```sh
pip install pandas
```

3. Run the application

```sh
python main.py
```

## Database Management

The database is automatically initialized using flightsDB.db.
To reset the database and load sample data, select the Admin Section in the menu.

## Usage Guide

When running `main.py` you will be prompt to select some options from a menu. Some of the options have sub-menus that are available to access more features inside the application.

* For some options where the user needs to input data or an ID, a table will be shown so the user can select the information accurately
* Inserting entries in the database will have to be done following the database structure.

