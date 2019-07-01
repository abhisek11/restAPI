
from django.contrib import admin
from django.urls import path
from updates.views import *






urlpatterns = [
    path('admin/', admin.site.urls),
    path('json/cbv/',JsonCBV.as_view()),
    path('json/cbv2/',JsonCBV2.as_view()),
    path('json/serialized/list/',SerilizedListView.as_view()),
    path('update_view/',update_model_detail_view),
]
