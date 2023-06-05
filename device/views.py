from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ZoneLevel(APIView):

    def post(self, request, **kwargs):
        res = kwargs
        return Response(res)
        
