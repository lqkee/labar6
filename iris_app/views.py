from django.shortcuts import render
from .models import IrisModel
from django.http import HttpResponse

def show_form(request):
    return render(request, 'iris_app/form.html')

def predict(request):
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        model = IrisModel()
        prediction = model.predict(sepal_length, sepal_width, petal_length, petal_width)

        return render(request, 'iris_app/result.html', {'prediction': prediction})
    else:
        return HttpResponse("Invalid request method.")
