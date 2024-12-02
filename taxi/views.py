from django.shortcuts import render
from .models import Taxi


def taxi_list(request):
    name = request.GET.get('name')
    license_plate = request.GET.get('license_plate')
    driver_name = request.GET.get('driver_name')
    passenger_capacity = request.GET.get('passenger_capacity')
    status = request.GET.get('status')
    car_model = request.GET.get('car_model')
    if name is not None and license_plate is not None and driver_name is not None and passenger_capacity is not None and car_model is not None:
        if passenger_capacity is not None:
            Taxi.objects.create(
                name=name,
                license_plate=license_plate,
                driver_name=driver_name,
                passenger_capacity=passenger_capacity,
                status=status,
                car_model=car_model,
            )


    taxis = Taxi.objects.all()
    return render(request, 'taxi/taxi_list.html', {'taxis': taxis})
