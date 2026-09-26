# Task 3 – Secure Coding

## Objective

The objective of this task was to understand secure coding practices by creating and testing a simple login application and reviewing the difference between a vulnerable implementation and a more secure implementation.

## Work Completed

For this task, I created and tested the following files:

- `vulnerable_app.py` – Python login application used for the initial implementation.
- `setup_db.py` – Script used to create and initialize the SQLite practice database.
- `secure_app.py` – Improved version of the login application.
- `security_review.txt` – Notes and security observations from the task.

## Testing

During the initial testing, the application produced a database error because the required `users` table had not yet been created.

I created the database using `setup_db.py` and then tested the login application again.

The test user was:

- Username: `testuser`
- Password: `test123`

After the database was initialized, the login application successfully authenticated the test user. The improved application was also tested successfully.

## Files

| File | Description |
|---|---|
| `vulnerable_app.py` | Initial login application |
| `setup_db.py` | SQLite database setup script |
| `secure_app.py` | Improved login application |
| `security_review.txt` | Security review and observations |

## Security Note

The practice database file containing test credentials is intentionally not included in this public repository to avoid unnecessarily exposing database contents or credentials.

## Learning Outcome

This task helped me understand basic secure coding concepts, database initialization, login authentication, testing, and the importance of reviewing application security before deployment.
