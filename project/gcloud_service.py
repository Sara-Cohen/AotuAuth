from service import Service

class GcloudService(Service):
    def apply_permission(self, user_id, access_id, access_type):
        # Implementation for applying permission in Gcloud
        pass

    def update_permission(self, user_id, access_id, access_type):
        # Implementation for updating permission in Gcloud
        pass

    def remove_permission(self, user_id, access_id):
        # Implementation for removing permission in Gcloud
        pass

    def get_name(self):
        return "Gcloud"
