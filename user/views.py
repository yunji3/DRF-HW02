from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from django.contrib.auth import login, logout, authenticate

from user.serializers import UserProfileSerializer, UserSerializer, UserSignupSerializer


class UserView(APIView):  # CBV 방식
    # permission_classes = [permissions.AllowAny]  # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated]  # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '가입이 완료되었습니다.'})
        else:
            print(serializer.errors)
            return Response({'message': '가입이 실패했습니다.'})

    # def put(self, request):
    #     return Response({'message': 'put method!!'})

    # def delete(self, request):
    #     return Response({'message': 'delete method!!'})


class UserApiView(APIView):
    # permission_classes = [permissions.AllowAny]

    # def get(self.request):
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "로그인 성공!!"})

    def delete(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공!!"})
