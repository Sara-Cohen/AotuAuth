from service_factory import ServiceFactory

class ServiceRequest:
    def __init__(self, service_name, user_id, access_id, access_type=None):
        self.service_name = service_name
        self.user_id = user_id
        self.access_id = access_id
        self.access_type = access_type

def main():
    # Example list from the front end
    requests = [
        ServiceRequest("AWS", "sara cohen", "myRepository", "admin"),
        ServiceRequest("GitHub", "Tehila-987983Tg", "standard"),
        ServiceRequest("Gcloud", "3456789085", "87384674", "read, write")
    ]

    # Process each request
    for request in requests:
        service = ServiceFactory.create_service(request.service_name)
        if service:
            service.apply_permission(request.user_id, request.access_id, request.access_type)
            print(f"Permission applied for {service.get_name()}")
        else:
            print(f"Unknown service: {request.service_name}")

    # Update permission example
    update_request = ServiceRequest("AWS", "sara cohen", "myRepository", "read-only")
    service = ServiceFactory.create_service(update_request.service_name)
    if service:
        service.update_permission(update_request.user_id, update_request.access_id, update_request.access_type)
        print(f"Permission updated for {service.get_name()}")

    # Remove permission example
    remove_request = ServiceRequest("AWS", "sara cohen", "myRepository")
    service = ServiceFactory.create_service(remove_request.service_name)
    if service:
        service.remove_permission(remove_request.user_id, remove_request.access_id)
        print(f"Permission removed for {service.get_name()}")

if __name__ == "__main__":
    main()
