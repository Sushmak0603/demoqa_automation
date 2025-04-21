# Automation Framework (Python + Selenium + Behave)
A robust and scalable test automation framework built using Python, Selenium, and Behave (BDD).
Designed with maintainability and extensibility in mind, this framework leverages modern automation best practices and tools to ensure efficient test development and execution.

### ✨ Key Features
- **Behavior-Driven Development (BDD)** with Behave for clear and collaborative test scenarios.
- **Page Object Model (POM)** design pattern for better organization and reusability of page elements and actions.
- **Reusable Page Handlers** to abstract UI logic and reduce redundant code.
- **Dynamic XPath Handling** to avoid hard-coded selectors and improve resilience against UI changes.
- **Scalability-First Design** ensuring easy expansion with new features, tests or step definitions.


### 💡 Good to haves implemented
- **Custom Logging** for detailed test execution logs, making debugging easier.
- **Allure Reporting** for generating comprehensive and visually appealing test reports.
- **Invoke CLI Integration** to simplify and streamline test execution from the command line

---

### 🛠️ Tech Stack
- **Language:** Python 3.8+
- **Automation:** Selenium WebDriver
- **BDD:** Behave
- **Reporting:** Allure
- **CLI Task Runner:** Invoke
- **Logging:** Python's built-in `logging` module

---

## 📁 Project Structure
```
/demoqa_automation
├── features/              # Main project directory
│   ├── steps/             # Step definitions for Behave
│   │   ├── base_steps.py  # Step definitions for common functionalities
│   │   ├── book_store_steps.py  # Step definitions for Book Store tests
│   │   ├── checkbox_steps.py  # Step definitions for Checkbox tests
│   │   ├── dynamic_properties_steps.py  # Step definitions for Dynamic Properties tests
│   │   ├── forms_steps.py  # Step definitions for form related tests
│   ├── book_store.feature  # Test cases in Gherkin format for Book Store
│   ├── checkbox.feature    # Test cases in Gherkin format for Checkbox
│   ├── dynamic_properties.feature  # Test cases in Gherkin format for Dynamic Properties
│   ├── forms.feature       # Test cases in Gherkin format for Forms
│   ├── environment.py   # Consists of hooks for Behave
├── pages  # Page Object Model (POM) implementation
│   ├── base_page.py        # Common methods for all pages
│   ├── book_store_page.py  # Page class for Book Store related locator variables and methods
│   ├── checkbox_page.py    # Page class for Checkbox related locator variables and methods
│   ├── dynamic_properties_page.py    # Page class for Dynamic Properties related locator variables and methods
│   ├── forms_page.py    # Page class for Forms related locator variables and methods
├── utils   # Utility modules and helper functions
│   ├── logger.py           # Custom logging utility
│   ├── page_manager.py     # Page manager to handle page object instantiation
├── logs   # Captures and stores logs
│   ├── run.log  # Captures test execution logs
├── reports   # Folder to capture allure report related details
│   ├── allure-results/  # Allure results folder
│   ├── allure-report/   # Allure report folder
├── requirements.txt  # List of dependencies
├── tasks.py  # Invoke tasks for running tests
├── README.md          # Project documentation

```

---

## ⚙️ Pre-requisites
### ✅ Python Installation
Check if **Python 3.8+** is installed. Verify python version by executing:
```bash
python --version
```

### ✅ Install any editor like PyCharm
Download link for PyCharm: https://www.jetbrains.com/pycharm/download/?section=windows

---

## 🔧 Set up steps
### 1️⃣ Set up the Python Interpreter in the editor
### 2️⃣ Create virtual environment to install packages
### 3️⃣ Install required packages
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```

---

## ▶️ Execution steps
For the ease of execution, python Invoke is used to run the tests.
Navigate to project directory:
```bash
cd demoqa_automation
```
### 🔁 To run all tests
```bash
invoke run-tests
```

### 📄To run specific feature file
```bash
invoke run-tests --features="features/book_store.feature"
invoke run-tests --features="features/checkbox.feature"
invoke run-tests --features="features/dynamic_properties.feature"
invoke run-tests --features="features/forms.feature"
```


### 📊 To create allure report
```bash
invoke report
```

---

---
