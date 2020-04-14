from .services import get_news
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import NewSerializer


class NewsList(views.APIView):

    def get(self, request):
        data = get_news()
        results = NewSerializer(data, many=True).data
        return Response(results)
