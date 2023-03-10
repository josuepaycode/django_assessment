import jwt
from functools import wraps
from django.conf import settings
from rest_framework.authentication import get_authorization_header
from rest_framework import exceptions

def role_authorization(roles):
    """
    This decorator ensures that the user has 
    the required role to use the endpoint
    """
    def wrapper(view_func):
        @wraps(view_func)
        def wrapped(request, *args, **kwargs):
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

                role = payload['role']

                if not role in roles:
                    raise exceptions.AuthenticationFailed('Insufficient permissions')

            except Exception as error:
                raise exceptions.ValidationError(str(error))
            else:
                return view_func(request, *args, **kwargs)
        return wrapped
    return wrapper
