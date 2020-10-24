import csv
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import MasterProductsConfigurableSerializer
from .models import MasterProductsConfigurable 

def index(request):
    template = 'generate_csv/index.html'  
    return render(request, template)

def get_file(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    products = MasterProductsConfigurable.objects.all()  
    models = []
    writer = csv.writer(response,  delimiter='|')  
    
    for product in products:
        if product.model not in models:
            models.append(product.model)

    for model in models:
        model_arr = [model]
        cont = 1
        for product in products:
            if model == product.model:
                if  cont==1:
                    model_arr.append(product.name)
                    cont+=1

                prod_str = ''
                prod_str = prod_str+'sku='+product.sku+',color='+product.attribute_color
                model_arr.append(prod_str)
        
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response, delimiter='|')
        writer.writerow(model_arr)
    return response 

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/api/product-list/',
        'Detail View': '/api/product-detail/<str:pk>/',
        'Create Product': '/api/product-create/',
    }
    return Response(api_urls)

@api_view(['GET'])
def product_list (request):
    products = MasterProductsConfigurable.objects.all()
    serializer = MasterProductsConfigurableSerializer(products, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def product_detail (request, pk):
    products = MasterProductsConfigurable.objects.get(sku=pk)
    serializer = MasterProductsConfigurableSerializer(products, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def product_create (request):
    serializer = MasterProductsConfigurableSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
