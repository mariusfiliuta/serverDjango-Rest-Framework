from mobileApi.models import *
from rest_framework import serializers
from django.db import models


class UserSerializer(serializers.ModelSerializer):
    #comments = CommentSerializer(many=True, read_only=False)
    #ratings = RatingSerializer(many=True, read_only=False)
    profile = serializers.SlugRelatedField(many=False, read_only=True, slug_field='profile_picture')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'profile')#, 'comments', 'ratings')


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Rating
        fields = ('id', 'rating_number', 'user', 'play')


class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Favorite
        fields = ('id', 'is_favorite', 'user', 'play')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'comment_text', 'created', 'user', 'play')


class TheaterSerializer(serializers.ModelSerializer):
    #play_representations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Theater
        fields = ('id', 'name', 'latitude', 'longitude', 'city')


class CategorySerializer(serializers.ModelSerializer):
    plays = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'plays')


class PlaySerializer(serializers.ModelSerializer):
    #play_representations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=False)
    category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    rating = serializers.SerializerMethodField('rating_method')
    #rating = serializers.FloatField(read_only=True)
    auth_user_favorite = serializers.SerializerMethodField('auth_user_favorite_method')
    auth_user_rating = serializers.SerializerMethodField('auth_user_rating_method')

    def auth_user_favorite_method(self, play):
        user = self.context['request'].user
        favorite = Favorite.objects.filter(user=user.id, play=play.id)

        if favorite.__len__() != 0:
            return FavoriteSerializer(favorite[0]).data
        else:
            return None

    def auth_user_rating_method(self, play):
        user = self.context['request'].user
        rating = Rating.objects.filter(user=user.id, play=play.id)

        if rating.__len__() != 0:
            return RatingSerializer(rating[0]).data
        else:
            return None

    def rating_method(self, play):
        sum = 0.0
        for rating in play.ratings.all():
            sum += rating.rating_number
        if len(play.ratings.all()) > 0:
            return sum/len(play.ratings.all())
        else:
            return 0.0

    class Meta:
        model = Play
        fields = ('id', 'name', 'description', 'image_paths', 'category', 'comments', 'rating', 'trailer_link',
                  'auth_user_favorite', 'auth_user_rating')

class ActorSerializer(serializers.ModelSerializer):
    #play_representations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'first_name', 'last_name', 'profile_picture', 'description')

class Play_RepresentationSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    theater = TheaterSerializer(many=False, read_only=False)
    play = PlaySerializer(many=False, read_only=False)

    class Meta:
        model = Play_Representation
        fields = ('id', 'date', 'theater', 'play', 'actors')


class CitySerializer(serializers.BaseSerializer):

    class Meta:
        model = Theater
        fields = ('city',)