from enum import unique
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    google_id = models.CharField(max_length=21, primary_key=True)
    username = models.CharField(max_length=31, null=True, blank=True)
    fullname = models.CharField(max_length=127, null=True, blank=True)
    picture = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=511, unique=True)

    class Meta:
        db_table = "user"


class Travel(BaseModel):
    name = models.CharField(max_length=127)
    boarding_datetime = models.DateTimeField(default=None, null=True, blank=True)
    departure_datetime = models.DateTimeField(default=None, null=True, blank=True)
    description = models.TextField(default=None, null=True, blank=True)
    budget = models.FloatField(default=0)
    url = models.CharField(max_length=255)

    class Meta:
        db_table = "travel"


class Picture(BaseModel):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)

    class Meta:
        db_table = "picture"


class TravelLog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    travel_name = models.CharField(max_length=127, null=True, blank=True)
    travel_boarding_datetime = models.DateTimeField(default=None, null=True, blank=True)
    travel_departure_datetime = models.DateTimeField(default=None, null=True, blank=True)
    travel_description = models.TextField(default=None, null=True, blank=True)
    travel_budget = models.FloatField(null=True, blank=True)
    travel_url = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "travel_log"
