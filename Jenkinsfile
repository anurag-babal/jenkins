pipeline {
  agent any
  stages {
    stage('Clone git') {
      steps {
        git 'https://github.com/anurag-babal/jenkins.git'
      }
    }
    stage('Build') {
      steps {
        sh "chmod u+x sum.py"
        sh "./sum.py"
      }
    }
    stage('Test') {
      steps {
        python3 test.py
      }
    }
  }
}
