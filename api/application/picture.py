from api.application.base import BaseApp, BaseError
from api.models import Picture


class PictureApp(BaseApp):

    def all(self, id):
        return Picture.objects.filter(travel_id=id).values()

    def create(self, picture_def):
        try:
            picture = Picture(**picture_def)
            picture.save()
            return picture
        except Exception as e:
            raise BaseError(e)
