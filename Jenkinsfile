pipeline {
   environment {
     REGISTRY_ENDPOINT = "https://[IMAGE_WITH_TAG]/v2/"
     IMAGE_WITH_TAG = "[IMAGE_WITH_TAG]"
     REGISTRY_CERTS = "registry"
   }
  agent {
    node {
      label 'python'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'python setup.py test'
      }
    }
    stage('Code Quality') {
      steps {
        script {
          try{
            checkstyle canComputeNew: false, defaultEncoding: '', healthy: '', pattern: '', unHealthy: ''
          }catch(e){
            echo e
          }
        }

      }
    }
    stage('Image Build&Publish') {
      steps {
        echo 'Build Images'
        script {
          docker.withRegistry("${REGISTRY_ENDPOINT}", "${REGISTRY_CERTS}") {
            sh 'docker build -t ${IMAGE_WITH_TAG} .'
            sh 'docker push ${IMAGE_WITH_TAG}'
          }
        }

      }
    }
  }
  triggers {
    pollSCM('* * * * *')
  }
}