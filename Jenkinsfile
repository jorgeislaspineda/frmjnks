pipeline {
    agent any
stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/jorgeislaspineda/frmjnks.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("jorgeislaspineda/frmjnks:latest")
                }
            }
        }  
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                kubernetesDeploy configs: 'deployment.yaml', kubeconfigId: 'kubeconfig-id'
            }
        }
    }
}