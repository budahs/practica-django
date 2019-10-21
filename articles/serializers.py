from rest_framework import serializers
from . import models

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['id','titulo','texto_introduccion']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['id',
                  'titulo',
                  'texto_introduccion',
                  'contenido',
                  'fecha_creacion',
                  'fecha_modificacion',
                  'estado',
                  'usuario',
                  'imagen',
                  'video'
                  ]
        read_only_fields = ['id', 'fecha_creacion', 'fecha_modificacion']