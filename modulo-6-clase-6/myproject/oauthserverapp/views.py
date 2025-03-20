from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class SecretMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Este es un recurso protegido"})
