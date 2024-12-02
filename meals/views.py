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


    meals = Meal.objects.all()
    return render(request, 'meals/meals_list.html', {'meals': meals})