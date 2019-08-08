pipeline {
   agent any
   environment {
         PATH = "/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/apache-maven/bin"
         M2_HOME = "/opt/apache-maven"
   }
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
		sh 'ssh root@192.168.33.11"rpm -e"'
		sh 'scp /root/calutfericit/target/rpm/unixutils-test-rpm/RPMS/noarch/unixutils-test-rpm-1.0.0-1.0.0.noarch.rpm root@192.168.33.11:/'
		sh 'ssh root@192.168.33.11"rpm -ivh"'
             }
       }
   }
}
