from rest_framework import serializers
from .models import User, UserProfile, Hobby

class HobbySerializer(serializers.ModelSerializer):
   same_hobby_people = serializers.SerializerMethodField()
   # obj : hobby 객체
   def get_same_hobby_people(self, obj):
      user = self.context.get('user')
      userprofiles = obj.userprofile_set.exclude(user=user)
      # userprofiles = obj.userprofile_set.all()
      name_list = [ userprofile.user.username for userprofile in userprofiles ]
      return name_list

   class Meta:
      model = Hobby
      fields = ['hobby', 'same_hobby_people']

   # class Meta:
   #    model = Hobby
   #    fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
   hobby = HobbySerializer(many=True)
   class Meta:
        model = UserProfile
        fields = ['age', 'hobby']

class UserSerializer(serializers.ModelSerializer):
   userprofile = UserProfileSerializer()
   class Meta:
        # serializer에 사용될 model, field지정
        model = User
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["username", "fullname", "email", "userprofile"]
# from dataclasses import field
# from blog.models import Category as CategoryModel
# from blog.models import Article as ArticleModel
# from blog.models import Comment as CommentModel
# from rest_framework import serializers
# from user.models import User as UserModel
# from user.models import UserProfile as UserProfileModel
# from user.models import Hobby as HobbyModel
#
# from blog.serizlizers import ArticleSerializer
#
#
# class UserSignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = "__all__"
#
#     def create(sefl, *args, **kwargs):
#         user = super().create(*args, **kwargs)
#         p = user.password
#         user.set_password(p)
#         user.save()
#         return user
#
#     def update(sefl, *args, **kwargs):
#         user = super().update(*args, **kwargs)
#         p = user.password
#         user.set_password(p)
#         user.save()
#         return user
#
#
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfileModel
#         fields = ["introduction", "birthday", "age"]
#
#
# class UserSerializer(serializers.ModelSerializer):
#     userprofile = UserProfileSerializer()
#     artielcs = ArticleSerializer(many=True, source="article_set")
#     comments = CommentSerializer(many=True, source="comment_set")
#
#     class Meta:
#         model = UserModel
#         fields = ["username", "fullname", "email",
#                   "join_data", "userprofile", "articles" "comments"]
