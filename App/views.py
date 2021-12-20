from functools import cache
import io
import json

from django.http import response
from App.models import Brand, Category, ImageLibrary, Product, ProductDetails, ProductTest, UsedFor
from App.serializer import BrandSerializer, CategorySerializer, ProductSerializer,  UsedForSerializer
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .methods import postMethod
from rest_framework.decorators import api_view

# Create your views here.

# for common products details


def productAllInfo(products):
    newProductList = []
    for pro in products:
        id = pro.id
        code = pro.code
        details = ProductDetails.objects.filter(product=pro.id).values()
        brand = Brand.objects.filter(id=pro.brand.id).values()
        category = Category.objects.filter(id=pro.id).values()
        images = ImageLibrary.objects.filter(product=pro.id).values()
        newProductList.append(
            {"id": id, "code": code, "details": details, "category": category, "brand": brand, "images": images})
    return newProductList


class UserFor_CRUD(APIView):
    def get(self, request, *args, **kwargs):
        data = UsedFor.objects.all()
        serializer = UsedForSerializer(data, many=True)
        return Response(serializer.data)


class Brnad_CRUD(APIView):
    def get(self, request, *args, **kwargs):
        data = UsedFor.objects.all()
        serializer = UsedForSerializer(data, many=True)
        return Response(serializer.data)


class Category_CRUD(APIView):
    def get(self, request, *args, **kwargs):
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return Response(serializer.data)


# class Categories(APIView):
#     def get(self, request, *args, **kwargs):
#         data = Category.objects.all()

#         serializer = CategorySerializerr(data, many=True)

#         # seralizer.data python data (orderDict)

#         # print(json.dumps(serializer.data))

#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         if(type(request.data) is list):
#             serializer = CategorySerializerr(data=request.data, many=True)
#             if serializer.is_valid():
#                 for obj in serializer.data:
#                     Category.objects.create(
#                         name=obj.get('name'),
#                         details=obj.get('details'),
#                         datalist=obj.get('datalist')
#                     )
#                 return Response(serializer.data)
#             return Response(serializer.errors)
#         else:
#             serializer = CategorySerializerr(data=request.data)
#             if serializer.is_valid():
#                 postMethod(Category, serializer.data)
#                 # Category.objects.create(
#                 #     name=serializer.data.get('name'),
#                 #     details=serializer.data.get('details'),
#                 #     datalist=serializer.data.get('datalist')
#                 # )
#                 return Response(serializer.data)
#         return Response(serializer.errors)

#     def put(self, request, *args, **kwargs):
#         serializer = CategorySerializerr(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)


class Product_CRUD(APIView):
    def get(self, request, *args, **kwargs):
        data = Product.objects.all()
        # print("AAaA==", data)
        serializer = ProductSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view()
def productByUsedFor(request, id):

    try:
        products = Product.objects.filter(usedFor=id)
        categoies = []
        brands = []
        print("sasas==", products)
        for pro in products:
            temp = Category.objects.get(id=pro.category.id)
            if temp not in categoies:
                categoies.append(temp)
            temp2 = Brand.objects.get(id=pro.brand.id)
            if(temp2 not in brands):
                brands.append(temp2)

        catSer = CategorySerializer(categoies, many=True)
        brandSer = BrandSerializer(brands, many=True)
        obj = {"categories": catSer.data, "brands": brandSer.data}

        return Response(obj)
    except:
        return Response("somthing error")


@api_view()
def productByBrand(request, id):

    try:
        products = Product.objects.filter(brand=id)
        productInfo = productAllInfo(products)
        return Response(productInfo)
    except:
        return Response("somthing error")


@api_view()
def productByCategory(request, id):

    try:
        products = Product.objects.filter(category=id)

        productInfo = productAllInfo(products)
        return Response(productInfo)
    except:
        return Response("somthing error")
