from .services import get_news, search_news
from rest_framework import views, permissions
from rest_framework.response import Response
from .serializers import NewSerializer


class NewsList(views.APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        data = get_news()
        results = NewSerializer(data, many=True).data
        return Response(results)


class NewsSearch(views.APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        if self.request.method == 'GET':
            query = self.request.GET.get('query', None)
            print("######"+query)
            data = search_news(query)
            results = NewSerializer(data, many=True).data
            return Response(results)
