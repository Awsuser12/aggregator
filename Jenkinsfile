pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = 'AKIAUZPNLVFPGWGVS7G3'
        AWS_SECRET_ACCESS_KEY = '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'
        AWS_DEFAULT_REGION = 'eu-north-1'
        ECR_REPO = '329599658334.dkr.ecr.eu-north-1.amazonaws.com/my-app'
        CLUSTER_NAME = 'my-eks-cluster'
        IMAGE_TAG = 'latestone'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                script {
                    // Build the Docker image
                    sh 'docker build -t ${ECR_REPO}:${IMAGE_TAG} .'
                }
            }
        }

        stage('Push to ECR') {
            steps {
                echo "Pushing Docker image to AWS ECR..."
                script {
                    // Log in to Amazon ECR
                    sh '''
                    aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${ECR_REPO}
                    docker push ${ECR_REPO}:${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                echo "Deploying to EKS..."
                script {
                    // Update kubeconfig for EKS cluster
                    sh '''
                    aws eks --region ${AWS_DEFAULT_REGION} update-kubeconfig --name ${CLUSTER_NAME}
                    cp /var/jenkins_home/deployment.yaml ${WORKSPACE}/deployment.yaml
                    kubectl apply -f ${WORKSPACE}/deployment.yaml
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "Verifying deployment..."
                script {
                    // Check if the pods are running
                    sh 'kubectl get pods'
                }
            }
        }
    }
}
