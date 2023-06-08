from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Zone



class ZoneLevel(APIView):

    def post(self, request, **kwargs):
        zones = Zone.objects.all()

        for value, zone in zip(kwargs.values(), zones):
            zone.level=value
            print(zone.level)
            zone.save()
        data={"created":"success!"}
        return Response(data, status=status.HTTP_200_OK)

