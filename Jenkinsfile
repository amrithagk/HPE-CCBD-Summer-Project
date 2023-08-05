pipeline {

    agent any 
        
    stages {

        stage("CLONE") {
            steps {
                git branch: 'sinchana',  credentialsId: '3cb433c7-91f6-4926-b54f-5688920e3ce1', url: 'https://github.com/amrithagk/HPE-CCBD-Summer-Project.git'
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

                
                bat 'behave amazon.feature -f allure_behave.formatter:AllureFormatter -o reports'

                echo "TEST complete."
                echo "Opening Allure Report"

                bat 'start /B cmd /c "allure serve reports"'
                
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
        success {
            echo "Tests passed! Deployment successful!"
        }
        failure {
            echo "Tests failed! Deployment failed!"
        }
    }
}
