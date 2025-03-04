from django.urls import path
from chat.views import RagAPIView

urlpatterns = [
    path("ask/", RagAPIView.as_view(), name="ask"),
]