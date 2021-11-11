from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rectAPI.models import account, custormer
from rectAPI.serializers import accountSerializers, customerSerializers


# Create your views here.

@csrf_exempt

def accountApi(request,id=0):
    if request.method == 'GET':
        accounts = account.objects.all()
        accounts_serializers = accountSerializers(accounts,many = True)
        return JsonResponse(accounts_serializers.data, safe = False)
    elif request.method == 'POST':
        account_data = JSONParser().parse(request)
        accounts_serializers = accountSerializers(data = account_data)
        if accounts_serializers.is_valid():
            accounts_serializers.save()
            return JsonResponse("Added successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT':
        account_data = JSONParser().parse(request)
        Account = account.objects.get(id = account_data['id'])
        accounts_serializers = accountSerializers(Account,data=account_data)
        if accounts_serializers.is_valid():
            accounts_serializers.save()
            return JsonResponse("Update successfully", safe = False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        accounts = account.objects.get(id=id)
        account.delete()
        return JsonResponse("Delete SuccessFUlly", safe = False)