from rest_framework import serializers
from rectAPI.models import account, custormer

class accountSerializers(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ('username','id')

class customerSerializers(serializers.ModelSerializer):
    class Meta:
        model = custormer
        fields = ('name','phone','dateofbirth','Address','id_account')
