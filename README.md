# Task Management API

## Overview

This is a RESTful API for managing tasks, built using Flask and MySQL. It supports creating, reading, updating, and deleting tasks, while ensuring secure access with JWT authentication. The API allows users to store tasks, track their status (Pending/Completed), and set due dates. 

## Features

- CRUD Operations: Create, Read, Update, and Delete tasks.
- JWT Authentication: Secure access for users.
- MySQL Database: Stores tasks with fields like Title, Description, Status, and Due Date.
- Filtering and Sorting: Filter tasks by status and sort by due date.
- Dockerization: Containerized application for easy deployment.

## Requirements

- Python 3.x
- MySQL
- Docker (optional)

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api


2. Install Dependencies
First, create and activate a virtual environment (optional but recommended):

python3 -m venv venv
source venv\Scripts\activate  

Then, install the required Python libraries:
pip install -r requirements.txt

3. Configure MySQL Database
Create a MySQL database and user for the application. In the .env file, update the MySQL connection details:


MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=Saisri@1968
MYSQL_DATABASE=task_management
JWT_SECRET_KEY=S3cUr3K3yF0rJWT!

4. Run Database Migrations
The application uses SQLAlchemy for database interaction. The first time you run the application, it will automatically create the necessary tables.

5. Run the API
Run the application locally:
python src/routes/routes.py
By default, the API will be available at http://localhost:5000.

6. Test the API
Once the application is running, you can test it using a tool like Postman or Swagger UI. Make sure to include a Bearer token when making requests to protected endpoints.

API Documentation
POST /tasks: Create a new task
GET /tasks: Retrieve all tasks
GET /tasks/:id: Retrieve a specific task by ID
PUT /tasks/:id: Update a task
DELETE /tasks/:id: Delete a task
Sample Request
Create Task (POST)

Request body:
{
  "title": "Finish API Documentation",
  "description": "Complete the API documentation for the Task Management System.",
  "status": "Pending",
  "dueDate": "2025-01-20"
}

Response:
{
  "message": "Task created successfully",
  "task": {
    "id": 1,
    "title": "Finish API Documentation",
    "description": "Complete the API documentation for the Task Management System.",
    "status": "Pending",
    "due_date": "2025-01-20"
  }
}

Docker Usage
If you prefer to run the API inside a Docker container, follow these steps:

1. Build the Docker Image
docker build -t task-api

2. Run the Docker Container

docker run -p 5000:5000 task-api
The application will be available at http://localhost:5000.

JWT Authentication
To access protected routes, you need to generate a JWT token.
Use the login endpoint (POST /login) to authenticate and obtain a token.
Add the token to the Authorization header of your requests as a Bearer token.

