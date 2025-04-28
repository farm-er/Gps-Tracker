
from django.http import JsonResponse
from django.conf import settings
import jwt  # If you're using JWT for authentication



# middle for drivers and managers authentification

# this middleware is not used at the moment 
# we're using the default middleware

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # You can get the token from headers or cookies
        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({'error': 'Authentication token is missing'}, status=401)

        try:

            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            request.user = decoded_token  # Store the decoded user info in the request
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        return self.get_response(request)