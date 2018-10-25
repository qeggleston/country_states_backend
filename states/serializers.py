from rest_framework import serializers
from states.models import State
from countries.models import Country

class StateSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    class Meta:
        model = State
        fields = ('id', 'name', 'code', 'country')    