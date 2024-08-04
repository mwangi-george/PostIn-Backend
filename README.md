# PostIn API Service

A personal project created to learn software engineering with python

## Description

PostIn is a RESTful API service developed using FastAPI. It provides endpoints for user and post management. The service is designed to be efficient, easy to use, and scalable.

## Features

- User Management
- Post Management
- Authentication and authorization 
- Detailed API documentation with OpenAPI

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mwangi-george/PostIn.git
    cd PostIn
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Make database migrations:**
   
    ```bash
   alembic upgrade head
   ```

## Running the Application

To start the FastAPI server, run the following command:

```bash
uvicorn app.main:app --reload
```

Live api service and documentation available at the following endpoints:

1. [Swagger Documentation](https://postin-api.onrender.com/docs)

2. [Redocly Documentation](https://postin-api.onrender.com/redoc)