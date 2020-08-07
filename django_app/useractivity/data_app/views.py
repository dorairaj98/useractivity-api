from rest_framework.response import Response
from rest_framework.views import APIView

from .models import user_data
from .serializer import user_dataserialziers

class users(APIView):
    def get(self, request):
        userlist = user_data.objects.all()
        serializer = user_dataserialziers(instance=userlist,many=True)
        return Response(serializer.data)
    def Post(self):
        pass
