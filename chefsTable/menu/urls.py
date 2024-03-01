from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    
    
    
    
    
    
    path('menu/', views.menu, name='menu'),
    path('booking/', views.tableBooking,  name="booking"),
    path('book/', views.book_table, name='book')
]
if settings.DEBUG: # only add the following code if DEBUG mode is on
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)