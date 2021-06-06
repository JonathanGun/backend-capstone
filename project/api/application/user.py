from api.application.base import BaseApp
from api.models import User

class UserApp(BaseApp):
    
    def get_user(self):
        return User.objects.filter(google_id=self.google_id).values().first()

