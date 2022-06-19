from dataclasses import field
from blog.models import Category as CategoryModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

from blog.serizlizers import ArticleSerializer


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(sefl, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(sefl, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    artielcs = ArticleSerializer(many=True, source="article_set")
    comments = CommentSerializer(many=True, source="comment_set")

    class Meta:
        model = UserModel
        fields = ["username", "fullname", "email",
                  "join_data", "userprofile", "articles" "comments"]
