from django.shortcuts import render
from .models import Meal


def meals_list(request):
    name = request.POST.get('name')
    ingredients = request.POST.get('ingredients')
    price = request.POST.get('price')
    type = request.POST.get('type')
    cuisine = request.POST.get('cuisine')
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