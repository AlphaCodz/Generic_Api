from rest_framework.views import APIView
from rest_framework.response import Response

class BaseView(APIView):
    required_post_fields = set()
    
    def post(self, request, format=None):
        for fields in self.required_post_fields:
            if not request.data.get(fields):
                res = {
                    "code":400,
                    "error": f"{fields} is required"
                }
                return Response(res,400)
        