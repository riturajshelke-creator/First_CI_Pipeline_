# Python CI Pipeline

## Project Description
This project demonstrates a Continuous Integration (CI) pipeline using GitHub Actions and Python.

It automatically executes Python test cases whenever code is pushed to the GitHub repository.

## Technologies Used
- Python 3.12
- Pytest
- Git
- GitHub
- GitHub Actions

## Project Structure

```text
First_CI_Pipeline/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── codes/
│
├── test_cases/
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project folder:

```bash
cd First_CI_Pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

Execute all test cases:

```bash
python -m pytest -v
```

## GitHub Actions

The GitHub Actions workflow automatically:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs required dependencies.
4. Executes pytest test cases.
5. Displays the test results.

## Objective

To understand and implement Continuous Integration using Python, Pytest, and GitHub Actions.

## Author

Rituraj Shelke