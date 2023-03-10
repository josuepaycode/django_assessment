import jwt
from django.conf import settings
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from authentication.models import Administrator

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(' ')

        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed('Token not valid')

        token = auth_token[1]

        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms='HS256'
            )

            username = payload['email']
            user = Administrator.objects.get(username=username)
            return (user, token)

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token is expired')
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Token is invalid')
        except Administrator.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')

        return super().authenticate(request)
