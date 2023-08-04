pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', credentialsId: 'amazon_automation', url: 'https://github.com/amrithagk/HPE-CCBD-Summer-Project.git'
            }
        }

        stage('Build') {
            steps {
                echo "BUILDING.."
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                bat '''cd "Automate add to cart"
                       cd steps
                       python login.py
                       python product_search.py
                       python reviews.py'''
            }
        }

        stage('Test') {
            steps {
                echo "Running allure report in the background"
                script {
                    def allureCommand = "allure"
                    def reportPath = "Automate add to cart/reports5/"

                    // Change the working directory to the correct path
                    def workingDirectory = "Automate add to cart"

                    // Checkout the sinchana branch
                    git branch: 'sinchana', credentialsId: 'amazon_automation', url: 'https://github.com/amrithagk/HPE-CCBD-Summer-Project.git'

                    // Run Allure serve in the background
                    bat "start /B cmd /c \"cd ${workingDirectory} && ${allureCommand} serve ${reportPath}\""
                }
            }
        }
    }
}
