from django.conf import settings
from django.urls import path
from .views import home,sign_up,sign_in,error_page
from django.conf.urls.static import static

urlpatterns = [
    
    path('',home,name='site_home'),
    path('register/',sign_up,name='sign_up'),
    path('login/',sign_in,name='sign_in'),
    path('404/',error_page)
    
]    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
