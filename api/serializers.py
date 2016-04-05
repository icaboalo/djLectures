from rest_framework import serializers
from lectura.models import *

#----------------------Default serializers----------------------#
class DefaultLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'type', 'lecture', 'date']