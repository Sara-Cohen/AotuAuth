from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def apply_permission(self, user_id, access_id, access_type):
        pass

    @abstractmethod
    def update_permission(self, user_id, access_id, access_type):
        pass

    @abstractmethod
    def remove_permission(self, user_id, access_id):
        pass

    @abstractmethod
    def get_name(self):
        pass
