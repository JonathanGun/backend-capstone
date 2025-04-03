import logging

import os
from django.http.response import HttpResponse
import jwt
import json
from datetime import datetime, timedelta

from google.oauth2 import id_token
from google.auth.transport import requests

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator

from api.application.base import BaseError
from api.application.user import UserApp
from api.application.travel import TravelApp
from api.application.picture import PictureApp
from api.application.travel_log import TravelLogApp
from api.utils import create_or_save
from api.serializers import (
    TravelSerializer,
    UserSerializer,
    TravelLogSerializer,
    PictureSerializer,
)

logger = logging.getLogger()


class ProtectedView(View):
    decorators = []

    @method_decorator(decorators)
    def dispatch(self, request, *args, **kwargs):
        self.session = request.session
        token = request.META.get("HTTP_KYUJITSU_TOKEN")
        jwt_decode = jwt.decode(token, os.environ.get("JWT_SECRET"), algorithm="HS256")
        if jwt_decode["exp"] < datetime.now().timestamp():
            return JsonResponse({"success": False, "msg": "token expired"})
        self.user = jwt_decode["user"]
        self.google_id = self.user["google_id"]
        if request.body:
            self.payload = json.loads(request.body)
        return super().dispatch(request, self.session, *args, **kwargs)


class LoginView(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        token = request.META.get("HTTP_OAUTH_TOKEN")
        idinfo = None
        try:
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), os.environ.get("CLIENT_ID")
            )
        except ValueError:
            return HttpResponse(status=400)
        user_def = {
            "google_id": idinfo["sub"],
            "username": idinfo["given_name"],
            "fullname": idinfo["given_name"],
            "picture": idinfo["picture"],
            "company": idinfo["hd"],
            "email": idinfo["email"],
        }
        data = {"user": user_def, "exp": datetime.now() + timedelta(hours=24)}
        encoded_jwt = jwt.encode(
            payload=data, key=os.environ.get("JWT_SECRET"), algorithm="HS256"
        )
        encoded_jwt = encoded_jwt.decode("utf-8")

        create_or_save(user_def)
        request.session["token"] = encoded_jwt
        return JsonResponse(
            {
                "token": encoded_jwt,
                "user": user_def,
            }
        )


class UserInfoView(ProtectedView):
    def get(self, request, session):
        return JsonResponse(self.user)


class TravelView(ProtectedView):
    def get(self, request, session):
        try:
            travel_app = TravelApp(self.google_id)
            travel_data = travel_app.all()
            return JsonResponse(
                {
                    "success": True,
                    "data": TravelSerializer(travel_data, many=True).data,
                },
                safe=False,
            )
        except Exception as e:
            logger.error(e)
            return JsonResponse(
                {
                    "success": False,
                    "msg": str(e),
                }
            )

    def post(self, request, session):
        try:
            travel_app = TravelApp(self.google_id)
            new_travel = travel_app.create(self.payload)

            return JsonResponse(
                {
                    "success": True,
                    "data": TravelSerializer(new_travel).data,
                }
            )
        except Exception as e:
            logger.error(e)
            return JsonResponse(
                {
                    "success": False,
                    "msg": str(e),
                }
            )


class TravelDetailView(ProtectedView):
    def get(self, request, session, id):
        try:
            travel_app = TravelApp(self.google_id)
            travel_detail = travel_app.one(id)
            return JsonResponse(
                {
                    "success": True,
                    "data": TravelSerializer(travel_detail).data,
                },
                safe=False,
            )
        except Exception as e:
            logger.error(e)
            return JsonResponse(
                {
                    "success": False,
                    "msg": str(e),
                }
            )

    def post(self, request, session, id):
        travel_app = TravelApp(self.google_id)
        travel_detail = travel_app.one(id)
        travel_log_def = {
            "user_id": self.google_id,
        }
        for k, v in travel_detail.items():
            if k in ["id", "created_at", "updated_at"]:
                continue
            travel_log_def["travel_" + k] = v
        travel_log_app = TravelLogApp(self.google_id)
        new_travel_log = travel_log_app.create(travel_log_def)
        return JsonResponse(
            {
                "success": True,
                "data": TravelLogSerializer(new_travel_log).data,
            }
        )


class TravelPictureView(ProtectedView):
    def post(self, request, session, id):
        try:
            picture_app = PictureApp(self.google_id)
            new_picture = picture_app.create(
                {
                    "url": self.payload["url"],
                    "travel_id": id,
                }
            )

            return JsonResponse(
                {
                    "success": True,
                    "data": PictureSerializer(new_picture).data,
                }
            )
        except Exception as e:
            logger.error(e)
            return JsonResponse(
                {
                    "success": False,
                    "msg": str(e),
                }
            )


class TravelLogView(ProtectedView):
    def get(self, request, session):
        try:
            travel_log_app = TravelLogApp(self.google_id)
            travel_logs = travel_log_app.all()
            return JsonResponse(
                {
                    "success": True,
                    "data": TravelLogSerializer(travel_logs, many=True).data,
                }
            )
        except Exception as e:
            logger.error(e)
            return JsonResponse(
                {
                    "success": False,
                    "msg": str(e),
                }
            )


class TravelLogDetailView(ProtectedView):
    def get(self, request, session, id):
        try:
            travel_log_app = TravelLogApp(self.google_id)
            travel_log = travel_log_app.one(id)
            return JsonResponse(
                {
                    "success": True,
                    "msg": TravelLogSerializer(travel_log).data,
                }
            )
        except Exception as e:
            logger.error(e)
            return JsonResponse(
                {
                    "success": False,
                    "msg": str(e),
                }
            )
