#importa a lib para serializers
from  rest_framework import serializers
#importa todos os models que criamos
from .models import * 

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'
        many=True
        
class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'
        many=True
        
class StarshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starships
        fields = '__all__'
        many=True
        

        