from django.contrib import admin

# Custom models registration
from articles.models import Article

admin.site.register(Article)

