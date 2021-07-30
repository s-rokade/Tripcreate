from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE

class Vendor(models.Model):
    organization_id = models.IntegerField()
    operating_unit = models.TextField()
    vendor_number=models.IntegerField(primary_key=True,default=0)
    vendor_name=models.TextField()
    vendor_type = models.TextField()
    address_line_1 = models.TextField()
    address_line_2 = models.TextField(null=True)
    address_line_3 = models.TextField(null=True)
    address_line_4 = models.TextField(null=True)
    city = models.TextField()
    state = models.TextField()
    country = models.TextField()
    postal_code = models.IntegerField()
    pay_group = models.TextField()
    gst_num = models.TextField()
    tax_region = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.vendor_name

    class Meta:
        db_table = "vendor"


class vehicle(models.Model):
    origin_id = models.IntegerField()
    vender_number = models.ForeignKey(Vendor, related_name="vendor_data",on_delete=CASCADE)
    vehicle_number = models.TextField(max_length=12, unique=True, primary_key=True)
    make = models.TextField(max_length=20)
    contractpayload_in_mt = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rcbook_payload_in_mt = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    length_in_ft = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    width_in_ft = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    height_in_ft = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    volume_in_cft = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    vehicle_manufacture_year = models.IntegerField()
    usage_zone = models.CharField(max_length=50)

    class Meta:
        db_table = "Vehicle_Table"


class TripTable(models.Model):
    trip_id = models.IntegerField(db_column='Trip_ID', primary_key=True, default='0')  # Field name made lowercase.
    trip_table_id = models.IntegerField(db_column='Trip_Table_ID')  # Field name made lowercase.
    origin_location = models.CharField(max_length=50, blank=True, null=True)

    trip_distance = models.IntegerField(db_column='Trip_distance', blank=True, null=True)  # Field name made lowercase.

    trip_time = models.TimeField(db_column='Trip_Time', blank=True, null=True)  # Field name made lowercase.

    destination_type = models.CharField(db_column='Destination_type', max_length=50, blank=True, null=True)  # Field name made lowercase.

    destination_code = models.CharField(db_column='Destination_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    planned_dispatch = models.TimeField(blank=True, null=True)

    planned_trip_end_time = models.TimeField(blank=True, null=True)

    trip_status = models.CharField(max_length=50, blank=True, null=True)

    trip_weight = models.IntegerField(blank=True, null=True)

    trip_volume = models.IntegerField(blank=True, null=True)

    store_drops = models.IntegerField(blank=True, null=True)

    trip_created_time = models.TimeField(blank=True, null=True)

    #vehicle_number = models.IntegerField(blank=True, null=True)

    vehicle_number = models.ForeignKey(vehicle, related_name="vehicle_data",on_delete=CASCADE)

    child_vendor_id = models.IntegerField(blank=True, null=True)

    contract_type = models.CharField(max_length=50, blank=True, null=True)

    contract_id = models.IntegerField(blank=True, null=True)

    vehicle_weight_utilization = models.IntegerField(blank=True, null=True)

    vehicle_volume_utilization = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'Trip_Table'



#####################################################################

class BolHeader(models.Model):
    bol_no = models.TextField(db_column='bol_no',primary_key=True, default='0')
    fms_location_master_id = models.IntegerField()
    ship_date = models.DateField()
    bol_value = models.DecimalField(max_digits=6, decimal_places=2)
    bol_weight = models.DecimalField(max_digits=6, decimal_places=2)
    bol_volume = models.DecimalField(max_digits=6, decimal_places=2)
    from_loc = models.IntegerField()
    to_loc = models.IntegerField()
    origin_type = models.TextField()
    trip_Id = models.IntegerField(blank=True,null=True)
    shipment = models.IntegerField()
    created_Date = models.DateField(auto_now_add=True)
    updated_Date = models.DateField(auto_now=True)

 
    class Meta:
        db_table = "fms_bol_header"
        indexes = [
            models.Index(fields=['bol_no','fms_location_master_id', 'ship_date', 'trip_Id', 'shipment'])]
    def __str__(self):
        return f'{self.bol_no}'



class dataTable(models.Model):
    dataTable_details_id = models.AutoField(primary_key=True)
    FROM_LOC = models.IntegerField()     
    TO_LOC  = models.IntegerField()  
    SHIP_DATE  = models.DateField()       
    SHIPMENT  = models.IntegerField()      
    #bol_no  = models.ForeignKey(BolHeader, on_delete=CASCADE, related_name='bol_nodata') 
    bol_no = models.TextField() 
    DISTRO_NO = models.IntegerField(blank=True,null=True)  
    CARTON = models.CharField(max_length=20)   
    ITEM  = models.CharField(max_length=25)  
    SEQ_NO  = models.IntegerField(blank=True,null=True)  
    QTY_EXPECTED = models.IntegerField()   
    UNIT_COST = models.IntegerField()  
    PROCESS_FLAG  = models.CharField(max_length=5)  

    def __str__(self):
        return f'{self.TO_LOC}'




class TripStoreDetail(models.Model):
    trip_store_details_id = models.AutoField(primary_key=True)
    #trip_id = models.ForeignKey(Trip, on_delete=models.PROTECT)
    trip_id = models.IntegerField()
    store_id = models.IntegerField()
    store_eta = models.DateTimeField()
    store_etd = models.DateTimeField()
    delivery_seq = models.IntegerField()
    actual_arr_time = models.DateTimeField()
    actual_dep_time = models.DateTimeField()
    pod_1 = models.TextField()
    pod_2 = models.TextField()
    origin_id = models.IntegerField()
    store_name = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
 
    class Meta:
        db_table = "fms_trip_store_details"
        indexes = [
            models.Index(fields=['trip_id'])
        ]

class Test(models.Model):
    name= models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
