from rest_framework.views import APIView
from rest_framework.response import Response

class BaseView(APIView):
    required_post_fields = set()
    
    def validate(self, request, format=None):
        for fields in required_post_field:
            if not request.data.get(fields):
                res = {
                    "code":400,
                    "message": f"{fields} is required"
                }
                return Response(res,400)
        