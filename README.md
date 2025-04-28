# Hello, Django!

This repository contains a simple Django application that serves as a tutorial for setting up a Django project in a database-first fashion.

This project has been presented during the Databases course.

## Getting Started

Assuming you have [uv](https://docs.astral.sh/uv/) installed, you can run the following command to install the dependencies:

```bash
uv sync
```

Before running the application, make sure to set up your database.
You can do this by running the `seed.sql` file in your MySQL instance.
If you need to change username and password, you can do so in the `hello/settings.py` file.

To run the application, use the following command:

```bash
uv run manage.py runserver
```