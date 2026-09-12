# Test automation (web browsing)

![CI - Test Status](https://github.com//vans-codelab/pytest-selenium-login-test/actions/workflows/perform-testrun.yml/badge.svg)

Automated browser tests simulating user interactions, implemented with Python, pytest and Selenium.

## Table of contents

- [Project overview](#project-overview)
- [Features](#features)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Project setup](#project-setup)
- [Test run (manual trigger, local run)](#test-run-manual-trigger-local-run)
- [Test report (manual trigger, local run)](#test-report-manual-trigger-local-run)
- [CI - GitHub Actions (automatic trigger, remote run)](#ci---github-actions-automatic-trigger-remote-run)
- [License](#license)


## Project overview
This test automation project is built with Python, pytest, and Selenium. 
It automates user interactions in a browser and verifies the expected outcomes using assertions.

Over time, additional features have been added (like logging, setup/teardown logic, and CI integration with GitHub Actions) 
to reflect a more realistic test automation environment.

This project demonstrates my practical approach to test automation, with a focus on clean, readable, and maintainable test code. 
It also serves as a foundation for expanding the test suite and exploring further automation concepts.


## Features
- Automated testing of browser-based user interactions
- CI integration via GitHub Actions (Automatic test run trigger)
- Test case covers verifying successful login on a webpage
- Automated screenshots and logging during test run
- Environment variables for credentials and base URL
- Applied Object-Oriented Programming (OOP) principles
- Setup and teardown routines via `conftest.py`
- Clean folder structure
- Easy to extend and maintain


## Project structure
The project follows a simple structure that separates application code from tests:

```
project/
├───src/                # Source code
├───tests/              # Tests and related files
│   ├───logs/           # Logs (are generated during test run)
│   ├───reports/        # HTML test reports (can be generated from a command line)
│   ├───screenshots/    # Screenshots (are captured during test run)

```


## Requirements
- **Programming Language:**  
  Developed and tested with Python 3.11.  
  Download Python at: https://www.python.org/downloads/  


- **Python Packages:**  
  See [requirements.txt](requirements.txt) for all dependencies.


## Project setup

### 1. Download the project

**Option A: Clone via Git**
```bash
git clone https://github.com/vans-codelab/pytest-selenium-login-test
cd pytest-selenium-login-test 
```

**Option B: Download ZIP from GitHub**  
Download ZIP from GitHub and extract it. Then navigate to the extracted folder with the following command:
```bash
cd <path-to-extracted-project-folder>
```

### 2. Create a virtual environment and activate it
Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
macOS/Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Add environment variables (optional)
This project uses environment variables which hold the credentials (username, password) and the base URL, 
to keep sensitive data private and configuration easily replaceable.

Since this project is based on an official demo website (https://the-internet.herokuapp.com), 
the data are publicly known and therefore used as fallback values if no environment variables are provided.

**To add environment variables:**  
Rename `.env.example` to `.env` (this file already contains the required variables)


## Test run (manual trigger, local run)
This section explains how to manually trigger an automated test run, executed locally.  
For automatic execution via CI/CD, see [GitHub Actions](#ci---github-actions-automatic-trigger-remote-run).

### Option 1 (recommended): Using the terminal or command line

This option is recommended for executing the full test suite.
- Ensure that the virtual environment of the downloaded project is activated (if not already done).
     ```bash
     cd <project-folder-path>
     ```
    Windows:
    ```bash 
    .venv\Scripts\activate
    ```
    macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```

- Run the tests
  ```bash
  python -m pytest
  ```

- Or run the tests in headless mode (= without visible browser window)
  ```bash
  python -m pytest --headless
  ```

### Option 2: Using an IDE (e.g. PyCharm)
To run a single test case or for easier debugging, an IDE can be used.  

1. Open the project folder in an IDE (e.g. PyCharm).
2. Ensure that the virtual environment is selected.
3. Run individual test files using the IDE's built-in test runner.


## Test report (manual trigger, local run)
This section explains how to generate a test report after running the automated tests locally.  

HTML test reports are stored in a `reports/` folder, which is part of the project structure.
To generate a test report after the test run has been performed, execute the following command: 

```bash
python -m pytest --html=tests/reports/report.html
```

This will create a HTML report inside the `reports/` folder.  
The report provides an overview of the executed tests and their results.


## CI - GitHub Actions (automatic trigger, remote run)

Via GitHub Actions the test run is automatically triggered on every push and pull request to the `main` branch.
In addition, it is also possible to trigger the test run manually.
In both cases, the tests are run remotely on GitHub.

**Workflow:** [`.github/workflows/perform-testrun.yml`](.github/workflows/perform-testrun.yml)

**Pipeline steps:**
1. Check out code
2. Set up Python 3.11
3. Install dependencies (`requirements.txt`)
4. Set report timestamp
5. Run tests in headless mode
6. Upload HTML report, logs, and screenshots as artifacts

**To manually trigger the workflow:**
1. Go to this project on GitHub and open the the `Actions` tab
2. Select the workflow `Perform Testrun`
3. Trigger the workflow via `Run workflow`

**To view the results of the automated test run:**
1. Go to this project on GitHub and open the the `Actions` tab
2. Select the workflow `Perform Testrun`
3. Select a run
4. Download the artifacts (report, logs, screenshots)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more information.
