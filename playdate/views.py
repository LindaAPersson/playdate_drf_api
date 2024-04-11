from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Playdate
from .serializers import PlaydateSerializer

# Create your views here.

class PlaydateList(APIView):
    def get(self,request):
        playdates = Playdate.objects.all()
        serializer = PlaydateSerializer(playdates, many=True)
        return Response(serializer.data)