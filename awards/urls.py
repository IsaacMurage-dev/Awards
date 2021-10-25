from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/$', views.project, name='project'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/profile/edit/$', views.edit, name='edit'),
    url(r'^user/(?P<user_id>\d+)$', views.user, name='aboutuser'),
    url(r'^project/(\d+)$', views.single_project, name='project'),
    url(r'^rating/(\d+)$', views.review_rating, name="review"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
