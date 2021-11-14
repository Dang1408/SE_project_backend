from rest_framework import serializers
from rectAPI.models import account, customer

class accountSerializers(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ('username','password','id')

class customerSerializers(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ('name','phone','dateofbirth','Address','id_account')
