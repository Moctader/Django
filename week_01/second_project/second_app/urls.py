from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses),
    path('feedback/', views.feedback),
]

# from django.urls import path
# from . import views

# urlpatterns = [
    
#     path('about/', views.about),
#     path('contact/', views.contact),
  
# ]
