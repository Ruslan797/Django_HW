from django.conf import settings
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LoginSerializer


def _set_auth_cookies(response: Response, access: str, refresh: str) -> None:
    response.set_cookie(
        settings.JWT_ACCESS_COOKIE_NAME,
        access,
        httponly=True,
        secure=getattr(settings, "JWT_COOKIE_SECURE", False),
        samesite=getattr(settings, "JWT_COOKIE_SAMESITE", "Lax"),
    )
    response.set_cookie(
        settings.JWT_REFRESH_COOKIE_NAME,
        refresh,
        httponly=True,
        secure=getattr(settings, "JWT_COOKIE_SECURE", False),
        samesite=getattr(settings, "JWT_COOKIE_SAMESITE", "Lax"),
    )


def _clear_auth_cookies(response: Response) -> None:
    response.delete_cookie(settings.JWT_ACCESS_COOKIE_NAME)
    response.delete_cookie(settings.JWT_REFRESH_COOKIE_NAME)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Пользователь зарегистрирован."}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        access = serializer.validated_data["access"]
        refresh = serializer.validated_data["refresh"]

        resp = Response({"detail": "Успешный вход."}, status=status.HTTP_200_OK)
        _set_auth_cookies(resp, access, refresh)
        return resp


class RefreshView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.COOKIES.get(settings.JWT_REFRESH_COOKIE_NAME)
        if not refresh_token:
            return Response({"detail": "Нет refresh токена в cookies."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            refresh = RefreshToken(refresh_token)
            access = str(refresh.access_token)


            if getattr(settings, "SIMPLE_JWT", {}).get("ROTATE_REFRESH_TOKENS", False):
                refresh.blacklist()
                new_refresh = str(RefreshToken.for_user(refresh.get("user_id")))

                new_refresh = str(refresh)
            else:
                new_refresh = str(refresh)
        except TokenError:
            return Response({"detail": "Refresh токен недействителен."}, status=status.HTTP_401_UNAUTHORIZED)

        resp = Response({"detail": "Access обновлён."}, status=status.HTTP_200_OK)
        _set_auth_cookies(resp, access, new_refresh)
        return resp



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.COOKIES.get(settings.JWT_REFRESH_COOKIE_NAME)

        resp = Response({"detail": "Выход выполнен."}, status=status.HTTP_200_OK)

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except TokenError:
                pass

        _clear_auth_cookies(resp)
        return resp

