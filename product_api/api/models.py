from django.db import models

class Store(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=246)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=246)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()

    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name