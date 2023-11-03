from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def home(request):
    data = {
        "urls": {
            "": reverse("home", request=request),
            # Add more URLs here for your views and endpoints
        }
    }
    return Response(data)