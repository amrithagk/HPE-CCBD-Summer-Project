# HPE-CCBD-Summer-Project

### A Behaviour-Driven-Development(BDD)-based testing framework to automate the process of testing software (the example of 'www.amazon.in' has been considered) using Behave, Selenium and Allure for test report generation and analysis

### To install the required libraries
  `pip install -r requirements.txt`

### To execute the tests  
  `behave -f allure_behave.formatter:AllureFormatter -o \<path to reports folder\> \<path to feature file\>`

### To view the allure reports
  `allure serve \<path to  to reports folder\>`

### The JenkinsFile contains the pipeline script.
