from .views import user_register_view,user_update_view
# from .views import user_register_view
from django.urls import path

urlpatterns = [
    path("register/", user_register_view, name='register'),
    path("update/", user_update_view, name='update'),
]
