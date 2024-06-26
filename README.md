

---

# TeamCollab

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/subreto-roy/TeamCollab.git
cd TeamCollab
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Create a Superuser

```bash
python manage.py createsuperuser
```

### 5. Run Server

```bash
python manage.py runserver
```

## API Documentation

This API provides endpoints to manage users, projects, tasks, and comments. Below are the available endpoints with their respective methods and descriptions.

### Authentication

#### Register User

- **Endpoint:** `/api/users/register/`
- **Method:** `POST`
- **Description:** Register a new user.
- **Request Body:**
  ```json
  {
      "username": "string",
      "email": "string",
      "password": "string",
      "first_name": "string",
      "last_name": "string"
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "username": "string",
      "email": "string",
      "first_name": "string",
      "last_name": "string",
      "date_joined": "datetime"
  }
  ```

#### Login User

- **Endpoint:** `/api/users/login/`
- **Method:** `POST`
- **Description:** Authenticate a user and return a token.
- **Request Body:**
  ```json
  {
      "username": "string",
      "password": "string"
  }
  ```
- **Response:**
  ```json
  {
      "refresh": "string",
      "access": "string"
  }
  ```

### User Endpoints

#### Get User Details

- **Endpoint:** `/api/users/{id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific user.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  {
      "id": 1,
      "username": "string",
      "email": "string",
      "first_name": "string",
      "last_name": "string",
      "date_joined": "datetime"
  }
  ```

#### Update User

- **Endpoint:** `/api/users/{id}/`
- **Method:** `PUT` or `PATCH`
- **Description:** Update user details.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Request Body:**
  ```json
  {
      "username": "string",
      "email": "string",
      "first_name": "string",
      "last_name": "string"
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "username": "string",
      "email": "string",
      "first_name": "string",
      "last_name": "string",
      "date_joined": "datetime"
  }
  ```

#### Delete User

- **Endpoint:** `/api/users/{id}/`
- **Method:** `DELETE`
- **Description:** Delete a user account.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:** `204 No Content`

### Project Endpoints

#### List Projects

- **Endpoint:** `/api/projects/`
- **Method:** `GET`
- **Description:** Retrieve a list of all projects.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  [
      {
          "id": 1,
          "name": "string",
          "description": "string",
          "owner": 1,
          "created_at": "datetime"
      }
  ]
  ```

#### Create Project

- **Endpoint:** `/api/projects/`
- **Method:** `POST`
- **Description:** Create a new project.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Request Body:**
  ```json
  {
      "name": "string",
      "description": "string",
      "owner": 1
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "name": "string",
      "description": "string",
      "owner": 1,
      "created_at": "datetime"
  }
  ```

#### Retrieve Project

- **Endpoint:** `/api/projects/{id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific project.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  {
      "id": 1,
      "name": "string",
      "description": "string",
      "owner": 1,
      "created_at": "datetime"
  }
  ```

#### Update Project

- **Endpoint:** `/api/projects/{id}/`
- **Method:** `PUT` or `PATCH`
- **Description:** Update project details.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Request Body:**
  ```json
  {
      "name": "string",
      "description": "string",
      "owner": 1
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "name": "string",
      "description": "string",
      "owner": 1,
      "created_at": "datetime"
  }
  ```

#### Delete Project

- **Endpoint:** `/api/projects/{id}/`
- **Method:** `DELETE`
- **Description:** Delete a project.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:** `204 No Content`

### Task Endpoints

#### List Tasks

- **Endpoint:** `/api/projects/{project_id}/tasks/`
- **Method:** `GET`
- **Description:** Retrieve a list of all tasks in a project.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  [
      {
          "id": 1,
          "title": "string",
          "description": "string",
          "status": "string",
          "priority": "string",
          "assigned_to": 1,
          "project": 1,
          "created_at": "datetime",
          "due_date": "datetime"
      }
  ]
  ```

#### Create Task

- **Endpoint:** `/api/projects/{project_id}/tasks/`
- **Method:** `POST`
- **Description:** Create a new task in a project.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Request Body:**
  ```json
  {
      "title": "string",
      "description": "string",
      "status": "string",
      "priority": "string",
      "assigned_to": 1,
      "due_date": "datetime"
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "title": "string",
      "description": "string",
      "status": "string",
      "priority": "string",
      "assigned_to": 1,
      "project": 1,
      "created_at": "datetime",
      "due_date": "datetime"
  }
  ```

#### Retrieve Task

- **Endpoint:** `/api/tasks/{id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific task.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  {
      "id": 1,
      "title": "string",
      "description": "string",
      "status": "string",
      "priority": "string",
      "assigned_to": 1,
      "project": 1,
      "created_at": "datetime",
      "due_date": "datetime"
  }
  ```

#### Update Task

- **Endpoint:** `/api/tasks/{id}/`
- **Method:** `PUT` or `PATCH`
- **Description:** Update task details.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Request Body:**
  ```json
  {
      "title": "string",
      "description": "string",
      "status": "string",
      "priority": "string",
      "assigned_to": 1,
      "due_date": "datetime"
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "title": "string",
      "description": "string",
      "status": "string",
      "priority": "string",
      "assigned_to": 1,
      "project": 1,
      "created_at": "datetime",
      "due_date": "datetime"
  }
  ```

#### Delete Task

- **Endpoint:** `/api/tasks/{id}/`
- **Method:** `DELETE`
- **Description:** Delete a task.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:** `204 No Content`

### Comment Endpoints

#### List Comments

- **Endpoint:** `/api/tasks/{task_id}/comments/`
- **Method:** `GET`
- **Description:** Retrieve a list of all comments on a task.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  [
      {
          "id": 1,
         "content": "string",
          "user": 1,
          "task": 1,
          "created_at": "datetime"
      }
  ]
  ```

#### Create Comment

- **Endpoint:** `/api/tasks/{task_id}/comments/`
- **Method:** `POST`
- **Description:** Create a new comment on a task.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Request Body:**
  ```json
  {
      "content": "string"
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "content": "string",
      "user": 1,
      "task": 1,
      "created_at": "datetime"
  }
  ```

#### Retrieve Comment

- **Endpoint:** `/api/comments/{id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific comment.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  {
      "id": 1,
      "content": "string",
      "user": 1,
      "task": 1,
      "created_at": "datetime"
  }
  ```

#### Update Comment

- **Endpoint:** `/api/comments/{id}/`
- **Method:** `PUT` or `PATCH`
- **Description:** Update comment details.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Request Body:**
  ```json
  {
      "content": "string"
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "content": "string",
      "user": 1,
      "task": 1,
      "created_at": "datetime"
  }
  ```

#### Delete Comment

- **Endpoint:** `/api/comments/{id}/`
- **Method:** `DELETE`
- **Description:** Delete a comment.
- **Request Header:** `Authorization: Bearer <access_token>`
- **Response:** `204 No Content`

---

