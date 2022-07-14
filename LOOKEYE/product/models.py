from django.db import models

class Product(models.Model) :
    #제품명
    name = models.CharField(max_length=50)
    #제품가격
    price = models.IntegerField()
    #제품유형 (선택리스트필드)
    classification = models.SmallIntegerField()
    #유통기한
    day_cnt = models.DateTimeField()
    #제조사
    manufacturer = models.CharField()
# Create your models here.
