# HPE-CCBD-Summer-Project

### A Behaviour-Driven-Development(BDD)-based testing framework to automate the process of testing software (the example of 'www.amazon.in' has been considered) using Behave, Selenium and Allure Framework for test report generation and analysis.
### The implementation of the 'TEST' stage of a CI/CD pipeline was done on Jenkins.

### To install the required libraries
  `pip install -r requirements.txt`

### To execute the tests  
  In the feature file, under the **Examples** block, specify all the desired testcases in the same order as the parameters have been listed in the 
  **Examples** block  
  
  Then run:
  `behave -f allure_behave.formatter:AllureFormatter -o <path to reports folder> <path to feature file>`

### To view the allure reports
  `allure serve <path to  to reports folder>`

### The Jenkinsfile contains the pipeline script.
