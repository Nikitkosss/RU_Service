from django.db import models


class Home(models.Model):
    address = models.CharField(max_length=100)


class Apartment(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    area = models.FloatField()


class WaterMeter(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    readings = models.JSONField()


class Tariff(models.Model):
    water_tariff = models.FloatField()
    area_tariff = models.FloatField()


class Billing(models.Model):
    month = models.DateField(auto_now_add=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    water_billing = models.FloatField()
    area_billing = models.FloatField()


class UtilityBill(models.Model):
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    calculation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Bill for Apartment {self.apartment.id}'
