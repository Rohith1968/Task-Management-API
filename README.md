# Task Management API

## Overview

The **Task Management API** is a RESTful service built using Flask and MySQL to efficiently manage tasks. It supports features like task creation, retrieval, updates, and deletion. Secure access is ensured via JWT authentication. The API allows users to organize their tasks with fields like title, description, status (Pending/Completed), and due dates.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete tasks.
- **JWT Authentication**: Secure endpoints to protect user data.
- **MySQL Integration**: Persistent storage for tasks.
- **Filtering & Sorting**: Filter tasks by status and sort them by due date.
- **Docker Support**: Simplified deployment with containerization.

## Prerequisites

- **Python**: Version 3.x
- **MySQL**: Database server
- **Docker**: Optional for containerized deployment

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api
```

### 2. Install Dependencies

#### Create and activate a virtual environment (optional):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

#### Install required packages:
```bash
pip install -r requirements.txt
```

### 3. Configure the MySQL Database

1. Create a MySQL database for the application:
   ```sql
   CREATE DATABASE task_management;
   ```
2. Update the `.env` file with your database credentials:
   ```
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=Saisri@1968
   MYSQL_DATABASE=task_management
   JWT_SECRET_KEY=S3cUr3K3yF0rJWT!
   ```

### 4. Run Database Migrations
When you start the application for the first time, it will automatically create the required tables in your database.

### 5. Run the Application
Start the API server locally:
```bash
python src/routes/routes.py
```
The API will be available at [http://localhost:5000](http://localhost:5000).

### 6. Test the API
Use tools like **Postman** or **Swagger UI** to interact with the API. Include a Bearer token in requests to protected endpoints.

---

## API Documentation

### Endpoints

#### Task Management
- **POST /tasks**: Create a new task.
- **GET /tasks**: Retrieve all tasks.
- **GET /tasks/:id**: Retrieve a specific task by ID.
- **PUT /tasks/:id**: Update an existing task.
- **DELETE /tasks/:id**: Delete a task.

#### Authentication
- **POST /login**: Authenticate and generate a JWT token.

### Sample Request

#### Create a Task (POST `/tasks`)

**Request Body:**
```json
{
  "title": "Finish API Documentation",
  "description": "Complete the API documentation for the Task Management System.",
  "status": "Pending",
  "dueDate": "2025-01-20"
}
```

**Response:**
```json
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
```

---

## Docker Instructions

### 1. Build the Docker Image
```bash
docker build -t task-api .
```

### 2. Run the Docker Container
```bash
docker run -p 5000:5000 task-api
```
The application will now be accessible at [http://localhost:5000](http://localhost:5000).

---

## JWT Authentication

To access protected routes:

1. **Login to Generate a Token:**
   - Use the `/login` endpoint with valid credentials to obtain a JWT token.
   - Example:
     ```json
     {
       "username": "user1",
       "password": "securepassword"
     }
     ```

2. **Include the Token in Requests:**
   - Add the token to the `Authorization` header as a Bearer token.
     ```
     Authorization: Bearer <your-jwt-token>
     ```

---

## Example Usage

### Fetch All Tasks (GET `/tasks`)

**Request Header:**
```http
Authorization: Bearer <your-jwt-token>
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Finish API Documentation",
    "description": "Complete the API documentation for the Task Management System.",
    "status": "Pending",
    "due_date": "2025-01-20"
  }
]
```



