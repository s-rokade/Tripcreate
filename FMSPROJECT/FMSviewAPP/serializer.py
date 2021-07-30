from rest_framework import serializers
from FMSviewAPP.models import Vendor,vehicle,TripTable, TripStoreDetail, BolHeader, dataTable

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields=["vendor_name"]

class VehicleSerializer(serializers.ModelSerializer):
    vender_number=VendorSerializer()
    class Meta:
        model=vehicle
        fields=["vehicle_number","vender_number","contractpayload_in_mt","rcbook_payload_in_mt"]

class TripCreationSerializer(serializers.ModelSerializer):
    vehicle_number=VehicleSerializer()
    class Meta:
        model=TripTable
        fields=("vehicle_number","trip_weight","trip_volume","vehicle_weight_utilization","vehicle_volume_utilization")

#########################################################################################



class TripStoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =TripStoreDetail 
        fields=["store_name"]



class BolHeaderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= BolHeader
        fields=["bol_no ","to_loc","trip_Id","bol_value"]


class dataTableSerializer(serializers.ModelSerializer):
    #bol_no=BolHeaderSerializer()
    class Meta:
        model= dataTable
        fields="__all__"
        #fields=["TO_LOC"]

class getdataTableSerializer(serializers.ModelSerializer):
    class Meta:
        model= dataTable
        fields=["TO_LOC","bol_no","QTY_EXPECTED","UNIT_COST"]



