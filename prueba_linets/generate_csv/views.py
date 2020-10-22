from django.shortcuts import render
from django.http import HttpResponse
from .models import MasterProductsConfigurable 
import csv
   
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MasterProductsConfigurableSerializer

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
                prod_str = ''
                prod_str = prod_str+product.sku+','+product.name+','+product.attribute_color
                model_arr.append(prod_str)
        
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response, delimiter='|')
        writer.writerow(model_arr)

    

    return response 


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<str:pk>/',
        'Create Product': '/product-create/',
    }
    return Response(api_urls)

@api_view(['GET'])
def productList (request):
    products = MasterProductsConfigurable.objects.all()
    serializer = MasterProductsConfigurableSerializer(products, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def productDetail (request, pk):
    products = MasterProductsConfigurable.objects.get(sku=pk)
    serializer = MasterProductsConfigurableSerializer(products, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def productCreate (request):
    serializer = MasterProductsConfigurableSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
