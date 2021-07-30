from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
'''from FMSviewAPP.models import Vendor, vehicle, TripTable, TripStoreDetail, BolHeader, dataTable
from rest_framework import serializers, status
from FMSviewAPP.serializer import VendorSerializer,TripStoreDetailSerializer, getdataTableSerializer, VehicleSerializer, TripCreationSerializer, BolHeaderSerializer, dataTableSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.http.response import Http404, HttpResponse
from rest_framework import status'''

'''class VedorAPI(viewsets.ModelViewSet):

    serializer_class= VendorSerializer
    queryset=Vendor.objects.all()

class getAPI(APIView):
    def get(self,request,vehicle_number):
        vehicle_number = vehicle_number
        TripsCreated = TripTable.objects.filter(trip_status="initiated",vehicle_number=vehicle_number)
        serializer=TripCreationSerializer(TripsCreated,many=True)
        data=serializer.data
        #print(data.values([0]['contractpayload_in_mt']))
        return Response(serializer.data, status=status.HTTP_200_OK)

class tripCreationView(APIView):
   def get(self,request,vehicle_number):
        vehicle_number = vehicle_number
        TripsCreated = TripTable.objects.filter(trip_status="initiated",vehicle_number=vehicle_number)
        #print(TripsCreated)
        #print(TripTable["trip_weight"])
        serializer=TripCreationSerializer(TripsCreated,many=True)
        data=serializer.data

        #iterate the list
        vehicle_wt_capacity = (data[0]['vehicle_number']['contractpayload_in_mt'])
        vehicle_vol_capacity = (data[0]['vehicle_number']['rcbook_payload_in_mt'])
        
        #converting decimale value to integer
        vehicle_wt=float(vehicle_wt_capacity)
        vehicle_vol=float(vehicle_vol_capacity)
        vehicle_wt_cap=int(vehicle_wt)
        vehicle_vol_cap=int(vehicle_vol)
        data[0]['vehicle_number']['contractpayload_in_mt']=(vehicle_wt_cap)*1000
        data[0]['vehicle_number']['rcbook_payload_in_mt']=(vehicle_vol_cap)*1000

        #iterate the list
        trip_weight = data[0]['trip_weight']
        trip_volume = data[0]['trip_volume']
        
        #converting decimale value to integer
        trip_weight_float = float(trip_weight)
        trip_volume_float = float(trip_volume)
        trip_weight_in =int(trip_weight_float)
        trip_volume_in =int(trip_volume_float)
        data[0]['vehicle_weight_utilization']=trip_weight_in/(vehicle_wt_cap*1000)
        data[0]['vehicle_volume_utilization']=trip_volume_in/(vehicle_vol_cap*1000)
        #print(TripsCreated["trip_volume"])
        return Response(serializer.data, status=status.HTTP_200_OK)'''



###################################################################################
from FMSviewAPP.models import TripStoreDetail, BolHeader, dataTable
from rest_framework import serializers, status
from FMSviewAPP.serializer import TripStoreDetailSerializer, getdataTableSerializer, BolHeaderSerializer, dataTableSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.http.response import Http404, HttpResponse

class UserSelectView1(APIView):
    def get(self,request):
        BolCreated1 = dataTable.objects.all()
        print(BolCreated1)
        return HttpResponse(BolCreated1)


def getdata(request):
    BolCreated1 = dataTable.objects.all()
    print(BolCreated1)
    return HttpResponse(BolCreated1)





class UserSelectView(APIView):
    def get(self,request, store_id):
        store_id= store_id
        #BolCreated = dataTable.objects.filter(TO_LOC=store_id)
        BolCreated = dataTable.objects.all()
        serializer= dataTableSerializer(BolCreated, many=True)
        print(BolCreated)
        return HttpResponse(BolCreated) 
        print(BolCreated)

        #create list of store_id
        storeId=[]
        for value in BolCreated:
            storeId.append(value)

        #store name  
        Trips=TripStoreDetail.objects.all().filter(store_id=storeId)
        serializer= TripStoreDetailSerializer(Trips,many=True)
        print(serializer.data)

        #check trip_id is null
        BolDetail= BolHeader.objects.all().filter(store_id=storeId, trip_id='null')
        for value in BolDetail:
            if value in storeId:
                continue
            else:
                storeId.remove(value)

        BolCreateddata = dataTable.objects.filter(PROCESS_FLAG ="no",TO_LOC=store_id)
        serializer_class=getdataTableSerializer(BolCreateddata,many=True)
        print(serializer_class)
        










