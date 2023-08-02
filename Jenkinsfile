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
                bat '''cd "Automate add to cart"
                       cd steps
                       python3 login.py
                       python3 search.py
                       python3 reviews.py'''
            }
        }

        stage('Test') {
            environment {
                PATH = "$PATH:c:/python311/lib/site-packages/behave/executable"
            }
            steps {
                bat 'behave "Automate add to cart/amazon_addtocart.feature"'
            }
        }
    }
}
