pipeline {

    agent any 
        
    stages {

        stage("CLONE") {
            steps {
                git branch: 'main',  credentialsId: '3cb433c7-91f6-4926-b54f-5688920e3ce1', url: 'https://github.com/amrithagk/HPE-CCBD-Summer-Project.git'
            }
        }

        stage("BUILD") {
            steps {
                echo "Executing BUILD stage"
                echo "Running Build ${env.BUILD_ID} on ${env.JENKINS_URL}"
                echo "BUILD complete."
            }
        }

        stage("TEST") {
            steps {
                
                echo "Starting TEST stage"

                dir('Automate add to cart') {
                    bat 'behave -f allure_behave.formatter:AllureFormatter -o allure_report'                    
                }

                echo "TEST complete."
            }
        }

        stage("DEPLOY") {
            steps {
                echo "Initiating Deployment..."
                echo "Deployment completed."
            }
        }
    }

    post {
        always 
        {    
            dir ("Automate add to cart")
            {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure_report']]
                ])
            }
        }
        success {
            echo "Tests passed! Deployment successful!"
        }
        failure {
            echo "Tests failed! Deployment failed!"
        }
     }
}
