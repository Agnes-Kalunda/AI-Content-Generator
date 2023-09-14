from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.home, name='home'),
    path('about-aggie-ai', views.about, name='about'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name="profile"),
    path('generate-blog-topic',views.blogTopic, name='blog-topic'),
    path('generate-blog-sections ', views.blogSections, name='blog-sections'),
    path('save-blog-topic', views.saveBlogTopic, name="save-blog-topic"),
    path('use-blog-topic', views.useBlogTopic, name="use-blog-topic"),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)