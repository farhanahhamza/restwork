from rest_framework import serializers
from.models import Manager

class empSerializers(serializers.Serializer):
    name=serializers.CharField(read_only=True)
    dept=serializers.CharField()
    qualiffic=serializers.CharField()
    
class ManagerModelSer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields="_all_"