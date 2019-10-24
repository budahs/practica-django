from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from . import models

class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = models.Category
        fields = ['id','nombre','slug']

class ArticleListSerializer(ModelSerializer):

    nombre = serializers.CharField(source='usuario.username')
    nombre_categoria = serializers.CharField(source='categoria.nombre')

    class Meta:
        model = models.Article
        fields = ['id','titulo','texto_introduccion','imagen','usuario','nombre','fecha_creacion','categoria','nombre_categoria','contenido']

class ArticleSerializer(ModelSerializer):

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
                  'video',
                  'categoria'
                  ]
        read_only_fields = ['id', 'fecha_creacion', 'fecha_modificacion', 'usuario']