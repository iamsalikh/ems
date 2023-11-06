# Education Management System

## Project Description

The Education Management System is a powerful application designed to efficiently manage educational processes within academic institutions. The project comprises four core directories: `assignments`, `courses`, `grades`, and `users`.

### Directory "assignments"

In this directory, the following functions are implemented:

- Creating new assignments for courses.
- Retrieving a list of assignments for a specific course.
- Fetching details about a specific assignment based on its ID.
- Editing assignments, including modifying descriptions and deadlines.

### Directory "courses"

This directory offers the following functions:

- Creating new courses.
- Listing all available courses.
- Accessing information about a specific course by its ID.
- Editing course details, including changing course names and managing course materials.

### Directory "grades"

The "grades" directory includes functions related to grading:

- Recording grades for completed assignments.
- Retrieving lists of grades for a particular student or assignment.
- Calculating the average grade for a student within a course.

### Directory "users"

In this directory, you can manage user-related functions:

- Registering new users.
- Authenticating users.
- Listing all users.
- Retrieving user information based on their ID.
- Managing user profiles, including changing passwords and contact information.

The Education Management System is designed to simplify and automate processes within educational institutions, providing easy access to information about courses, assignments, grades, and user accounts.
___
## Installation and Requirements

To run this project, ensure that you have the following dependencies:

- [Python](https://www.python.org/downloads/) (recommended version 3.7 and above)

To install all the necessary Python libraries from the `requirements.txt` file, execute the following command:

```bash
pip install -r requirements.txt
```
### Running the Project
To run the project, use Uvicorn:
```bash
uvicorn main:app --reload
```
You'll also need to clone this repository using the following command:
```bash
git clone https://github.com/iamsalikh/education-management-system.git
```

# education-management-system
