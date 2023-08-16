from django.urls import path

from apps.second_assignment.views import CompanyCommentRetrieveAPIView, CompanyProductRetrieveAPIView

urlpatterns = [
    path('company/<int:pk>/comments/', CompanyCommentRetrieveAPIView.as_view(), name='com-comments-detail'),
    path('company/<int:pk>/products/', CompanyProductRetrieveAPIView.as_view(), name='com-products-detail')
]
