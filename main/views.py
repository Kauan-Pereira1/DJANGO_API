#importa as tabelas models que criamos
from .models import *
#importa os serializer que criamos
from .serializers import *
#Importar a classe de configuração da API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PeopleAPIView(APIView):
    def post(self, request):
        #recebe o json que veio do cliente"
        peopleJson = request.data
        #converter json em python
        PeopleSerialized = PeopleSerializer(data=peopleJson)
        #verifica a conversão e valida
        PeopleSerialized.is_valid(raise_exception=True)
        #salva no banco de dados (insert into people..)
        PeopleSerialized.save()
        return Response(status=status.HTTP_201_CREATED, data=PeopleSerialized.data)    
    def get(self, request, peopleId = ''):
        if peopleId == '': #se estiver vazio, pega tudo!
            #primeiro vamos fazer um select all do banco:
            peoplefound = People.objects.all() #select *from people;
            #agora pegamos os dados em python e mandamos para o json
            peopleSerialized = PeopleSerializer(peoplefound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(peopleSerialized.data)
        else: #coletando people do id solicitado!
            try:
                peoplefound = People.objects.get(id=peopleId)
                #select *from people where id = peopleId
                peopleSerialized = PeopleSerializer(peoplefound, many=False)
                return Response(peopleSerialized.data)
            except People.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data='People Not Found your asshole!')
        
        
class PlanetAPIView(APIView):
    def post(self, request):
        #recebe o json que veio do cliente"
        planetJson = request.data
        #converter json em python
        PlanetSerialized = PlanetSerializer(data=planetJson)
        #verifica a conversão e valida
        PlanetSerialized.is_valid(raise_exception=True)
        #salva no banco de dados (insert into people..)
        PlanetSerialized.save()
        return Response(status=status.HTTP_201_CREATED, data=PlanetSerialized.data)    
    def get(self, request, planetsId=''):
        if planetsId == '':
            #primeiro vamos fazer um select all do banco:
            planetfound = Planet.objects.all() #select *from people;
            #agora pegamos os dados em python e mandamos para o json
            planetSerialized = PlanetSerializer(planetfound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(planetSerialized.data)
        else:
            try:
                planetfound = Planet.objects.get(id=planetsId)
                planetSerialized = PlanetSerializer(planetfound, many=False)
                return Response(planetSerialized.data)
            except Planet.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data='Planet Not Found your asshole!')
        
        
class StarshipsAPIView(APIView):
    def post(self, request):
        #recebe o json que veio do cliente"
        starshipsJson = request.data
        #converter json em python
        StarShipSerialized = StarshipsSerializer(data=starshipsJson)
        #verifica a conversão e valida
        StarShipSerialized.is_valid(raise_exception=True)
        #salva no banco de dados (insert into people..)
        StarShipSerialized.save()
        return Response(status=status.HTTP_201_CREATED, data=StarShipSerialized.data)    
    def get(self, request, starshipId = ''):
        if starshipId == '':
            #primeiro vamos fazer um select all do banco:
            starsShipsfound = Starships.objects.all() #select *from people;
            #agora pegamos os dados em python e mandamos para o json
            starsShipsSerialized = StarshipsSerializer(starsShipsfound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(starsShipsSerialized.data)
        else:
            try:
                starsShipsfound = Starships.objects.get(id=starshipId)
                starsShipsSerialized = StarshipsSerializer(starsShipsfound, many=False)
                return Response(starsShipsSerialized.data)
            except Starships.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data='StarShip Not Found your asshole!')
