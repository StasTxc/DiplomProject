from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
import django_filters.rest_framework
from . import serializers
from . import models





#Создание компании
class CompanyCreateView(generics.CreateAPIView):
    serializer_class = serializers.CompanyDetailSerializers

#Удаление/обновление инфы о компании
class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CompanyDetailSerializers
    queryset = models.Company.objects.all()


#Вывод инфы о компаниях на мапу
class CompanyMapView(generics.ListAPIView):
    queryset = models.Company.objects.exclude(lat=0.0).exclude(lon=0.0)
    serializer_class = serializers.CompanyMapSerializers


#вывод инфы о компании c едой
class CompanyInfoView(generics.ListAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanyInfoSerilizers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ['id']








#Создание еды
class FoodCreateView(generics.CreateAPIView):
    serializer_class = serializers.FoodSerializers

#редактирование/удаление еды
class FoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FoodSerializers
    queryset = models.Food.objects.all()

#Вывод по типам еды
class FoodFilterListView(generics.ListAPIView):
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ['food_type']

#вывод на мейн страницу
class FoodListView1(generics.ListAPIView):
    queryset = models.Food.objects.filter(food_type='1').reverse()[:5]
    serializer_class = serializers.FoodSerializers

class FoodListView2(generics.ListAPIView):
    queryset = models.Food.objects.filter(food_type='2').reverse()[:5]
    serializer_class = serializers.FoodSerializers

class FoodListView3(generics.ListAPIView):
    queryset = models.Food.objects.filter(food_type='3').reverse()[:5]
    serializer_class = serializers.FoodSerializers




#Создание телефона
class TelephoneUserView(generics.CreateAPIView):
    serializer_class = serializers.TelephoneSerilizers

#Обновление удаление телефона
class TelephoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TelephoneSerilizers
    queryset = models.Profile.objects.all()
