from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="books")
    distribution_expense = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.title
