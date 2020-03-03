from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers


class Cats(APIView):
    def __init__(self, name, age, race):
        self.name = name
        self.age = age
        self.race = race


class CatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cats
        fields = ['name', 'age', 'race']


# ViewSets define the view behavior.
class CatsViewSet(viewsets.ModelViewSet):
    # queryset = Cats.objects.all()
    serializer_class = CatsSerializer
