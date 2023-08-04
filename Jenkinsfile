pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', credentialsId: 'GHcreds', url: 'https://github.com/amrithagk/HPE-CCBD-Summer-Project.git'
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
                dir('Automate add to cart') {
                    bat 'behave amazon_addtocart.feature'
                }
                script {
                    def allureCommand = "allure"
                    def reportPath = "reports/"  // Assuming reports folder is directly in the sinchana branch
                    
                    // Checkout the sinchana branch
                    git branch: 'sinchana', credentialsId: 'GHcreds', url: 'https://github.com/amrithagk/HPE-CCBD-Summer-Project.git'
                    
                    // Run Allure serve in the background
                    bat "start /B cmd /c \"${allureCommand} serve ${reportPath}\""
                }
            }
        }
    }
}
