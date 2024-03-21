from django.contrib import admin

from cars.models import Users, Manufacturer, Cars


@admin.site.register(Users)
class UsersAdmin(admin.ModelAdmin):
    # liked list_display ichiga qoshamiz
    list_display = ["pk", "full_name", "user_name", "password", "phoneNumber", "user_image"]
    search_fields = ["user_name", "phoneNumber"]
    ordering = ["pk"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["pk", "manufacturer_name"]
    search_fields = ["manufacturer_name"]
    ordering = ["manufacturer_name"]


@admin.register(Cars)
class AdminCars(admin.ModelAdmin):
    list_display = ["pk", "car_name", "car_manufacturer", "car_year", "car_user", "car_description",
                    "car_number", "car_color", "car_price", "made_in"]
    search_fields = ["car_name", "car_year", "car_number"]
