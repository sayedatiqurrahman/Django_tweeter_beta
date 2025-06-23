
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

# for auth handling
# from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('tweet.urls'), name='tweet_main_root_url'),
    path("tweet/", include('tweet.urls'), name='tweet_main_root_url'),

    # auth urls at root urls.py (compulsory)
    path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
