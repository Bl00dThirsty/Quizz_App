from django.contrib import admin
from django.urls import path
from app.quizz.views import index
from app.accounts.views import signup


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
]
