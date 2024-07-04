from service import Service

class GitHubService(Service):
    def apply_permission(self, user_id, access_id, access_type):
        # Implementation for applying permission in GitHub
        pass

    def update_permission(self, user_id, access_id, access_type):
        # Implementation for updating permission in GitHub
        pass

    def remove_permission(self, user_id, access_id):
        # Implementation for removing permission in GitHub
        pass

    def get_name(self):
        return "GitHub"
