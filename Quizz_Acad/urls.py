from django.contrib import admin
from django.urls import path
from app.quizz.views import index
from app.accounts.views import signup
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', index, name='index'),
    path('admin/', admin.site.urls),
    path('', signup, name="signup"),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
