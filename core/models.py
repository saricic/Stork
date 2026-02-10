from django.db import models
from django.contrib.auth.models import User

ORDER_CHOICES = (
    ('stork', 'Stork'),
    ('comfort', 'Comfort'),
    ('XL', 'XL'),
    ('Premium', 'Premium'),
)


class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pickUpAdress = models.CharField(max_length=150)
    dropOffAdress = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    choice = models.CharField(
        max_length=20,
        choices=ORDER_CHOICES,
        default='stork'
        )

    def __str__(self):
        return self.pickUpAdress

    class Meta:
        ordering = ['created']


