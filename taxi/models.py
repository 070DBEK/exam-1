from django.db import models

class Taxi(models.Model):
    name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    passenger_capacity = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Available', 'Available'),
            ('Busy', 'Busy'),
            ('Under Maintenance', 'Under Maintenance')
        ]
    )
    car_model = models.CharField(max_length=100)

    def __str__(self):
        return self.name
