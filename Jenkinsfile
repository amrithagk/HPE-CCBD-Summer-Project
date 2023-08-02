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
                    bat "start /B ${allureCommand} serve ${reportPath}"
                }
            }
        }
    }
}
