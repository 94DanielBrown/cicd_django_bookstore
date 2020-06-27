pipeline {
  agent any
  stages {
    stage("Git Checkout"){
      steps{
        git credentialsId: 'gitlab', url: 'https://gitlab.com/danielbrown-examples/djangobooks_cicd'
      }
    }


  }
}
