from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'name', 'author', 'description', 'updated_on')

        extra_kwargs = {
            'id': {'read_only': True},
            'updated_on': {'read_only': True}
        }
