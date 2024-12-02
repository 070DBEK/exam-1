from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(
        max_length=20,
        choices=[
            ('Appetizer', 'Appetizer'),
            ('Main Course', 'Main Course'),
            ('Dessert', 'Dessert')
        ]
    )
    cuisine = models.CharField(max_length=50)

    def __str__(self):
        return self.name
