pipeline {
   agent any
   stages {
       stage('Clean') {
           steps {
               echo 'Cleaning..'
               sh 'mvn clean'
           }
       }
       stage('Test') {
           steps {
               echo 'Testing..'
               sh 'mvn test'
           }
       }
       stage('Package') {
           steps {
               echo 'Deploying....'
               sh 'mvn package'
           }
       }
       stage('Deploy'){
          steps {
             echo 'Deploy..'
             }
       }
   }
}
