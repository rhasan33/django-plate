from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request: Request) -> Response:
    data = {
        'message': 'hotel booking application',
        'method': request.method
    }
    return Response(data={'message': data}, status=status.HTTP_200_OK)
