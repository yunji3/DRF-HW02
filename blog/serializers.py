from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Article, Comment, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_name"]


class CommentSerializer(serializers.ModelSerializer):
   class Meta:
      model = Comment
      fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, source = 'comment_set')

    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = Article
        fields = ['category', 'title', 'contents', 'comments']