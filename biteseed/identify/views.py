from django.shortcuts import render,HttpResponse
from .models import *
from django.http import JsonResponse
import json
from .serializers import *

# Create your views here.
def data(request):
    return render(request,'json.html')

def json1(request):
    if request.method=='POST':
        json_data1=request.POST['exampleFormControlTextarea1']
        email=request.POST['exampleFormControlInput1']
        phoneNumber=request.POST['exampleFormControlInput2']
        json_data = json.loads(json_data1)
        for data21 in range(len(json_data)):
            for data2 in json_data:
                d=contact(
                    phoneNumber   = data2['phoneNumber'],
    email            =    data2['email'],
    linkedId          =   data2['linkedId'],
    linkPrecedence     =  data2['linkPrecedence'],
    createdAt          =  data2['createdAt'],             
    updatedAt           = data2['updatedAt'],            
    deletedAt           = data2['deletedAt']
                )
                d.save()
        data1=contact.objects.filter(email=email)
        serializer1=id_serializer(data1,many=True)
        id_1=[]
        for j in serializer1.data:
            id_1.append(j['id'])
        objs=contact.objects.filter(email=email)
        objs1=contact.objects.filter(phoneNumber=phoneNumber)
        objs2=contact.objects.filter(linkedId__in=id_1)
        serializer2=contact_serializer(objs1,many=True)
        serializer3=contact_serializer(objs2,many=True)
        serializer=contact_serializer(objs,many=True)
        print(serializer.data)
        phoneNumber=[]  
        email=[]
        linkedid=[]
        for i in serializer.data:
            phoneNumber.append(i['phoneNumber'])
            email.append(i['email'])
            linkedid.append(i['id'])

        for i1 in serializer2.data:
            phoneNumber.append(i1['phoneNumber'])
            email.append(i1['email'])
            linkedid.append(i1['id'])

        for i2 in serializer3.data:
            phoneNumber.append(i2['phoneNumber'])
            email.append(i2['email'])
            linkedid.append(i2['id'])
        # print(phoneNumber)
        phoneNumber=list(set(phoneNumber))
        email=list(set(email))
        linkedid=list(set(linkedid))
        data={
            'phonenumber':phoneNumber,
            'email':email,
            'linkedid':linkedid
        }
        return JsonResponse(data)
    return render(request,'json.html')