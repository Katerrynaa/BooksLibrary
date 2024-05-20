from rest_framework import serializers
from .models import Books, Genre
from rest_framework.validators import UniqueTogetherValidator



class BaseBookSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())

    class Meta:
        model = Books 
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['genre'] = instance.genre.name
        return representation


class BooksSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta):
        validators = [
            UniqueTogetherValidator(
                queryset=Books.objects.all(),
                fields=['author', 'title', 'year', 'country']
            )
        ]

class RatingSerializer(BaseBookSerializer):
    rating = serializers.StringRelatedField(many=True)

    class Meta(BaseBookSerializer.Meta):
        fields = ['author', 'title', 'year', 'country', 'genre', 'rating']


class PriceSerializer(BaseBookSerializer):
    price = serializers.StringRelatedField()

    class Meta(BaseBookSerializer.Meta):
        fields = ['author', 'title', 'year', 'country', 'genre', 'rating', 'price']


class WeeklySerializer(BaseBookSerializer):
    announcement = serializers.StringRelatedField()

    class Meta(BaseBookSerializer.Meta):
        fields = ['author', 'title', 'year', 'country', 'genre', 'rating', 'price', 'announcement']