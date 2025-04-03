from api.application.base import BaseApp, BaseError
from api.models import TravelLog

class TravelLogApp(BaseApp):
    
    def all(self):
        return TravelLog.objects.filter(user_id=self.google_id).values()
    
    def one(self, id):
        return TravelLog.objects.filter(id=id).values().first()
    
    def create(self, travel_log_def):
        try:
            travel_log = TravelLog(**travel_log_def)
            travel_log.save()
            return travel_log
        except Exception as e:
            raise BaseError(e)

