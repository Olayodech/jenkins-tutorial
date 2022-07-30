pipeline{
    environment{
        registry="olayodech/flask-app"
        registryCredential='docker hub'
        dockerImage=""
        HOME="${env.WORKSPACE}"
    }
    withCredentials([gitUsernamePassword(credentialsId: 'git_hub_token', gitToolName: 'git-tool')]) {
    }
    agent any {
        stages{
            stage ('Check out')
            {
                steps{
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

                }
            }
            stage('Cleaning up'){
                steps{
                    sh "docker rmi $registry:$BUILD_NUMBER"
                }
            }
        }
    }
    post {
        always {
            junit "*.xml"
        }
    }
}