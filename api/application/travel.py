from api.application.base import BaseApp, BaseError
from api.models import Travel


class TravelApp(BaseApp):

    def all(self):
        return Travel.objects.values()

    def one(self, id):
        return Travel.objects.filter(id=id).values().first()

    def create(self, travel_def):
        try:
            travel = Travel(**travel_def)
            travel.save()
            return travel
        except Exception as e:
            raise BaseError(e)
