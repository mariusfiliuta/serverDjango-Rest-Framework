from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from mobileApi import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()

urlpatterns = [
                url(r'^admin/', include(admin.site.urls)),
                url(r'^auth/convert-token/?$', views.ConvertTokenViewCustom.as_view(), name="convert_token"),
                url(r'^auth/', include('rest_framework_social_oauth2.urls')),
                url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                url(r'^plays/$', views.PlayListView.as_view()),
                url(r'^playsRepresentations/$', views.Play_RepresentationListView.as_view()),
                url(r'^plays/(?P<pk>[0-9]+)/$', views.PlayView.as_view()),
                url(r'^categories/$', views.CategoriesListView.as_view()),
                url(r'^theaters/$', views.TheatersListView.as_view()),
                url(r'^comment/$', views.CommentView.as_view()),
                url(r'^comment/(?P<pk>[0-9]+)/$', views.CommentView.as_view()),
                url(r'^rating/$', views.RatingView.as_view()),
                url(r'^rating/(?P<pk>[0-9]+)/$', views.RatingView.as_view()),
                url(r'^cities/', views.CityView.as_view()),
                url(r'^favorite/$', views.FavoriteView.as_view()),
                url(r'^favorite/(?P<pk>[0-9]+)/$', views.FavoriteView.as_view()),
                url(r'^favorites/', views.FavoritesView.as_view())

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

