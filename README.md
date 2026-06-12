# OrangeHRM Playwright Automation Framework

## Overview

This project is an end-to-end UI automation framework built for the OrangeHRM application using Playwright, Python, and Pytest. The framework follows the Page Object Model (POM) design pattern to create maintainable, scalable, and reusable automation scripts.

The framework demonstrates industry-standard automation practices including test organization, configuration management, reporting, screenshot capture, and CI/CD readiness.

## Tech Stack

* Python
* Playwright
* Pytest
* Page Object Model (POM)
* Git
* GitHub
* Environment Variables (.env)

## Framework Features

* Page Object Model Design Pattern
* Reusable Page Classes
* Centralized Configuration Management
* Environment Variable Support
* Screenshot Capture
* Test Reporting
* Data-Driven Testing Support
* CI/CD Ready Structure

## Project Structure

```text
Orange_HRM/
│
├── config/
│   └── config.py
│
├── pages/
│   └── page classes
│
├── tests/
│   └── test scripts
│
├── test_data/
│   └── test data files
│
├── utils/
│   └── helper functions
│
├── reports/
│
├── screenshots/
│
├── logs/
│
├── .github/workflows/
│   └── Orange_HRM.yml
│
├── .env
├── .gitignore
├── conftest.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/MukundaShanbogh/Orange_HRM.git
```

Navigate to the project:

```bash
cd Orange_HRM
```

Create virtual environment:

```bash
python -m venv orange_hrm_env
```

Activate virtual environment:

Windows:

```bash
orange_hrm_env\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_login.py
```

Run tests in headed mode:

```bash
pytest --headed
```

## Test Scenarios Covered

### Login Module

* Invalid Login
* Empty Credentials Validation
* Valid Login
* Logout Functionality

### Employee Management

* Add Employee
* Search Employee
* Update Employee
* Delete Employee

### Dashboard

* Verify Dashboard Visibility
* Verify Navigation Menu

## Reporting

Reports are generated inside the reports directory after execution.

Screenshots for failed tests are stored in the screenshots directory.

## Future Enhancements

* Allure Reporting
* API Automation Integration
* GitHub Actions CI/CD
* Parallel Execution
* cross platform 

## Author

Mukunda Shanbogh

Automation Test Engineer

Skills:

* Playwright
* Python
* Pytest
* Selenium
* REST API Testing
* Git & GitHub
* CI/CD
