pipeline{
    environment{
        registry="olayodech/flask-app"
        registryCredential='docker hub'
        dockerImage=""
        HOME="${env.WORKSPACE}"
    }
   
    agent any 
        stages{
            stage ('Check out')
            {
                steps{
                    git branch: 'main', credentialsId: 'github_access', url: 'https://github.com/Olayodech/jenkins-tutorial'
                    sh 'git clone https://github.com/Olayodech/jenkins-tutorial.git'
                    sh 'git checkout master'
                }
            }
            stage ('Testing')
            {
                steps{
                    sh 'pip install requirements.txt'
                    sh 'pytest-3 --junitxml results.xml'
                }
            }
            stage ('Building Docker Image')
            {
                steps{
                    script{
                        dockerImage=docker.build(registry)
                    }
                }
            }
            stage ('Push Image To Docker Hub')
            {
                steps{
                    script{
                        docker.withRegistry("registryCredential"){
                            dockerImage.push("${env.BUILD_NUMBER}")
                        }
                    }
                }
            }
            stage('Deploy to docker swarm')
            {
                steps{
                    sh 'uname -a'
                }
            }
            stage('Cleaning up'){
                steps{
                    sh "docker rmi $registry:$BUILD_NUMBER"
                }
            }
        }
    post {
        always {
            junit "*.xml"
        }
    }
}