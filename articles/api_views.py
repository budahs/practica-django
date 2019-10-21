from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from articles.models import Article
from articles.serializers import ArticleListSerializer, ArticleSerializer


class ArticleViewSet(ListCreateAPIView):

    queryset = Article.objects.all()

    def get_serializer_class(self):
        return ArticleListSerializer if self.request.method == 'GET' else ArticleSerializer

class ArticleDetail(RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer