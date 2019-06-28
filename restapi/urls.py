
from django.contrib import admin
from django.urls import path
from updates.views import *






urlpatterns = [
    path('admin/', admin.site.urls),
    path('update_view/',update_model_detail_view)
]
