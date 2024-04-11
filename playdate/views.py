from django.http import Http404
from rest_framework import status
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

class PlaydateListDetail(APIView):
    serializer_class = PlaydateSerializer
    
    def get_object(self, pk):
        try:
            playdate = Playdate.objects.get(pk=pk)
            return playdate
        except Playdate.DoesNotExist:
            raise Http404
    
    def get(self,request, pk):
        playdate = self.get_object(pk)
        serializer = PlaydateSerializer(playdate)
        return Response(serializer.data)
    
    def put(self, request, pk):
        playdate = self.get_object(pk)
        serializer = PlaydateSerializer(playdate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)