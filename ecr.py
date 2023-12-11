# pip install awscli boto3
import boto3

region = 'us-east-1'
ecr_repo_name = 'vpro-app-image'

def create_ecr_repository():
    ecr_client = boto3.client('ecr', region_name=region)

    response = ecr_client.create_repository(repositoryName=ecr_repo_name)
    ecr_repo_uri = response['repository']['repositoryUri']
    print(f"ECR repository {ecr_repo_name} created with URI: {ecr_repo_uri}")

if __name__=='__main__':
    create_ecr_repository()

