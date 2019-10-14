from rest_framework import routers
from articles import api_views as article_views

router = routers.DefaultRouter()
router.register(r'articles', article_views.ArticleViewSet)
