from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200, blank=True)
    price = models.FloatField()

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "price": self.price
        }
