from rest_framework import serializers
from .models import PersonInfo

class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInfo
        fields = ['id', 'FirstName', 'LastName', 'Phone','Email','Address','City','State','Zip','Country']