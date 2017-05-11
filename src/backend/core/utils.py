from rest_social_auth.serializers import UserJWTSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return UserJWTSerializer(user).data
