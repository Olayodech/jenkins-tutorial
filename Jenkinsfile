pipeline{
    environment
    {
        registry = "olayodech/flask-app"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
        HOME = "${env.WORKSPACE}"
        git_token = "github_accesses"
    }
   
    agent any 
        stages{
            stage ('Check out')
            {
                steps{
                    git branch: 'main', credentialsId: 'github_accesses', url: 'https://github.com/Olayodech/jenkins-tutorial'                   
                     // sh 'git clone https://olayodech:github.com/Olayodech/jenkins-tutorial.git'
                    sh 'git checkout main'
                }
            }
            stage ('Testing')
            {
                steps{
                    sh 'pip3 install -r requirements.txt'
                    // sh 'pytest-3 --junitxml results.xml'
                }
            }
            stage ('Building Docker Image')
            {
                steps{
                    script{
                        docker.withRegistry(registryCredential){
                            dockerImage=docker.build(registry)
                            // docker.buid
                        }
                    }
                }
            }
            stage ('Push Image To Docker Hub')
            {
                steps{
                    script{
                        docker.withRegistry('', registryCredential){
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