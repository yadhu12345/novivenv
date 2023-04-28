from django.db import models

class item(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return str(self.name)
    def __str__(self):
        return str(self.image)
    def __str__(self):
        return str(self.price)

class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    quantity = models.IntegerField()