from django.contrib import admin

# Register your models here.
'''from FMSviewAPP.models import Vendor, vehicle, TripTable, TripStoreDetail, BolHeader, dataTable

admin.site.register(Vendor)
admin.site.register(vehicle)
admin.site.register(TripTable)
admin.site.register(TripStoreDetail)
admin.site.register(BolHeader)
admin.site.register(dataTable)'''


from FMSviewAPP.models import  TripStoreDetail, BolHeader, dataTable

admin.site.register(TripStoreDetail)
admin.site.register(BolHeader)
admin.site.register(dataTable)
