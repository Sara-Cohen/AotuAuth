from service import Service

class AWSService(Service):
    def apply_permission(self, user_id, access_id, access_type):
        # Implementation for applying permission in AWS
        pass

    def update_permission(self, user_id, access_id, access_type):
        # Implementation for updating permission in AWS
        pass

    def remove_permission(self, user_id, access_id):
        # Implementation for removing permission in AWS
        pass

    def get_name(self):
        return "AWS"
