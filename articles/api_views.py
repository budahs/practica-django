from rest_framework import viewsets
from . import models
from . import serializers


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()

    def get_serializer_class(self):
        return serializers.ArticleListSerializer if self.request.method == 'GET' else serializers.ArticleSerializer