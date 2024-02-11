# Django Authentication Project

This Django project implements email-based authentication using Django Rest Framework (DRF) and JWT tokens.

##### Project Overview

The project includes the following components:
- Custom user model for email-based authentication.
- REST APIs for user registration and login.
- JWT token-based authentication for securing APIs.

## Testing

### Testing

To test the APIs use Postman, follow these steps:
### Testing with Postman

To test the APIs using Postman, follow these steps:

1. **Install Postman**: If you haven't already, download and install Postman from [https://www.postman.com/](https://www.postman.com/).

2. **Import Collection**: Import the Postman collection file provided in the project repository.

3. **Set Environment Variables (Optional)**: Set up environment variables for the API base URL and authentication tokens (if required).

4. **Run Requests**: Run the requests in the Postman collection to test the following endpoints:

    - **User Registration**:
        - **URL**: `http://localhost:8000/api/register/`
        - **Method**: `POST`
        - **Body**: JSON object containing user data:
            ```json
            {
                "username": "example_user",
                "email": "user@example.com",
                "password": "your_password"
            }
            ```
        - **Expected Response**: HTTP status code 201 (Created) on successful registration.

    - **User Login**:
        - **URL**: `http://localhost:8000/api/login/`
        - **Method**: `POST`
        - **Body**: JSON object containing login credentials (either username or email and password):
            ```json
            {
                "username": "example_user",
                "password": "your_password"
            }
            ```
            or
            ```json
            {
                "email": "user@example.com",
                "password": "your_password"
            }
            ```
        - **Expected Response**: HTTP status code 200 (OK) on successful login, along with a JWT token in the response body.



## Running the Project Locally

To run the project locally, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine:

   ```bash
     git clone https://github.com/your-username/django-authentication-project.git
   
2. **Navigate to Project Directory**:
    ```bash
        cd myproject
    
4. **Create Virtual Environment: (optional but recommended)**
5. **Install Dependencies**:
    ```bash
        pip install -r requirements.txt
   
7. **Apply Migrations:**
    python manage.py migrate

8. **Run Development Server:**
    python manage.py runserver

8. **Access APIs**:
The project should now be running locally. Access the API endpoint at http://localhost:8000/api/login or http://localhost:8000/api/register.

