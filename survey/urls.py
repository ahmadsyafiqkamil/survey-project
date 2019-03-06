
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from account import views
# from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
    path('',include('dashboard.urls')),
    # path('dashboard/',views.dashboard, name= "dashboard"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
