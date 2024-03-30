
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from users import views as user_views
from django.contrib.auth import views as auth_views
from students.views import ArticlesLoginView, ArticlesLogOutView, ArticlesstatisticsView,ArticlesLogOutView2
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('students/', include('students.urls')),
    path('register/', user_views.register, name='register'),
    #path('test/', user_views.test, name='test'),
    path('profile/', user_views.profile, name='profile'),
   # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', ArticlesLogOutView.as_view(), name='logout'),
    path('logout2/', ArticlesLogOutView2.as_view(), name='logout2'),
    path('login/', ArticlesLoginView.as_view(), name='login'),
    path('statistics/', ArticlesstatisticsView.as_view(), name='statistics'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
