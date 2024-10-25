# Project Management Application using Python-Djnago-Drf

This is a RESTful API for managing projects.

## Setup Instructions

1. Clone the repository:
   ```
    git clone https://github.com/anirbanchakraborty123/Project_management_application.git
    cd management_api
   ```

2. Create a virtual environment:
   ```
   - python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
      ```
       venv\Scripts\activate
      ```
  
   - On macOS and Linux:
     ```
       source venv/bin/activate
     ```
  
4. Install dependencies:
```
   - pip install -r requirements.txt
```

5. Apply migrations:
```
   - python manage.py migrate
```

6. Start the development server:
```
   - python manage.py runserver
```

7. The API's will be accessible at 'http://localhost:8000/api/v1/' with mandatory JWT bearer access_token Authentication Header.
```
   - You can get new access_token using login creds-(username,passsowrd) on below apis
   - Get new access_token 'POST api/v1/user/login/'
      - payload={
        email,password
      }
      - response={
        access_token,refresh_token
      }
   - Refresh expired access_token by passing refresh_token to 'POST api/v1/token/refresh/'
     - payload={
        refresh_token
     }
     - response={
        access_token,refresh_token
     }
  ```  
### Swagger OPEN API Documentation:

   You can view swagger api document of all available Rest apis:
   - You can test them after authentication:
   - http://127.0.0.1:8000/api/v1/swagger/
     ```
```
## API Endpoints

### User Authentication

- Register User (POST /api/v1/user/register/): Creates a new user.
- Login User (POST /api/v1/user/login/): Authenticates and returns a token.
- Get User Details (GET /api/v1/user/{id}/): Retrieves user details.
- Update User (PUT/PATCH /api/v1/users/{id}/): Updates user info.
- Delete User (DELETE /api/v1/users/{id}/): Deletes user account.

## Project Endpoints

- List Projects (GET /api/v1/projects/): Retrieves all projects.
- Create Project (POST /api/v1/projects/): Creates a new project.
- Retrieve Project (GET /api/v1/projects/{id}/): Gets details of a project.
- Update Project (PUT/PATCH /api/v1/projects/{id}/): Updates project info.
- Delete Project (DELETE /api/v1/projects/{id}/): Deletes a project.

## Task Endpoints

- List Tasks (GET /api/v1/projects/{project_id}/tasks/): Lists tasks in a project.
- Create Task (POST /api/v1/projects/{project_id}/tasks/): Creates a new task.
- Retrieve Task (GET /api/v1/tasks/{id}/): Retrieves task details.
- Update Task (PUT/PATCH /api/v1/tasks/{id}/): Updates task info.
- Delete Task (DELETE /api/v1/tasks/{id}/): Deletes a task.

##Comment Endpoints

- List Comments (GET /api/v1/tasks/{task_id}/comments/): Lists comments on a task.
- Create Comment (POST /api/v1/tasks/{task_id}/comments/): Creates a new comment.
- Retrieve Comment (GET /api/v1/comments/{id}/): Retrieves comment details.
- Update Comment (PUT/PATCH /api/v1/comments/{id}/): Updates comment info.
- Delete Comment (DELETE /api/v1/comments/{id}/): Deletes a comment.

