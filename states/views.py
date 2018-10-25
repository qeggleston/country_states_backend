from django.shortcuts import render
from states.models import State
from countries.models import Country
from states.serializers import StateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class StateList(APIView):
    def get(self, request, code, format=None):
        states = State.objects.filter(country__code=code)
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)
    def post(self, request, code, format=None):
        serializer = StateSerializer(data=request.data)
        
        if(serializer.is_valid()):
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class StateDetail(APIView):
    def get_object(self, code): 
        try:
            return State.objects.get(code=code)
        except State.DoesNotExist:
            raise Http404
    def get(self, request, code, format=None):
        state = self.get_object(code)
        serializer = StateSerializer(state)
        return Response(serializer.data)
    def put(self, request, code, format=None):
        state = self.get_object(code)
        serializer = StateSerializer(state, data=request.data)
        if(serializer.is_valid):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, code, format=None):
        state = self.get_object(code)
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)