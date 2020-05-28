from django.contrib import admin
from django.urls import path,include
import get_random_quote
from . import views, settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from get_random_quote import views as random_views
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('random/',random_views.get_random_quote,name="random"),
    path('',views.index,name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

 