# Technical Evaluation for Swapcard

This repository contains a test automation that performs a Books search on Google, visits the shopping tab, applies value filters and display order filters, shows the product, and checks if the second product with a review matches the test data. It was developed in Python with Selenium Webdriver, and the report is generated with Allure Reports.

## Requirements
- Python 3.10+;
- ``pip`` - Python Index Package;
- Chrome installed;

## Setup and run automation
- Clone this repository:
  ``git clone https://github.com/tamaraferreira/sdet-automation-test.git``
- On the terminal:
  ``cd sdet-automation-test``
- Setup the virtual environment with the following commands:
  - To create virtual environment: 
      - For Windows: ``python -m venv venv``
      - For Linux/Mac: ``source venv/bin/activate``

  
  - To activate virtual environment: ``venv\Scripts\activate``
  
  
- Install dependencies: ``pip install -r requirements.txt``
- **Run tests:** ``pytest``
- Run tests in headless mode: ``pytest --headless true``
- The reports are generated after each execution. To open the reports in the browser, use teh command: ``allure open allure-report``.
