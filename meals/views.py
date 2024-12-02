from django.shortcuts import render
from .models import Meal

def meals_list(request):
    name = request.GET.get('name')
    ingredients = request.GET.get('ingredients')
    price = request.GET.get('price')
    type = request.GET.get('type')
    cuisine = request.GET.get('cuisine')
    if name is not None and ingredients is not None and price is not None and type is not None and cuisine is not None:
        if type is not None:
            Meal.objects.create(
                name=name,
                ingredients=ingredients,
                price=price,
                type=type,
                cuisine=cuisine,
            )


    taxis = Meal.objects.all()
    return render(request, 'taxi/taxi_list.html', {'taxis': taxis})