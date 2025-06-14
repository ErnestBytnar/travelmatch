
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.users.models import TravelPriority


# Create your views here.

@api_view(['GET'])
def get_travel_priority(request):
    priorities = TravelPriority.objects.all()
    data = [{"id": p.id, "code": p.code} for p in priorities]
    return Response(data)