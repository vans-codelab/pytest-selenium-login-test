# Test automation (web browsing)
Automated browser tests simulating user interactions, implemented with Selenium and Pytest.

## Table of contents

- [Project overview](#project-overview)
- [Features](#features)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Project setup](#project-setup)
- [Test run (manual trigger, local run)](#test-run-manual-trigger-local-run)
- [Test report (manual trigger, local run)](#test-report-manual-trigger-local-run)
- [CI/CD - GitHub Actions (automatic trigger, remote run)](#cicd---github-actions-automatic-trigger-remote-run)
- [License](#license)


## Project overview
This project automates user interactions in a browser, such as clicks and inputs, and verifies expected outcomes using assertions.

It is part of my personal learning journey into test automation. 
Over time, I have been improving the project by adding features like structured tests, logging, and setup/teardown logic to simulate a more realistic project environment.
As I am still learning and growing in this area, I am always open to feedback and suggestions.


## Features
- Automated testing of browser-based user interactions
- CI/CD integration via GitHub Actions (Automatically triggered test run via git push and PR)
- Test case covers verifying successful login on a webpage
- Automated screenshots and logging during test run
- Clean folder structure
- Applied Object-Oriented Programming (OOP) principles
- Setup and teardown routines via `conftest.py`
- Easy to extend and maintain


## Project structure
The project follows a simple structure that separates application code from tests:

```
project/
├───src/              -> Source code
├───tests/            -> Test case(s) and related files
│   ├───logs/         -> Logs (are generated during test run)
│   ├───reports/      -> HTML test reports (can be generated from a command line)
│   ├───screenshots/  -> Screenshots (are captured during test run)

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

## Test run (manual trigger, local run)
This section explains how to manually trigger an automated test run, executed locally.  
For automatic execution via CI/CD, see [GitHub Actions](#cicd---github-actions-automatic-trigger-remote-run).

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

- Run all test cases
  ```bash
  pytest 
  ```
- Or run all test cases in headless mode (= without visible browser window)
  ```bash
  pytest --headless
  ```

### Option 2: Using an IDE (e.g. PyCharm)
To run a single test case or for easier debugging, an IDE can be used.  

1. Open the project folder in an IDE (e.g. PyCharm).
2. Ensure that the virtual environment is selected.
3. Run individual test files using the IDE's built-in test runner.


## Test report (manual trigger, local run)
This section explains how to generate a test report when the automated test run has been triggered manually and executed locally.  

HTML test reports are stored in a `reports/` folder, which is part of the project structure.
To generate a test report after the test run has been performed, execute the following command: 

```bash
pytest --html=tests/reports/report.html
```

This will create a HTML report inside the `reports/` folder.  
The report provides an overview of the executed test case(s) and their results.


## CI/CD - GitHub Actions (automatic trigger, remote run)

Via GitHub Actions the test run is automatically triggered on every push and pull request to the `main` branch.
The test is then run remotely on GitHub.

**Workflow:** [`.github/workflows/perform-testrun.yml`](.github/workflows/perform-testrun.yml)

**Pipeline steps:**
1. Check out code & set up Python 3.11
2. Install dependencies (`requirements.txt`)
3. Set report timestamp
4. Run tests in headless mode (`pytest --headless`)
5. Upload HTML report, logs, and screenshots as artifacts

**To view the results of the automated test run:**
1. Open the `Actions` tab of this project on GitHub
2. Select a run
3. Download the artifacts (report, logs, screenshots)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more information.
