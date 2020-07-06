pipeline {
    agent any
    environment {
        ECR_REPO='403053754364.dkr.ecr.us-east-1.amazonaws.com/djangobooks-cicd'
        DEBUG=0
        ENV='production'
    }
    stages {
      stage('Git Checkout'){
        steps{
          git([ branch: 'master', credentialsId: 'gitlabcreds', url: 'https://gitlab.com/danielbrown-examples/djangobooks_cicd'])
        }
      }
      stage('Run pytest'){
        steps{
          sh 'pipenv install --dev'
          sh '/usr/local/bin/docker-compose up -d --build'
          sh 'sleep 30'
          sh 'pipenv run pytest'
        }
      }
     stage("Push docker image"){
         steps{
             sh 'docker tag "cicd_test" ${ECR_REPO}'
             withAWS(credentials: 'aws_credentials', region: 'us-east-1'){
                 sh '$(aws ecr get-login --no-include-email)'
                 sh 'docker push ${ECR_REPO}'
             }
         }
     }
    stage("Deploy to Testing Environment"){
        steps{
           sh 'echo "Deploy to ecs"' 
        }
    }
    stage("Deploy to production"){
        steps{
            sh 'echo "Deploy with kubernetes"'
        }
    }
         
    }// End of Stages   
}//End of pipeline
