from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone


class RegistedMoreThanThreeDayUser(BasePermission):
    message = "가입 후 3일 이상 지난 사용자만 사용할 수 있습니다."

    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_authenticated and
                    request.user.join_data < (timezone.now() - timedelta(dats=3)))
