from django.urls import path
from . import views

urlpatterns = [
        path("", views.home, name="home"),
        path("update_webhook/", views.update_webhook, name="webhook")
    ]