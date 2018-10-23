from django.shortcuts import render
from countries.models import Country
from countries.serializers import CountrySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CountryList(APIView):
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CountryDetail(APIView):
    def get_object(self, code): 
        try:
            return Country.objects.get(code=code)
        except Country.DoesNotExist:
            raise Http404
    def get(self, request, code, format=None):
        country = self.get_object(code)
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    def put(self, request, code, format=None):
        country = self.get_object(code)
        serializer = CountrySerializer(country, data=request.data)
        if(serializer.is_valid):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, code, format=None):
        country = self.get_object(code)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)