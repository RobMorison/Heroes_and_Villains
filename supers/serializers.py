from rest_framework import serializers
from .models import Supers

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id', 'name', 'alter_ego', 'primary_abililty', 'secondary_ability', 'catchphrase', 'super_types']
        depth = 1