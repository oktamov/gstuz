from django.urls import path

from .views import CategoryView, FormCreateView, CompanyRetrieveView, DocumentCustomFilterView, SendVerificationCodeView

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('documents/', DocumentCustomFilterView.as_view(), name='document-list'),
    path('forms/create/', FormCreateView.as_view(), name='form-create'),
    path('company/', CompanyRetrieveView.as_view(), name='company-detail'),
    path('send/code/', SendVerificationCodeView.as_view(), name='send-code'),

]
