
from django.shortcuts import render
from django.http import HttpResponse
from .models import MasterProductsConfigurable 
import csv
   

def index(request):
    template = 'generate_csv/index.html'
    
    return render(request, template)



def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    products = MasterProductsConfigurable.objects.all()  
    models = []
    writer = csv.writer(response,  delimiter='|')  
    # response.write(u'\ufeff'.encode('utf8'))
    
    for product in products:
        if product.model not in models:
            models.append(product.model)

    for model in models:
        model_arr = [model]
        print(model_arr)
        for product in products:
            if model == product.model:
                model_arr.append(product.sku)
                model_arr.append(product.name)
                model_arr.append(product.attribute_color)
        
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response, delimiter='|')
        writer.writerow(model_arr)

    

    return response 