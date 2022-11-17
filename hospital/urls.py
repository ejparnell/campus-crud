from django.urls import path
from .views import DoctorsView

urlpatterns = [ 
    path('', DoctorsView.as_view(), name='docs')
]