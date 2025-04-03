from django.urls import path

from api import views

urlpatterns = [
    path('user_info/', views.UserInfoView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('travel/', views.TravelView.as_view()),
    path('travel/<int:id>', views.TravelDetailView.as_view()),
    path('travel/<int:id>/picture', views.TravelPictureView.as_view()),
    path('travel_log/', views.TravelLogView.as_view()),
    path('travel_log/<int:id>', views.TravelLogDetailView.as_view()),
]
