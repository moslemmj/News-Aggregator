from .services import get_news, search_news
from rest_framework import views
from rest_framework.response import Response
from .serializers import NewSerializer


class NewsList(views.APIView):

    def get(self, request):
        data = get_news()
        results = NewSerializer(data, many=True).data
        return Response(results)


class NewsSearch(views.APIView):

    def get(self, request):
        if self.request.method == 'GET':
            query = self.request.GET.get('query', None)
            data = search_news(query)
            results = NewSerializer(data, many=True).data
            return Response(results)
