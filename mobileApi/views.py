import json

from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import generics
from rest_framework.filters import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_social_oauth2.oauth2_backends import KeepRequestCore
from rest_framework_social_oauth2.oauth2_endpoints import SocialTokenServer
from mobileApi.models import *
from mobileApi.serializers import *
from datetime import *
from django.db.models import Avg
from punctArtDjango.permissions import IsOwnerOrReadOnly
from oauth2_provider.models import AccessToken, Application
from braces.views import CsrfExemptMixin
from oauth2_provider.views.mixins import OAuthLibMixin
from oauth2_provider.settings import oauth2_settings
from models import User
from oauth2_provider.views import TokenView
from rest_framework_social_oauth2.views import ConvertTokenView
from social_django.models import UserSocialAuth


class ConvertTokenViewCustom(ConvertTokenView):
    def post(self, request, *args, **kwargs):
        request._request.POST = request._request.POST.copy()
        for key, value in request.data.items():
            request._request.POST[key] = value

        url, headers, body, status = self.create_token_response(request._request)
        response = Response(data=json.loads(body), status=status)

        for k, v in headers.items():
            response[k] = v
        try:
            user = AccessToken.objects.get(token=response.data['access_token']).user
            response.data['user'] = UserSerializer(user).data
            del response.data['refresh_token']
            del response.data['scope']
            del response.data['token_type']
            del response.data['expires_in']
        except Exception as e:
            return response

        return response


class PlayListView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = Play.objects.all()
    serializer_class = PlaySerializer
    filter_fields = '__all__'

    def get(self, request,  *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Play_RepresentationListView(mixins.ListModelMixin, generics.GenericAPIView):

    #model = Play_Representation
    serializer_class = Play_RepresentationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('play__category', 'theater', 'theater__city')
    search_fields = ('play__name', 'play__category__name', 'theater__name', 'actors__first_name', 'actors__last_name', 'theater__city')
    ordering_fields = ('date', 'rating')
    ordering = ('date',)

    def get_queryset(self):
        return Play_Representation.objects.annotate(rating=Avg('play__ratings__rating_number')).filter(date__gte=datetime.now())

    def get(self, request,  *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoriesListView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = '__all__'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TheatersListView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
    filter_fields = '__all__'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FavoritesView(mixins.ListModelMixin, generics.GenericAPIView):

    serializer_class = PlaySerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        user = self.request.user
        return Play.objects.filter(favorites__user=user.id, favorites__is_favorite=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CityView(APIView):

    #queryset = Theater.objects.all()
    #serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        cities = [theater.city for theater in Theater.objects.all()]
        return Response(cities)


class PlayView(mixins.RetrieveModelMixin, generics.GenericAPIView):

    queryset = Play.objects.all()
    serializer_class = PlaySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CommentView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RatingView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FavoriteView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

