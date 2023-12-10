from django.urls import path
from . import views

# http://localhost:8000

# http://localhost:8000/result

urlpatterns = [
    path("", views.root),
    path("result/", views.result_info),
    
]

