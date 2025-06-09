# My Own CRM

This project provides a minimal Customer Relationship Management (CRM) system
built with Python and Flask. It demonstrates a simple way to track customers
using a RESTful API backed by SQLite.

## Features

- Create, list, update and delete customers
- Stores data in a local SQLite database
- Simple Flask application

## Setup

1. Install dependencies (preferably in a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

2. Start the application:

   ```bash
   python -m crm.app
   ```

   The API will be available at `http://localhost:5000`.

## API Endpoints

- `GET /customers` – list all customers
- `POST /customers` – create a customer (`name` and `email` in JSON body)
- `PUT /customers/<id>` – update a customer
- `DELETE /customers/<id>` – delete a customer

This repository is a simple starting point for building a more complex CRM system.

## Login Pages

Basic login forms are available for different user roles:

- `http://localhost:5000/login/admin`
- `http://localhost:5000/login/personnel`
- `http://localhost:5000/login/customer`

These pages provide simple username and password fields but do not implement
full authentication.
