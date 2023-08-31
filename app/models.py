from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class Car(models.Model):
    type = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images')
    name = models.CharField(help_text='Moshina nomi', max_length=15)
    adreess = models.CharField(help_text='Manzil', max_length=20)
    made_date = models.DateField(help_text='Ishlab chiqarilgan sana', max_length=20)
    made_in = models.CharField(help_text='Ishlab chiqarilgan joy', max_length=20)
    probeg = models.FloatField(help_text='Probeg', max_length=20)
    colour = models.CharField(help_text='Moshina ranggi', max_length=20)
    added_date = models.DateTimeField(help_text='Qoshilgan sana', max_length=20)
    author_name = models.CharField(help_text='Moshina egasi', max_length=20)
    description = models.TextField(help_text='Moshina tavsifi', max_length=20)
    def __str__ (self):
        return f"{self.id} |  {self.name}"
