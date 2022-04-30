pipeline {

  agent any

  stages {

    stage('Checkout Source') {
      steps {
        git url:'https://github.com/vamsijakkula/hellowhale.git', branch:'master'
      }
    }
    
      stage("Build image") {
            steps {
                script {
                    myapp = docker.build("vamsijakkula/hellowhale:${env.BUILD_ID}")
                }
            }
        }
    
      stage("Push image") {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                            myapp.push("latest")
                            myapp.push("${env.BUILD_ID}")
                    }
                }
            }
        }

    
    stage('Deploy App') {
      steps {
        script {
          kubernetesDeploy(configs: "hellowhale.yml", kubeconfigId: "mykubeconfig")
        }
      }
    }

  }

}
