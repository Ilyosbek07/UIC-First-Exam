from django.urls import path

from apps.jobhunt.views import StatisticsAPIView

urlpatterns = [
    path('statistics/', StatisticsAPIView.as_view(), name='statistics')
]
