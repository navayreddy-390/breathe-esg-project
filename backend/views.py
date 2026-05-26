from rest_framework.views import APIView
from rest_framework.response import Response

class UploadSAPView(APIView):
    def post(self, request):
        return Response({"message": "SAP file uploaded successfully"})
