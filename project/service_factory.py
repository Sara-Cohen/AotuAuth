from aws_service import AWSService
from github_service import GitHubService
from gcloud_service import GcloudService

class ServiceFactory:
    @staticmethod
    def create_service(service_name):
        if service_name == "AWS":
            return AWSService()
        elif service_name == "GitHub":
            return GitHubService()
        elif service_name == "Gcloud":
            return GcloudService()
        else:
            return None
