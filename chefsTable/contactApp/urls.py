from django.urls import path, include
from . import views 


urlpatterns = [
    path('', views.contact_table, name='contact'),
    path('contact_info/', views.tableContacting, name="contact_info")
    
]