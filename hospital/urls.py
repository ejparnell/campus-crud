from django.urls import path
from .views import DoctorDetailView, DoctorsView

urlpatterns = [ 
    path('', DoctorsView.as_view(), name='docs'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doc')
]