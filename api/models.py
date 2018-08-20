from django.contrib.gis.db import models


class Language(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=15, null=False)
    symbol = models.CharField(max_length=1, null=False, default="")
    abbreviation = models.CharField(max_length=5, null=False, default="")

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    language = models.ForeignKey(Language, null=True, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency, null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    polygon = models.PolygonField(null=True, blank=True)
    provider = models.ForeignKey(Provider, null=False, on_delete=models.CASCADE)

    objects = models.GeoManager()

    def __str__(self):
        return self.name
