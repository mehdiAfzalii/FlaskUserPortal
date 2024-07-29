# Flask Web Application

This is a simple Flask web application that allows users to sign up and log in. User data is stored in a JSON file.

## Features

1. **Sign Up**: Users can create an account by providing their name, username, and password.
2. **Log In**: Users can log in using their credentials.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository or download the source code.

2. Install the required packages using pip:

   ```bash
   pip install flask
   ```

### Running the Application

1. Run the Flask application:

   ```bash
   flask --debug run
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

### Project Structure

- `app.py`: The main Python file containing the Flask application.
- `templates/signup.html`: The HTML template for the sign-up page.
- `templates/login.html`: The HTML template for the login page.
- `db.json`: The JSON file where user data is stored.

### Endpoints

- **`/` (Sign Up Page)**: 
  - `GET`: Renders the sign-up form.
  - `POST`: Handles the sign-up process.

- **`/login` (Login Page)**:
  - `GET`: Renders the login form.
  - `POST`: Handles the login process.

### How It Works

1. **Sign Up**:
   - Users enter their name, username, and password.
   - The application checks if the username already exists. If not, it saves the user data to `db.json`.

2. **Log In**:
   - Users enter their username and password.
   - The application checks if the credentials match an existing account in `db.json`.

### Note

- Ensure that `db.json` is present in the same directory as `app.py` for the application to function correctly. If it doesn't exist, create a new file named `db.json` and initialize it with an empty array: `[]`.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/) for the framework used in this project.
