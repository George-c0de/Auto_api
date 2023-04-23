from django.urls import path

from api.views import ApiGetText

urlpatterns = [
    path('api/send_text/', ApiGetText.as_view()),
]
