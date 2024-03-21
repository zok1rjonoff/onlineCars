from django.shortcuts import render

from cars.models import Cars, Manufacturer


def get_all_cars(request):
    manufacturer = Manufacturer.objects.all()
    print(manufacturer)
    return render(request, "index.html", {"manufacturer": manufacturer})

