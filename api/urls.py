from django.urls import path

from api.views import ApiGetText, MyAsyncView

urlpatterns = [
    path('api/get_text/', ApiGetText.as_view()),
    path('run/docker/', MyAsyncView.as_view())
]
