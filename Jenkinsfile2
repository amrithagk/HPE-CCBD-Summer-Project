pipeline {

    agent any 
        
    stages {

        stage("CLONE") {
            steps {
                git branch: 'main',  credentialsId: 'GHcreds', url: 'https://github.com/amrithagk/HPE-CCBD-Summer-Project.git'
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
                    bat 'behave -f allure_behave.formatter:AllureFormatter -o reports7'                    
                }

                echo "TEST complete."
                echo "Opening Allure Report"

                dir('Automate add to cart') {
                    bat 'start /B cmd /c "allure serve reports7"'
                }

            }
        }

        stage("DEPLOY") {
            steps {
                echo "Initiating Deployment..."
                echo "Deployment complete."
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
