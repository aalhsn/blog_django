from rest_framework import serializers
from .models import Article, Genre


class ArticlesListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = ['title', 'author', 'img', 'food_type']
    
    def get_author(self, obj):
		    return (obj.author.name)